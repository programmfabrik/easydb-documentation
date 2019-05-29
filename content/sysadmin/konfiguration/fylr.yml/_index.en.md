---
title: Fylr
layout: config
menu:
  main:
    name: "fylr.yml"
    identifier: sysadmin/konfiguration/fylr.yml
    parent: sysadmin/konfiguration
    weight: 70
fylr.yml:
  - server.accounts
  - server.addr
  - objectstore.dir
  - objectstore.uids[].uid
  - objectstore.uids[].name
  - objectstore.uids[].allowed_instances[].id
---

# Fylr

**Flyr** is a companion product for **easydb**. It serves as server for additional services which are not covered by the **easydb server**. More information on Fylr can be found on its website [**fylr.io**](https//fylr.io).

**easydb** optionally uses two features of Fylr:

* *Objectstore*: Used to keep datamodels among **easydb** in sync. This is useful for setups where **production** and **development** servers are separated.
* *Zip*: For users of the connector plugin, Fylr provides a service to zip files for download on the fly.

## Configuration

| Config                                        | Format | Description                                                  |
| --------------------------------------------- | ------ | ------------------------------------------------------------ |
| `server.addr`                                 | String | Address of the server.                                       |
| `server.accounts`                             | Map    | Key-Value map of **login** and **password** for access of the admin pages on Fylr. |
| `objectstore.dir`                             | String | Top-Level-Directory where Fylr stores its data.              |
| `objectstore.uids[].uid`                      | String | UID of the storage, this is a unique id for each storage group. |
| `objectstore.uids[].allowed_instances[].id`   | String | Identifier of one of the clients for the storage.            |
| `objectstore.uids[].allowed_instances[].name` | String | Optional name for the client, as shown in the overview page on Fylr. |
| `zip.allowed_urls[]`                          | String | If set, the *Zip*  service is enabled and allows Zipfiles to be created with files originating the given URLs. Each entry is endpoint |

## Configuration files

To show you more than just a few basics, we use an unusal elaborate example.

An elaborate main configuration file, `/srv/easydb/config/fylr.yml`, could look like this:

*(From now on we are assuming that `/srv/easydb` is your base directory where you installed easydb.)*

```yaml
hostname:
  fylr: easydb-fylr:4000

external_url: https://easydb-system.example.com
objectstore:
  uids: []

link_shortener:
  default_expire_days: 3650

root_password: my_secret

smtp:
  server: relay.example.com
  hostname: easydb-system.example.com
  from-address: noreply@easydb-system.example.com
```

In an additional configuration file, `/srv/easydb/config/fylr.d/objectstore_uids.yml`, you could provide a list of objectstores:


```yaml
objectstore:
  uids:
    # for project #12345
    - uid: 'e978560a-bd52-4a56-86d4-ed29d6041d21'
      name: 'objectstore1'
      allowed_instances:
        - id: '5fa800a5-0b08-4650-9ea4-7a566eb0dac3'
          name: access_by_production
        - id: 'abcdefghijklmnopqRSTUVWXYZ'
          name: access_by_internal
    - uid: 'f637ff9b-26ef-48a9-9019-a90deb254a70'
      allowed_instances:
        - id: '7e7896cb-2f4a-4b4d-9d72-34b7cf535c0c'
```


