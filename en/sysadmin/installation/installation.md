# Installation

Please note the [prerequisites](../requirements/requirements.html) for the installation in advance.

## Load easydb on the server

You will receive from us the Username, Password and the name of your "Solution". Here's an example:

    KONTONAME=zeus
    SOLUTION=pantheon
    docker login --username=$KONTONAME docker.easydb.de:5000

The above command will request you to enter in your password. $KONTONAME is a placeholder. The following commands will then be authorized:

    docker pull docker.easydb.de:5000/pf/server-$SOLUTION
    docker pull docker.easydb.de:5000/pf/fylr
    docker pull docker.easydb.de:5000/pf/webfrontend
    docker pull docker.easydb.de:5000/pf/elasticsearch
    docker pull docker.easydb.de:5000/pf/eas
    docker pull docker.easydb.de:5000/pf/postgresql

Between 4 to 8 gigabytes are downloaded, distributed to the components of the easydb.
Please ensure sufficient space. Under Debian and Ubuntu e.g. in /var/lib/docker.

To update the easydb, use the above commands as well.

Note: The storage requirement will quickly increase with updates if old docker data was not cleaned up.

## Define the data store {#mount}

In this example, we use the "/srv/easydb" directory for all data that is generated. Please adjust at least the first line to your requirements:

    BASEDIR=/srv/easydb
    mkdir -p $BASEDIR/config
    cd $BASEDIR
    mkdir -p webfrontend eas/{lib,log,tmp} elasticsearch/var pgsql/{etc,var,log,backup} easydb-server/{nginx-log,var}
    chmod a+rwx easydb-server/nginx-log elasticsearch/var eas/tmp; chmod o+t eas/tmp

## Adjustments

Optional adjustments are made in `easydb5-master.yml`, in the directory BASEDIR/config. Please add the following lines:

    easydb-server:
      docker-hostname: easydb-server
      pgsql:
        database: easydb
      server:
        external_url: http://hostname.as.seen.in.browser.example.com

Please note the special features of your solution. For the "base" solution, [documented here](../../solutions/base/base.html).

## Completion of the installation

    docker network create easy5net

This allows communication between the components.


## Start

The six components of the easydb are started with one command each.

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

    sysctl -w vm.max_map_count=262144
    # ... can be added persistently via /etc/sysctl.conf instead.

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
        --volume=$BASEDIR/eas/tmp:/tmp \
        docker.easydb.de:5000/pf/eas

---

    docker run -d -ti \
        --name easydb-fylr \
        --net easy5net \
        --volume=$BASEDIR/config:/config \
        docker.easydb.de:5000/pf/fylr

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

---

These are the dependencies:

* easydb-eas depends on easydb-postgresql
* easydb-server depends on easydb-postgresql and easydb-elasticsearch
* easydb-webfrontend depends on easydb-server

Particularly at the first start we recommend a waiting time of 20 seconds between the components so that the initial data structures can be created.

Each time between the start of easydb-elasticsearch and easydb-server you may need a waiting time. Its length depends on hardware and accumulated data.

To help you with integrating easydb into system init, we present an example solution in bash scripting language.

The following (part of an) init-script waits for easydb-elasticsearch:

~~~~
MAXWAITCYCLE=24    # prevent hanging around in hopless cases
                   # prevent disturbing later (re)starts

waitforelastic(){  # sleep until elasticsearch is ready
    until
        docker exec -ti easydb-elasticsearch cat /var/log/elasticsearch/docker-cluster.log 2>/dev/null |grep -q 'Cluster health status changed from .* to \[GREEN\]' 2>/dev/null
    do
        sleep 10
        MAXWAITCYCLE=$((MAXWAITCYCLE-1))
        [ $MAXWAITCYCLE -lt 1 ] && break
    done
}

case "$1" in
start|restart)
        $0 stop 2>&1 | sed '/No such container:/d; s/^/stopping: /'
        set -e
        run-easydb-elasticsearch
        run-easydb-pgsql
        sleep 10
        run-easydb-eas
        waitforelastic
        run-easydb-server
        sleep 10
        run-easydb-webfrontend
;;
stop)
        /usr/bin/docker stop  easydb-webfrontend
        /usr/bin/docker rm -v easydb-webfrontend
        /usr/bin/docker stop  easydb-server
        /usr/bin/docker rm -v easydb-server
        /usr/bin/docker stop  easydb-eas
        /usr/bin/docker rm -v easydb-eas
        /usr/bin/docker stop  easydb-elasticsearch
        /usr/bin/docker rm -v easydb-elasticsearch
        /usr/bin/docker stop  easydb-pgsql
        /usr/bin/docker rm -v easydb-pgsql
~~~~


---

# Result

At port 80 of your server, the easydb is now ready for requests from web browsers.

---

# Further Reading

More commands are listed in chapter [Operation](../betrieb/betrieb.html), for example how to update or backup.

If you install more than one easydb on one server, please see the additions in chapter [Instantiation](../instances/instances.html).

