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
