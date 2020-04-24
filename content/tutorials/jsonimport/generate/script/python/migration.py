#!/usr/bin/python
# coding=utf8

import sqlite3
import json
import datetime
import sys

# import the helper functions from easydb-migration-tools
# sys.path.append('../easydb-migration-tools/json_migration/')
sys.path.append('/home/pf/migration/easydb-migration/easydb-migration-tools/json_migration/') # xxx
import migration_util


# helper function
# convert the date format from the CSV file (d.m.yyyy) to the valid easydb format (yyyy-mm-dd)
def format_date(input):

    # try to parse the input string into a datetime object and format it
    try:
        d = datetime.datetime.strptime(input, '%d.%m.%Y')
        return migration_util.datetime_to_date(d)
    except Exception as e:
        print 'Datetime format error:', e
        return None


# helper function
# dump the json object with `payload_data` in the file `payload_path`
def save_payload(payload_path, payload_data):
    payload_file = open(payload_path, 'w')
    payload_file.write(json.dumps(payload_data, indent=2))
    payload_file.close()


def tags_payload(payload_path):

    # create a simple hard coded payload that includes the tag

    payload = {
        'import_type': 'tags',
        'tags': [
            {
                '_tags': [
                    {
                        'tag': {
                            'displayname': {
                                'en-US': 'Public Access'
                            },
                            'displaytype': 'facet',
                            'enabled': True,
                            'frontend_prefs': {
                                'webfrontend': {
                                    'color': 'green',
                                    'icon': 'fa-eye'
                                }
                            },
                            'is_default': False,
                            'reference': 'public',
                            'sticky': False,
                            'type': 'individual'
                        }
                    }
                ],
                'taggroup': {
                    'displayname': {
                        'en-US': 'Tag Group 1'
                    },
                    'reference': 'taggroup1',
                    'type': 'checkbox'
                }
            }
        ]
    }

    # save the payload
    filename = 'basetype_tags.json'
    save_payload(payload_path + '/' + filename, payload)

    return filename


def pools_payload(payload_path):

    # create a simple hard coded payload that includes the pool

    payload = {
        'import_type': 'pool',
        'pools': [
            {
                '_basetype': 'pool',
                'pool': {
                    '_version': 1,
                    'lookup:_id_parent': {
                        'reference': 'system:root'
                    },
                    'name': {
                        'en-US': 'Migrated Objects'
                    },
                    'reference': 'migrated_objects'
                }
            }
        ]
    }

    # save the payload
    filename = 'basetype_pools.json'
    save_payload(payload_path + '/' + filename, payload)

    return filename


def orte_to_payloads(connection, payload_path, parent_id='', parent_lookup='', level=0):

    # array of ordered payload names that will be returned as the result
    payload_names = []

    # array of ordered payload names that were returned by a recursive call of this function
    new_payload_names = []

    # get a connection cursor
    cursor = connection.cursor()

    # perform select statements to get data from the sqlite
    # find all rows from "source.orte.csv" where the parent is the same as the given parent value
    result = migration_util.execute_statement(
        cursor=cursor,
        sql="""
            SELECT id, name
            FROM "source.orte.csv"
            WHERE parent = '%s'
        """ % parent_id)

    # list of the generated linked objects that are saved in the payload for the current level
    orte_objects = []

    # iterate over all rows from the result and generate payloads
    # each row is a tuple with the values for the columns id and name
    for row in result:

        # get the values from the rows by using the column index
        id = row[0]
        name = row[1]

        # generate and append the payload
        object = {
            '_objecttype': 'orte',
            '_mask': '_all_fields',
            'orte': {
                '_version': 1,
                'name': name
            }
        }

        # if there is a parent, include the lookup for the parent id
        if len(parent_lookup) > 0:
            object['orte']['lookup:_id_parent'] = {
                'name': parent_lookup
            }

        print 'orte: level %d: %s' % (level, name)

        orte_objects.append(object)

        # recursively call the function for the children of the current object
        new_payload_names = orte_to_payloads(connection, payload_path, parent_id=id, parent_lookup=name, level=level + 1)

    # close the connection cursor
    cursor.close()

    # if there are generated objects for the payload, generate and save this payload file
    if len(orte_objects) > 0:
        payload = {
            'import_type': 'db',
            'objecttype': 'orte',
            'objects': orte_objects
        }

        # generate a filename that includes the objecttype and the current level
        filename = 'userobject-orte-level-%d.json' % level

        # dump the dict object with the payload data as a json object and save it in the file
        save_payload(payload_path + '/' + filename, payload)

        # the returned array must have the current payload name as the first element
        payload_names = [filename]

    # to keep the order, add the ordered payload names from all children
    for p in new_payload_names:
        payload_names.append(p)

    return payload_names


