# New records

## Create new records

![New records](new_object.png)

To get records for main object types into the easydb, you can simply open this dialog from your desktop using drag & drop. Alternatively, go to the main menu here.

| Setting | Note |
|--|--|
| Object Type | The object type for which the new records are created. Here are only the main object types listed. If you hold down the ALT key and then click on the pulldown, all object types appear with additional information|
| Pool | Select the pool in which the records are to be created. The selection of the pool determines the choice of the*mask*and the*field*|
| Mask | Mask to be used for editing. In accordance with the settings in the management of the rights, you will see one or more masks here|
| File by File | If you want to upload files, specify the field for which the files are intended. Note that in this step, files can only be assigned to one field at a time. So if you want to upload two files for a record (for example, *front* and *back*), you can do this only in the editor|
| Mapping | Select a mapping to add metadata from the files to the input form. |

In the large area there is the possibility to upload further files with <code class="button">+ files</code> and<code class="button"> + directory</code>. <code class="button">+ Directory</code> is currently only offered in*Google Chrome*and*Apple Safari*. You can also drag additional files into this area by drag & drop.

Click <code class="button">Next ...</code> to open the editor.


## New records editor

![New Records Editor with 9 Images](new_object_edit.png)

On the left you will see the list of the new data sets that are created when you click on <code class="button">Save</code>. At the top there is *Template*. The entries here refer to all data records that you create.

You can click *Template* or another record to fill the fields in the editor with the corresponding data. Data set by default appears as placeholders in the input fields of the actual data set. Here, you can specify different data by selecting the individual data records.

Use the menu at the bottom left to load more records into the editor. You can upload files or directories, or create empty records.

The selected record can be removed from the menu at the bottom left with <i class="fa fa-minus"></i>.

On the right side of the screen, you will see the *file preview* with zoom enabled.

At the top right, there is a pull-down to switch to another mask when multiple masks are available.

After the input, the process can be terminated with <code class="button">Save</code>. If there is a required field, this must be completed before the operation can be saved. If the required field is multilingual, only one of the fields must be filled to complete the process.

More information on the editor can be found in the corresponding chapter [Editor](../search/editor/).

## Duplicate check

![Duplicate Review](dublettencheck.png)

When uploading new records, easydb checks whether the record is already included. You can then decide whether you want this record <code class="button">skip</code> or<code class="button"> import</code>.

If the duplicate is deleted, it is removed from the upload process and the upload process continues with the remaining records, if multiple records have been selected.

If you agree with <code class="button">Import</code> to accept the duplicate, you can proceed with the creation of the data record as usual.

The duplicate note appears for each duplicate record individually. The check box "Apply to all" allows the process to be transferred once to all duplicates that are in the current upload process.

Technically, the duplicate check is performed by calculating a test value (MD5 hash), which also includes the IPTC, XMP and EXIF ​​metadata contained in images, for example.

## <a name="batch"></a>Serial images and links

When uploading records to easydb, serial images and versions can be created in the editor for new records.

If the object type option is configured, you can in ```Field for Records``` specify how the uploaded records and related files / records are placed in easydb.

**Series** are recognized by the filename and automatically grouped to a record, provided the data model for this object type provides multiple files per record. The distinction is made by the notation "_" (dash), "" (space), "-" (hyphen) followed by a number and the file transmission (eg file-1.jpg, file- 2.jpg or bild_1.png, bild_2.png).

If they are files that have the same filename and only differ from the file end, they are recognized as **versions** in easydb (for example, foto.jpg and foto.png). The first file is created as an original, all subsequent as a version. This can then be changed again in the template on the record by calling the versions in the field for the file and moving them manually.

