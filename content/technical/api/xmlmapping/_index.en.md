---
title: "84 - xmlmapping"
menu:
  main:
    name: "xmlmapping"
    identifier: "technical/api/xmlmapping"
    parent: "technical/api"
---
# Save, load metadata profiles from import and export

### Get available mapping profiles

	GET /api/v1/xmlmapping/list?token=<token>

Returns a list of available profiles and mappings. Each mapping is linked to one profile. Profiles are stored in `schema/base/xmlmapping-profiles/[<profile>[.cson.json|.json]]`.

```javascript
[
	{
		profile: "photoshop.cson.json",
		displayname: {
			de_DE: "...",
			en_US: "..."
		},
		mappings: [
		    {
			   id: 2,
			   displayname: [
			      de_DE: "...",
				  en_US: "..."
			   }
		    }
		]
	}
]
```

### Get a specific mapping profile

	GET /api/v1/xmlmapping/profile/<profile-name>?token=<token>

Returns the profile with the name `<profile-name>`.


### Create a new mapping

	PUT /api/v1/xmlmapping/mapping?token=<token>

Create a new metadata mapping. Mappings are stored per db for all users. Mappings get updated on schema updates.

The mapping is stored in a JSON file in the schema folder of the current user schema: `schema/<db>/<current>/xmlmapping-mappings/<mapping_id>.json`.


### Update a mapping

	POST /api/v1/xmlmapping/mapping/<mapping_id>?token=<token>

Update the metadata mapping with the ID `<mapping_id>`.


### Get a mapping

	GET /api/v1/xmlmapping/mapping/<mapping_id>?token=<token>

Get the metadata mapping with the ID `<mapping_id>`.


### Delete a mapping

	DELETE /api/v1/xmlmapping/mapping/<mapping_id>?token=<token>

Delete the metadata mapping with the ID `<mapping_id>`.

## Structure of a mapping profile

### XML Namespaces

- `xml_base`
	- XML-base in `"/"`-Notation as base for all XML elements
- `xml`:
	- Name of the element, relative to the parent field and to `xml_base`

### Field types

- `element`
	- create an element with fixed attributes and a fixed text
- `text`:
	- fill the text of an element with information from the easydb
	- optionally combine this with `"concat"` and `"condition"`
- `attribute`:
	- fill the attribute with information from the easydb
- `list`:
	- fill repeating elements with information from the easydb
	- this includes `"fields"`

### Example

```json
{
    "id": 1, // issued by the server
    "displayname": {
        "de_DE": "<mapping_name DE>",
        "en_US": "<mapping name EN>"
    },
    "profile": "photoshop_cs6.cson.json", // file for the mapping structure used
    "xml_base": "/x:xmpmeta/rdf:RDF",
    "fields": [
        {
            "type": "element",
            "xml": "/x:xmpmeta",
            "attributes": {
                "xmlns:x": "adobe:ns:meta/",
                "x:xmptk": "Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27"
            }
        },
        {
            "type": "element",
            "xml": "/x:xmpmeta/rdf:RDF",
            "attributes": {
                "xmlns:rdf": "adobe:ns:meta/",
                "x:xmptk": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
            }
        },
        {
            "type": "group",
            "fields": [
                {
                    // for frontend use only
                    "internal_mapping_reference": "0.4.5.2",
                    "type": "element",
                    "xml": "Iptc4xmpCore:CreatorContactInfo",
                    "attributes": {
                        "rdf:parseType": "Resource"
                    }
                },
                {
                    "type": "element",
                    "xml": "Iptc4xmpCore:IntellectualGenre",
                    "attributes": {},
                    "text": "Profile"
                },
                {
                    "type": "text",
                    "xml": "Iptc4xmpCore:CreatorContactInfo/Iptc4xmpCore:CiAdrExtadr",
                    "easydb": [
                        "bilder.titel",
                        "video.titel",
                        "bilder._nested:bilder__schlagwort.lk_schlagwort_id.schlagwort.name"
                    ],
                    "concat": ", " // if previous attribute value exists, then use "," before the bilder.id value
                },
                {
                    "type": "attribute",
                    "xml": "Iptc4xmpCore:CreatorContactInfo/Iptc4xmpCore:CiAdrExtadr",
                    "attribute": "easydb_id",
                    "easydb": "bilder.id",
                    "concat": ", "
                },
                {
                    "type": "attribute",
                    "xml": "Iptc4xmpCore:CreatorContactInfo/Iptc4xmpCore:CiAdrExtadr",
                    "attribute": "easydb_id",
                    "easydb": "video.id",
                    "concat": ", "
                },
                // writing of l10n_text files
                {
                    "type": "text",
                    "xml": "dc:description/rdf:bag",
                    // with language_attribute given, multiple element dc:description are created for each
                    // language found in the data of bilder.description
                    "language_attribute": "xml:lang",
                    "easydb": "bilder.description",
                    "concat": ", "
                },
                // writing of text (fixed value)
                {
                    "type": "text_fixed",
                    "xml": "dc:description/rdf:bag",
                    "text": "fixed text"
                },
                // writing of l10n text (fixed l10n value)
                {
                    "type": "text_fixed",
                    "xml": "dc:description/rdf:bag",
                    "language_attribute": "xml:lang",
                    "text": {
                        "de-DE": "fixed text",
                        "en-US": "fixed text"
                    }
                },
                // save the artist in "<dc:artist>Schneider, Helge</dc:artist>"
                {
                    "type": "text",
                    "xml": "dc:artist",
                    "easydb": "bilder.lk_kuenstler_id.kuenstler.name"
                },
                {
                    "type": "text",
                    "xml": "dc:artist",
                    "easydb": "bilder.lk_kuenstler_id.kuenstler.vorname",
                    "concat": ", "
                },
                // save the url of a file
                {
                    "type": "text_eas_url",
                    "xml": "file_url",
                    "easydb": "bilder.datei",
                    "version": "original", // original | huge | medium | small
                    "watermark": null      // false | true | null
                },
                // save the artist, if it is a singer
                {
                    "type": "text",
                    "xml": "/dc:singer",
                    "empty": true, // write element even if it is empty?
                    "conditions": [
                        {
                            "type": "any", // any | all | none
                            "list": [
                                {
                                    "type": "eq_no_case",
                                    "easydb": "bilder.lk_kuenstler_id.kuenstler.type",
                                    "value": "singer"
                                },
                                {
                                    "type": "eq",
                                    "easydb": "bilder.lk_kuenstler_id.kuenstler.type",
                                    "value": "Sänger"
                                }
                            ]
                        }
                    ],
                    "easydb": [
                        "bilder.lk_kuenstler_id.kuenstler.name",
                        "bilder.lk_kuenstler_id.kuenstler.vorname"
                    ],
                    "concat": ", "
                },
                // write artist id into attribute von "dc:artist"
                {
                    "type": "attribute",
                    "xml": "/dc:artist",
                    "name": "easydb:artist-id",
                    "easydb": [
                        "bilder.lk_kuenstler_id"
                    ]
                },
                // nested table with linked object (schlagwort)
                {
                    "type": "list",
                    "xml": "/dc:subject/rdf:Bag/rdf:li",
                    "fields": [
                        {
                            "type": "text",
                            "easydb": [
                                "bilder._nested:bilder__schlagwort.lk_schlagwort_id.schlagwort.name"
                            ]
                        }
                    ]
                },
                // nested table with linked object (ort)
                {
                    "type": "list",
                    "xml": "/Iptc4xmpExt:Locations/Iptc4xmpExt:Location",
                    "fields": [
                        {
                            "type": "element",
                            "xml": "rdf:Bag/rdf:li",
                            "attributes": {
                                "rdf:parseType": "Resource"
                            }
                        },
                        {
                            "type": "text",
                            "xml": "rdf:Bag/rdf:li/Iptc4xmpExt:City",
                            "easydb": [
                                "bilder._nested:bilder__orte.lk_ort_id.ort.ort"
                            ]
                        }
                    ]
                },
                // nested tables are kept
                {
                    "type": "list",
                    "xml": "/materialen/material",
                    "fields": [
                        {
                            "type": "text",
                            "xml": "name",
                            "easydb": [
                                "bilder._nested:bilder__material.name"
                            ]
                        },
                        {
                            "type": "list",
                            "xml": "techniken/technik",
                            "fields": [
                                {
                                    "type": "text",
                                    "easydb": [
                                        "bilder._nested:bilder__material._nested:bilder__material__technik.lk_technik_id.technik.name"
                                    ]
                                }
                            ]
                        }
                    ]
                },
                // merge from second nested table into first nested table
                {
                    "type": "list",
                    "xml": "/materialen/material",
                    "fields": [
                        {
                            "type": "text",
                            "xml": "name",
                            "easydb": [
                                "bilder._nested:bilder__material.name"
                            ]
                        },
                        {
                            "type": "text",
                            "xml": "technik",
                            "easydb": [
                                "bilder._nested:bilder__material._nested:bilder__material__technik.lk_technik_id.technik.name"
                            ],
                            "concat": ", "
                        }
                    ]
                }
            ]
        }
    ]
}
```
<!--
```javascript
  bilder.titel
  video.titel
  bilder.lk_ort_id.ort.name
  [
    bilder._nested:bilder__schlagwort.bemerkung
    bilder._nested:bilder__schlagwort.lk_kuenstler_id.kuenstler.name
    bilder._nested:bilder__schlagwort.lk_kuenstler_id.kuenstler.vorname
  ,
    bilder._nested:bilder__schlagwort.bemerkung
    bilder._nested:bilder__schlagwort.lk_schlagwort_id.schlagwort.name
  ]


       <Iptc4xmpExt:Locations>
         <Iptc4xmpExt:Location>
            <rdf:Bag>
               <rdf:li rdf:parseType="Resource">
                  <Iptc4xmpExt:Sublocation>Moore family farm</Iptc4xmpExt:Sublocation>
                  <Iptc4xmpExt:City>Watseka</Iptc4xmpExt:City>
                  <Iptc4xmpExt:ProvinceState>Illinois</Iptc4xmpExt:ProvinceState>
                  <Iptc4xmpExt:CountryName>United States of America</Iptc4xmpExt:CountryName>
                  <Iptc4xmpExt:CountryCode>US</Iptc4xmpExt:CountryCode>
                  <Iptc4xmpExt:WorldRegion>North America</Iptc4xmpExt:WorldRegion>
               </rdf:li>
            </rdf:Bag>
         </Iptc4xmpExt:Location>
         <Iptc4xmpExt:Location>
            <rdf:Bag>
               <rdf:li rdf:parseType="Resource">
                  <Iptc4xmpExt:Sublocation>Moore family farm</Iptc4xmpExt:Sublocation>
                  <Iptc4xmpExt:City>Watseka</Iptc4xmpExt:City>
                  <Iptc4xmpExt:ProvinceState>Illinois</Iptc4xmpExt:ProvinceState>
                  <Iptc4xmpExt:CountryName>United States</Iptc4xmpExt:CountryName>
                  <Iptc4xmpExt:CountryCode>US</Iptc4xmpExt:CountryCode>
                  <Iptc4xmpExt:WorldRegion>North America</Iptc4xmpExt:WorldRegion>
               </rdf:li>
            </rdf:Bag>
         </Iptc4xmpExt:Location>
       </Iptc4xmpExt:Locations>





         <Iptc4xmpCore:IntellectualGenre>Profile</Iptc4xmpCore:IntellectualGenre>
         <Iptc4xmpCore:Location>Moore family farm</Iptc4xmpCore:Location>
         <Iptc4xmpCore:CountryCode>US</Iptc4xmpCore:CountryCode>
         <Iptc4xmpCore:CreatorContactInfo rdf:parseType="Resource">
            <Iptc4xmpCore:CiAdrExtadr>Big Newspaper, 123 Main Street</Iptc4xmpCore:CiAdrExtadr>
            <Iptc4xmpCore:CiAdrCity>Boston</Iptc4xmpCore:CiAdrCity>
            <Iptc4xmpCore:CiAdrRegion>Massachusetts</Iptc4xmpCore:CiAdrRegion>
            <Iptc4xmpCore:CiAdrPcode>02134</Iptc4xmpCore:CiAdrPcode>
            <Iptc4xmpCore:CiAdrCtry>United States</Iptc4xmpCore:CiAdrCtry>
            <Iptc4xmpCore:CiTelWork>+1 (800) 1234567</Iptc4xmpCore:CiTelWork>
            <Iptc4xmpCore:CiEmailWork>johndoe@bignewspaper.com</Iptc4xmpCore:CiEmailWork>
            <Iptc4xmpCore:CiUrlWork>http://www.bignewspaper.com</Iptc4xmpCore:CiUrlWork>
         </Iptc4xmpCore:CreatorContactInfo>




         <dc:subject>
            <rdf:Bag>
               <rdf:li>agriculture</rdf:li>
               <rdf:li>farm laborer</rdf:li>
               <rdf:li>farmer</rdf:li>
            </rdf:Bag>
         </dc:subject>



         <dc:rights>
            <rdf:Alt>
               <rdf:li xml:lang="x-default">©2010 Big Newspaper, all rights reserved</rdf:li>
            </rdf:Alt>
         </dc:rights>

```

 -->

