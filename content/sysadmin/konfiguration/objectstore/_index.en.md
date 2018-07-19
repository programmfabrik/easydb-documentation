---
title: "45 - Daten Model-Server"
menu:
  main:
    name: "Daten Model-Server"
    identifier: "sysadmin/konfiguration/objectstore"
    parent: "sysadmin/konfiguration"
---
# Data model server

The data model server can be used to run for diesselbe easydb with multiple servers (test, staging, production)
The data model (schema, masks, localization), centrally.

## Configuration in the easydb

Installation in easydb is done in server.yml.

	default_client:
		datamodel:
			uid: 6b6640c4-771a-4a66-9308-dbc372b0bcdf
			server: http://10.150.0.2:3000

The * uid * must be on all easydb diesselbe, as well as the specified server.

# Installation

The data model server is installed from a GIT checkout of easydb-objectstore.
