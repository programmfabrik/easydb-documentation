---
title: "43 - Hotfolder"
menu:
  main:
    name: "Hotfolder"
    identifier: "sysadmin/konfiguration/global/apache2/hotfolder"
    parent: "sysadmin/konfiguration/global/apache2"
    weight: 3
---
# Hotfolder einrichten

The hotfolder is a special directory in easydb. Inside this directory all files will be automatically inserted inside your easydb. To configure an hotfolder on user sight, see [collection](/en/webfrontend/datamanagement/search/uickaccess/collection). 
This article is about the administrator sided hotfolder configuration. 

## Release of the working directory

The working directory, in which the hotfolder will be reachable must be released with operating system means. Normally this will be done by *WebDAV*. Other options like *FTP* or *SMB* are also possible but not described here. 

### Configuration of *WebDAV*

WebDAV requires an Apache web server connected in front of the Docker containers, as described in [configuration of HTTPS](/en/sysadmin/konfiguration/https)

First of all your should activate the Apache module
{{< getFileContent file="/content/sysadmin/konfiguration/includes/apache2/enable-webdav-module.md" markdown="true" >}}

The hotfolder directory should exist and accessible by apache. To ensure the webserver has access to the folder, change the owner of the directory to `www-data`:
{{< getFileContent file="/content/sysadmin/konfiguration/includes/bash/create-hotfolder-chown.md" markdown="true" >}}

Following configurations are necessary for the working directory (`/media/hotfolder` as example). Some options in `VirtualHost` were removed to ensure this gets not to big.

{{< getFileContent file="/content/sysadmin/konfiguration/includes/apache2/enable-hotfolder.md" markdown="true" >}}

## Configuration of easydb-server

easydb-server creates subdirectories for each released collection inside the above mentioned working directory. Because **hotfolder** is an plugin you have to activate it. 

{{< getFileContent file="/content/sysadmin/konfiguration/includes/bash/hotfolder-configuration.md" markdown="true" >}}

The above mentioned url is the common windows format webdav-url. In this example the easydb is accessable by `https://easydb.example.com`.

To use the `/hotfolder` inside the `easydb-server`-container you have to allow the access to the hotfolder-workingdirectory (`/media/hotfolder`). This must be configured inside the [start-script](/en/sysadmin/installation):

{{< getFileContent file="/content/sysadmin/konfiguration/includes/docker/docker-allow-hotfolder-access.md" markdown="true" >}}