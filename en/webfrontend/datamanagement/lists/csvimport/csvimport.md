# CSV Importer

easydb allows the import of records and users via CSV (*UTF-8* or *UTF-16*). The CSV-Importer can be found in lists via the <i class="fa fa-cog"></i>-symbol at the bottom of the sidebar.


![CSV-Importer](csv_importer.png)

## Functionality

* Import simple object types
* Import of hierarchical object types
* Import of linked data sets (simple & hierarchical) which are created completely and linked
* Import a level of multiple fields (e.g., media to tags) (further nested levels can not be considered)
* Update the records in the CSV importer
* Create nine records in the CSV importer

### Supported field types

- One-line text
- Multi-line text
- Simple text (string)
- Date
- Date + Time
- Linked records (also hierarchical)
- number (integer)
- comma number (2 digits)
- Yes / No field (boolean)
- Files
- All custom data types

If you need support for other types, please send your request to our support.


## CSV file

You create a file in CSV format outside the easydb. This file must be in *UTF-8* encoding or *UTF-16* encoding, otherwise special characters may not be imported correctly.

For example, when using Microsoft Excel, choose "Unicode text" to save.

The easydb CSV Importer has automatic detection for the following separators:

- **,** *(comma)*
- **;** *(semicolon)*
- **&lt;TAB&gt;**

And for the following quotes:

- **"** *(Double quotes)*
- **'** *(single quotes)*

The file must contain an identifier for the column in the first line. This column is displayed as a source field as part of the mapping in the easydb CSV importer.

In a second column you can already enter the target field in the easydb. The CSV importer then already displays the target column in the mapping.

The following format must be used for the target columns:

### Simple fields (text, boolean, whole and comma numbers)

Use the name of the column as specified in the data model. The name of the object type can optionally be prefixed to the name. For a column **title** in the object type **media** that would be either **title** or **media.title**.
For Yes / No fields (Boolean) use "1" for Yes and "0" for No.
Integers must be entered without decimal places. Commands may have two decimal places, but with a "." Must be attached.
Example:
- Title: One-line text
- Description: Multi-line text
- Construction project: Boolean
- Duration: Integer
- Costs: number of commissions

| Title | Description | development | duration | costs |
| - | - | - | - | - |
| House construction | No description. | 1 | 2 | 2.5 |
| Apartment building | "A multi-line <br> description is placed <br>in quotes " | 1 | 4 | 17.85 |
| Fuchsbau | No description. | 0 | 1 | 0 |

### Hierarchical text fields

When importing main object types, the hierarchy levels must be specified in their own columns.

|location#0|location#1|location#2|
|---|---|---|
|Germany|||
| *may remain empty* |Brandenburg||
|||Potsdam|
|Italy|Trentino-Alto Adige|Bolzano|
|Italy|Lacio|Rome|

You can omit the entry from the father in individual lines (see: *Can be left blank*) if it is in the line before it. The entry is automatically assigned to the lines below, up to the line in which a new entry begins (*here in the example to Italy*).

Hierarchy levels are displayed with "#<level>" numbered. Note that the number starts with 0.

### Linked object types

To specify linked records in the CSV, use the name of the column (optionally with the object type), and then the name of the column in the linked object type. Instead of specifying the name of the target column in the object type, you can also specify the object ID of the linked data set directly.

| Keyword#name | Artist#name | Atritst#firstname |
| - | - | - |
| Mona Lisa | da Vinci | Leonardo |
| Skrik | Munch | Edvard |

If the linked object type is hierarchical, you can specify only one column of the linked object type (for example, "ort#name", but not "ort#name_alternative"). The linked hierarchical records are then generated directly.

| Title | Location#name |
| - | - |
|The Brandenburg Gate | Germany > Brandenburg > Potsdam | 
|Colloseum | Italy > Lacio > Rome |
|Marketplaces| Italy > Trentino-Alto Adige > Bolzano |

You can optionally write terms in quotation marks. If the term is a &lt; or &gt; , You must use quotation marks. If separators occur within a term, they are taken over by the quotation marks. If you want to include a term with a punctuation mark, it must be enclosed in quotation marks (double quotes), including the quotation marks.

