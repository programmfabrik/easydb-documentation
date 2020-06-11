---
title: "39 - Installation under Red Hat"
menu:
  main:
    name: "Installation under Red Hat"
    identifier: "sysadmin/installation/redhat"
    parent: "sysadmin"
    weight: -999
---
# Installation

Please follow the [prerequisites](../requirements) for the installation in advance.

This is the installation under Red Hat Enterprise Linux (RHEL) 8.1. For Debian and Ubuntu see [here](../).

## podman plugin

easydb need the translation of DNS names into container IP addresses, inside containers.

Thus install the [https://github.com/containers/dnsname/blob/master/README_PODMAN.md dnsname plugin] 
```
dnf install containernetworking-plugins dnsmasq
yum module install go-toolset
dnf group install "Development Tools"
cd /usr/src
git clone https://github.com/containers/dnsname
cd dnsname
make all
make install PREFIX=/usr
```

... this creates `/usr/libexec/cni/dnsname`


## create container network
```
podman network create easydb_default
```

 ... also creates `/etc/cni/net.d/easydb_default.conflist`. If this file does not contain the following:
```
      {
         "type": "dnsname",
         "domainName": "dns.podman"
      },
```

 ... then your software version may not be new enough (containernetworking-plugins).

Add into the file `vi /etc/containers/libpod.conf` ...
```
cni_default_network = "easydb_default"
```

  ... or else the mapped ports are not working (`curl webfrontend-container-IP` works, but not `curl main-IP`)


## Download the easydb software to your server

You will receive from us the username, password and the name of your "solution". Here is an example:

```bash
KONTONAME=kunde1234
SOLUTION=base
mkdir /root/.containers
podman login --username=$KONTONAME --authfile=/root/.containers/auth.json docker.easydb.de
```

The above command will request you to enter your password. Do not forget to replace `kunde1234`. The following commands will then be authorized:

```bash
podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/server-$SOLUTION
podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/webfrontend
podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/elasticsearch
podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/eas
podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/postgresql-11
podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/fylr
```

If you bought the pdf-creator plugin you also have to pull the `chrome` container image:
```bash
podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/chrome
```

Between 4 to 10 gigabytes are thus downloaded.
Please provide sufficient space under `/var/lib/containers`.

To update the easydb, use the above commands as well.

Note: The storage requirement will quickly increase with updates if old container data was not cleaned up.

## Define the data store {#mount}

In this example, we use the `/srv/easydb` directory for all data that is generated. Please adjust the first line to your requirements:

```bash
BASEDIR=/srv/easydb
mkdir -p $BASEDIR/config
cd $BASEDIR
mkdir -p webfrontend eas/{lib,log,tmp} elasticsearch/var pgsql/{etc,var,log,backup} easydb-server/{nginx-log,var} fylr/objectstore
chmod a+rwx easydb-server/nginx-log elasticsearch/var eas/tmp; chmod o+t eas/tmp
touch config/eas.yml config/fylr.yml config/elasticsearch.yml
chown 1000:1000 fylr/objectstore
chown 33:33 eas/{lib,log}
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


### trust between the components
```bash
podman network inspect easydb_default|sed -n 's/.*"subnet":/trusted-net:/p'|tr -d '"' > config/eas.yml
```
... results in an `eas.yml` like:
```
trusted-net: 10.89.0.0/24
```

### elasticsearch memory
```bash
echo vm.max_map_count=262144 > /etc/sysctl.d/easydb-elasticsearch.conf
sysctl --load /etc/sysctl.d/easydb-elasticsearch.conf
```

## container creation scripts

The components of the easydb are separated into one container each and are created with one command per container:

```bash
BASEDIR=/srv/easydb
SOLUTION=base

cat >$BASEDIR/run-pgsql.sh <<EOFEOFEOF
if podman run -d -ti \\
    --name easydb-pgsql \\
    --net easydb_default \\
    --volume=$BASEDIR/config:/config:z \\
    --volume=$BASEDIR/pgsql/etc:/etc/postgresql:Z \\
    --volume=$BASEDIR/pgsql/log:/var/log/postgresql:Z \\
    --volume=$BASEDIR/pgsql/var:/var/lib/postgresql:Z \\
    --volume=$BASEDIR/pgsql/backup:/backup:Z \\
    --restart=always \\
    docker.easydb.de/pf/postgresql-11
then
    /srv/easydb/maintain systemd-integrate easydb-pgsql
fi
EOFEOFEOF
chmod a+rx $BASEDIR/run-pgsql.sh

cat >$BASEDIR/run-elasticsearch.sh <<EOFEOFEOF
if podman run -d -ti \\
    --name easydb-elasticsearch \\
    --net easydb_default \\
    --volume=$BASEDIR/config:/config:z \\
    --volume=$BASEDIR/elasticsearch/var:/var/lib/elasticsearch:Z \\
    --restart=always \\
    docker.easydb.de/pf/elasticsearch
then
    /srv/easydb/maintain systemd-integrate easydb-elasticsearch
fi
EOFEOFEOF
chmod a+rx $BASEDIR/run-elasticsearch.sh

cat >$BASEDIR/run-eas.sh <<EOFEOFEOF
if podman run -d -ti \\
    --name easydb-eas \\
    --net easydb_default \\
    --volume=$BASEDIR/config:/config:z \\
    --volume=$BASEDIR/eas/lib:/var/opt/easydb/lib/eas:Z \\
    --volume=$BASEDIR/eas/log:/var/opt/easydb/log/eas:Z \\
    --restart=always \\
    docker.easydb.de/pf/eas
then
    /srv/easydb/maintain systemd-integrate easydb-eas
fi
EOFEOFEOF
chmod a+rx $BASEDIR/run-eas.sh

cat >$BASEDIR/run-server.sh <<EOFEOFEOF
if podman run -d -ti \\
    --name easydb-server \\
    --net easydb_default \\
    --volume=$BASEDIR/config:/config:z \\
    --volume=$BASEDIR/easydb-server/var:/easydb-5/var:Z \\
    --volume=$BASEDIR/easydb-server/nginx-log:/var/log/nginx:Z \\
    --restart=always \\
    --security-opt seccomp=unconfined \\
    docker.easydb.de/pf/server-$SOLUTION
then
    /srv/easydb/maintain systemd-integrate easydb-server
fi
EOFEOFEOF
chmod a+rx $BASEDIR/run-server.sh

cat >$BASEDIR/run-webfrontend.sh <<EOFEOFEOF
if podman run -d -ti \\
    --name easydb-webfrontend \\
    --net easydb_default \\
    --volume=$BASEDIR/config:/config:z \\
    -p 80:80 \\
    --restart=always \\
    docker.easydb.de/pf/webfrontend
then
    /srv/easydb/maintain systemd-integrate easydb-webfrontend
fi
EOFEOFEOF
chmod a+rx $BASEDIR/run-webfrontend.sh

cat >$BASEDIR/run-fylr.sh <<EOFEOFEOF
if podman run -d -ti \
    --name easydb-fylr \\
    --net easydb_default \\
    --volume=$BASEDIR/config:/config:z \\
    --restart=always \\
    docker.easydb.de/pf/fylr
then
    /srv/easydb/maintain systemd-integrate easydb-fylr
fi
EOFEOFEOF
chmod a+rx $BASEDIR/run-fylr.sh
```

The option `restart=always` ensures that the containers are started together with the docker engine, e.g. during server start. This serves as integration into the linux init system.

These are the dependencies:

* easydb-eas depends on easydb-postgresql
* easydb-server depends on easydb-postgresql and easydb-elasticsearch
* easydb-webfrontend depends on easydb-server

During their startup, these containers are waiting for their dependencies to come up. After the dependencies are up, this initial waiting is finished and will not be repeated if the dependencies go down again. Thus, if you e.g. restart easydb-postgresql you have to manually restart easydb-eas and easydb-server (with `systemctl restart easydb-eas easydb-server`).

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

More commands are listed in chapter [Operation](../operations), for example how to update or backup.

To use a https certificate refer to [this page](../configuration/apache2/).

If you install more than one easydb on one server, please see the additions in chapter [Instantiation](instances).

## maintenance script

```bash
touch $BASEDIR/maintain
chmod a+x $BASEDIR/maintain
vi $BASEDIR/maintain
```

maintain consists of:
```bash
#!/bin/bash

# purpose of this script: execute maintenance tasks around easydb:
#
# - create containers using podman using the run-*.sh scripts ("start")
# - integrate with systemd so that containers start during boot
# - stop and remove containers and remove them from systemd ("stop")
# - backup sql
# - update easydb via podman and preserve previous state
# - cleanup superfluous podman files ("cleanup")

# usage:
#
# $0 status                  # shows running containers
# $0 update                  # downloads newest easydb version
# $0 update-auto             # dito plus restart and log into $UPDATELOG
# $0 backup                  # dumps sql into /srv/easydb/pgsql/backup
#                            # is also part of update and update-auto
# $0 cleanup                 # is also part of update and update-auto
# $0 systemd-integrate fylr  # create & enable service file for running(!) container (e.g. fylr)
# $0 stop                    # stops & removes easydb containers and service-files
#                            # Danger: stop will be in effect even after reboot.
# $0 start                   # calls the run-*sh scripts, which should
#                            # create and start the containers, call systemd-integrate
# $0 restart                 # both of the above
# $0 clear_ip_lock abcdef    # remove ip reservations for container abcdef

# Data directory with the subdirectories "config", "easydb-server", etc.:
BASEDIR=/srv/easydb
# Which variant of the image easydb-server shall be used:
SOLUTION=base
# Space-separated list of names of dbs in postgres in container "easydb-pgsql" to dump:
DBS="eas easydb5"
# Of eas DB in $DBS keep this many newest dumps:
KEEPDBS=7
# Where to write log messages to while doing update-auto:
UPDATELOG=/var/log/easydb-update.log

# read local values:
[ -e /etc/default/easydb5 ] && . /etc/default/easydb5

## functions to shorten the script:
stop(){
    systemctl stop $1
    # if systemd-integration somehow does not work, stop it anyway:
    if /usr/bin/podman ps --format="{{.Names}}" | grep -qw $1; then
        /usr/bin/podman stop $1
    fi
}
systemd-desintegrate(){
    systemctl disable $1
    rm /etc/systemd/system/$1.service
    systemctl daemon-reload
}
remove(){
    systemd-desintegrate "$1"
    if /usr/bin/podman ps -a | grep -q $1; then
        /usr/bin/podman rm -v $1
    else
        echo "WARNING: no $1 present to remove"
    fi
}
get_id(){
    /usr/bin/podman inspect $1|sed -n 's/"Id"://p'|tr -d '[:space:]",'
}

case "$1" in
start)
    set -e
    $BASEDIR/run-elasticsearch.sh
    $BASEDIR/run-pgsql.sh
    $BASEDIR/run-eas.sh
    $BASEDIR/run-server.sh
    $BASEDIR/run-webfrontend.sh
    $BASEDIR/run-fylr.sh
    ;;
