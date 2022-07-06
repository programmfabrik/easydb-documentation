---
menu:
  main:
    name: "5.102 (Late June 2022)"
    identifier: "5.102"
    parent: "releases"
    weight: -602
---

> This version **does not require a new index build**

# Version 5.102.1

*Released on 06.07.2022*

# Webfrontend
## Fixed

* fixed internal function used by external plugin
* fixed template for date range fields in editor

# Server
## Fixed

* fixed error in database upgrade
* fixed metadata mapping in export

# Version 5.102.0

*Released on 29.06.2022*

# Webfrontend

## New

* The deep link url for objects has been changed. It now uses the `UUID` of the object instead of the `ID`. Works with old urls that use the `ID`
* Added support for custom data types in the metadata mapping
* Added a new option in the Objecttype manager which can be used to dynamically add new menu buttons that open a list view for the specific objecttype

## Improved

* Now the datamodel shows the internal names and masks next to the localized name in the list
* Now the view preferences on collections are persisted
* Now in the datamodel editor the field option "Range" with the check "Mandatory" shows a info tag on the field
* Added a new internal attribute in date range columns when having the textual representation activated. It is used to keep the textual representation entered by the user instead of replacing it with the automatic textual representation
* Date range columns with textual representation activated allow open from/to dates when using `after` and `before` words
* Start filtering when having at least one character in the filter
* Removed the filter checkbox for number fields in the mask editor
* Save the selected `filters` when saving a search
* Allow adding new tags to an object that would cause the user to lose permissions after saving

## Fixed

* Fixed a bug where in some situations duplicate eas check creates an empty record
* In the event manager the button "Show" is not visible when the event is for a deleted record
* Fixed the asset browser showing the watermark version of images when the image is too small. The watermark previews are only shown if there is no other version available
* Fixed the filename suggestion (for `file` fields) in the expert search and added a new internal parameter in the api
* **Search token**: Fixed the display of the suggested token when having multiple tokens in the expert search
* Fixed a problem when using the 'dive' feature of hierarchical objects in the search result when using the connector plugin
* Fixed a problem in the group editor when having a nested together with a multilingual text field

# Server

## New

* **Datamodel**: the field type `daterange` has a new multilanguage text field to save free text with the date values

## Improved

* **Search**: subfields for `daterange` field types (`.from`, `.to`) can be used for searching and sorting
* **Event Polling**: `API_PROGRESS` events have a limited info object when events are polled, while no other event type has an info object for polling
* **/api/v1/db**: further improvements for `all_versions=true` (bulk API in preparation for migration purposes)

## Fixed

* **Datamodel**: fixed renaming of multilanguage text fields
* **CSV Export**: exporting of URLs of asset versions fixed and restructured (selected version URLs from export dialog are considered)
* User picture in the user dialogue was sometimes removed, this is avoided now


# Checksums

Here are the checksums of our Docker images (latest version): 

```ini
docker.easydb.de/pf/chrome               sha256:ba4c705b074e7752c90edb6397cf405ca34030e9f58dc95750dd7d3b94e4a488
docker.easydb.de/pf/eas                  sha256:27a523e91a9321d10896019c4f002ebdd9b88b9e448ac7a1b42dd14379687291
docker.easydb.de/pf/elasticsearch        sha256:2e3fa619198a63ae432fd4cb25d295e7e017563186c5c5a42c3f0fdba2ef20f8
docker.easydb.de/pf/fylr                 sha256:a501864a51611ca067fcaaccbcec0395aa3853ac5442fb2d14c0bbfbb5284b74
docker.easydb.de/pf/postgresql-11        sha256:da6ab72d9726b921e55121ed9329c1a236b5922db531e73a23bb042c36c45251
docker.easydb.de/pf/postgresql-14        sha256:53d1e9cff20dc6d942fbb9f9abb0410cf6a09d522f4aa7258b0659195cb6108e
docker.easydb.de/pf/server-base          sha256:d338ebabe00ee81cd62363bda4164d2ba1e6960b4d6c100c5647a468d1f31a13
docker.easydb.de/pf/webfrontend          sha256:4e40150a6f17092b8be6365d51bb8fc3844e36766ed6c76826891e52e74c7a2f
```
