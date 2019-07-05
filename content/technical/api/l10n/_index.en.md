---
title: "64 - l10n"
menu:
  main:
    name: "l10n"
    identifier: "technical/api/l10n"
    parent: "technical/api"
---
# Retrieve localization keys

    GET /api/v1/l10n/user/{CURRENT|HEAD|<version>}?token=<token>

Retrieve localization keys for user schema.

## Path parameters

|   |   |
|---|---|
| `CURRENT`, `HEAD` or `<version>` | Schema version |

## Query String

|   |   |
|---|---|
| `token`   | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Output

The localization keys

## Permissions

The session must be authenticated.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 500 | [Server error](/en/technical/errors): internal server error |





# Update localization keys

    POST /api/v1/l10n/user/{CURRENT|HEAD}?token=<token>

Update localization keys for the user schema.
Changes of localization keys require a frontend reload for all other users of the system.

## Path parameters

|   |   |
|---|---|
| `CURRENT` or `HEAD` | Schema version |

## Query String

|   |   |
|---|---|
| `token`   | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Permissions

The system right "system.datamodel" with level "development" is required.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [No System Right](/en/technical/errors): the user lacks the required system right |
| 500 | [Server error](/en/technical/errors): internal server error |

# Webfrontend

#### Placeholders

Localization values can have placeholders with different output types and the most common is `string`. 

Example: ```Welcome %(username)!```

Basically it's necessary to wrap the placeholder's key with **%(`key`)s**. The last `s` means that the output will be a plain string.

| Type | Input | Output |
|---|---|---|
| s | String | String |
| D | String date | Formatted Date |
| d | String date | Formatted Date & time |
| t | Objecttype name | Localized objecttype name |
| c | ```<table_name>.<column_name>``` | Localized column name |
| p | Pool ID | Localized pool name |
| g | Group ID | Localized group name |
| m | Mask ID | Localized mask name |
| r | Server right name | Localized right name |

Note: Except for ```d``` and ```D``` types, the output will be the same as the input if it couldn't be formatted correctly (for example, objecttype doesn't exist).

#### Usage of localization keys in the frontend:

```javascript
// Without values
let value = $$("your.csv.key.without-placeholders");


// With values
value = $$("your.csv.key.with-placeholders", {
    username: "Guest"
});
```