See the following table for the definition of the options, that were used in the above example

| Tag       | Option | Function / Meaning |
| --- | --- | --- |
| `displayname` |                | Profile name (how it is shown in the frontend). `"de-DE", "en-US"` for multilanguage selection |
| `xml_base`    |                | Base namespace for the produced XML |
| `tabs`        |                | Contains definitions of multiple tabs |
| `tab`         |                | Definition of a tab (should be unique) |
| `text`        |                | Tab name (how it is shown in the frontend). `"de-DE", "en-US"` for multilanguage selection. |
| `fields`      |                | Definition of fields in a tab |
| `attributes`  |                | Specifiy used namespaces in the XML field |
| `type`        | `Hidden`       | Hidden field, for example for options |
|               | `Ouput`        | Label (how it is shown in the frontend) |
|               | `Input`        | Field for the Input |
| `xml_export`  | `path`         | Mapped metadata field, fully qualified name of the metadata tag |
|               | `list = true`  | Multiple values can be written into the metadata field |
|               | `date = true`  | The metadata field has a date format of schema *YYYY-MM-DD* |
|               | `time = true`  | The metadata field has a time format of schema *HH:MM:SS* |
| `x`           |                | Define a position inside a table on the X axis |
| `y`           |                | Define a position inside a table on the Y axis |

