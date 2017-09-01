# Profiles

Profiles are used to define the import and export of metadata. A distinction is made between import or export profiles. In addition, profiles are divided into three types, which are available to all other areas:

- exiftool_export (Download, Export)
- exiftool_import (New records, object type management, pool management)
- xml_export (Export)

The profiles **EXPORT** and **IMPORT** are currently available. 

## Set up and apply mapping

Multiple mappings can be defined for each profile. To create a new mapping, click the plus sign in the list of profiles below and select the profile for which you want to set up a mapping.

![New Mapping](profiles_neu.png)

Assign a name for the mapping. The fields of the easydb are assigned to the fields of the mapping by drag & drop. For example, in the example below, the Title field was moved from left to right in the Document Title field.

To remove the field selection, drag the entry slightly next to the field.

![Create new mapping](profiles_interface.png)

Depending on the profile, there are many target fields in the mapping, into which the easydb fields can be mapped. Multiple easydb fields can be mapped into a mapping field.

After the field assignment has been completed, the mapping is saved with the `Save` {.button} button. In the exporter. The screenshot below shows the exporter with the newly created mapping.

![Exporter and Mapping Selection](profiles_exporter.png)

When uploading new data sets, the mapping can be selected in the uploader. Existing metadata are then mapped directly to the selected profile. The screenshot below shows the Uploader. A file has already been uploaded and the mapping "basic information" has been selected in the mapping pulldown.

Click on the button `weiter` {.button} to get to the editor. If the uploaded file is now selected, the contents of the fields show a preview of the mappings performed. In this example, the information for "Title" and "Description" was mapped.

![Prefilled fields](profiles_uploader.png)