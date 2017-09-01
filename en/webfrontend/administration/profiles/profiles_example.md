# Profile: Example

The following example defines an export profile with two tabs. The "Basic" tab with the fields "Title" and "Date", as well as another tab "IPTC" without fields. In order to create a valid XML in the mapping, "names" are used in "attributes".

```
displayname:
	"de-DE": "Beispiel für ein Exportprofil"
	"en-US": "Example"

xml_base: "/ExifTool:exiftool"

tabs: [
	tab: "base"

	text:
		"de-DE": "Basis"
		"en-US": "Base"

	fields: [
		type: "Hidden"
		attributes:
			"xmlns:ExifTool": "http://ns.exiftool.ca/ExifTool/1.0/"
			"xmlns:ExifIFD": "http://ns.exiftool.ca/EXIF/ExifIFD/1.0/"
			"xmlns:IFD0": "http://ns.exiftool.ca/EXIF/IFD0/1.0/"
			"xmlns:IPTC": "http://ns.exiftool.ca/IPTC/IPTC/1.0/"
			"xmlns:XMP-iptcCore": "http://ns.exiftool.ca/XMP/XMP-iptcCore/1.0/"
			"xmlns:XMP-dc": "http://ns.exiftool.ca/XMP/XMP-dc/1.0/"
	,
		type: "Output"
		text:
			"de-DE": "Titel"
			"en-US": "Title"
		x: 0
		y: 0
	,
		type: "Input"
		xml_export: [
			path: "XMP-dc:Title"
			l10n: true
		,
			path: "IPTC:Headline"
		]
		x: 1
		y: 0
	,
		type: "Output"
		text:
			"de-DE": "Datum"
			"en-US": "Date"
		x: 0
		y: 1
	,
		type: "Input"
		xml_export: [
			path: "XMP-dc:Date"
			list: true
			date: true
			time: true
		,
			path: "IPTC:DateCreated"
			date: true
		,
			path: "IPTC:TimeCreated"
			time: true
		]
		x: 1
		y: 1
	]
,
	tab: "iptc"

	text:
		"de-DE": "IPTC"
		"en-US": "IPTC"

	fields: [
	
	]
]
```