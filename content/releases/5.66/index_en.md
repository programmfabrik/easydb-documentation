---
menu:
  main:
    name: "5.66"
    identifier: "5.66"
    parent: "releases"
    weight: -566
---

> A re-index is required for this release, please allow adequate time for installing the update. 

# Version 5.66.0

*Published on 22.04.2020*

### Server

*New & Improved*

- /api/group: Groups have an IPv4 filter for subnets now. This allows you to filter group assignments to specific IP address ranges. 
- /api/xmlmapping: Field names are checked for validity.

*Fixed*

- Problems with reindex/purge for multi-instance Elastics installations have been fixed. 
- /api/search: sorting for flat hierarchies was fixed.
- /api/db: `_path` in old versions is now shown correctly.
- /api/export: `easydb_flat` format has been fixed for some cases with reverse nested.

### Webfrontend

*New & Improved*

- messages: The message type `Download` now allows to add a form in which a maximum number of selected checkboxes can be specified.
- Mask management: Improved support for sorting multiple fields.
- CSV importer: Better organization of linked object options and other minor improvements and bug fixes.
- Mask management: Demo data can now be downloaded from the data model instead of just being displayed.
- Basic configuration: For larger input forms a `+` button is now used to add more entries. 
- Connector: Security improvements in password management.

*Fixed*

- The upload settings for folders have in some cases displayed fields from reverse nested without supporting them. The display of the pool in this dialog was also corrected.
- Improved multi-instance support for easydb 6 when closing the sidebar.
- Filtertree: Language dependent output of B.C. data was corrected.
- New objects: The display of pools could get confused in some cases.
