---
title: yaml configuration for frontend purging
layout: config
menu:
  main:
    name: "configure purge"
    identifier: "sysadmin/configuration/easydb-server.yml/example/purge"
    parent: "sysadmin/configuration/easydb-server.yml/example"
    weight: -999
easydb-server.yml:
---

# Allow to empty the database

To be able to replace the database with a fresh, empty one, via the webfrontend, add this to your yml-configuration, e.g. in `easydb-server.yml`:

## easydb-server.yml

```yaml
server:
  api:
    settings:
      purgedata: true
```

The default is: `false`, or in other words: disabled.

Make sure to not duplicate lines in the same file. For example, do not put `server:` twice into the same yml-file.

`easydb-server.yml` is part of the directory `config` in your central data storage directory which was set up during [installation](../../../installation).

> Warning: Using the now enabled feature is destructive and cannot be undone (better have backups at hand).

# Allow to empty the database and schema


To be able to replace the database and schema, via the webfrontend, to their state just after a fresh installation, add this to your yml-configuration, e.g. in `easydb-server.yml`:

## easydb-server.yml

```yaml
server:
  api:
    settings:
      purgeall: true
```

The default is: `false`, or in other words: disabled.

Make sure to not duplicate lines in the same file. For example, do not put `server:` twice into the same yml-file.

`easydb-server.yml` is part of the directory `config` in your central data storage directory which was set up during [installation](../../../installation).

> Warning: Using the now enabled feature is destructive and cannot be undone (better have backups at hand).

# further reading

* [This configuration in context of a whole configuration file](../../../../tutorials/testsystem/#configuration-of-easydb5)

* [Documentation of the feature in the frontend](../../../../webfrontend/administration/server-status/)

* [List of all configuration directives](../)

* [List of configuration files](../../)
