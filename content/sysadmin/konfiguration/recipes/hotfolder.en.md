---
title: "43 - Hotfolder"
menu:
  main:
    name: "Hotfolder"
    identifier: "sysadmin/konfiguration/recipes/hotfolder"
    parent: "sysadmin/konfiguration/recipes"
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
```apache
a2enmod dav_fs
```

The hotfolder directory should exist and accessible by apache. To ensure the webserver has access to the folder, change the owner of the directory to `www-data`:
```bash
mkdir -p /media/hotfolder
chown www-data. /media/hotfolder
```

Following configurations are necessary for the working directory (`/media/hotfolder` as example). Some options in `VirtualHost` were removed to ensure this gets not to big.

```apache
<VirtualHost *:443>
	AliasMatch ^/upload(.*)$ /media/upload$1
	<Location /upload>
		ProxyPass "!"
		Require all granted
		DAV on
		Options -MultiViews
		ErrorDocument 404 "Not Found"
		ErrorDocument 500 "Internal Server Error"
		ErrorDocument 502 "Bad Gateway"
	</Location>

	ProxyPass / http://127.0.0.1:80/
	ProxyPassReverse / http://127.0.0.1:80/
	…
</VirtualHost>
```

## Configuration of easydb-server

easydb-server creates subdirectories for each released collection inside the above mentioned working directory. Because **hotfolder** is an plugin you have to activate it. 

```yaml
easydb-server:
  hotfolder:
    enabled: true
    urls:
      - type: windows_webdav
        url: \\easydb.example.com@SSL\upload\collection
        separator: \
      - type: webdav_http
        urls: https://easydb.example.com/upload/collection
        separator: /
	
	plugins:
    enabled+:
      - base.hotfolder
```

The above mentioned url is the common windows format webdav-url. In this example the easydb is accessable by `https://easydb.example.com`.

To use the `/hotfolder` inside the `easydb-server`-container you have to allow the access to the hotfolder-workingdirectory (`/media/hotfolder`). This must be configured inside the [start-script](/en/sysadmin/installation):

```bash
docker run -d -ti \
	--name easydb-server \
	…
	--volume=/media/hotfolder:/hotfolder \
	docker.easydb.de:5000/pf/server-$SOLUTION
```