### Multiple fields

Multiple fields are referenced in the column name with the full path to the field. Note that you can import only the first level of the multiple fields with the CSV importer. Contact support if you want to import deeper nesting.


|titel|people[].person#name|people[].person#vorname|keyword[].keyword#name|
|---|---|---|---|
|Image with 4 persons |Lee Lewis<br>Perkins<br>Presley<br>Cash|Jerry<br>Carl<br>Elvis<br>Johnny|Keyword 1<br>Keyword 2<br>Keyword 3|
|Image with 2 persons|Allen<br>Jackson|Woody<br>Michael|Keyword 1<br>Keyword 2<br>Keyword 3|


Multiple fields are generated line by line. For the first example, "Picture with 4 people", 4 lines with the entries *Jerry Lee Lewis*, *Carl Perkins*, *Evlis Presley* and *Johnny Cash* are created from the people's multiple fields. Therefore, in order to create data sets with several entries in a multiple field, these must be separated by line breaks within the separators. In a text editor without further formatting, the following structure results for the first data record in the table:

```Csv
"title";"people[].person#name";"people[].person#firstname.";"keyword[]keyword#name"
"Picture with 4 people";
"Lee Lewis
Perkins
Presley
Cash";"Jerry
Carl
Elvis
Johnny ";"Keyword 1
Keyword 2
Keyword 3 "
```

### Files

You can use the CSV Importer to acquire metadata (for example, through the hotfolder), if the files were uploaded with a unique file name that you use in the CSV. To do this, specify the column name of the file field.

>NOTE: A hierarchical folder structure in which the data to be imported is stored can also be stored in a CSV file via a separate "Filesystem2CSV" Python script (see www.github.com/programfabrik). In this way, folder names in easydb can be imported as (hierarchical) categories or keywords.

#### Import files 

There is the possibility to import files via URL with the CSV Importer. The configuration options can be found in chapter [Import files](../importfiles/importfiles.html).

### Groups (user import only)

You can use the column name "_groups#find" to add groups to users. The groups are specified as commasparated. First the ID is searched, then the internal name, then the display name (in all languages) to find and assign the group.

## Preparation

The CSV file is uploaded and the following setting is made:

| Setting | Description |
| - | - |
| CSV field names | Row that contains the column names. |
| Target field name | Line that contains the target field names. |
| Object type | Object type to be imported. |
|Pool |Specifies the pool. The pool is only set when inserting records|
| Mask | Mask to be used for the import. |
| File upload type | This option is available if the objecttype contains one or more fields of type 'file'. See [Import files](../importfiles/importfiles.html) |
| Field to update | Specify a field to search the records if you want to make an update. If you have specified filenames in your CSV, select the file field|
| - | In the case of multilingual fields, you have the possibility to make the match over a certain language (e.g., name # en-DE or name # en-US). To activate the selection, specify in the Mapping tab for which fields, which languages ​​should be available|
| Append Multiple Fields | This option adds multiple fields that are not replaced as usual with an update |
| Create linked records | Specify whether linked records should be created before the actual import or not. You can not insert or update records with new linked records with the option turned off|
|Comment |Comment on saving the records|
| Package size | size of the processing packets to be sent to the server|


### Actions

| Button | Description |
| - | - |
| Re-read | Reads the CSV and discards all information that has already been loaded
| CSV | When preparing and after saving, more information is generated, which is written back to the CSV. With **Save CSV** you can get this information to your desktop. For example, the record IDs are written back to the CSV when records are recreated
| Prepare ... | Prepares the CSV import. This includes searching for existing records and linked records. After the preparation, you can check in the table view which lines are collected in which way
| Insert | Starts the CSV import and inserts new records. Previously, all unknown linked records are created again
| Refresh | Starts the CSV import and updates existing records. Previously, all unknown linked records are created again. Note that empty columns are also sent to the server
| Insert + Refresh | Performs both steps directly in sequence. |