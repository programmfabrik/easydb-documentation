---
title: "93 - dbapi"
menu:
  main:
    name: "dbapi"
    identifier: "technical/internal/dbapi_export/dbapi_export"
    parent: "technical/internal"
---
# dbapi_export

For each mask and version, bare objects are exported and cached in *ez_object_cache*. Bare objects do not contain linked objects, only their IDs. The same
applies to linked users, groups and pools.

When an object is exported, the corresponding bare objects are recursively loaded - that is, searched for and if not found, created and stored - and the
The object is assembled.

When assembling will be:

 - Deleted fields that do not match the format
 - Deleted fields, depending on whether the object is for the index or for the client
 - added users and groups: changelog, owner (*)

(\*) Base-Objekte könnten auch als Datei abgelegt werden. Sie werden aber schon schnell bearbeitet. Man müsste sehen, ob es sich lohnt. Bereits generierte Base-Objekte werden
für die ganze Operation gecacht. Also, wenn beispielsweise der Owner im Changelog auftaucht, was normalerweise der Fall ist, wird er nur einmal generiert.

## Bare objects

### Meta-Info

The field `_meta` contains information for assembling bare objects:

- Standard
- Move-To-All

#### Standard

The field `_meta. _standard` indicates how far standard is ready or needs more information and contains the necessary information to build "_standard",
if necessary:

The fields `text` and `eas` have the following values:

    full ": `_standard. text` or `_standard. eas` is complete, i. e. all information that the object needs to build standard is in the object itself.
    1 ": `_standard. text. 1` or `_standard. eas. 1` is complete, but the others are not
    none ": `_standard. text` or `_standard. eas` is missing completely

The field `value` contains a JSON representation of the default result, where the mask ID and object ID are stored in LinkedObjects.

If an object is built as a main object and `_standard` is "full", the server doesn't have to do anything anymore.
If the object needs a standard (i. e. not "short"), the values for standard must be collected recursively.

If an object is built as a LinkedObject and `_standard` is "1", the server doesn't have to do anything anymore.

#### Move-To-All

The fields `_move_to_all_full` and `_move_to_all_standard` contain values that must be written directly to `_all` because they are needed in fulltext,
but are not in a field indexed with `copy_to_all`.

The fields from `_move_to_all_full` must be copied to `_all` if the object is in a fulltext context.

If the object is rendered in the standard representation or not rendered at all, the values from `_move_to_all_standard` should also be copied. This applies to objects in the
Path and invisible Linked Objects.

## Cache invalidation

The cache is empty at the beginning. There is nothing special to be done with newly created objects.

The cache must be set during processing or Delete (see below).

In addition, the cache must be invalidated if re-indexing is required, that is, if the base schema, user schema, or index version
change.

### Edit object ###

When an object is edited, the cache for the object itself must be cleared.
a the version is incremented, this is not absolutely necessary, but it's good to dispose of old documents from the cache.

In addition, other objects whose versions have not changed must be invalidated:

Hierarchical object types:

For hierarchical object types, the father must be invalidated. If the hierarchy is still linked back, you must
all ancestors will be invalidated.

All descendants must be invalidated.

#### Back-linked objects

While a bare object is being calculated, all backlinked links are collected and stored in "ez_object_cache: dependencies".
When an object is edited, all the objects affected are invalidated using this table, recursively.



