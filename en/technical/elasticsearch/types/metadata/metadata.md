# Metadata

This type contains information about the versions this index works currently with.

| Field                     | Datatype     | Visible | Comments |
|---------------------------|--------------|---------|----------|
| `base_schema_version`     | long         | Yes     | The current base schema version |
| `user_schema_version`     | long         | Yes     | The current user schema version |
| `index_version`           | long         | Yes     | The current index version |

This type only contains one document and is actually never searched, but directly accessed
as "metadata/1".

Easydb uses this information to detect an obsolete mapping that needs to be updated.
The `index_version` and `base_schema_version` can only change when updating the Easydb software.
The `user_schema_version` changes every time a user commits a new schema and maskset version.

If the Easydb notices a change in the `base_schema_version` or the `index_version`, it will destroy
the current index and build a new one, as there may be changes in the mappings that are incompatible
with the code. But in the case of a change of the `index_version`, only the mappings will be updated.
As the objects are reindexed, which may take a long time, the older versions are replaced with the new ones.

The attribute `_schema_version` contains the object's current user schema version.
At a certain moment, there may be objects with different `_schema_version` numbers. The document
"metadata/1" contains the current `user_schema_version`, so that a client can know whether the result of
a search is the current object or an older version.
