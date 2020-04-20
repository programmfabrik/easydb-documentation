---
title: "JSON-Importer"
menu:
  main:
    name: "JSON-Importer"
    identifier: "tools/jsonimport"
    parent: "tools"
---
# JSON Importer

The JSON importer can be used to bulk import data in [JSON format](/en/technical/datamanagement/jsonimport/).

A step by step tutorial on how to generate JSON Payloads can be found [here](/en/tutorials/jsonimport/).

The importer can be found under "Tools &gt; JSON Importer".

The configuration for the JSON importer can be uploaded in a manifest file \(.json\). The manifest contains payloads and other information which will preset the importer.



![](jsonimporter_en_en.png)



## Fields

| Option                          | Description                                                  |
| ------------------------------- | ------------------------------------------------------------ |
| URL manifest.json               | This is a URL to get the manifest.json by clicking 'Load' button next to the input \(optional). This file can contain the following settings, alternatively, they must be entered in the JSON Importer form. |
| Source                          | Name of the source instance \(optional). Can be freely selected. This information is not migrated, it is only used for identification purposes. |
| Payloads base URI               | Base URI for all the payloads in the list. It will be prepended to each payload. The default value will be the same base URL of the manifest. If the payloads are not stored in the same folder as the manifest (or on another server), this is needed to build absolute paths from the payload file names. This value needs to be the relative path to the payload folder. |
| Batch size                      | Quantity of objects pushed to the server per request.        |
| File upload type                | See [Import files](../csvimport/examples/files/)             |
| Metadata mapping                | Metadata mapping used for files. (Optional)                  |
| Ignore file upload errors       | When checked, all errors of file uploads will be ignored and the import process will continue. All errors will be available in the logs. |
| Ignore unique constraint errors | When checked, all 'constraint' errors from the server will be ignored. |
| File replace url                | The location for each file URL will be replaced by the value configured here.(Optional) |



## Payload list

This list show all available payloads. It is possible to see the content by clicking them.

| Header         | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| Status         | Current status of the payload. Pending/Success/Error         |
| URL            | The url of the payload                                       |
| Starting batch | Number of the starting batch. As default the first one is selected, so all batches are processed. |
| Batches        | Quantity of batches (they will depend on the quantity of objects and the selected batch size) |
| Objects        | Quantity of objects.                                         |
| Objecttype     | Objecttype of the payload.                                   |
| Actions        | Opens the payload in a new tab.                              |
| Enabled        | Checkbox to enable or skip the payload (Ctrl+Click to select/unselect all in the selected page, or click in the button below to select/unselect in all pages) |



## Buttons

| Function                       | Description                                                  |
| ------------------------------ | ------------------------------------------------------------ |
| Download logs in CSV format.   | Download the logs in CSV format.                             |
| Clear the logs                 | Clear the logs of the last run.                              |
| See the last report generated. | See the report of the last run.                              |
| Prepare                        | By clicking some validations are performed before the actual import can be started. |
| Start                          | It starts the import of all the enabled payloads.            |



