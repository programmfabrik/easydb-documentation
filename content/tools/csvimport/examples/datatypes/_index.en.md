---
title: "CSV-Import examples"
menu:
  main:
    name: "Examples"
    identifier: "tools/csvimport/examples/datatypes"
    parent: "tools/csvimport/examples"
---
# Examples per data type

At this point you will find an example of data preparation in CSV format for each data type available in easydb. For more information see our [general notes](./../../general/) or the explanation of the CSV importer options. For best practice instructions, see our tutorials. You can download a CSV file with all examples here.

<br>

## Pools

If you only want to import data records into one pool, you do not have to enter the pool in the CSV file, but simply select it in the import settings. However, if you have data records that are to be stored in different pools or if you want to change the pool for data records that already exist in the system, you must add the pool in the CSV file. You can use the ID, short name or reference of the pool in the CSV file. If no pool is specified for a record in the CSV file, the pool from the import settings is used.

| id   | Title                | Pool   |
| ---- | -------------------- | ------ |
| 1    | Berlin by Night      | Pool A |
| 2    | Berliner Fernsehturm |        |
| 3    | Berliner Dom         | Pool B |

In the import mapping, select "_pool" for the column containing the pool and the "ID", "Short name" or "Reference" field.

<br>

## Single Line & Multi Line Text, Simple Text (String)

It is recommended to enclose the texts in double quotation marks. If a text contains a comma, semicolon, backslash, tab or a break, double quotes must be used so that they are not interpreted as column separators.

| id   | title (single line text) | description (multiline text)                                 | signature (string)|
| ---- | ------------------------ | ------------------------------------------------------------ | ----------------- |
| 1    | Berlin by Night          | The image shows the illuminated Alexanderplatz at night.     | signature_2019_001 |
| 2    | Berlin Cathedral         | "The Berlin Cathedral in the midday sun.<br> <br>Many people lie on the lawn in front of the Berlin Cathedral." | SIgnature_2018_002 |
| 3    | Berlin from above        |                                                              | Signature_2017_003 |

In the mapping, only the corresponding target fields have to be selected in each case. There are no further options.

<br>

## Single line & multiline text (multilingual)

For multilingual fields, the contents for the different languages are stored internally in separate fields. Therefore, the languages must also be written in different columns in the CSV file.

| id   | title_de                                        | title_en                                 | title_es          |
| ---- | ----------------------------------------------- | ---------------------------------------- | ----------------- |
| 1    | German title                                    | English title                            | Título en español |
| 2    | Only a German title is available here           | |
| 3    | We have this title in German and English        | |

In the mapping, the same target field must first be selected for both columns. Then the corresponding language can be selected. If a language is not displayed in the pulldown, it must first be activated by the administrator in the [Base configuration](../../../administration/base-config/general).

<br>

## Date, date + time

When importing dates, both the German and American formats are supported.

| id   | recording date (date) | recording time (date + time)     |
| ---- | --------------------- | -------------------------------- |
| 1    | 2019-12-06            | 2019-12-09 13:39:00              |
| 2    | 24.12.2019            |                                  |
| 3    | 2018-11               | 2019-12-09                       |
| 4    | 2017                  |                                  |

In the mapping, only the corresponding target fields have to be selected in each case. There are no further options.

<br>

## Date (range)

The date range field is characterized by the fact that the values are stored internally in two fields. There is a "from" and "to" field. Therefore, the start and end date must also be written in two columns in the CSV file. Again, the German as well as the American format are accepted.

| id   | date_from  | datum_to   |
| ---- | ---------- | ---------- |
| 1    | 2019-10-01 | 2019-10-08 |
| 2    | 2016-01    | 2018-12    |
| 3    | 2009       | 2019-12-31 |

In the mapping, the same target field must first be selected for both columns. Then it can be selected whether the data should be written in "from" or "to".

<br>

## Number (integer), decimal number (2 digits)

Beim Import von Kommazahlen wird sowohl der Punkt als auch das Komma unterstützt. Tausender-Trenner (Punkt oder Komma) dürfen aktuell nicht verwendet werden.

| id   | number (number)| value (decimal number) |
| ---- | ------------- | ---------------- |
| 1    | 1             | 1.40             |
| 2    | 2             | 5,80             |
| 3    | 3             | 35               |

In the mapping, only the corresponding target fields have to be selected in each case. There are no further options.

<br>

## Yes/No field (Boolean)

Fields of type "Yes/No field (Boolean)" are displayed as checkbox in easydb frontend. The two states "enabled" and "disabled" can be set by "true" or "1" and "false" or "0" during import. Empty fields in the CSV correspond to "false".

| id   | original_present   |
| ---- | ------------------ |
| 1    | true               |
| 2    | false              |
| 3    |                    |

Only the corresponding target field has to be selected in the mapping. There are no further options.

<br>

## Simple linking with flat list

If a flat list is stored in easydb for a field, these links can also be imported via CSV. The entry to be linked can, but does not have to exist in the stored list.

| id   | kategorie       |
| ---- | --------------- |
| 1    | Personen        |
| 2    | Gebäude         |
| 3    | Veranstaltungen |

