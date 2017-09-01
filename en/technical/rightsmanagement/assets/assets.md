# Rights management for assets

These rights affect the manipulation and visibility of asset values for user-defined objects.
The realms for assets are the same realms that apply for [objects](/technical/rightsmanagement/objects/objects.md).
In general, the rights management for assets works the same as for objects.

Asset versions can be subject to rights management or not (see EAS rights management configuration).
The rights `asset_show` and `asset_download` refer only to the rights managed versions (the other ones are always visible).

## Rights

| Right           | Parameters                         | Realm                   | Grantable in collection | Description |
|-----------------|------------------------------------|-------------------------|-------------------------|-------------|
|`asset_show`     | versions (preview-versions)        | object                  | yes | Version is available for this object in the given versions |
|                 | [column_ids (column-select)]       |                         | | |
|`asset_show`     | versions (preview-versions)        | objecttype-without-pool | yes | Version is available for objects of this objecttype (no pool) in the given versions |
|                 | [column_ids (column-select)]       |                         | | |
|`asset_show`     | versions (preview-versions)        | pool                    | yes | Version is available for objects in this pool in the given versions |
|                 | [column_ids (column-select)]       |                         | | |
|`asset_show`     | versions (preview-versions)        | tag                     | yes | Version is available for objects with this tag in the given versions |
|                 | [column_ids (column-select)]       |                         | | |
|`asset_show`     | versions (preview-versions)        | collection              | yes | Version is available for objects in this collection in the given versions |
|                 | [column_ids (column-select)]       |                         | | |
|`asset_download` | versions (preview-versions)        | object                  | yes | Version is available for download for this object in the given versions |
|                 | [column_ids (column-select)]       |                         | | |
|`asset_download` | versions (preview-versions)        | objecttype-without-pool | yes | Version is available for download  for objects of this objecttype (no pool) in the given versions |
|                 | [column_ids (column-select)]       |                         | | |
|`asset_download` | versions (preview-versions)        | pool                    | yes | Version is available for download  for objects in this pool in the given versions |
|                 | [column_ids (column-select)]       |                         | | |
|`asset_download` | versions (preview-versions)        | tag                     | yes | Version is available for download  for objects with this tag in the given versions |
|                 | [column_ids (column-select)]       |                         | | |
|`asset_download` | versions (preview-versions)        | collection              | yes | Version is available for download  for objects in this collection in the given versions |
|                 | [column_ids (column-select)]       |                         | | |
|`asset_upload`   | [column_ids (column-select)]       | objecttype-without-pool | no  | Upload assets for this objecttype |
|                 | [limit (int)]                      |                         |     | |
|                 | [classes (string-list)]            |                         |     | |
|                 | [extensions (string-list)]         |                         |     | |
|                 | [allow_update_and_remove (bool)]   |                         |     | (also allows to remove and replace assets) |
|`asset_upload`   | [column_ids (column-select)]       | pool                    | no  | Upload assets for this pool |
|                 | [limit (int)]                      |                         |     | |
|                 | [classes (string-list)]            |                         |     | |
|                 | [extensions (string-list)]         |                         |     | |
|                 | [allow_update_and_remove (bool)]   |                         |     | (also allows to remove and replace assets) |
|`asset_upload`   | [column_ids (column-select)]       | collection              | no  | Upload assets for this collection |
|                 | [limit (int)]                      |                         |     | |
|                 | [classes (string-list)]            |                         |     | |
|                 | [extensions (string-list)]         |                         |     | |
|                 | [allow_update_and_remove (bool)]   |                         |     | (also allows to remove and replace assets) |

Asset rights can be filtered. In all cases, an empty attribute means "do not filter":

- `column_ids`: which columns are affected by the right; if this parameter does not exist or its value is an empty array, all columns are allowed
- `limit`: limit (in bytes) for an upload
- `classes`: allowed file classes for an upload: if a class is allowed, uploading files of the class is allowed regardless of their extension
- `extensions`: allowed file extensions for an upload

The versions have a hierarchy, defined by their order in the settings file.
