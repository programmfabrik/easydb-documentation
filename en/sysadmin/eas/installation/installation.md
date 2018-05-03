# Installing the easydb asset server

## Package installation

After entering the installation source in `/etc/apt/sources.list`, the installation of the necessary software is done with the following commands:

~~~
 apt-get update
apt-get install easydb-asset-server
~~~


Due to the dependencies of the package, all programs required by EAS are installed, including ImageMagick (image processing), MPlayer/FFmpeg (video recognition and conversion), OpenOffice.org (office conversion), the PostgreSQL database server and the Apache web server.


Database
=========

The EAS needs a PostgreSQL database. The EAS can be installed together with easydb in a database, because EAS uses only the schema `eas`; however, Typically they are separate databases.

The database in the EAS is connected via the variable `EAS_PG_DSN` in the [Configuration File](/sysadmin/eas/conf/conf.html).

Create the EAS database
-------------------------

The EAS needs an existing database, the creation and maintenance of the schema is done automatically. For a standard installation the following command is recommended (creates an empty database named `easydb` as user` postgres`):

    createdb -U postgres easydb

&nbsp;

Configuration of the partitions
=============================

By default, the EAS is loaded with 2 [partitions](/sysadmin/eas/partitions/partitions.html), the assets are stored in `/var/opt/easydb/lib/eas/assets/orig ` (Uploaded assets) and `/var/opt/easydb/lib/eas/assets/dest ` (Created versions). This setting can only be used in of the database.

&nbsp;

EAS Worker
==========

The EAS-Worker is used for the asynchronous calculation of the asset versions. This consists of one or more processes using the script `/etc/init.d/easydb-asset-server`.

For an accurate analysis, it can be helpful to the worker only with

    /etc/init.d/easydb-asset-server debug

To make configuration or installation problems easier to see. Then a worker is started in the active window, which can cancelled with `Ctrl + C`.

The current state of worker processes can be seen with

    /etc/init.d/easydb-asset-server status

Among other things, the number of, successful or otherwise, completed jobs.

> The paths refer to paths in the container, not to paths directly on your server that is running the docker container.

&nbsp;

EAS Service
===========

To respond to requests through the easydb or other services exists the so-called EAS service. This accepts tasks synchronously must be edited.

A configuration file is provided, which macros for the Apache-@mod_macro@-Module. This file includes the following package:

    Include /etc/opt/easydb/eas/apache-easydb-asset-server.inc

The macros are for use within a `VirtualHost` definition
intended. Two macros are defined: `EasydbAssetServer` and `EasydbAssetServerAllowedHost`. The former configures the EAS service and can be used with one standard installation of the EAS as in the example. The second macro defines the hosts that access the EAS service allowed. Here the external address of the easydb must be specified, too when the easydb and EAS are running on the same machine.

    <VirtualHost eas.example.org>
        Use EasydbAssetServer /opt/easydb/eas /var/opt/easydb/lib/eas/partitions /var/run/easydb/fcgi-socket
        Use EasydbAssetServerAllowedHost 192.0.2.10
    </VirtualHost>


As of version 4.2 of the EAS, `EasydbAssetServer` still has a third parameter. This determines the socket, via which the Apache web server per FastCGI accesses the EAS service. With this macro, the name of the sockets to the Apache, the EAS receives the configuration via the parameter `EAS_FCGI_SOCKET` in the [Configuration file](/sysadmin/eas/conf/conf.html).

If the access of several hosts is allowed, the configuration must be look something like this:

    <VirtualHost eas.example.org>
        Use EasydbAssetServer /opt/easydb/eas /var/opt/easydb/lib/eas/partitions /var/run/easydb/fcgi-socket
        Use EasydbAssetServerAllowedHost "192.0.2.10 192.0.2.11"
    </VirtualHost>

> The paths refer to paths in the container, not to paths directly on your server that is running the docker container.

Set up the EAS service for different virtual hosts
------------------------------------------------------------

> HTTPS is set up outside of docker and not by the method described here. The following example will only illustrate the requirements of the EAS in particular constellations.

You want the EAS service to be available across multiple virtual hosts usually several VirtualHost sections in Apache configuration
used.

From **version 4.2.40** this is without problems with the macro `EasydbAssetServerExt` is possible. In addition to `EasydbAssetServer` a unique identifier is selected for each VirtualHost entry
(The 2nd parameter):

~~~~
<VirtualHost eas.example.org:80>
    Use EasydbAssetServerExt /opt/easydb/eas "default" /var/opt/easydb/lib/eas/partitions /var/run/easydb/fcgi-socket
    Use EasydbAssetServerAllowedHost 192.0.2.10
</VirtualHost>

<VirtualHost eas.example.org:443>
    Use EasydbAssetServerExt /opt/easydb/eas "ssl" /var/opt/easydb/lib/eas/partitions /var/run/easydb/fcgi-socket
    Use EasydbAssetServerAllowedHost 192.0.2.10
</VirtualHost>
~~~~

The other settings necessary for SSL were stored in the VirtualHost examples omitted for clarity. Of course, is still a combination of the easydb and the EAS in a VirtualHost entry.

Before **Version 4.2.40** (You have a newer version) was only circumstantially realizable, because of the first parameter of the `EasydbAssetServer` macro (the path to the EAS) for each VirtualHost entry must be unique. In this case, file system, a symbolic link to `/opt/easydb/eas` can be created (e.g., `eas-ssl`) and the first parameter for `EasydbAssetServer` would then be `/opt/easydb/eas-ssl`.

This example can also be found in the following directory:

    /etc/opt/easydb/eas/apache-easydb-asset-server-virtual-host.inc.example

> The paths refer to paths in the container, not to paths directly on your server that is running the docker container.

&nbsp;

Free software
==============

Many tasks of the EAS are carried out with source-open free software, especially with ImageMagick (image processing), MPlayer/FFmpeg (video recognition and conversion), OpenOffice.org (Office Conversion), the PostgreSQL database server, and the Apache Web server.