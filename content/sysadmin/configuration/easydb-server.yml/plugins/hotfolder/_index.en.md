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

The hotfolder is a special directory for easydb. Files in this directory will be automatically imported into easydb.

To configure a hotfolder on the user's side, see [collection](/en/webfrontend/datamanagement/search/quickaccess/collection/#uploading-hotfolder).
This article is about the administrator's side of the hotfolder configuration. (Both sides are needed)

## Serving of the working directory

The working directory, in which the hotfolder will be reachable must be served to users with operating system means so that users can put new files there. Normally this will be done by *WebDAV*. Other options like *FTP* or *SMB* are also possible but not described here.

### Configuration of *WebDAV*

WebDAV requires an Apache web server connected in front of the Docker containers, as described in configuration of [Apache2/HTTPS](/en/sysadmin/configuration/apache2)

First of all your should activate the Apache module
```apache
a2enmod dav_fs
```

The hotfolder directory should exist and be accessible by apache. To ensure the webserver has access to the folder, change the owner of the directory to `www-data` (valid for Debian Linux):
```bash
mkdir -p /media/hotfolder
chown www-data. /media/hotfolder
```

The following configuration is necessary for the working directory (`/media/hotfolder` as example). Some options in `VirtualHost` were removed to ensure this listing stays small enough.

```apache
<VirtualHost *:443>
    AliasMatch ^/upload(.*)$ /media/hotfolder$1
    <Location /upload>
        ProxyPass "!"
        <LimitExcept POST PUT DELETE MKCOL COPY MOVE>
            Require all granted
        </LimitExcept>
        <Limit POST PUT DELETE MKCOL COPY MOVE>
            Require all denied
        </Limit>
        DAV on
        Options -MultiViews
        ErrorDocument 404 "Not Found"
        ErrorDocument 500 "Internal Server Error"
        ErrorDocument 502 "Bad Gateway"
    </Location>
    <LocationMatch /upload/collection/[^/]+/[^/]+/.*>
        Require all granted
        DAV on
        Options -MultiViews
        ErrorDocument 404 "Not Found"
        ErrorDocument 500 "Internal Server Error"
        ErrorDocument 502 "Bad Gateway"
    </LocationMatch>

    ProxyPass / http://127.0.0.1:80/
    ProxyPassReverse / http://127.0.0.1:80/
</VirtualHost>
```

## easydb-server configuration

easydb-server creates one subdirectory inside the above mentioned working directory for each collection that is [configured](/en/webfrontend/datamanagement/search/quickaccess/collection/#uploading-hotfolder) in the webfrontend to allow upload.

### Access for the easydb-server container

To access the hotfolder inside the `easydb-server`-container you have to mount it into the container during its creation. In our example `/media/hotfolder` will be visible as the expected `/hotfolder` inside the container, and the container creation is done inside the easydb-typical [start-script](/en/sysadmin/installation):

```bash
docker run -d -ti \
	--name easydb-server \
	…
	--volume=/media/hotfolder:/hotfolder \
	docker.easydb.de/pf/server-$SOLUTION
```

  ... only the volume line has been added. Some other lines are shown as orientation, but not all.

### Server YAML configuration

Example Configuration:

```yaml
hotfolder:
  enabled: true
  directory: /srv/easydb/webdav
  urls:
    - type: windows_webdav
      url: \\easydb.example.com@SSL\upload\collection
      separator: \
    - type: mac_finder
      url: https://easydb.example.com/upload/collection
      separator: /
    - type: webdav
      url: https://easydb.example.com/upload/collection
      separator: /

plugins:
  enabled+:
    - base.hotfolder
```

  ... placed into e.g. `/srv/easydb/config/easydb-server.yml`:

We assume that your easydb uses https.

### Server YAML variables to configure the Hotfolder

| Variable | Type | Required | Description |
|---|---|---|---|
| `hotfolder` | List | No | Parent element which contains the configuration for easydb's hotfolder |
| &#8680;`enabled` | `bool` | Yes | If the Hotfolder is enabled on this Server (default: `false`) |
| &#8680;`directory` | `string` | Yes | Path of the local Hotfolder to check for files |
| &#8680;`urls` | List | Yes | List of URL Configurations: |
| &#8680;&#8680;`type` | `string` | Yes | Type of the Hotfolder URL: one of `"windows_webdav"`, `"webdav_http"` |
| &#8680;&#8680;`url` | `string` | Yes | URL of the WebDAV Folder |
| &#8680;&#8680;`separator` | `string` | Yes | Separator Token that is used in the URL (default: `/`) |
| &#8680;`delay` | `int` | No | Time in seconds between each check for new files in the Hotfolder (default: `10`) |
| &#8680;`number_of_workers` | `int` | No | Number of Worker Instances, currently ignored, only one worker is implemented |
| &#8680;`upload_batches` | `bool` | No | `true`: upload the generated objects generated from files in the Hotfolder in batches; `false`: upload single objects (default: `false`) |
| &#8680;`upload_batch_size` | `int` | No | Number of Objects to be uploaded in the same batch (default: `10`, ignored for `upload_batches = false`) |

### Frontend localization for URL types

The frontend localizations for different types of hotfolder URLs can be added to the localization files in `server/base/l10n`. For each `type` in `urls`, a new localization can be added:

	"server.base.hotfolder.urls.type.<type>": "URL Type"

where `<type>` is the configured URL type.

The server already supports localizations for the following URL types:

* Type `windows_webdav`: "Windows Explorer"
* Type `mac_finder`: "Mac Finder"
* Type `webdav`: "WebDAV"
* Type `webdav_http`: "Browser (WebDAV)"