In the mapping, first select the corresponding target field. Then select the field from the linked object type. easydb uses this field to check whether the entry already exists in the list. If yes, the existing entry will be linked. If not, a new entry will be created in the list and linked (provided that the checkbox "Create linked objects" is activated on the "File" tab during CSV import).

<br>

## Simple linking with hierarchical list

If a hierarchical list is stored in easydb for a field, these links can also be imported via CSV. The entry to be linked can, but does not have to exist in the stored list.

| id   | location                                      |
| ---- | --------------------------------------------- |
| 1    | Germany > Berlin                              |
| 2    | Ireland > Dublin                              |
| 3    | United Kingdom > Scotland > Glasgow           |

In the mapping, first select the corresponding target field. Then select the field from the linked object type. easydb uses this field to check whether the entry already exists in the list. If yes, the existing entry will be linked. If not, a new entry will be created in the list and linked (provided that the checkbox "Create linked objects" is activated on the "File" tab during CSV import). When importing hierarchical lists, the separator used can still be selected (">" or "/").

<br>

## Repeatable free text field

If the target field is a so-called multiple field (i.e. several entries can be made per data record), all entries in the CSV file must be written in one cell and separated with a break. Use double quotes to import texts that contain a break.

| id   | repeatable_free_text_field                                   |
| ---- | ------------------------------------------------------------ |
| 1    | First text<br>Second text<br>Third text                      |
| 2    | "Text that contains a break<br/>."<br/>"Text without a break, but with a comma." |

Only the corresponding target field has to be selected in the mapping. There are no further options.

> Alternatively, each entry of the repeatable field can also be written into a separate column. When importing, however, it should be noted that this must be done in several stages, since the target field may only ever be selected once during mapping. In the first run, the first column is mapped and imported. In the second pass, only the second, etc. It is important that in this case the option "Append multiple fields" is activated under "Import settings", so that the entries in the multiple field are supplemented and not overwritten each time.

<br>

## Nested Fields

If the target field is a so-called nested field in which another object type is referenced, all entries to be linked in the CSV file must be written in one cell and separated with a break. Use double quotes to import entries that contain a break or separator.

| id   | keywords                                      |
| ---- | --------------------------------------------- |
| 1    | Sun<br>Moon<br>Stars                          |
| 2    | "City, Country, River Game"<br/>"Children's Games" |

This works even if the linked object type is hierarchical:

| id   | former_locations |
| ---- | ------------------------------------------------------------ |
| 1    | Germany > Berlin<br>Ireland > Dublin<br>United Kingdom > Scotland > Glasgow |

In the mapping, first select the corresponding target field. Then select the field from the linked object type. easydb uses this field to check whether the entry already exists in the list. If yes, the existing entry will be linked. If not, a new entry will be created in the list and linked (provided that the checkbox "Create linked objects" is activated on the "File" tab during CSV import). When importing hierarchical lists, the separator used can still be selected (">" or "/").

> Alternatively, each entry of the repeatable field can also be written into a separate column. When importing, however, it should be noted that this must be done in several stages, since the target field may only ever be selected once during mapping. In the first run, the first column is mapped and imported. In the second pass, only the second, etc. It is important that in this case the option "Append multiple fields" is activated under "Import settings", so that the entries in the multiple field are supplemented and not overwritten each time.

<br>

## Nested field with multiple fields

If the target field is a so-called nested field, which contains more than one field, these fields must be divided into individual columns. If more than one entry is to be linked to a data record, these must again be entered in a cell and separated by a break.

| id   | further_ids                  | id_type                         |
| ---- | ---------------------------- | ------------------------------- |
| 1    | IDA123<br>ID1XYZ<br>IDA1B2C3 | Altsystem XY<br>  <br>Portal XY |

> Alternatively, each entry of the repeatable field can also be written into its own column. In our example, there would be a total of 6 columns for the three entries ("further_id1", "further_id1_type", "further_id2", "further_id2_type", "further_id3", "further_id3_type"). When importing, however, it should be noted that this must be done in multiple steps, since you may only ever select the target field once during mapping. So in the first run you map and import the first column. In the second pass, only the second, etc. It is important that in this case the option "Append multiple fields" is activated under "Import settings", so that the entries in the multiple field are supplemented and not overwritten each time.

<br>

## Files

The import of files is explained in the examples.

<br>

## Plugins

To import content into Custom Data Fields, it is best to first manually create a record in easydb and export it as [CSV](../../../features/export). There you can have a look at the structure of the content. This varies depending on the plugin. Sometimes not all information is needed for the import, but can be added automatically by the Custom-Data-Updater. You can find more information at the respective [Plugins](https://github.com/programmfabrik).

The following information is sufficient for the GND custom data type:

```text
{
  "conceptURI": "http://d-nb.info/gnd/118868284",
  "conceptName": "Jobs, Steve  (1955 - 2011)"
}
```



The following information is sufficient for the GVK custom data type:

```text
{
  "conceptURI": "http://uri.gbv.de/document/gvk:ppn:1039947670",
  "conceptName": "K. Lynch, „Steve Jobs“. Harvard Common Press, Minneapolis, 2018."
}
```



Only the corresponding target field has to be selected in the mapping. There are no further options.
