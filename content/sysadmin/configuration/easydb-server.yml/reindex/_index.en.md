---
title: yaml configuration allowing reindex
layout: config
menu:
  main:
    name: "allow reindex"
    identifier: "sysadmin/configuration/easydb-server.yml/reindex"
    parent: "sysadmin/configuration/easydb-server.yml"
    weight: -999
easydb-server.yml:
---

The elasticsearch index is automatically updated when needed but in some situations you may want to force a complete recreation. Which does not destroy any data but may take several minutes or even several hours, depending on your data.

# Allow to recreate the elasticsearch index

To be able to restart the indexation via the webfrontend, add this to your yml-configuration, e.g. in `easydb-server.yml`:

```yaml
server:
  api:
    settings:
      reindex: true
```

The default is: `false`, or in other words: disabled.

Make sure to not duplicate lines in the same file. For example, do not put `server:` twice into the same yml-file.

`easydb-server.yml` is part of the directory `config` in your central data storage directory which was set up during [installation](../../../installation).

-----

Further reading:

* [Documentation of the feature in the frontend](../../../../webfrontend/administration/server-status/)

* [List of all configuration directives](../)

* [List of configuration files](../../)
