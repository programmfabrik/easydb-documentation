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

Please follow the [prerequisites](../../requirements) for the installation in advance.

The recommended installation is with Debian or Ubuntu: see [here](../).

This page is the installation under Red Hat Enterprise Linux (RHEL) 8.1, which is less robust but also works.

## podman plugin

easydb needs translation of DNS names into container IP addresses, inside containers.

Therefore install the [dnsname plugin](https://github.com/containers/dnsname/blob/master/README_PODMAN.md).

First make sure that you have up to date packages, or else the dnsname plugin might not work:
```
dnf update
```

Then, install the dnsname plugin:
```
dnf install containernetworking-plugins dnsmasq
dnf module install go-toolset
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
 ... this creates `/etc/cni/net.d/easydb_default.conflist`. If this file does not contain the following:

```
      {
         "type": "dnsname",
         "domainName": "dns.podman"
      },
```

 ... then your version of containernetworking-plugins may not be new enough. `dns.podman` seems to be just an arbitrary name, though.

Add into the file `/etc/containers/libpod.conf` ...
```
cni_default_network = "easydb_default"
```

  ... or else the mapped ports are not working (`curl webfrontend-container-IP` works, but not `curl main-host-IP`, both from the podman host system)


## Download the easydb software to your server {#download}

You will receive from us the username and password.
In case you did not receive a "solution" name, then assume that this is `base`. Here is an example:

```bash
KONTONAME=kunde1234
SOLUTION=base
mkdir /root/.containers
podman login --username=$KONTONAME --authfile=/root/.containers/auth.json docker.easydb.de
```

The above command will request you to enter your password. Do not forget to replace `kunde1234`. The following commands will then be authorized. Please continue with them:

```bash
podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/server-$SOLUTION
podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/webfrontend
podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/elasticsearch
podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/eas
podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/postgresql-14
podman pull --authfile=/root/.containers/auth.json docker.easydb.de/pf/fylr
```

Between 4 to 10 gigabytes are thus downloaded.
Please provide sufficient space under `/var/lib/containers`.

Please note: Whenever you want to download easydb updates, repeat the above commands. To complete the update process, you then just need to re-create the containers (see below, `maintain restart`).

Take care: The storage requirement will quickly increase with updates if old container data and old container images are not cleaned up regularly.

## Define the data store {#mount}

In this example, we use the directory `/srv/easydb` for all data that is generated. Please adjust the first line to your requirements:

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

Please note: The last two lines are only valid for the "base" solution ([documented here](../../../solutions/base)).


### trust between the components
```
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

The components of the easydb are separated into one container each and are created with one command per container. In this example, we put them into separate scripts:

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
    docker.easydb.de/pf/postgresql-14
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
    docker.easydb.de/pf/eas
then
    /srv/easydb/maintain systemd-integrate easydb-eas --requires srv-easydb-eas-lib.mount --after srv-easydb-eas-lib.mount # example
fi
EOFEOFEOF
chmod a+rx $BASEDIR/run-eas.sh

cat >$BASEDIR/run-server.sh <<EOFEOFEOF
if podman run -d -ti \\
    --name easydb-server \\
    --net easydb_default \\
    --cap-add SYS_PTRACE \\
    --volume=$BASEDIR/config:/config:z \\
    --volume=$BASEDIR/easydb-server/var:/easydb-5/var:Z \\
    --volume=$BASEDIR/easydb-server/nginx-log:/var/log/nginx:Z \\
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
    docker.easydb.de/pf/fylr
then
    /srv/easydb/maintain systemd-integrate easydb-fylr
fi
EOFEOFEOF
chmod a+rx $BASEDIR/run-fylr.sh
```

Make sure to replace the example name `srv-easydb-eas-lib.mount` in `run-eas.sh` with your correct systemd mount name.

The call `/srv/easydb/maintain systemd-integrate` ensures that the containers are started together with Linux.

These are the dependencies:

* easydb-eas depends on easydb-postgresql
* easydb-server depends on easydb-postgresql, easydb-eas and easydb-elasticsearch
* easydb-webfrontend depends on easydb-server

During their startup, these containers are waiting for their dependencies to come up. After the dependencies are up, this initial waiting is finished and will not be repeated if the dependencies go down again. Thus, if you e.g. restart easydb-postgresql you have to manually restart easydb-eas and easydb-server (with `systemctl restart easydb-eas easydb-server`).


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
# $0 systemd-integrate fylr  # create & enable service file for running(!) container
# $0 stop                    # stops & removes easydb containers and systemd service-files
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
# Of each DB in $DBS keep this many newest dumps:
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
    $BASEDIR/run-fylr.sh
    $BASEDIR/run-pgsql.sh
    $BASEDIR/run-eas.sh
    $BASEDIR/run-server.sh
    $BASEDIR/run-webfrontend.sh
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
    # usage:   $0 systemd-integrate containername [podman generate systemd options]
    # example: maintain systemd-integrate easydb-eas --requires srv-easydb-eas-lib.mount --after srv-easydb-eas-lib.mount
    # all arguments after (in the above exmaple) easydb-eas are optional

    CNT=$2 # container name
    if [ -z "$CNT" ] ; then
        echo "ERROR: no container given as 2nd argument, ABORTING"
        exit 14
    fi
    shift  # $2 becomes $1, $3 becomes $2, etc., removing systemd-integrate from the arguments
    shift  # removing the container name from the arguments, the rest goes to podman

    if /usr/bin/podman ps --format="{{.ID}} {{.Names}}" | grep -qw $CNT; then
        ID=`get_id $CNT`
        /usr/bin/podman generate systemd $@ $CNT \
            | sed '/^ExecStart=/iExecStartPre=/bin/bash -c "'"$BASEDIR"'/maintain clear_ip_lock '$ID'"' \
            > /etc/systemd/system/$CNT.service
        systemctl daemon-reload
        systemctl enable $CNT 2>&1|grep -vE '^Created '
        systemctl start $CNT # does not start a 2nd one but instead recognizes that it is started
    else
        echo "WARN: no container '$CNT' running, nothing done"
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
    echo ___start___ >> $UPDATELOG
    date             >> $UPDATELOG
    if   $0 backup   >> $UPDATELOG
    then $0 tag      >> $UPDATELOG
         $0 cleanup  2>&1 >>$UPDATELOG |tee -a $UPDATELOG |grep -v ' image is in use by a container'

         $0 pull     >> $UPDATELOG
         date        >> $UPDATELOG
         $0 restart  2>&1 >>$UPDATELOG |tee -a $UPDATELOG |grep -v '^Creating'
                                                          #^^^^^^^^^^^^^^^^^^
                                                          # prevent lines starting with "Creating"
                                                          # from reaching cron mails, because
                                                          # they're neither warnings nor errors
                                       #^^^^^^^^^^^^^^^^^ put stderr into LOG
                         #^^^^^^^^^^^^ put stdout into LOG(does NOT affect stderr)
                    #^^^^ put stderr where stdout currently points to. (make it reach grep)
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
    /usr/bin/podman tag docker.easydb.de/pf/postgresql-14:latest   docker.easydb.de/pf/postgresql-14:previous
    /usr/bin/podman tag docker.easydb.de/pf/fylr:latest         docker.easydb.de/pf/fylr:previous
    ;;
pull)
    /usr/bin/podman pull -q --authfile=/root/.containers/auth.json docker.easydb.de/pf/server-$SOLUTION
    /usr/bin/podman pull -q --authfile=/root/.containers/auth.json docker.easydb.de/pf/webfrontend
    /usr/bin/podman pull -q --authfile=/root/.containers/auth.json docker.easydb.de/pf/elasticsearch
    /usr/bin/podman pull -q --authfile=/root/.containers/auth.json docker.easydb.de/pf/eas
    /usr/bin/podman pull -q --authfile=/root/.containers/auth.json docker.easydb.de/pf/postgresql-14
    /usr/bin/podman pull -q --authfile=/root/.containers/auth.json docker.easydb.de/pf/fylr
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
/srv/easydb/maintain start
```

We assume you used `/srv/easydb` as the data storage.

We recommend that you use `/srv/easydb/maintain status` before and after such a manual start.

---

# Result

At port 80 of your server, the easydb is now ready for requests from web browsers.

Your firewall may block this, however. Consider:

```bash
firewall-cmd --zone=public             --add-service=http
firewall-cmd --zone=public --permanent --add-service=http
```

Beware: After any `firewall-cmd --reload` you have to recreate all containers with e.g. `/srv/easydb/maintain restart` to recreate the needed firewall routes for container-to-container communication. We advise you to not assume that a reboot would do the same.


---

# Initial login

After the installation you can log in with the following profile for the first time:

- Login: ***root***
- Password: ***admin*** 

We strongly recommend that you change your password immediately after you have logged in.

---

# Further Reading

More commands are listed in chapter [Operation](../../operations), for example how to backup.
