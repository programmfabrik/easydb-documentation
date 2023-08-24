---
title: "42 - Uninstallation"
menu:
  main:
    name: "Uninstallation"
    identifier: "sysadmin/uninstallation"
    parent: "sysadmin"
    weight: -999
---
# Uninstallation

Summary: Undo all the steps of your installation.

The rest of this page is an example uninstallation under Debian or Ubuntu, which is based on our recommended [Installation](../installation).

# Considerations

If you want to make a backup uninstalling, see chapter [Operation](../operations) on how to do that. Make sure you move the backup somewhere safe.

If you installed more than one easydb on one server (uncommon), see how they might be separated in chapter [Instantiation](../installation/instances).

# Stop easydb

Stop the easydb components with:

```bash
docker stop  easydb-webfrontend
docker rm -v easydb-webfrontend

docker stop  easydb-server
docker rm -v easydb-server

docker stop  easydb-fylr
docker rm -v easydb-fylr

docker stop  easydb-eas
docker rm -v easydb-eas

docker stop  easydb-elasticsearch
docker rm -v easydb-elasticsearch

docker stop  easydb-pgsql
docker rm -v easydb-pgsql
```

This will also prevent the docker contianers from being started after errors and after booting the underyling Linux, even with the `--restart=always` option which we recommend during container creation.

If you have done integration into init, systemd, etc., then consider removing that, too. But typically, that is not needed and not done.


# Remove the data store {#mount}

In the example installation, we use the "/srv/easydb" directory for all data, including configuration, SQL data, assets, scripts.

Be careful to delete the correct directory and not anything you want to keep, like backups.

```bash
BASEDIR=/srv/easydb
rm -rf $BASEDIR
```


# Remove dedicated docker network

```bash
docker network rm easy5net
```


# Log rotation

Remove `/etc/logrotate.d/easydb`, if you followed the recommended place to configure log rotation.

---

# requirements and related infrastructure

Consider whether you want to keep docker, the requirement for easydb.

If you configured a webserver for easydb, for example Apache as in [this page](../configuration/apache2/), remove that configuration.