stop)
    if [ -z "$2" ] ; then
        stop   easydb-webfrontend
        remove easydb-webfrontend
        stop   easydb-server
        remove easydb-server
        stop   easydb-eas
        remove easydb-eas
        stop   easydb-elasticsearch
        remove easydb-elasticsearch
        stop   easydb-fylr
        remove easydb-fylr
        stop   easydb-pgsql
        remove easydb-pgsql
    else
        stop   "$2"
        remove "$2"
    fi
;;
restart)
    $0 stop 2>&1 | sed '/Network easydb.* not found/d'
    $0 start
;;
systemd-integrate)
    if [ -z "$2" ] ; then
        echo "ERROR: no container given as 2nd argument, ABORTING"
        exit 14
    fi
    if /usr/bin/podman ps --format="{{.ID}} {{.Names}}" | grep -qw $2; then
        ID=`get_id $2`
        /usr/bin/podman generate systemd $2 \
            | sed '/^ExecStart=/iExecStartPre=/bin/bash -c "'"$BASEDIR"'/maintain clear_ip_lock '$ID'"' \
            > /etc/systemd/system/$2.service
        systemctl daemon-reload
        systemctl enable $2
        systemctl start $2 # does not start a 2nd one but instead recognizes that it is started
    else
        echo "WARN: no container '$2' running, nothing done"
    fi
