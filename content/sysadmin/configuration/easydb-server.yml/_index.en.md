---
title: "easydb-server.yml"
layout: config
menu:
  main:
    name: "easydb-server.yml"
    identifier: "sysadmin/configuration/easydb-server.yml"
    parent: "sysadmin/configuration"
    weight: 20
---

# easydb-server.yml

## Types

Variables are structured in maps, but a general map is not a valid type for a variable. The types supported are:

| Easydb-Type   | YAML-Type                | Comments |
|---------------|--------------------------|----------|
| String        | String                   | |
| Integer       | Integer                  | |
| Boolean       | Boolean, String, Integer | `true`: `true, "on", "1", 1` |
|               |                          | `false`: `false, "off", "0", 0, null`, not set |
| File          | String                   | either absolute or relative to the YAML file in which the variable is defined |
| Catalogue     | String                   | as file |
| File-List     | Sequence of Strings      | not set = `null` = empty list |
|               |                          | each file is absolute or relative to the YAML file in which it is defined, i.e. a list can contain files with different relative paths |

## replacements

If a variable has already been defined, its value is replaced if it is redefined at a later time. Further opportunities are:

- `variable+`: adds a new value (only valid for lists). Example: Activate two more plugins with the list "enabled":

```yaml
  plugins:
    enabled+:
      - base.custom-data-type-link
      - base.custom-data-type-gnd
```
- `variable-`:
  - if the variable is a list, the specified values are deleted from the list
  - if the variable is a scalar, it becomes undefined
  - if the variable is a map, all variables below it are undefined

- `variable-key`: only for lists of maps, remove all entries from the list whose value for "key" is included in the specified list

A list of easydbs variables can be found [here](available-variables/).