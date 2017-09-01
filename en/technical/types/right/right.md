# Right

A right is identified by a name and may have additionally parameters. The call [/api/right](/technical/api/right/right.md) can be used to
get the right descriptions, which specify how a right is used. When setting rights inside ACLs, you use a right specification.

## <a name="description"></a> Right description

Right descriptions are read-only JSON objects that describe a right.

| Name            | Description                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------------------|
| `name`          | Name of the right (string, unique)                                                                     |
| `type`          | Type of the right (string): **right** or **choice** (see below)                                        |
| `group`         | Group (string, optional): can be used by the frontend to group rights                                  |
| `comment`       | Comment about the right (string, optional)                                                             |
| `parameters`    | Parameters for the right (array of [parameter descriptions](#parameter), optional): for "right" type   |
| `has_grantable` | Whether this right has the `_grantable` flag (boolean): for "right" type                               |
| `rights`        | Rights to choose from (array of [right descriptions](#description), optional): for "choice" type       |

The type "right" represents a normal right. Choice is a construct to group several related rights together, so that the
frontend can show them as a choice and not as single rights. The idea is that a right implies other rights.

## <a name="parameter"></a> Parameter description

| Name          | Description                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------|
| `name`        | Name of the parameter (string)                                                                         |
| `type`        | Type of the parameter (string): see below                                                              |
| `comment`     | Comment about the parameter (string)                                                                   |
| `required`    | Whether the parameter is required when providing a right specification (boolean)                       |
| `range_from`  | Lower bound for the value (integer, optional)                                                          |
| `range_to`    | Upper bound for the value (integer, optional)                                                          |
| `choices`     | Valid values (array of strings, optional)                                                              |

The following table provides information about the parameter types.

| Type                        | Comment |
|-----------------------------|---------|
| **text**                    | `choices` may restrict the parameter value                                    |
| **integer**                 | `range_from` and `range_to` may restrict the parameter value                  |
| **boolean**                 | |
| **mask-select**             | Masks per objecttype |
| **objecttype-select**       | Objecttype filter |
| **pool-select**             | Pool filter |
| **column-select**           | List of asset columns |
| **string-list**             | List of strings |

Notice that rights of type choice are no "real" rights, but groups of rights. The rights inside a choice are identified by
their name; the name of the "choice right" is irrelevant.

## <a name="specification"></a> Rights specification

A rights specification is the way rights are specified for users / groups (`_system_rights`) and inside ACL (`_acl`).

A rights specification is a map containing a key for each right (its name). If the right has parameters, they are given as a map with
the parameter name as key. The parameter value depends on its type:

| Type                  | JSON representation |
|-----------------------|---------------------|
| **text**              | string |
| **integer**           | integer |
| **boolean**           | boolean |
| **mask-select**       | map with an objecttype ID as key and a list of mask IDs as value ([schema-table](/technical/types/schema/schema.md#table).table\_id &#8614; [mask](/technical/types/maskset/maskset.md#mask).mask\_id) (\*) |
| **objecttype-select** | array of objecttype IDs ([schema-table](/technical/types/schema/schema.md#table).table\_id) |
| **pool-select**       | array of pool IDs ([pool](/technical/types/pool/pool.md).pool.\_id) |
| **column-select**     | array of column IDs ([schema-column](/technical/types/schema/schema.md#column).\_id) |
| **string-list**       | array of strings |

Additionally, if the right description specifies that the right has the grantable flag (`has_grantable`), if can be provided as `_grantable` (bool, optional, defaults to **false**);

If the right has no parameters and no grantable flag, its value will be an empty object.

(\*) **mask-select** also allows to specify the standard mask as "standard"

Example:


[include](./rights.json)


## TODO

- `required`, `range_from`, `range_to`, `choices`
- check EAS column ID, mask ID, objecttype ID, pool ID

