---
title: "9 - Operations"
menu:
  main:
    name: "Operations"
    identifier: "sysadmin/operations"
    parent: "sysadmin"
    weight: -996
---
# Operation

# Update

To **update** the easydb software, repeat the download section of the installation:

For Debian/Ubuntu: [Here](../installation#download)

For Red Hat: [Here](../installation/redhat#download)

However, the downloaded version will not be used until the containers have been stopped and recreated.

# Stop Containers {#stop}

To **stop** the easydb and remove the current containers, use the following commands:

For Red Hat:

```bash
/srv/easydb/maintain stop
```


For Debian/Ubuntu:

Check that in your installation the container is indeed named `easydb-server`, with `docker ps`. Then:

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

If you are running more than one easydb on the same server, please note the additions in chapter [instantiation](../installation/instances/#instances).

&nbsp;

# Recreate Containers

To recreate the containers, repeat the start section of the installation:

For Debian/Ubuntu: [Here](../installation#start)

For Red Hat: [Here](../installation/redhat#start)

&nbsp;

# Status

Which easydb components are currently running can be displayed with `docker ps`. Here is a sample display while all components are running:

```bash
CONTAINER ID        IMAGE                                       COMMAND             CREATED             STATUS              PORTS                   NAMES
efe480718a0e        docker.easydb.de/pf/webfrontend        "/startup.sh"       9 days ago          Up 9 days           0.0.0.0:80->80/tcp      easydb-webfrontend
cdfe24889c0c        docker.easydb.de/pf/server-base        "/startup.sh"       9 days ago          Up 9 days           80/tcp, 3451-3452/tcp   easydb-server
2a77e387f88a        docker.easydb.de/pf/fylr               "/startup.sh"       2 days ago          Up 2 days           4000/tcp                easydb-fylr
8a17a2a5ea26        docker.easydb.de/pf/eas                "/startup.sh"       10 weeks ago        Up 10 weeks         80/tcp                  easydb-eas
19bf53e50287        docker.easydb.de/pf/elasticsearch      "/startup.sh"       10 weeks ago        Up 10 weeks         9200/tcp, 9300/tcp      easydb-elasticsearch
1a51017ae36e        docker.easydb.de/pf/postgresql         "/startup.sh"       10 weeks ago        Up 10 weeks         5432/tcp                easydb-pgsql
```

To display dormant components, use `docker ps -a`.

&nbsp;

## Monitoring

You can use our free [plugin](https://github.com/programmfabrik/check-easydb5) which works with either Nagios or Icinga, to monitor your easydb.

## Backup 

Please refer to [backup and restore](../backupandrestore) manual. 
