# Install EasyDB in Debian 8

Documentation based on an installation of Debian with image debian-8.8.0-amd64-netinst.iso and HTTP Server options selected during installation.
Debian was installed in a VirtualBox machine with a NAT network interface, and the host is connected to a Programmfabrik VPN. Connection to the VPN is required to clone the git repository of easydb.


## Add required repositories

Commands are executed as the root user.

* Edit */etc/apt/sources.list* and add after each line begining with "deb", " main non-free".
    Example:
```
deb http://ftp.us.debian.org/debian/ jessie main contrib non-free
```

* Add Programmfabrik, elasticsearch and backports repos:
    At the end of file */etc/apt/sources.list* add the following lines:

```
# programmfabrik-keyring
deb http://packages-testing.programmfabrik.de/be52ae33594eb794828ccd4837cf08ae/debian  ./
# easydb asset server
deb http://archive.programmfabrik.de/ jessie main non-free

deb http://ftp.uk.debian.org/debian jessie-backports main

deb http://packages.elastic.co/elasticsearch/1.7/debian stable main
```

* Add key for Elasticsearch repository:

```
$ wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add -
```

* Update package's list:

```
$ apt-get update
```

## Install required packages:

```
$ apt-get install build-essential postgresql-9.4 postgresql-contrib-9.4 libboost-all-dev git autoconf2.13 libpqxx-dev mm-common libxml2-dev libglibmm-2.4-dev docbook-xsl libossp-uuid-dev libgmime-2.6-dev libcurl4-gnutls-dev libxslt1-dev libfcgi-dev libyaml-cpp-dev libarchive-dev python-yaml nodejs nodejs-legacy npm ruby libapache2-mod-fastcgi libapache2-mod-fcgid libapache2-mod-macro libapache2-mod-php5 libapache2-mod-shib2 python-ldap
```

## Configure PostgreSQL:

* Edit */etc/postgresql/9.?/main/pg_hba.conf* and add the following line:

```
local   all             postgres                                trust
```

* Restart PostgreSQL:

```
$ /etc/init.d/postgresql restart
```

* Create databases:

```
$ createdb -U postgres eas
$ createdb -U postgres easy5
```

## Install coffeescript 1.10

```
$ wget http://xxxx/coffeescript-1.10.0.tar.gz
$ tar xvfz coffeescript-1.10.0.tar.gz
$ cd coffeescript-1.10.0
$ npm install
$ bin/cake install
```

## Install easydb-l10n2json.py

Download and place it in some directory in $PATH, for instance: */usr/local/bin*

```
$ wget http://xxxx/easydb-l10n2json.py
$ mv easydb-l10n2json.py /usr/local/bin/
```

## EASYDB

* Private / public key

    A private/public key is required for cloning repository.  Klaus generated it for me.
    ssh-agent have to be running and the key needs to be added before cloning the repo.

    With the keys *KEY_NAME / KEYNAME.pub* in *WHEREVER_DIRECTORY* directory:

```
$ mkdir ~/.ssh
$ chmod 700 ~/.ssh
$ cd WHEREVER_DIRECTORY
$ mv KEY_NAME KEY_NAME.pub ~/.ssh/
$ cd ~/.ssh
$ chmod 600 KEY_NAME*
$ eval `ssh-agent`
$ ssh-add ~/.ssh/KEY_NAME
```

* Clone repository and compile

    Option *-j4* of *make* could generate the error *exhausted memory*, if this happen try wity *make -j2* or just *make*

```
$ mkdir ~/easydb
$ cd ~/easydb
$ git clone --recursive git@git.programmfabrik.de:easydb 5
$ make -j4 
```

## Install easydb-asset-server

Accept the instalation of unaunthicated packages

```
# sudo apt-get install easydb-asset-server
```

Configure it based on

- [http://docs.easydb.de/latest-stable/system/eas/installation/](http://docs.easydb.de/latest-stable/system/eas/installation/)
- [http://docs.easydb.de/latest-stable/system/eas/conf/](http://docs.easydb.de/latest-stable/system/eas/conf/)


## Configure Apache

```
$ cd /etc/apache2/conf-enabled
$ sudo ln -s /etc/opt/easydb/eas/apache-easydb-asset-server.inc apache-easydb-asset-server.conf
```

* Download *apache-fastcgi.conf* and *easydb-5-macros.conf* and copy to */etc/apache2/conf-available/*
    Files can be download from [here](http://xxx)

    Enable configuration:
```
$ cd /etc/apache2/conf-enabled
$ ln -s ../conf-available/apache-fastcgi.conf
$ ln -s ../conf-available/easydb-5-macros.conf
```

* Configure VirtualHost
    Replace */etc/apache2/sites-available/000-default.conf* with [virtualhost.conf](http://xxxx)

* Install required modules

    Command:
    ```$ a2enmod MODULE_NAME```

    Modules: ```actions dav_fs include mpm_prefork proxy socache_shmcb ssl```

* Uninstall mpm_event

```
$ a2dismod mpm_event
```

* Create required paths

```
$ mkdir $HOME/logs
$ mkdir $HOME/easdoc
```

* Restart apache

```
$ /etc/init.d/apache2 restart
```

## Configure EASYDB
[https://tickets.programmfabrik.de/wiki/Entwicklungsumgebung%20einrichten](https://tickets.programmfabrik.de/wiki/Entwicklungsumgebung%20einrichten)

## Install and Configure Elasticsearch
[https://tickets.programmfabrik.de/wiki/easydb5/InstallationPROD#repositories](https://tickets.programmfabrik.de/wiki/easydb5/InstallationPROD#repositories)

