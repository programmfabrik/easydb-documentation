---
title: "Using the JSON Importer"
menu:
  main:
    name: "Json Importer"
    identifier: "tutorials/jsonimport"
    parent: "tutorials"
---

# Using the JSON Importer

This is a step by step tutorial on how to generate JSON Payloads, that can be imported into the easydb using the [JSON Importer](/en/tools/jsonimport/) in the frontend.

This tutorial uses an [example datamodel](/en/tutorials/jsonimport/datamodel) that covers most (but not necessarily all) aspects of importing payloads.

### The general steps are:

1. Creating payloads for [basetypes](#payloads-for-basetypes)
	1. [Tags](#tags)
	2. [Users](#users)
	3. [Groups](#groups)
	4. [Pools](#pools)
	5. [Objecttype Settings](#objecttype-settings)
	6. [Messages](#messages)

2. Creating payloads for [user objects](#payloads-for-user-objects) (actual easydb objects that contain data)
	1. [Simple objects](#simple-linked-objects) that are linked in main objects
	2. [Main objects](#main-objects) that link to simple objects

3. [Collections](#collections) and collection objects

4. If necessary, [import second versions](#importing-of-second-versions-of-objects) of objects to link to objects that could not be referenced in the first import round

### Important things to consider

* The order of importing is important!
	* Every object that is referenced by another object, must have already imported in a different payload, otherwise a database error can be caused
	* Every parent of a hierarchical basetype or object must have been imported before
		* Hierarchical objects must be imported level by level
		* This means the payloads have to be sorted to represent a breadth first search of the hierarchical tree
	* Linked objects that are referenced must have been imported before

* Masks should not be used for importing, since values might be ignored if they are not enabled in the mask
	* Always use `"_mask": "_all_fields"` so that all fields are imported without any limitations

<!-- todo -->

## Payloads for basetypes

Basetype payloads should always be imported first since they are referenced in most user objects. There is no strict order of the basetypes, but you have to consider that they can reference each other. Since circular references between basetypes are possible, importing of second versions of the basetypes might be needed (update migration).

Possible, but not exclusive, references between basetypes:

* Tags:
	* do not reference other basetypes
	* can be referenced by all other basetypes by tagfilter based rights management
	* tags, users, groups as part of the rightsmanagement

* User:
	* can reference groups (as being inside a group)
	* tags, users, groups as part of the rightsmanagement

* Group:
	* tags, users, groups as part of the rightsmanagement

* Pools:
	* hierachical, so pools reference other pools as a parent
	* tags, users, groups as part of the rightsmanagement

* Objecttypes:
	* users and groups for column filters
	* tags, users, groups as part of the rightsmanagement

* Messages:
	* groups to filter which users should see the message
	* tags, users, groups as part of the rightsmanagement

### Tags

### Users

### Groups

### Pools

### Objecttype Settings

### Messages

## Payloads for user objects

### Simple linked objects

### Main objects

## Collections

## Importing of second versions of objects