---
title: Fylr
layout: config
menu:
  main:
    name: "fylr.yml"
    identifier: sysadmin/konfiguration/fylr.yml
    parent: sysadmin/konfiguration
    weight: 9
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

