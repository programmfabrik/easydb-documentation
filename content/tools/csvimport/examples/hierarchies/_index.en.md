---
title: "CSV import examples hierarchical lists"
menu:
  main:
    name: "Hierarchies"
    identifier: "tools/csvimport/examples/hierarchies"
    parent: "tools/csvimport/examples"
---
# Import of hierarchical lists

Hierarchical lists contain entries that can have parent and child entries. These lists can consist of only one field, or multiple fields. The CSV file must contain a column header. This can be freely assigned. It is recommended to use meaningful names, because these names will be used later during mapping. If the column headers in the CSV file correspond to the internal field names in easydb, the field mapping is done automatically.

> Please also note the [general notes](../../general).

## Example file "Places

| id | level1 | level2 | level3 |
| ---- | ---------------------- | ----------- | ---------- |
| 1 | Germany | |
| 2 | Berlin | |
| 3 | | Brandenburg | |
| 4 | | Potsdam |
| 5 | United Kingdom | |
| 6 | | Scotland | |
| 7 | | Glasgow |
| 8 | | England | |
| 9 | | London |
| 10 | | Brighton |
| 11 | | Manchester |



Alternatively, the data can be structured as follows. However, it is important that each level appears in a separate line in the CSV file (lines 1, 3, 5, 6, 8 must not be omitted):

| id | level1 | level2 | level3 |
| ---- | ---------------------- | ----------- | ---------- |
| 1 | Germany | |
| 2 | Germany | Berlin | |
| 3 | Germany | Brandenburg | |
| 4 | Germany | Brandenburg | Potsdam |
| 5 | United Kingdom | |
| 6 | United Kingdom | Scotland | |
| 7 | United Kingdom | Scotland | Glasgow |
| 8 | United Kingdom | England | |
| 9 | United Kingdom | England | London |
| 10 | United Kingdom | England | Brighton |
| 11 | United Kingdom | England | Manchester |



In addition, it is possible to import the hierarchies by referring to the respective parent entry. However, it is important that each level appears in a separate line in the CSV file (lines 1, 3, 5, 6, 8 must not be omitted):

| id | parent | name |
| ---- | ---------------------- | ---------------------- |
| 1 | Germany |
| 2 | Germany | Berlin |
| 3 | Germany | Brandenburg |
| 4 | Brandenburg | Potsdam |
| 5 | United Kingdom |
| 6 | United Kingdom | Scotland |
| 7 | Scotland | Glasgow |
| 8 | United Kingdom | England |
| 9 | England | London |
| 10 | England | Brighton |
| 11 | England | Manchester |

When mapping here you have to select the field "id_parent" for the column "parent" and the corresponding easydb field for the column "name". If your file contains parent entries that are not yet available in easydb, you have to perform the import twice. In the first step all entries are created and in the second import the links between parent and new child entries are created. Prerequisite is that in the import settings the "field to update" was selected over which the matching should take place (in our example e.g. "id").



> If you want to export a hierarchical list from easydb and import it afterwards, you have to select "Hierarchies as columns" when exporting. 



## Example "Categories

| id | level1 | level2 | remark |
| ---- | -------- | ---------- | ------------------------------------------------------------ |
| 1 | people | | This category includes e.g. staff photos or photos of events. |
| 2 | Buildings | |
| 3 | | Building #1 | This building was the former seat of the department XYZ. Currently the department ABC is located there. |
| 4 | | Building #2 | This building was built in 1986.                               |

## Procedure

- first open the CSV importer
- upload your CSV file
- select "1st line" for CSV field name
- select the target object type and the corresponding mask
- switch to the tab "Import Mapping" and select the same target field for each column containing hierarchical data and enter the level number (Attention: the first level must start with 0)
- select also for all other columns in the CSV the corresponding target fields (e.g. for "Birthplace" or "Remarks")
- switch back to the "Import Settings" tab and select the "Update field" if there are already entries in the list that should be updated if necessary
- click on "Prepare" and you will get an overview how many lines will be imported or updated
- then the import / update can be started