---
title: "140 - Tag Entry"
menu:
  main:
    name: "Tag Entry"
    identifier: "technical/types/tag_entry"
    parent: "technical/types"
---
# Tag Entry

An entry in a tag list. It identifies the tag and can optionally have parameters.
See [tag management](/en/technical/tagmanagement) for detailed information.

## Attributes

| Name          | Description                                                                                               |
|---------------|-----------------------------------------------------------------------------------------------------------|
| `_id`         | Tag ID (integer, rw): ref [tag](/en/technical/types/tag).\_id |
| `is_default`  | Marks this tag as "default" (boolean, optional): defaults to **false** |
| `sticky`      | Specifies that this entry should be sticky in hierarchies (boolean, optional): defaults to **false** |
| `enabled`     | Specifies if the tag is enabled (boolean, r) |

Remarks:

- `is_default` is only available for pools and objecttypes
- `sticky` is only available for pools
- `enabled` is only available for pools

