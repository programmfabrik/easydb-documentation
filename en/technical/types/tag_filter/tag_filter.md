# Tag filter

A tag filter.

## Attributes

A tag filter is defined by three lists of tags (array of integers). At least one tag must be given in any list. Empty
lists can be ommited.

| Name  | Description |
|-------|-------------|
| `all` | tags that the object must have in order for this filter to work |
| `any` | the object must have at least one of these tags for this filter to work |
| `not` | the object can not have any of these tags, or the filter will fail |

