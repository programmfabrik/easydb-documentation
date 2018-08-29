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

{{< getFileContent file="/content/sysadmin/konfiguration/includes/fylr-tbl-variables.md" markdown="true" >}}

