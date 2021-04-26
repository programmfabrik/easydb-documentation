---
title: "CSV import examples lists"
menu:
  main:
    name: "Lists"
    identifier: "tools/csvimport/examples/lists"
    parent: "tools/csvimport/examples"
---
# Importing flat lists

Flat lists contain entries that all have the same rank. These lists can consist of only one field, or they can consist of multiple fields. The CSV file must contain a column header. This can be freely assigned. It is recommended to use meaningful names, because these names will be used later during mapping. If the column headers in the CSV file correspond to the internal field names in easydb, the field mapping is done automatically.

> Please also note the [general notes](../../general).

## Example file "keywords

| keywords
| ------------ |
| sun |
| moon |
| stars |



## example file "persons

| first name | last name | birthplace | remark |
| ------- | ---------- | ------------------------------------------------ | ------------------------- |
| Steve | Jobs | United States > California > San Francisco | Co-founder of Apple Inc. |
| Bill | Gates | United States > Washington > Seattle | Founder of Microsoft |
| Mark | Zuckerberg | United States > New York > White Plains | Founder of Facebook Inc. |

> In our example, the birthplace is a link to a hierarchical list. See also [Data types - Simple linking with hierarchical list](../../datatypes).



## Procedure

- first open the CSV importer
- upload the file
- select "1st line" for CSV field name
- select the target object type and the corresponding mask
- switch to the "Mapping" tab and select the corresponding target fields there
- switch back to the "File" tab and select the "Field for update" if there are already entries in the list that should be updated if necessary
- click on "Prepare" and you will get an overview how many lines will be imported or updated
- then the import / update can be started