### Get a list of available metadata tags

	GET /api/v1/xmlmapping/tags

Get a List of available metadata tags known to *[exiftool](https://www.sno.phy.queensu.ca/~phil/exiftool/)*. The list is precompiled and was generated by running and reformatting a current version of *exiftool*.

The metadata information is stored in the following structure:

```json
{
    "exiftool_version": "10.40",
    "timestamp": "2019-05-16T17:27:34Z",
    "xmlns": {
		"File": "http://ns.exiftool.ca/File/1.0/",
		...
    },
    "tags": [
        {
            "group": "File",
            "path": "File:ImageWidth",
            "writable": false,
            "description": {
                "de-DE": "Bildbreite",
                "en-US": "Image Width",
                "es-ES": "Ancho Imagen",
                "it-IT": "Larghezza immagine"
            }
		},
		...
    ]
}
```

- `exiftool_version`, `timestamp`
	- information about the time when the tags were generated and which version of *exiftool* was used
- `xmlns`
	- lists known metadata namespaces
- `tags`
	- list of tag definitions:
	- `group`
		- namespace group to which the tag belongs
		- corresponds with the key in `xmlns`
	- `path`
		- fully qualified name of the metadata tag
	- `writable`
		- defines wether *exiftool* allows this tag to be written in a file
		- all tags can be used for import mappings
		- only tags where `writable = true` can be used for export mappings
	- `description`
		- translated description of the tag
		- available in the frontend languages (`"de-DE", "en-US", "es-ES", "it-IT"`), as far as they are available in *exiftool*
