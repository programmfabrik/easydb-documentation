# Retrieve masks

    GET /api/v1/mask/{HEAD|CURRENT}[/<name>]?token=<token>[&format=<format>]

Retrieve the mask definitions for the `CURRENT` or `HEAD` version. If the
parameter `name` is given, retrieve just one mask.

## Path parameters

|   |   |
|---|---|
| `HEAD|CURRENT` | Maskset version |
| `name`         | Mask name, to retrieve a specific mask |

The version that is currently active is `CURRENT`. A new `HEAD` version is created when
the user updates the maskset. Use [/api/v1/schema/commit](/technical/api/schema/schema.md#commit) to commit changes,
so that the HEAD version becomes the new CURRENT.

## Query String

|   |   |
|---|---|
| `token`  | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |
| `format` | The format the definition will be output in (optional): see below |

Available formats:

- `xml`: mask set as XML document (this is the default format)
- `json`: mask set as JSON object

## Output

A [maskset](/technical/types/maskset/maskset.md) containing all masks or just the mask `name` for the requested version.

## Permissions

This call requires an authenticated session. Frontends can use the "system.datamodel.current" right to decide
if they show the maskset to the user.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 403 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 404 | [Not Found](/technical/errors/errors.md#not_found): the requested maskset version / mask was not found |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |





# Generate masks with all fields

    GET /api/v1/mask/{HEAD|CURRENT}/_all_fields?token=<token>[&format=<format>]

Retrieve the mask definitions containing all fields for the `CURRENT` or `HEAD` version.

This call generates a mask for each table in the schema that contains all fields. Notice that this call
does not return actual masks, but generated ones. The idea is that the frontend can have a default mask
that can be used as such or changed. However, in order to be able to use it, it should be updated in the
HEAD maskset using the POST method.

## Path parameters

|   |   |
|---|---|
| `HEAD|CURRENT` | Maskset version |

## Query String

|   |   |
|---|---|
| `token`  | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |
| `format` | Format, like in the previous call |

## Output

A [maskset](/technical/types/maskset/maskset.md) containing the generated masks.

## Permissions

This call requires an authenticated session. Frontends can use the "system.datamodel.current" right to decide
if they show the maskset to the user.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 403 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 404 | [Not Found](/technical/errors/errors.md#not_found): the requested maskset version was not found |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |





# Update user mask definition

    POST /api/v1/mask/HEAD?token=<token>

Update the mask definition for the `HEAD` schema version.

The mask definition has to be in JSON format.

## Query String

|   |   |
|---|---|
| `token`  | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Input

The new [maskset](/technical/types/maskset/maskset.md).

## Output

The updated mask definition.

## Permissions

The user needs the "system.datamodel.development" right.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [No Preferred Mask](/technical/errors/errors.md#no_preferred_mask): no preferred mask was specified for an objecttype (the error parameter specifies which) |
| 400 | [More Than One Preferred Masks](/technical/errors/errors.md#more_than_one_preferred_masks): more than one preferred masks were specified for an objecttype (the error parameter specifies which) |
| 403 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 403 | [No System Right](/technical/errors/errors.md#no_system_right): user lacks the required "system.datamodel.development" right |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |
