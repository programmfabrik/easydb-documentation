---
title: "39 - Installation"
menu:
  main:
    name: "Installation"
    identifier: "sysadmin/installation"
    parent: "sysadmin"
    weight: -998
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
docker pull docker.easydb.de/pf/postgresql-11
docker pull docker.easydb.de/pf/fylr
```

If you bought the pdf-creator plugin you also have to pull the `chrome` docker container:
```bash
docker pull docker.easydb.de/pf/chrome
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

The components of the easydb are separated into one docker container each and are created with one command per container:

```bash
BASEDIR=/srv/easydb
docker run -d -ti \
    --name easydb-pgsql \
    --net easy5net \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/pgsql/etc:/etc/postgresql \
    --volume=$BASEDIR/pgsql/log:/var/log/postgresql \
    --volume=$BASEDIR/pgsql/var:/var/lib/postgresql \
    --volume=$BASEDIR/pgsql/backup:/backup \
    docker.easydb.de/pf/postgresql-11
```

```bash
sysctl -w vm.max_map_count=262144
# ... can be added persistently via /etc/sysctl.conf instead.

BASEDIR=/srv/easydb
docker run -d -ti \
    --name easydb-elasticsearch \
    --net easy5net \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/elasticsearch/var:/var/lib/elasticsearch \
    docker.easydb.de/pf/elasticsearch
```

```bash
BASEDIR=/srv/easydb
docker run -d -ti \
    --name easydb-eas \
    --net easy5net \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/eas/lib:/var/opt/easydb/lib/eas \
    --volume=$BASEDIR/eas/log:/var/opt/easydb/log/eas \
    --volume=$BASEDIR/eas/tmp:/tmp \
    docker.easydb.de/pf/eas
```

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

```bash
BASEDIR=/srv/easydb
docker run -d -ti \
    --name easydb-webfrontend \
    --net easy5net \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    -p 80:80 \
    docker.easydb.de/pf/webfrontend
```

```bash
BASEDIR=/srv/easydb
docker run -d -ti \
    --name easydb-fylr \
    --net easy5net \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/fylr/objectstore:/objectstore \
    docker.easydb.de/pf/fylr
```

The option `restart=always` ensures that the containers are started together with the docker engine, e.g. during server start. This serves as integration into the linux init system.

These are the dependencies:

* easydb-eas depends on easydb-postgresql
* easydb-server depends on easydb-postgresql and easydb-elasticsearch
* easydb-webfrontend depends on easydb-server

During their startup, the containers are waiting for their dependencies to come up. After the dependencies are up, this initial waiting is finished and will not be repeated if the dependencies go down again. Thus, if you e.g. restart easydb-postgresql you have to manually restart easydb-eas and easydb-server (with `docker restart easydb-eas easydb-server`).

---

# Result

At port 80 of your server, the easydb is now ready for requests from web browsers.

---

# Initial login

After the installation you can log in with the following profile for the first time:

- Login: ***root***
- Password: ***admin*** 

We strongly recommend that you change your password immediately after you have logged in.

---

# Further Reading

More commands are listed in chapter [Operation](../betrieb), for example how to update or backup.

To use a https certificate refer to [this page](../configuration/apache2/).

If you install more than one easydb on one server, please see the additions in chapter [Instantiation](instances).

------

If you are interested in a complete tutorial, please follow this [link](/en/tutorials/testsystem/).