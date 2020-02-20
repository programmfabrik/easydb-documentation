---
title: "Postgres Upgrade (11)"
menu:
  main:
    name: "Postgres Upgrade (11) (fix me)"
    identifier: "sysadmin/installation/postgres_upgrade"
    parent: "sysadmin/installation"
    weight: -990
---

# Postgres Upgrade

During release **5.62** we also upgraded the operation system inside of our docker-containers to **Debian Buster (10)**. Since postgres made also an application upgrade from **9.x** to **11** we also had to upgrade postgres to version: **11**. Keep in mind that upgrades of such container consumes a lot of time.

get the newest postgres container made by programmfabrik:
```bash
docker pull docker.easydb.de/pf/postgresql-11
```