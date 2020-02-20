---
title: "Hotfolder"
menu:
  main:
    name: "Hotfolder"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/hotfolder"
    weight: -947
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
easydb-server.yml:
  - plugins.enable.base.hotfolder
---

# Hotfolder Plugin

The hotfolder is a special directory in easydb. Inside this directory all files will be automatically inserted inside your easydb. To configure an hotfolder on user sight, see [collection](/en/webfrontend/datamanagement/search/quickaccess/collection).
This article is about the administrator sided hotfolder configuration.

## Release of the working directory

The working directory, in which the hotfolder will be reachable must be released with operating system means. Normally this will be done by *WebDAV*. Other options like *FTP* or *SMB* are also possible but not described here.

### Configuration of *WebDAV*

WebDAV requires an Apache web server connected in front of the Docker containers, as described in configuration of [Apache2/HTTPS](/en/sysadmin/configuration/apache2)

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
	...
</VirtualHost>
```

## easydb-server configuration

easydb-server creates subdirectories for each released collection inside the above mentioned working directory. Because **hotfolder** is a plugin, you have to activate it.

```yaml
plugins:
  enabled+:
    - base.hotfolder
```

### Server YAML Variables to configure the Hotfolder

hotfolder:
  directory: /srv/easydb/webdav
  urls:
    - type: windows_webdav
      url: \\master.pf-berlin.de@SSL\upload\collection
      separator: \




| Variable | Type | Required | Description |
|---|---|---|---|
| `hotfolder` | List | No | Parent element which contains the configuration for easydb's hotfolder |
| &#8193;`enabled` | `bool` | Yes | If the Hotfolder is enabled on this Server (default: `false`) |
| &#8193;`directory` | `string` | Yes | Path of the local Hotfolder to check for files |
| &#8193;`urls` | List | Yes | List of URL Configurations: |
| &#8193;&#8193;`type` | `string` | Yes | Type of the Hotfolder URL: one of `"windows_webdav"`, `"webdav_http"` |
| &#8193;&#8193;`url` | `string` | Yes | URL of the WebDAV Folder |
| &#8193;&#8193;`separator` | `string` | Yes | Separator Token that is used in the URL (default: `/`) |
| &#8193;`delay` | `int` | No | Time in seconds between each check for new files in the Hotfolder (default: `10`) |
| &#8193;`number_of_workers` | `int` | No | Number of Worker Instances (default: `5`) |
| &#8193;`upload_batches` | `bool` | No | `true`: upload the generated objects generated from files in the Hotfolder in batches; `false`: upload single objects (default: `false`) |
| &#8193;`upload_batch_size` | `int` | No | Number of Objects to be uploaded in the same batch (default: `10`, ignored for `upload_batches = false`) |

### Frontend localization for URL types

The frontend localizations for different types of hotfolder URLs can be added to the localization files in `server/base/l10n`. For each `type` in `urls`, a new localization can be added:

	"server.base.hotfolder.urls.type.<type>": "URL Type"

where `<type>` is the configured URL type.

The server already supports localizations for the following URL types:

* Type `windows_webdav`: "Windows WebDAV"
* Type `webdav_http`: "Browser (WebDAV)"

### Example Configuration
We assume that your easydb uses https.

The following configuration can be placed into e.g. `/srv/easydb/config/easydb-server.yml`:

```yaml
hotfolder:
  enabled: true
  urls:
    - type: windows_webdav
      url: \\easydb.example.com@SSL\upload\collection
      separator: \
    - type: webdav_http
      url: https://easydb.example.com/upload/collection
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
	docker.easydb.de/pf/server-$SOLUTION
```

