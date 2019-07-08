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

# Webfrontend placeholders

Localization values can have placeholders with different output types and the most common is `string`.

Basically it's necessary to wrap the placeholder's key with **%(`key`)s**. 
The last `s` means that the output will be a plain string, but there is more output types available.

##### Examples of usage:
- Key: `your.csv.key.without-placeholders` 
- Value: `Hello, this is a value without placeholders.`

```javascript
// Without values
let value = $$("your.csv.key.without-placeholders");
// value -> `Hello, this is a value without placeholders.`
```

- Key: `your.csv.key.with-placeholders` 
- Value: `Hello %(username)s, welcome to %(app_name)s. Your account was created on %(date)d. `

```javascript
// With values
let value = $$("your.csv.key.with-placeholders", {
    username: "Guest",
    date: "01.01.2000",
    app_name: "EasyDB"
});
// value -> Hello Guest, welcome to EasyDB. Your account was created on 01/01/2000.
```

- Key: `your.csv.key.with-placeholders` 
- Value: `The objecttype %(objecttype)t supports pools, so it can use the pool %(pool)p.`

```javascript
// With values
let value = $$("your.csv.key.with-placeholders", {
    objecttype: "image_object_type",
    pool: 1,
});
// value -> The objecttype Image supports pools, so it can use the pool Standard Pool.
```

#### Available output types

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

> Note: Except for ```d``` and ```D``` types, the output will be the same as the input if it couldn't be formatted correctly (for example, objecttype doesn't exist).

#### Array input

If the input is an array, it will format each element and output them separated by comma.

It's possible to prepend/append a fixed text. To do so, it's necessary to add a starting and ending ```|``` to the placeholder's key.

> Note: When using prepend/append, the array won't be separated by comma.

##### Example

Key: ```List of values: %(#|value|.)s```

Each element of the array will have ```#``` at the beginning and ```.``` at the ending.

Output: ```List of values: #value1.#value2.#value3.```

Also It's also possible to just prepend or append by leaving one empty. ```List of values: %(#|value|)s```

#### Localization keys in values

Localization keys can be used as values of another localization keys with `$(key)`

##### Example
- Key: `inner.key`
- Value: `Some text`
- Second key: `outer.key`
- Second key value: `The value of the inner key is: $(inner.key)`
- Output: `The value of the inner key is: Some text`