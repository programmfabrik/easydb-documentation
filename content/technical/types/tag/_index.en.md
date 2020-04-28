---
title: "139 - Tag"
menu:
  main:
    name: "Tag"
    identifier: "technical/types/tag"
    parent: "technical/types"
---
# Tag

Tags can be attached to different kinds of base and user objects. They can be used to assign rights, as well
as to build workflows.

Tags can be grouped in "tag groups".

## <a name="tag"></a> Tag description

| Name         | Description                                                                                                  |
|--------------|--------------------------------------------------------------------------------------------------------------|
| `_basetype`  | Name of the base type (string, r): **tag**                                                                   |
| `_acl`       | ACL (array of [acl entries](/en/technical/types/acl_entry), rw, optional)                                    |
| `tag`        | Tag attributes:                                                                                              |
| &#8614; `_id`            | Tag ID (integer, unique, r)                                                                      |
| &#8614; `lookup:_id`     | [Lookup for tag ID](/en/technical/datamanagement/lookups/#tags)                                  |
| &#8614; `type`           | Tag type (string, optional, rw): **individual** (default), **all\_versions**                     |
| &#8614; `displaytype`    | Display type (string, rw)                                                                        |
| &#8614; `enabled`        | Mark this tag as enabled (boolean, optional, rw): defaults to **true**                           |
| &#8614; `sticky`         | Mark this tag as sticky (boolean, optional, rw): defaults to **false**                           |
| &#8614; `is_default`     | Mark this tag as being default (boolean, optional, rw): defaults to **false**                    |
| &#8614; `displayname`    | Name to display for the tag ([l10n](/en/technical/types/l10n), unique in the context of a tag group, rw) |
| &#8614; `description`    | Description of the tag ([l10n](/en/technical/types/l10n), optional, rw)                          |
| &#8614; `frontend_prefs` | Frontend preferences (JSON object, optional, nullable, rw)                                       |
| &#8614; `reference`      | Tag reference (string, unique, optional, rw): can be used for lookups for `_id`             |
| &#8614; `shortname`      | Tag short name (string, unique, optional, rw): can be used for lookups for `_id`             |

For information about the meaning of `enabled` and `sticky`, see [rights management](/en/technical/rightsmanagement).

The tag type controls how this tag will be used across versions:

- **individual** tags are set for a specific object version
- **all\_versions** tags: the current version sets or unsets the global tags for all versions

## <a name="taggroup"></a> Tag group description

| Name         | Description                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------|
| `_basetype`  | Name of the base type (string, r): **taggroup**                                                        |
| `_tags`      | Tags in this tag group (array of [tag descriptions](/en/technical/types/tag), rw)                      |
| `taggroup`   | Tag group attributes:                                                                                  |
| &#8614; `_id`         | Tag group ID (integer, unique, r)                                                             |
| &#8614; `lookup:_id`  | [Lookup for tag group ID](/en/technical/datamanagement/lookups/#tags)                         |
| &#8614; `type`        | Tag group type (string, rw): **checkbox**, **choice**                                         |
| &#8614; `displayname` | Name to display for the tag group ([l10n](/en/technical/types/l10n), unique, rw)              |
| &#8614; `reference`   | Tag group reference (string, unique, rw): used for lookups for `_id`                          |
| &#8614; `shortname`   | Tag group short name (string, unique, rw)                                                     |

## Related operations

- [/tag](/en/technical/api/tags): set/change tags