;;
systemd-desintegrate)
    if [ -z "$2" ] ; then
        echo "ERROR: no container given as 2nd argument, ABORTING"
        exit 14
    fi
    systemd-desintegrate "$2"
;;
status)
    /usr/bin/podman ps
;;
update)
    if   $0 backup
    then $0 tag
         $0 cleanup
         $0 pull
    else
        echo "ERROR: backup failed - not updating!">&2
    fi
    ;;
update-auto)
    echo             >> $UPDATELOG
    date             >> $UPDATELOG
    if   $0 backup   >> $UPDATELOG
    then $0 tag      >> $UPDATELOG
         $0 cleanup  >> $UPDATELOG
         $0 pull     >> $UPDATELOG
         date        >> $UPDATELOG
         $0 restart  2>&1 >>$UPDATELOG |tee -a $UPDATELOG |grep -v '^Creating'
                                                          #^^^^^^^^^^^^^^^^^^
                                                          # prevent lines starting with "Creating"
                                                          # from reaching cron mails, because
                                                          # they're neither warnings nor errors
                                       #^^^^^^^^^^^^^^^^^ put stderr into LOG
                         #^^^^^^^^^^^^ put stdout into LOG(does NOT affect stderr)
                    #^^^^ put stderr where stdout currently points to. (make it reach cron mails)
    else
        echo "ERROR: backup failed - not updating!">> $UPDATELOG
        echo "ERROR: backup failed - not updating!">&2
    fi
    ;;
