---
title: "39 - Installation"
menu:
  main:
    name: "Installation"
    identifier: "sysadmin/installation"
    parent: "sysadmin"
    weight: 2
---
# Installation

Please follow the [prerequisites](../requirements) for the installation in advance.

## Load easydb on the server

You will receive from us the username, password and the name of your "solution". Here's an example:

```bash
KONTONAME=kunde1234
SOLUTION=base
docker login --username=$KONTONAME docker.easydb.de
```

The above command will request you to enter your password. $KONTONAME is a placeholder. The following commands will then be authorized:

```bash
docker pull docker.easydb.de/pf/server-$SOLUTION
docker pull docker.easydb.de/pf/webfrontend
docker pull docker.easydb.de/pf/elasticsearch
docker pull docker.easydb.de/pf/eas
docker pull docker.easydb.de/pf/postgresql
docker pull docker.easydb.de/pf/fylr
```

Between 4 to 8 gigabytes are downloaded, distributed to the components of the easydb.
Please provide sufficient space. Under e.g. Debian and Ubuntu in /var/lib/docker.

To update the easydb, use the above commands as well.

Note: The storage requirement will quickly increase with updates if old docker data was not cleaned up.

## Define the data store {#mount}

In this example, we use the "/srv/easydb" directory for all data that is generated. Please adjust the first line to your requirements:

```bash
BASEDIR=/srv/easydb
mkdir -p $BASEDIR/config
cd $BASEDIR
mkdir -p webfrontend eas/{lib,log,tmp} elasticsearch/var pgsql/{etc,var,log,backup} easydb-server/{nginx-log,var} fylr/objectstore
chmod a+rwx easydb-server/nginx-log elasticsearch/var eas/tmp; chmod o+t eas/tmp
touch config/eas.yml config/fylr.yml config/elasticsearch.yml
chown 1000:1000 fylr/objectstore
```

## Adjustments

Adjustments are made in the directory $BASEDIR/config. Please add at least the following lines to `$BASEDIR/config/easydb-server.yml`:

```yaml
docker-hostname: easydb-server
pgsql:
  database: easydb5
server:
  external_url: http://hostname.as.seen.in.browser.example.com
extension:
  external-user-schema: true
```

Please note: The last two lines are only valid for the "base" solution ([documented here](../../solutions/base)).

## Completion of the installation

```bash
docker network create easy5net
```

This allows communication between the components.


## Start

The components of the easydb are started with one command each.

Please integrate these commands into the respective init-system of your server.

```bash
BASEDIR=/srv/easydb
docker run -d -ti \
    --name easydb-pgsql \
    --net easy5net \
    --security-opt seccomp=unconfined \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/pgsql/etc:/etc/postgresql \
    --volume=$BASEDIR/pgsql/log:/var/log/postgresql \
    --volume=$BASEDIR/pgsql/var:/var/lib/postgresql \
    --volume=$BASEDIR/pgsql/backup:/backup \
    docker.easydb.de/pf/postgresql
```

---

```bash
sysctl -w vm.max_map_count=262144
# ... can be added persistently via /etc/sysctl.conf instead.

BASEDIR=/srv/easydb
docker run -d -ti \
    --name easydb-elasticsearch \
    --net easy5net \
    --security-opt seccomp=unconfined \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/elasticsearch/var:/var/lib/elasticsearch \
    docker.easydb.de/pf/elasticsearch
```

---

```bash
BASEDIR=/srv/easydb
docker run -d -ti \
    --name easydb-eas \
    --net easy5net \
    --security-opt seccomp=unconfined \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/eas/lib:/var/opt/easydb/lib/eas \
    --volume=$BASEDIR/eas/log:/var/opt/easydb/log/eas \
    --volume=$BASEDIR/eas/tmp:/tmp \
    docker.easydb.de/pf/eas
```
---

```bash
BASEDIR=/srv/easydb
SOLUTION=base
docker run -d -ti \
    --name easydb-server \
    --net easy5net \
    --security-opt seccomp=unconfined \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/easydb-server/var:/easydb-5/var \
    --volume=$BASEDIR/easydb-server/nginx-log:/var/log/nginx \
    docker.easydb.de/pf/server-$SOLUTION
```

---

```bash
BASEDIR=/srv/easydb
docker run -d -ti \
    --name easydb-webfrontend \
    --net easy5net \
    --security-opt seccomp=unconfined \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    -p 80:80 \
    docker.easydb.de/pf/webfrontend
```
---

```bash
BASEDIR=/srv/easydb
docker run -d -ti \
    --name easydb-fylr \
    --net easy5net \
    --security-opt seccomp=unconfined \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/fylr/objectstore:/objectstore \
    docker.easydb.de/pf/fylr
```

---

These are the dependencies:

* easydb-eas depends on easydb-postgresql
* easydb-server depends on easydb-postgresql and easydb-elasticsearch
* easydb-webfrontend depends on easydb-server

During the first start we recommend a waiting time of 20 seconds between the components so that the initial data structures can be created.

---

# Result

At port 80 of your server, the easydb is now ready for requests from web browsers.

---

# Initial login

After the installation you can log in with the following profile for the first time:
Name: root
Password: admin 

We strongly recommend that you change your password immediately after you have logged in.

---

# Further Reading

More commands are listed in chapter [Operation](../betrieb), for example how to update or backup.

To use a https certificate refer to [this page](../konfiguration/recipes/https/).

If you install more than one easydb on one server, please see the additions in chapter [Instantiation](../instances).

