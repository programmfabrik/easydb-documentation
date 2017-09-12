# Installation

Please note the [prerequisites](../requirements/requirements.md) for the installation in advance.

## Load easydb on the server

You will receive from us the Kontoname, Password and the name of your "Solution". Here's an example:

    KONTONAME=zeus
    SOLUTION=pantheon
    docker login --username=$KONTONAME docker.easydb.de:5000

The above command will poll the password. $ KONTONAME is a placeholder and is replaced with the dollar sign. The following commands are then authorized:

    docker pull docker.easydb.de:5000/pf/server-$SOLUTION
    docker pull docker.easydb.de:5000/pf/webfrontend
    docker pull docker.easydb.de:5000/pf/elasticsearch
    docker pull docker.easydb.de:5000/pf/eas
    docker pull docker.easydb.de:5000/pf/postgresql

Approximately 7 gigabytes are downloaded, distributed to the five executable components of the easydb.
Please ensure sufficient space. Under Debian and Ubuntu e.g. in /var/lib/docker.

To update the easydb, use the above commands as well. The storage requirement will only increase slightly.

## Identify the data store

In this example, we use the/srv/easydb directory for all data that is generated. Please adjust at least the first line to your requirements:

    BASEDIR=/srv/easydb
    mkdir -p $BASEDIR/config
    cd $BASEDIR
    mkdir -p webfrontend eas/{lib,log} elasticsearch/var pgsql/{etc,var,log,backup} easydb-server/{nginx-log,var}
    chmod a+rwx easydb-server/nginx-log elasticsearch/var

## Adjustments

Optional adjustments are made in `easydb5-master.yml`, in the directory BASEDIR/config. Create these with at least the following equipment:

    easydb-server:
      docker-hostname: easydb-server
      pgsql:
        database: easydb
      server:
        external_url: http://hostname.as.seen.in.browser.example.com

Please note the special features of your solution. For the "base" solution, e.g. [Documented here](../../solutions/base/base.md).

## Completion of the installation

    Docker network create easy5net

This allows communication between the components.


## Start

The five components of the easydb are started with one command each.

Please integrate these commands into the respective init-system of your server.


    docker run -d -ti \
        --name easydb-pgsql \
        --net easy5net \
        --volume=$BASEDIR/config:/config \
        --volume=$BASEDIR/pgsql/etc:/etc/postgresql \
        --volume=$BASEDIR/pgsql/log:/var/log/postgresql \
        --volume=$BASEDIR/pgsql/var:/var/lib/postgresql \
        --volume=$BASEDIR/pgsql/backup:/backup \
        docker.easydb.de:5000/pf/postgresql

---

    docker run -d -ti \
        --name easydb-elasticsearch \
        --net easy5net \
        --volume=$BASEDIR/config:/config \
        --volume=$BASEDIR/elasticsearch/var:/var/lib/elasticsearch \
        docker.easydb.de:5000/pf/elasticsearch

---

    docker run -d -ti \
        --name easydb-eas \
        --net easy5net \
        --volume=$BASEDIR/config:/config \
        --volume=$BASEDIR/eas/lib:/var/opt/easydb/lib/eas \
        --volume=$BASEDIR/eas/log:/var/opt/easydb/log/eas \
        docker.easydb.de:5000/pf/eas

---

    docker run -d -ti \
        --name easydb-server \
        --net easy5net \
        --volume=$BASEDIR/config:/config \
        --volume=$BASEDIR/easydb-server/var:/easydb-5/var \
        --volume=$BASEDIR/easydb-server/nginx-log:/var/log/nginx \
        docker.easydb.de:5000/pf/server-$SOLUTION

---

    docker run -d -ti \
        --name easydb-webfrontend \
        --net easy5net \
        --volume=$BASEDIR/config:/config \
        -p 80:80 \
        docker.easydb.de:5000/pf/webfrontend



The order of the five commands shown here fulfills the dependencies between the components and must therefore be observed.

Particularly at the first start we recommend a waiting time of 10 seconds between the components so that the initial data structures can be created.

This guide will still make small changes to the easydb updates.

---

# Result

At port 80 of your server, the easydb is now ready for requests from web browsers.


---

# Advanced

The commands for terminating the easydb are listed in chapter [Operation](../betrieb/betrieb.md).

If you install more than one easydb on one server, please see the additions in chapter [Instantiation](../instances/instances.md).
