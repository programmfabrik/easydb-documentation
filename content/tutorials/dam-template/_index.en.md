---
title: "DAM Template"
menu:
  main:
    name: "DAM Template"
    identifier: "tutorials/dam-template"
    parent: "tutorials"
---
# Tutorial: How to use the DAM template

This is a short description of how to use our template for standard DAM easydb’s. Before starting with the steps mentioned below, you need to install your easydb. Once your easydb is up and running, follow these steps to start with a
- standard data model,
- base configuration,
- metadata mapping and
- user groups.

You’ll be able to adjust all these settings after the setup.

## Login in the template easydb
- go to http://dam-template.5.easydb.de/
- log in with
- user = root and
- password = admin

## Download Data Model
- open menu
- go to “Data Model”
- click on the settings icon in the first pane on the bottom
- click on “Download data model (JSON)”

## Download Base Configuration
- go to “Base Configuration”
- click on the settings icon in the first pane on the bottom
- click on “Download Config”

## Download Metadata Mapping
- go to “Metadata Mapping”
- click on “Download”

## Download Permissions
- go to “Rights Im-/Export”
- click on “Export”

## Login in the target easydb
- now open the easydb you installed and log in

## Upload Data Model
- go to “Data Model” and click on the settings icon in the first pane on the bottom
- click on “Upload Data Model (JSON)” and choose the file you previously downloaded

## Upload Base Configuration
- go to “Base Configuration” and click on the settings icon in the first pane on the bottom
- click on “Upload Config” and choose the file you previously downloaded

## Upload Metadata Mapping
- go to “Metadata Mapping” and click on the settings icon in the first pane on the bottom
- click on “Upload” and choose the file you previously downloaded

## Upload Permissions
- go to “Rights Im-/Export”
- click on “Import” and upload the file you previously downloaded
- click on “Groups” and check “Transfer permissions” and “Transfer system rights”
- click on “Transfer”
- click on “Tags” and check “Transfer permissions” and click on “Transfer”
- click on “Object Types” and check the “Selection”
- click on “Transfer”
- click on the small arrow before “Pools”
- click on “All Pools” and check the “Selection”
- click on “All Pools” in the pane that’s labeled “Target” and click on “Transfer”
- do the same for the other pools (if needed)
- then click on “Done”
- close the pop up

Your easydb is now ready to use. Create some users and assign them to groups, so they get access.