backup)
    # do sql backup of all sql dbs $DBS (one per instance and one for eas)
    # Note: there are only $KEEPDBS kept - repeating this quickly removes all old backups (on this host) !
    cd $BASEDIR/pgsql/backup          || exit 2
    /usr/bin/podman ps|grep -q 'easydb-pgsql$' || exit 3
    for DB in $DBS; do
            $0 sqldump $DB            || exit 4
    done
    exit 0
    ;;
sqldump)
    # do sql backup of one given sql db name (inside container "easydb-pgsql")
    DB="$2"
    TIME=`date +%Y-%m-%d_%Hh%Mm%Ss`
    FILE=$DB."$TIME".pgdump
    /usr/bin/podman exec easydb-pgsql pg_dump -U postgres -v -Fc -f /backup/$FILE $DB > $FILE.log 2>&1
    EXCODE=$?
    if [ $EXCODE -gt 0 ] ; then
        rm $FILE &>/dev/null
        mv $FILE.log  $FILE.log.FAIL &>/dev/null
        echo "pg_dump $DB exited with $EXCODE. Logfile is $BASEDIR/pgsql/backup/$FILE.log.FAIL"
        echo "pg_dump $DB exited with $EXCODE. Logfile is $BASEDIR/pgsql/backup/$FILE.log.FAIL" >&2
        exit 4
    else
        # rotate so that only the last $KEEPDBS valid dumps remain. Also for logs.
        ls -1 --color=no $DB.*s.pgdump    |sort -r|tail -n +$((KEEPDBS+1))|while read i; do rm $i; done
        ls -1 --color=no $DB.*s.pgdump.log|sort -r|tail -n +$((KEEPDBS+1))|while read i; do rm $i; done
    fi
    exit 0
    ;;
tag)
    # tag the current image version as "previous" - good before an update if you want to go back.
    # Danger: this will overwrite the "previous"ly preserved image version!
    /usr/bin/podman tag docker.easydb.de/pf/server-$SOLUTION:latest docker.easydb.de/pf/server-$SOLUTION:previous
    /usr/bin/podman tag docker.easydb.de/pf/webfrontend:latest      docker.easydb.de/pf/webfrontend:previous
    /usr/bin/podman tag docker.easydb.de/pf/eas:latest              docker.easydb.de/pf/eas:previous
    /usr/bin/podman tag docker.easydb.de/pf/elasticsearch:latest    docker.easydb.de/pf/elasticsearch:previous
    /usr/bin/podman tag docker.easydb.de/pf/postgresql-11:latest   docker.easydb.de/pf/postgresql-11:previous
    /usr/bin/podman tag docker.easydb.de/pf/fylr:latest         docker.easydb.de/pf/fylr:previous
    ;;
pull)
    /usr/bin/podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/server-$SOLUTION
    /usr/bin/podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/webfrontend
    /usr/bin/podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/elasticsearch
    /usr/bin/podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/eas
    /usr/bin/podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/postgresql-11
    /usr/bin/podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/fylr
    ;;
clear_ip_lock)
    # delete files that lock IP addresses for a given container-id

    if [ -z "$2" ] ; then
        echo "WARNING: no container id given" >&2
        exit 0
    fi

    grep --color=no -l $2 /var/lib/cni/networks/easydb_default/* |while read file
    do
        echo "deleting dangling lock $file"
        rm -f  "$file"
    done
    exit 0
;;
cleanup)
    #  free disk space
    #
    #  In our experience, used containers are not damaged by these commands
    #  and used images are not damaged even if they have no running container.
    #  Some error messages may be generated, however ("could not remove").

    echo "removing left over temporary files..."
    LIST=$(/usr/bin/podman ps -qa --no-trunc --filter "status=exited")
    if [ "$LIST" ] ; then
        /usr/bin/podman rm -v $LIST #>/dev/null
        echo "... done."
    else
        echo "... none found."
    fi

    echo "removing unused images..."
    LIST=$(/usr/bin/podman images --filter "dangling=true" -q --no-trunc)
    if [ "$LIST" ] ; then
        /usr/bin/podman rmi $LIST #>/dev/null
        echo "... done."
    else
        echo "... none found."
    fi

    echo "removing unused volumes..."
    /usr/bin/podman volume prune -f
    echo "... done."
    
    echo All done cleaning up.
    ;;
*)
    echo "ERROR: argument '$1' not implemented."
    ;;
esac
```

# Start

This will create the containers and start them and integrate them into systemd. They will then automatically start on Linux boot.

```bash
$BASEDIR/maintain status
$BASEDIR/maintain start
$BASEDIR/maintain status
```

