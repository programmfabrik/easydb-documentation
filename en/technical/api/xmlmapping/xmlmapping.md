# Save, load metadata profiles from import and export

###### GET /api/v1/xmlmapping/list?token=\<token\>

Returns a list of available profiles and mappings. Each mapping is linked to one profile. Profiles are stored in

`frontend-schema/base/xmlmapping-profiles/[<profile>[.cson.json|.json]]`

```js
[
	{
		profile: "photoshop.cson.json",
		displayname: {
			de_DE: "...",
			en_US: "..."
		},
		mappings: [
		    {
			   id: 2
			   displayname: [
			      de_DE: "...",
				  en_US: "..."
			   }
		    }
		]
	}
]
```

###### GET /api/v1/xmlmapping/profile/<profile-name>?token=\<token\>

Returns the profile.


###### PUT /api/v1/xmlmapping/mapping?token=\<token\>

Create a new metadata mapping. Mappings are stored per db for all users. Mappings get updated on schema updates.

`frontend-schema/<db>/<current>/xmlmapping-mappings/<mapping>.json`


###### POST /api/v1/xmlmapping/mapping/\<id\>?token=\<token\>

Update a metadata mapping.


###### GET /api/v1/xmlmapping/mapping/\<id\>?token=\<token\>

Get a metadata mapping.


###### DELETE /api/v1/xmlmapping/mapping/\<id\>?token=\<token\>


- *xml\_base*:    xml-base in "/" notation als basis für alle xml element
- *xml*:         name des elements, wenn relativ dann zum übergeordneten feld und am ende zur xml_base

field types:

- *element*:     erzeugt ein element mit fixen attributen und fixem text
- *text*:        befüllen eines element-texts mit informationen aus der easydb, optional versehen mit "concat" und "condition"
- *attribute*:   befüllen eines attributes mit informationen aus der easydb
- *list*:        befüllen sich wiederholender element mit informationen aus der easydb, enthält "fields"


```js
{
  "id": <id> // issued by the server
  "displayname": {
    de_DE: "<mapping_name DE>"
	en_US: "<mapping name EN>"
  }
  "profile": "photoshop_cs6.cson.json" // file for the mapping structure used
  "xml_base": "/x:xmpmeta/rdf:RDF"
  "fields": [
     {
	    type: "element"
        xml: "/x:xmpmeta"
		attributes: {
			"xmlns:x": "adobe:ns:meta/"
			"x:xmptk": "Adobe XMP Core 5.3-c011 66.145661, 2012/02/06-14:56:27"
		}
	 },
	 {
	    type: "element"
        xml: "/x:xmpmeta/rdf:RDF"
		attributes: {
			"xmlns:rdf": "adobe:ns:meta/"
			"x:xmptk": "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
		}
	 },
	 {
        type: "group",
		fields: [
            {
				// for frontend use only
				internal_mapping_reference: "0.4.5.2"
				type: "element"
			    xml: "Iptc4xmpCore:CreatorContactInfo"
				attributes: {
					"rdf:parseType": "Resource"
				}
			},
            {
				type: "element"
			    xml: "Iptc4xmpCore:IntellectualGenre"
				attributes: {}
				text: "Profile"
			},
            {
				type: "text"
			    xml: "Iptc4xmpCore:CreatorContactInfo/Iptc4xmpCore:CiAdrExtadr"
				easydb: ["bilder.titel","video.titel","bilder._nested:bilder__schlagwort.lk_schlagwort_id.schlagwort.name"]
				concat: ", "
			},
            {
				type: "attribute"
			    xml: "Iptc4xmpCore:CreatorContactInfo/Iptc4xmpCore:CiAdrExtadr"
				attribute: "easydb_id"
				easydb: "bilder.id"
				concat: ", " // if previous attribute value exists, then use "," before the bilder.id value
			},
            {
				type: "attribute"
			    xml: "Iptc4xmpCore:CreatorContactInfo/Iptc4xmpCore:CiAdrExtadr"
				attribute: "easydb_id"
				easydb: "video.id"
				concat: ", "
			},
			// writing of l10n_text files
            {
				type: "text"
			    xml: "dc:description/rdf:bag"
				// with language_attribute given, multiple element dc:description are created for each
				// language found in the data of bilder.description
				language_attribute: "xml:lang"
				easydb: "bilder.description"
				concat: ", "
			},
			// writing of text (fixed value)
            {
				type: "text_fixed"
			    xml: "dc:description/rdf:bag"
				text: "fixed text"
			},
			// writing of l10n text (fixed l10n value)
            {
				type: "text_fixed"
			    xml: "dc:description/rdf:bag"
				language_attribute: "xml:lang"
				text: {
				  "de-DE": "fixed text"
				  "en-US": "fixed text"
				}
			},
			// schreibt kuenstler in <dc:artist>Schneider, Helge</dc:artist>
            {
				type: "text"
			    xml: "dc:artist"
				easydb: "bilder.lk_kuenstler_id.kuenstler.name"
			},
            {
				type: "text"
			    xml: "dc:artist"
				easydb: "bilder.lk_kuenstler_id.kuenstler.vorname"
				concat: ", "
			},
			// schreibt URL einer datei
            {
				type: "text_eas_url"
			    xml: "file_url"
				easydb: "bilder.datei"
				version: "original|huge|medium|small"
				watermark: false|true|null
			},
			// schreibt kuenstler, wenn Sänger
            {
				type: "text"
			    xml: "/dc:singer"
				// write element even if it is empty?
				empty: true|false
				conditions: [
					{
						type: "any|all|none"
						list: [
							{
								type: "eq_no_case",
								easydb: "bilder.lk_kuenstler_id.kuenstler.type",
								value: "singer"
							},
							{
								type: "eq",
								easydb: "bilder.lk_kuenstler_id.kuenstler.type",
								value: "Sänger"
							}
						]
					}
				],
				easydb: ["bilder.lk_kuenstler_id.kuenstler.name", "bilder.lk_kuenstler_id.kuenstler.vorname"]
				concat: ", "
			},
			// schreibt kuenstler id in attribute von dc:artist
            {
				type: "attribute"
			    xml: "/dc:artist"
				name: "easydb:artist-id"
				easydb: ["bilder.lk_kuenstler_id"]
			},
			// 1 wiederholgruppe mit verlinktem objekt (schlagwort)
            {
				type: "list"
			    xml: "/dc:subject/rdf:Bag/rdf:li"
				fields: [
					{
						type: "text"
						easydb: ["bilder._nested:bilder__schlagwort.lk_schlagwort_id.schlagwort.name"]
					}
				]
			},
			// 1 wiederholgruppe mit verlinktem objekt (ort)
            {
				type: "list"
			    xml: "/Iptc4xmpExt:Locations/Iptc4xmpExt:Location"
				fields: [
					{
						type: "element"
					xml: "rdf:Bag/rdf:li"
						attributes: {"rdf:parseType": "Resource"}
					},
					{
						type: "text"
						xml: "rdf:Bag/rdf:li/Iptc4xmpExt:City"
						easydb: ["bilder._nested:bilder__orte.lk_ort_id.ort.ort"]
					}
				]
			},
			// 2 wiederholgruppen bleiben erhalten
            {
				type: "list"
			    xml: "/materialen/material"
				fields: [
					{
						type: "text"
						xml: "name"
						easydb: ["bilder._nested:bilder__material.name"]
					},
					{
						type: "list"
						xml: "techniken/technik"
						fields: [
							{
								type: "text"
								easydb: ["bilder._nested:bilder__material._nested:bilder__material__technik.lk_technik_id.technik.name"]
							}
						]
					}
				]
			},
			// aus 2. wiederholgruppe merge in die 1. wiederholgruppe
            {
				type: "list"
			    xml: "/materialen/material"
				fields: [
					{
						type: "text"
						xml: "name"
						easydb: ["bilder._nested:bilder__material.name"]
					},
					{
						type: "text"
						xml: "technik"
						easydb: ["bilder._nested:bilder__material._nested:bilder__material__technik.lk_technik_id.technik.name"]
						concat: ", "
					}
				]
			}
		]
     }
  ]




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

Die Definition der einzelnen in dem Beispiel verwendeten Optionen, entnehmen Sie der nachstehenden Tabelle:

| Tag       | Option | Funktion / Bedeutung       |
| ------------- |:-------------:| -----|
| displayname	|				| Ist der im Frontend anzuzeigende Text des Profilnamens (de-DE o. en-US: Anzeige je nach Sprachauswahl). |
| xml_base		|				| Ist die Basis für das zu erzeugende XML. |
| tabs			|				| Dienst zur Verwendung mehrere Tabs. |
| tab			| 				| Dient zur Definition eines Tabs (sollte eindeutig sein). |
| text			| 				| Ist die im Frontend anzuzeigende Tab- oder Labelbeschriftung (de-DE o. en-US: Anzeige je nach Sprachauswahl). |
| fields		| 				| Definiert die Felder innerhalb eines Tabs. |
| attributes	|				| Dienst der Angabe verwendeter Namespaces innerhalb des zu erzeugenden XML-Files. |
| type			| Hidden 		| Nicht sichtbares Feld. Z.B. für Optionen |
| 				| Ouput 		| Anzuzeigendes Label |
| 				| Input 		| Feld für die Eingabe |
| xml_export	| path			| Angabe des Metadatenfeldes, auf welches gemappt werden soll. |
|				| list = true	| Gibt an, ob in das Metdatenfeld mehrere Werte geschrieben werden können. |
|				| date = true	| Gibt an, ob es sich um ein Datumsformat nach Schema *2015-06-15* handelt. |
|				| time = true	| Gibt an, ob es sich um ein Uhrzeitformat nach Schema *12:05:16* handelt. |
| x				| 				| Definiert die Position innerhalb einer Tabelle auf der X-Achse. |
| y				| 				| Definiert die Position innerhalb einer Tabelle auf der Y-Achse. |
