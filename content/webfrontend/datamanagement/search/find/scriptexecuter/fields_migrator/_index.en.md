---
title: "Fields Migrator - ScriptExecuter Plugins"
menu:
  main:
    name: "Fields migrator"
    identifier: "webfrontend/datamanagement/search/find/scriptexecuter/fields_migrator"
    parent: "webfrontend/datamanagement/search/find/scriptexecuter"
---

# Fields migrator

Fields migrator is a plugin of the ScriptExecuter, and it can be used to migrate data from one field to another field within the same object type.

![](scriptexecuter_fields_migrator_en.png)

|Field| Explanation |
|---|---|
|Object type | It's necessary to choose just one object type, objects with different object types will be ignored. |
|Field from | The data will be taken from this field, but it won't be removed. It's not possible to use a field inside a nested field. |
|Field to | This is the destination field for the data. It's possible to use a field inside a nested field (just one level).|
|Caster | It's explained below, |
|Caster options form | Options form given by the caster.|

### Caster

To transfer the data from one field to another field is necessary to know how each field manages its data.
The caster is responsible to make the conversion from one type to another type.
If both fields have the same type they will have a caster which transfers the data without making a conversion (there are exceptions, see the table below).

Custom data types: Casters are plugins, so it's possible to add custom casters to transfer data from/to custom-data-types.

#### Available casters

| From / To                       | Single line text | Single line text (multilingual) | Multiline text | Multiline text (multilingual) | Simple text (string) | Date | Date (range) | Date + time | Number/Decimal | File | Yes/No (Boolean) | Linked object        |
|---------------------------------|------------------|---------------------------------|----------------|-------------------------------|----------------------|------|--------------|-------------|----------------|------|------------------|----------------------|
| Single line text                |YES               |                                 |                |                               |                      |YES   |YES           |             |                |      |                  |                      |
| Single line text (multilingual) |                  |YES                              |                |                               |                      |      |              |             |                |      |                  |                      |
| Multiline text                  |                  |                                 |YES             |                               |                      |      |              |             |                |      |                  |                      |
| Multiline text (multilingual)   |                  |                                 |                |YES                            |                      |      |              |             |                |      |                  |                      |
| Simple text (string)            |                  |                                 |                |                               |YES                   |      |              |             |                |      |                  |                      |
| Date                            |YES               |                                 |                |                               |                      |YES   |YES           |             |                |      |                  |                      |
| Date (range)                    |YES               |                                 |                |                               |                      |YES   |YES           |             |                |      |                  |                      |
| Date + time                     |                  |                                 |                |                               |                      |      |              |YES          |                |      |                  |                      |
| Number/Decimal                  |                  |                                 |                |                               |                      |      |              |             |YES             |      |                  |                      |
| File                            |                  |                                 |                |                               |                      |      |              |             |                |      |                  |                      |
| Yes/No (Boolean)                |                  |                                 |                |                               |                      |      |              |             |                |      |YES               |                      |
| Linked object                   |                  |                                 |                |                               |                      |      |              |             |                |      |                  |YES (same object type)|

### Caster example

In this example the field 'from' is type Date and field 'to' is type Date range.

The caster gives additional options to choose whether the date value will be transferred to 'date from', 'date to' or 'both'.

![](scriptexecuter_fields_migrator_example_en.png)
