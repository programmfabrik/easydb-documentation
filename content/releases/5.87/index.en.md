---
menu:
  main:
    name: "5.87 (Late July 2021)"
    identifier: "5.87"
    parent: "releases"
    weight: -587
---

> **No re-index** is necessary for this release. 

# Version 5.87.2

*Released on 02.08.2021*

## Web frontend

### Improved

- **Detail**: Display of linked objects without file has been streamlined.

### Fixed

- **Search**: Display problem in table view when switching object types quickly has been fixed.
- **Users / group searches**: Archived users are no longer displayed.

### Server

- **/api/objects**: Format *xml_easydb* could not be produced in some cases and reported a timeout.

# Version 5.87.1

*Published on 29.07.2021*

## Web frontend

### Fixed

- **Search**: fixed error when loading search in data models with linked objects for EAS standard fields.

# Version 5.87.0

*Released on 28.07.2021*

## Web frontend

### New

- **Group manager**: IP filter now understands IPv6 (easydb 6 only).

### Improved

- **Plugin Typo3**: Combined fields are no longer separated with a ;.
- **Export manager**: The event information is displayed completely in a tooltip.

### Fixed

- **Dialogs**: HTML escaping was fixed in some dialogs.
- **Datamodel**: When opening the data model, a consistency check is performed and a message is displayed if the model has problems. We have corrected an inconsistency in reverse linked masks which can be fixed by resaving the data model (and activating it afterwards). 
- The **configured logo** was not displayed correctly in Firefox in some cases.

## Server

### New

- **Mask management**: A new option allows to create the default info with only the first entry in a multiple field.
- Files with extension `.obj` are added to the `vector3d` file class.

### Improved

- **XML export**: For hierarchical objects _has_children is exported as well. For reverse linked objects the _system_object_id is exported.
- **/api/settings**: New field version. This version is the only version we leave in the API for easydb 6.
- **Export**: Settings how many exports can be created at the same time in the background. This allows better resource management in larger installations.
- **All plugins** delivered by Programmfabrik are now in their own repositories. This change should have no visible impact but is a preparation for compatibility with easydb 6. 

### Fixed

- **Data model**: Potential internal storage errors have been corrected.
- **Search**: Indexing of time periods for aggregations can now handle time zones.
- **User management**: Verification of allowed characters in usernames.
- **/api/session**: The `cookieauth parameter has been removed and is no longer supported.
- **/api/mask**: improved checking for some cases of incorrect reverse linked fields.
- **/api/mask**: renaming of reverse linked fields is now done correctly.
- **Email**: A problem with sending emails was fixed.

# Checksums

Here are the checksums of our Docker images (latest version): 

```ini
docker.easydb.de/pf/chrome               sha256:ce4ccb312e12cdcb8daa9151e80081738b2612b1c109ecdcb39519e3f367c6ec
docker.easydb.de/pf/eas                  sha256:0f5b60d7aac9d6f3d832b62e2f02bdf2dda0519528ded041308ab29cbb3ee4b1
docker.easydb.de/pf/elasticsearch        sha256:2a9ca9620e35567d8ea6c666055e4377ca556d16b0a619f2198d9cc9fe9bc526
docker.easydb.de/pf/fylr                 sha256:153b381eb3bfdac633a3a119a69a3fc9f16806de0aa83c95e9d2e149fb19d665
docker.easydb.de/pf/postgresql-11        sha256:74a9fa8e0ee63bfe39f11adabbeaa141921fd2443e5735f85b73e249acf4e566
docker.easydb.de/pf/server-base          sha256:b015967978f0e1259cf3cbc6a43d20c51f59b6a6960423239b70455ea212e703
docker.easydb.de/pf/webfrontend          sha256:401925e16c0b6542ffc70cc3427c68fed2c5e674b36ff9beccacbe92a7e50a75
```

*Translated with www.DeepL.com/Translator*