def linked_objects_payloads(connection, payload_path):

    # array of ordered payload names that will be returned as the result
    payload_names = []

    # perform select statements to get data from the sqlite
    cursor = connection.cursor()
    result = migration_util.execute_statement(
        cursor=cursor,
        sql="""
            SELECT fotograf, schlagworte
            FROM "source.bilder.csv"
        """)
    cursor.close()

    personen = set()
    schlagwoerter = set()

    for row in result:
        # different columns contain the values for different linked objects that are later linked into the main objects

        # column 'fotograf' (index 0) -> objecttype personen
        text = row[0]
        if len(text) > 0:
            personen.add(text)

        # column 'schlagworte' (index 1) -> objecttype schlagwoerter
        text = row[1]
        if len(text) > 0:
            # split multiple values
            values = text.split(';')
            for v in values:
                v = v.strip()
                if len(v) > 0:
                    schlagwoerter.add(v)

    # generate payloads from the collected values

    if len(personen) > 0:

        payload = {
            'import_type': 'db',
            'objecttype': 'personen',
            'objects': []
        }

        for p in personen:
            payload['objects'].append({
                '_objecttype': 'personen',
                '_mask': '_all_fields',
                'personen': {
                    '_version': 1,
                    'name': p
                }
            })

            print 'personen: %s' % p

        # dump the dict object with the payload data as a json object and save it in the file
        filename = 'userobject-personen.json'
        save_payload(payload_path + '/' + filename, payload)

        # add the filename to the payload list
        payload_names.append(filename)

    if len(schlagwoerter) > 0:

        payload = {
            'import_type': 'db',
            'objecttype': 'schlagwoerter',
            'objects': []
        }

        for s in schlagwoerter:
            payload['objects'].append({
                '_objecttype': 'schlagwoerter',
                '_mask': '_all_fields',
                'schlagwoerter': {
                    '_version': 1,
                    'name': s
                }
            })

            print 'schlagwoerter: %s' % s

        # dump the dict object with the payload data as a json object and save it in the file
        filename = 'userobject-schlagwoerter.json'
        save_payload(payload_path + '/' + filename, payload)

        # add the filename to the payload list
        payload_names.append(filename)

    return payload_names


