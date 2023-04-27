---
title: "Import files"
menu:
  main:
    name: "Import files"
    identifier: "tools/csvimport/examples/files"
    parent: "tools/csvimport/examples"
---
# Import files

Files can also be imported via the CSV importer. If the files are already accessible via the web, you can simply use this URL in the CSV file.

If the files are located locally on your computer, they must first be made available via a web server, since web browsers do not support direct access to files on your computer. For example, see this list of web servers: https://slashdot.org/software/p/Tiny-Web-Server/alternatives.

## Import Procedure
- first open the CSV importer 
- upload your CSV file 
- select "1st Row" for "CSV Field Names" 
- select the target object type, pool and the corresponding mask 
- switch to the tab "Import Mapping" and select the corresponding target field for the column containing the URLs 
- for "Type" select "url" to import new files 
- switch back to the tab "Import Settings" and select the "Update Field" if there are already records in the list that should be updated if necessary 
- click on "Prepare" and you will get an overview how many rows will be imported or updated 
- then the import / update can be started