---
title: "100 - Janitor"
menu:
  main:
    name: "Janitor"
    identifier: "technical/janitor"
    parent: "technical"
---
# Janitor

The Janitor is a process running inside the easydb-server. Its purpose is to clean up temporary data in filesystem or database.

For a list of configuration options see the [YAML configuration reference](/en/sysadmin/konfiguration/easydb-server.yml/#server).

> **Caution!** Most of the configuration options for the Janitor were moved to the [Base Configuration](/en/webfrontend/administration/base-config/janitor/).
>
> The following YAML configuration varibles are obsolete and are ignored:
>
> * `server.janitor.interval` (now **Janitor-Intervall** in Base Configuration)
> * `server.janitor.max_age` (now **Expiration time for exports and downloads** in Base Configuration)

## The following tasks are performed by the Janitor process:

* All files prepared by exports older than a configurable period are removed. The default retention period is 3 days. Exports which are affected by this cleanup have to be restarted before any files can be downloaded again.
* All events of the types `OBJECT_INDEX`, `API_PROGRESS`, `SUGGEST_INDEX_START`, `SUGGEST_INDEX_DONE`, `SUGGEST_INDEX_PROGRESS`, `SUGGEST_INDEX_FAILED` older than 1 week are removed from the database.
* The clients blocked because of too many wrong login attempts are checked and released if the blocking period is over.
* All linked assets are reported to the asset server, which cleans up assets no longer linked in easydb.
* Expired sessions can be deleted (set **Purge expired sessions from the database** in Base Configuration) after they are expired (**Expiration time for sessions** in Base Configuration)

By default the Janitor runs every 10 minutes (**Janitor-Intervall** in Base Configuration). This interval should only be changed if there are load problems related to the Janitor process. The client block check runs at a separate, smaller interval which can't be configured.
