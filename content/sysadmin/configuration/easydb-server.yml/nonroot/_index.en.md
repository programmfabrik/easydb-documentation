---
title: yaml configuration run easydb as nonroot user
layout: config
menu:
  main:
    name: "nonroot user"
    identifier: "sysadmin/configuration/easydb-server.yml/nonroot"
    parent: "sysadmin/configuration/easydb-server.yml"
    weight: -999
easydb-server.yml:
---

You can run the easydb processes as a nonroot user.

# run easydb processes as nonroot user

To switch the user which runs the easydb processes, add this to your yml-configuration, e.g. in `easydb-server.yml`:

```yaml
server:
  euid: 33
  egid: 33
```
and change the owner of the following directories:

```bash
chown www-data:www-data \
  /srv/easydb/easydb-server/var \
  /srv/easydb/easydb-server/nginx-log \
  /srv/easydb/easydb-server/hotfolder
  ```

The default is: `root`.

If you use `WebDAV` with the hotfolder plugin, you have to use the ID of the user `root` or `www-data`. Otherwise the user is not authorized to create the Files and Folders inside the Hotfolder.

Make sure to not duplicate lines in the same file. For example, do not put `server:` twice into the same yml-file.

`easydb-server.yml` is part of the directory `config` in your central data storage directory which was set up during [installation](../../../installation).