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

Localization values can have placeholders to replace them with desired values. 

To use them it's necessary to wrap the placeholder's key with **%(`key`)s**. 
The last `s` means that the output will be a plain `string`, which is the most common type, but there is more output types.

### Examples of usage:

#### Keys definition
| Key | Value |
|---|---|
|`your.csv.key.without-placeholders` | Hello, this is a value without placeholders. |
|`your.csv.key.with-placeholders`| Hello %(username)s, welcome to %(app_name)s. Your account was created on %(date)d. |
|`your.csv.key.with-placeholders`| The objecttype %(objecttype)t supports pools, so it can use the pool %(pool)p. |

#### Javascript usage

```javascript
// Without values
let value = $$("your.csv.key.without-placeholders");
// value -> `Hello, this is a value without placeholders.`
```

```javascript
// With values
let value = $$("your.csv.key.with-placeholders", {
    username: "Guest",
    date: "01.01.2000",
    app_name: "EasyDB"
});
// value -> Hello Guest, welcome to EasyDB. Your account was created on 01/01/2000.
```

```javascript
// With values
let value = $$("your.csv.key.with-placeholders", {
    objecttype: "image_object_type",
    pool: 1,
});
// value -> The objecttype Image supports pools, so it can use the pool Standard Pool.
```

## Available output types

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

> The output will be the same as the input if it couldn't be formatted correctly (for example, objecttype doesn't exist), 
excepting for ```d``` and ```D``` types, where the output will be null.

## Array input

If the input is an array, it will format each element and output them separated by comma, unless it has a prepend/append value, where it won't be separated by comma but for that value.

The prepend/append value is a fixed text that can be added to the key. To do so, add a starting and ending ```|``` to the placeholder's key. 
As a result, after each value is formatted, the prepend/append value will be added at the beginning/ending of it.

To just append or just prepend, leave the value empty.

### Examples

| Key | Output |
|---|---|
|`List of values separated by comma: %(values)s`|List of values separated by comma: value1, value2, value3 |
|<code>List of values with prepend and append value (using markdown): \n%(*&#124;values&#124;\n)s</code>| List of values with prepend and append value: <br>• value1<br>• value2<br>• value3<br>|
|<code>List of values with append value (using markdown): \n%(&#124;values&#124;\n)s</code>|List of values with append value: <br>value1<br>value2<br>value3<br>|
|<code>List of values with prepend value: %(#&#124;values&#124;)s</code>|List of values with prepend value: #value1#value2#value3|

## Localization keys in values

Localization keys can be used as values of another localization keys with `$(key)`

### Example
| First key | First value | Second key | Second value | Output |
|---|---|---|---|---|
|`inner.key`|Some text|`outer.key`|The value of the inner key is: $(inner.key)| The value of the inner key is: Some text|