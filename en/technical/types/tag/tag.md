# Tag

Tags can be attached to different kinds of base and user objects. They can be used to assign rights, as well
as to build workflows.

Tags can be grouped in "tag groups".

## <a name="tag"></a> Tag description

| Name         | Description                                                                                                  |
|--------------|--------------------------------------------------------------------------------------------------------------|
| `_basetype`  | Name of the base type (string, r): **tag**                                                                   |
| `_acl`       | ACL (array of [acl entries](/technical/types/acl_entry/acl_entry.html), rw, optional)                                            |
| `tag`        | Tag attributes:                                                                                              |
| &#8614; `_id`            | Tag ID (integer, unique, r)                                                                      |
| &#8614; `type`           | Tag type (string, optional, rw): **individual** (default), **all\_versions**                     |
| &#8614; `displaytype`    | Display type (string, rw)                                                                        |
| &#8614; `enabled`        | Mark this tag as enabled (boolean, optional, rw): defaults to **true**                           |
| &#8614; `sticky`         | Mark this tag as sticky (boolean, optional, rw): defaults to **false**                           |
| &#8614; `is_default`     | Mark this tag as being default (boolean, optional, rw): defaults to **false**                    |
| &#8614; `displayname`    | Name to display for the tag ([l10n](/technical/types/l10n/l10n.html), unique in the context of a tag group, rw) |
| &#8614; `description`    | Description of the tag ([l10n](/technical/types/l10n/l10n.html), optional, rw)                                  |
| &#8614; `frontend_prefs` | Frontend preferences (JSON object, optional, nullable, rw)                                       |

For information about the meaning of `enabled` and `sticky`, see [rights management](/technical/rightsmanagement/rightsmanagement.html).

The tag type controls how this tag will be used across versions:

- **individual** tags are set for a specific object version
- **all\_versions** tags: the current version sets or unsets the global tags for all versions

## <a name="taggroup"></a> Tag group description

| Name         | Description                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------|
| `_basetype`  | Name of the base type (string, r): **taggroup**                                                        |
| `_tags`      | Tags in this tag group (array of [tag descriptions](/technical/types/tag/tag.html#tag), rw)                          |
| `taggroup`   | Tag group attributes:                                                                                  |
| &#8614; `_id`         | Tag group ID (integer, unique, r)                                                             |
| &#8614; `type`        | Tag group type (string, rw): **checkbox**, **choice**                                         |
| &#8614; `displayname` | Name to display for the tag group ([l10n](/technical/types/l10n/l10n.html), unique, rw)                      |

## Related operations

- [/tag](/technical/api/tags/tags.html): set/change tags