def main_objects_payloads(connection, payload_path):

    # array of ordered payload names that will be returned as the result
    payload_names = []

    # objects for the list in the payload
    objects = []

    # perform select statements to get data from the sqlite
    cursor = connection.cursor()
    result = migration_util.execute_statement(
        cursor=cursor,
        sql="""
            SELECT inventarnummer,
                "date-from", "date-to",
                "title-de", "title-en",
                "date",
                image,
                ort, fotograf, schlagworte,
                public = 'true',
                __source_unique_id
            FROM "source.bilder.csv"
            WHERE inventarnummer != ''
        """)
    cursor.close()

    for row in result:

        # main object of objecttype `bilder`, reverse linked in objecttype `objekte`
        # create two objects from one row

        ##################################

        # structure for `bilder` object
        # this object will be included in the reverse nested table in the `objekte` object

        # use the __source_unique_id (index 10) to build a unique reference for the object

        reference = 'bild_' + row[11].strip()
        print 'bilder:', reference

        obj_bilder = {
            '_pool': {
                'pool': {
                    'lookup:_id': {
                        'reference': 'migrated_objects'
                    }
                }
            },
            '_version': 1,
            'reference': reference
        }

        # fill `bilder` object with data
        # for every text in the result row, strip the text to remove trailing whitespaces
        # only use the data if the text is not an empty string (since there is no NULL)

        # bilder.titel (index 3, 4)
        # l10n field, build object with values for different languages

        title_de = row[3].strip()
        title_en = row[4].strip()

        obj_bilder['titel'] = {
            'de-DE': title_de if len(title_de) else None,
            'en-US': title_en if len(title_en) else None
        }

        # bilder.aufnahmedatum (index 5)
        # date field, build object with date value

        obj_bilder['aufnahmedatum'] = {
            'value': format_date(row[5].strip()) # helper function to format the date
        }

        # bilder.datei (index 6)
        # asset field, build array with one object with asset url

        url = row[6].strip()
        if len(url) > 0:
            obj_bilder['datei'] = [
                {
                    'eas:url': url,
                    'preferred': True
                }
            ]

        # bilder.aufnahmeort (index 7)
        # linked objekt of objecttype `orte`, lookup by name

        ort = row[7].strip()
        if len(ort) > 0:
            obj_bilder['aufnahmeort'] = {
                '_mask': '_all_fields',
                '_objecttype': 'orte',
                'orte': {
                    'lookup:_id': {
                        'name': ort
                    }
                }
            }

        # bilder.personen (index 8)
        # linked objekt of objecttype `personen` in nested table, lookup by name

        person = row[8].strip()
        if len(person) > 0:
            obj_bilder['_nested:bilder__personen'] = [
                {
                    'bemerkung': 'Fotograf',
                    'person': {
                        '_mask': '_all_fields',
                        '_objecttype': 'personen',
                        'personen': {
                            'lookup:_id': {
                                'name': person
                            }
                        }
                    }
                }
            ]

        # bilder.schlagwoerter (index 9)
        # linked objekts of objecttype `schlagwoerter` in nested table, lookup by name
        # multiple values are separated by `;`, split the text, insert one linked object for each value

        obj_bilder['_nested:bilder__schlagwoerter'] = []

        schlagwoerter = row[9].strip()
        if len(schlagwoerter) > 0:
            values = schlagwoerter.split(';')
            for v in values:
                v = v.strip()

                if len(v) > 0:
                    # insert a new linked object with a lookup for this value
                    obj_bilder['_nested:bilder__schlagwoerter'].append(
                        {
                            'schlagwort': {
                                '_mask': '_all_fields',
                                '_objecttype': 'schlagwoerter',
                                'schlagwoerter': {
                                    'lookup:_id': {
                                        'name': v
                                    }
                                }
                            }
                        }
                    )

        ##################################

        # structure for `objekte` object
        obj_objekte = {
            '_mask': '_all_fields',
            '_objecttype': 'objekte',
            '_tags': [],
            'objekte': {
                '_pool': {
                    'pool': {
                        'lookup:_id': {
                            'reference': 'migrated_objects'
                        }
                    }
                },
                '_version': 1,
                # directly include the `bilder` object that was just created
                '_reverse_nested:bilder:objekte': [
                    obj_bilder
                ]
            }
        }

        # fill `objekte` object with data

        # check if the row is marked as `public`, if so add the tag
        # column: index 10, the return value here is a bool (see SELECT statement)

        if row[10]:
            obj_objekte['_tags'].append(
                {
                    'lookup:_id': {
                        'reference': 'public'
                    }
                }
            )

        # objekte.inventarnummer (index 0)
        # simple text field

        obj_objekte['objekte']['inventarnummer'] = row[0].strip()

        print 'objekte:', obj_objekte['objekte']['inventarnummer']

        # objekte.datierung (index 1, 2)
        # date range field, build object with two date values
        # start value (from): index 1
        # end value (to): index 2

        obj_objekte['objekte']['datierung'] = {
            'from': format_date(row[1].strip()), # helper function to format the date
            'to': format_date(row[2].strip()) # helper function to format the date
        }

        # append the generated object to the list of objects in the payload
        objects.append(obj_objekte)

    # build the payload with the objects

    if len(objects) > 0:
        payload = {
            'import_type': 'db',
            'objecttype': 'objekte',
            'objects': objects
        }

        # save the payload in a file and add the filename to the return value array
        filename = 'userobject-objekte-1.json'
        save_payload(payload_path + '/' + filename, payload)

        payload_names.append(filename)

    return payload_names


if __name__ == "__main__":

    payload_path = 'generated_payloads'

    payloads = []

    # connect to the sqlite database
    connection = migration_util.connect_to_sqlite('migration_data.sqlite')

    # basetype tag
    payloads.append(tags_payload(payload_path))

    # basetype pool
    payloads.append(pools_payload(payload_path))

    # read the hierarchic place names from orte.csv
    payloads += orte_to_payloads(connection, payload_path)

    # read the main table and generate payloads for all collected linked objects
    payloads += linked_objects_payloads(connection, payload_path)

    # read the main table again and generate payloads for main objects
    payloads += main_objects_payloads(connection, payload_path)

    # create the manifest
    manifest = {
        'source': 'Example Migration',
        'batch_size': 100,
        'eas_type': 'url',
        'payloads': payloads
    }

    # save the manifest file
    manifest_file = open(payload_path + '/manifest.json', 'w')
    manifest_file.write(json.dumps(manifest, indent=2))
    manifest_file.close()

    # close the connection to the sqlite database
    connection.close()
