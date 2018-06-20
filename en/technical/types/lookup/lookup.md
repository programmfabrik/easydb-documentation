# ID Lookup by Object / Base Type references

During creating / updating objects using POST / PUT, the server needs to link uploaded objects to other objects (hierarchical or as linked objects), and to base types like Pools, Tags etc.

The server parses the JSON Payloads and replaces all lookup keywords with the result of the lookup queries.

## Lookup Keywords

- `"lookup:_id"`: find the ID (`_id`) of an object by the given reference
- `"lookup:_parent_id"`: find the parent ID (`_parent_id`) of a hierarchical object by the given reference

## Lookup Value

```js
{
    "lookup:<id>": {
        "<reference column>": "<value>"
    }
}
```

The Server performs a query to find the corresponding id:

```sql
SELECT "<id>"
    FROM "<table>"
    WHERE "<reference column>" = '<value>'
```

This query must return exactly **1** ID as the result, otherwise the lookup failed.

## Objects / Base Types with references

### Lookups in User Objects

| Referenced ID / Base Type ID | Lookup String | JSON key | Table | Database Column | API |
|---|---|---|---|---|---|
| Object ID | `"lookup:_id"` | `_id` | `<object>` | `"id:pkey"` | `/api/v1/db/<objecttype>` |
| Parent ID for a hierarchical object type | `"lookup:_parent_id"` | `_parent_id` | `<object>` | `"id:parent"` |
| ID of a linked object | `<linked_object>."lookup:_id"` | `<linked_object>._id` | `<linked_object>` | `"id:pkey"` |
| Pool ID | `_pool.pool."lookup:_id"` | `_pool.pool._id` | `ez_pool` | `"ez_pool:id"` |
| Tag ID | `_tags[]."lookup:_id"` | `_tags[]._id` | `ez_tag` | `ez_tag:id` |
| Collection ID |  |  |  |  |

### Lookups in Base Types

| Base Type | Referenced Base Type | Lookup String | JSON key | Table | Database Column | API |
|---|---|---|---|---|---|---|
| Pool | Parent Pool | `"lookup:_parent_id"` |
