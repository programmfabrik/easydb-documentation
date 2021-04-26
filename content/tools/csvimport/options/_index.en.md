---
title: "CSV-Import Settings"
menu:
  main:
    name: "CSV-Import Settings"
    identifier: "tools/csvimport/options"
    parent: "tools/csvimport"
---
# CSV importer options

The CSV importer offers various setting options, which will be explained below.

![CSV-Importer](csv_importer.png)



## Import settings

After you have uploaded a file in the "CSV file" field, the following settings are available:

| Setting | Description |
| ----------------------------- | ------------------------------------------------------------ |
| CSV file | First click on this button to select a CSV file for import. With the "X" you can remove the file again. |
| CSV Field Names | Select the row where the column names are located so that they are not imported. |
| Target Field Names | Select the line that contains the target field names so that the mapping will be done automatically and they will not be imported. The notation is explained in the [general settings](../general). |
| Object type | Select the object type to be imported.    |
| Pool | Specify the pool in which the new records are to be created. The pool is only set when records are inserted. If existing records are updated via the CSV importer, the pool will not be changed. For this purpose, please use the group editor. |
| Mask | Select here the mask to be used for the import. |
| Upload type for files | Select the method to upload the files:            |
| |"Direct": The file will be downloaded and then uploaded with /eas/put. |
| |"URL (remote PUT)": The file will not be downloaded and /eas/put will be called directly from the file URL. The file is downloaded from the server and uploaded. (This option is the fastest.) |
| |"Ignore files": All files will be ignored.         |
| | For more information about uploading files via the CSV importer, see the [Examples](../examples/files). |
| Metadata Mapping | Select the metadata mapping to be applied when importing files. |
| Update field | By selecting the default entry "- Insert new -" all rows of the CSV file will be created as new records in easydb. Select a field here to identify existing records and update them with the contents from the CSV file. Please note that you must first select fields in the "Mapping" tab so that they are available for selection in the pulldown. Select the file field if you have specified file names in your CSV and that is what you want the matching to occur over. In case of multilingual fields you have then the possibility to make the matching over a certain language (e.g. name#de-DE or name#en-US). To activate the selection, define in the tab "Mapping" for which fields, which languages should be available. |
| Append multiple fields | By default, when updating data records available in easydb, all entries in multiple fields will be replaced by the contents from the CSV file. With this option, the contents from the CSV file will be appended to the existing entries for multiple fields instead. Use this function, for example, to add keywords in addition to those already assigned to the record. |
| Create Linked Records | Specify whether linked records should be created before the actual import or not. If this option is turned off, all linked records must already exist in easydb. If you click on "Prepare", a corresponding message will appear, should the CSV file refer to entries that could not be found in easydb. |
| Pool for linked records | This option appears only if the selected object type refers to another object type where pool management is also activated. Thus different pools can be specified for linked object types with activated pool management. |
| Comment | Enter a comment for the CSV import here, which will subsequently appear in the change history of the imported / updated records. |
| Packet Size | Size of the processing packets that will be sent to the server one by one. In case of very complex data models and data volumes, a timeout may occur. In this case, try using a smaller packet size. |
| Show localized names | If enabled, the second tab "Mapping" for easydb fields will show the names from the editor/detail. Otherwise the internal field names from the data model will be used. |

## Information

Below the import settings an import overview is displayed after preparing. The checkboxes are used to filter the entries in the table view.

| Name | Comment |
| --------------- | ------------------------------------------------------------ |
| Rows | Number of rows in CSV |
| Ready | Number of rows ready to import |
| Invalid | Number of rows that are invalid |
| In Processing | Number of rows being processed |
| Finished | Number of rows that have been finished processing |
| Error | Number of lines where an error occurred during processing |
| Warning | Number of rows that can be imported but for which there is a warning |
| Insertable | Number of rows / entries that would be inserted / created |
| Updateable | Number of rows / entries that would be updated |
| Deletable | Number of rows / entries that would be deleted |

## Import mapping



Fields for which no mapping has been selected will not be changed when updating records that already exist in easydb. Fields for which a mapping has been selected, but where there is no content in the CSV file, will empty any existing content when updating records.



## Table View

In the Table View you can see the data contained in your CSV file. After preparing and importing, additional information is automatically added (recognizable by the column names "easydb|"). You can read which information this is at the end of the article in the "Log" section.



## Record preview

In the "Dataset Preview" tab you can see the data that would be imported according to the import mapping in the easydb detail view. Please note that this is only a preview of the mapped fields. When updating existing records, the result may differ.



## JSON preview

In the "JSON Preview" tab you can see the data that would be imported according to the import mapping in the JSON structure. 

## Actions

The lower part of the CSV importer contains the following functions:

| Button | Description |
| --------------------------- | ------------------------------------------------------------ |
| Reread | Rereads the CSV and discards all information already loaded by preparing. |
| Save CSV | When preparing and after saving, more information is created and written back to the CSV (see table below). With "Save CSV" you can save this information to your desktop. |
| Download settings | Download the made import settings and the import mapping as JSON file here. |
| Upload settings | Upload the import settings and the import mapping as JSON file here. |
| Prepare...              | Prepares the CSV import. This includes checking the data and searching for already existing and linked records. |
| Insert | Starts the CSV import and inserts all new records. Already existing records will not be updated. |
| Update | Starts the CSV import and updates existing records. Records that do not exist yet will not be created in easydb. Note, however, that empty columns in the CSV will cause the update to empty the contents of these fields in the easydb records. |
| Insert + Update | Performs both steps directly one after the other.            |

## Protocol

After preparing and after importing certain information is recorded by easydb. These can be seen in the table view in the CSV importer or can be downloaded as a CSV file after the import.

| Column | Meaning |
| -------------------------------- | ------------------------------------------------------------ |
| easydb\|row_idx | row number, starting at 0 |
| easydb\operation | action that will be performed ("insert", "update", "delete") |
| easydb\|status | import status ("ready", "invalid", "failed", "done"). Lines with status "invalid" cannot be imported (example: wrong date format). Lines with status "failed" were not imported correctly (example: mandatory field violation). |
| easydb\|timestamp | date + time when import/update/delete by CSV importer took place |
| easydb\status_text | In case of status "invalid" and "failed" contains further information about the occurred error |
| easydb\|warning_text | Contains further information if an attempt is made to import invalid JSON into custom data type fields |
| easydb\id | ID of the record found in easydb (for records created by CSV import this column remains empty) |
| easydb\|version | version of the record |
| easydb\|id_parent | ID of parent record (only for hierarchical object types) |
| easydb\depth | Depth of record (only for hierarchical object types), starting at 0 |
| easydb\|path | Path of the record (only for hierarchical object types) |
| easydb\|eas_ids\|file | Contains the internal EAS ID of the file uploaded via the CSV importer (see [Upload files](../examples/files)). |
| easydb\|eas_ids\|file\|metadata | Contains the metadata taken from the file uploaded via the CSV importer (see [Upload files](../examples/files)). |
| easydb\|*object type*\|*mask* | A separate column is generated for all linked object types. After preparing this column you can see if the linked entries already exist in easydb (an ID is shown for them), if they are newly created (they appear with "new") or if the option "Create linked entries" is disabled, if they were not found in easydb (they appear with "searching"). |

