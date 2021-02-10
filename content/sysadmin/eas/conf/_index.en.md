---
title: "32 - Configurations Data"
menu:
  main:
    name: "Configurations Data"
    identifier: "sysadmin/eas/conf"
    parent: "sysadmin/eas"
---

Configuration Variables
=======================

> Paths on this page refer to paths inside of the container easydb-eas, unless stated otherwise.
> For configuration outside of the container, see [here](/en/sysadmin/configuration/eas).

The configuration file of the easydb asset server is `/etc/opt/easydb/eas/easydb-asset-server.conf`.

Settings for the start and the environment of the EAS are in [/etc/default/easydb-asset-server](../initconf).

System Settings
===================

Number of workers
-----------------

### EAS\_NUM\_WORKERS

The EAS can simultaneously start several so-called worker processes to better use the resources available. For that, keep the number of workers smaller than the number of processor cores in the system. We recommend to leave some for the other processes of EAS and easydb.

Worker processes are for the actual calculation of the preview versions and other potentially time - intensive work like to create ZIP archives and PowerPoint presentations.

    EAS_NUM_WORKERS=1

The variable "EAS\_NUM\_SOFFICE" (below) must always be set to a higher value value than EAS\_NUM\_WORKERS.

Number of EAS service processes (as of version 4.2)
------------------------------------------------

### EAS_NUM_SERVICES

The service processes accept requests from the easydb and answers these either directly or creates work assignments for the worker processes in the queue. There should always be sufficient service processes available, since otherwise the interaction with which easydb is blocked. For many installation is the default value of 5 is sufficient, especially since connections are only rejected, if the number of simultaneous connections reaches the limit of `3 × EAS_NUM_SERVICES + 10`.

    EAS_NUM_SERVICES=5

FastCGI socket for EAS service (from version 4.2)
-----------------------------------------------

### EAS_FCGI_SOCKET

    EAS_FCGI_SOCKET=/var/run/EasyDB/fcgi-socket

Number of OpenOffice.org services (as of version 4.2)
---------------------------------------------------

### EAS_NUM_SOFFICE

    EAS_NUM_SOFFICE=2

Baseport for OpenOffice.org Services (from version 4.2)
------------------------------------------------------

### EAS_SOFFICE_BASEPORT

    EAS_SOFFICE_BASEPORT=2002

user configuration
---------------------

### EAS_EUID

### EAS_EGID

The EAS worker porcesses change their user and group when starting to fulfill their tasks. Currently, the same user as the Apache web server's is used.
In Debian, the user is using `www-data` and the group is `www-data`, UID and GID are` 33`.

    EAS_EUID=33
    EAS_EGID=33

Database Configuration
=======================

### EAS\_PG\_DSN

The DSN (Data Source Name) determines the connection to the PostgreSQL database. The following values are possible (blank separated):

- `host`: hostname of the database server or local
    Socket directory
- `port`: Port of the DB server, also necessary for socket connection
- `user`: user name
- `dbname`: Name of the database
- `password`: (optional) Password with appropriate configuration of the
    DB server

<!-- -->

    EAS_PG_DSN=host=/var/run/postgresql port=5432 user=postgres dbname=easydb

directory settings
========================

Restrictions of source directories
--------------------------------------

### EAS\_SAFE\_PATHS

Here, you can restrict from which directories the EAS is allowed to access assets. For safety reasons this list should be as restrictive as possible, but must include the upload directory of the easydb (a PHP setting for easydb 4).

    EAS_SAFE_PATHS=/var/home:/tmp

Log directory
---------------------

### EAS\_LOG\_DIR

All messages from the EAS are stored in this directory.
Very early warning messages and errors can also be in `/tmp`.

    EAS_LOG_DIR=/var/opt/EasyDB/log/eas

Runtime data directory
-----------------------------

### EAS\_VAR\_DIR

In this directory, the EAS worker places status information and `PID` files.

    EAS_VAR_DIR=/var/run/EasyDB

Directory for temporary files
---------------------------------
### EAS\_TMP\_DIR

Below this directory, temporary files are stored as required by the creation of image versions. The default is `/tmp`. A directory is created for each task and deleted after completion.

    EAS_TMP_DIR=/tmp

Directory for temporary files of the zoomer (as of EAS 4.2.36)
-------------------------------------------------------------

### EAS\_ZOOMER\_TMP\_DIR

The easydb zoomer temporarily stores uncompressed images for quick access. This is usually done in a directory named "zoomer" in the temporary directory ("/tmp" or `EAS_TMP_DIR`). This zoomer-directory is automatically cleared by the [Janitor](#Janitor), so it should be used exclusively for this purpose.

    EAS_ZOOMER_TMP_DIR=/var/tmp/zoomer-eas

Base directory for partitions
--------------------------------

### EAS\_PARTITION\_BASE\_DIR

This directory contains symbolic links to the actual EAS partition directories. The links are determined by the database ID of the partition and managed by the EAS worker. A common directory is necessary to limit the configuration effort since the Apache must deliver the files in the individual partitions and they are not individually known to the web server.

    EAS_PARTITION_BASE_DIR=/var/opt/EasyDB/lib/eas/partitions

Minimum size for partitions
----------------------------

### EAS\_PARTITION\_MIN\_FREE {##eas-partition-min-free}

If the EAS determines that this minimum storage in bytes on an EAS partition is not available, the partition is deactivated. Then, no new data ist stored there but it is still read from. The default value is 1 gigabyte.

    EAS_PARTITION_MIN_FREE=1073741824

Code Directory
----------------

### EAS\_EXEC\_DIR

The code from this directory is running. Normally this setting should not be changed.

    EAS_EXEC_DIR=/opt/easydb/eas

Automatic EAS migration
==========================

### EAS\_MIGRATE\_ASSETS

### EAS\_ORIGINAL\_STORE

### EAS\_VERSIONS\_STORE

The EAS can migrate assets of the old, file-based type during access to the database. This allows a gradual conversion to the new system. By default, however, this behavior is disabled, since many requests for non-existent assets may result in performance degradation.

    EAS_MIGRATE_ASSETS= 1
    EAS_ORIGINAL_STORE=/home/eas40/orig
    EAS_VERSIONS_STORE=/home/eas40/dest


E-mail configuration
====================

### EAS\_EMAIL\_SMTP\_SERVER

### EAS\_EMAIL\_FROM\_ADDRESS

### EAS\_EMAIL\_ENVELOPE\_SENDER

A working SMTP server is necessary for the e-mail transmission of assets. Currently, the server name and the `From:` address of the outgoing emails can be configured.

    EAS_EMAIL_SMTP_SERVER=localhost
    EAS_EMAIL_FROM_ADDRESS=root@localhost

In addition, the envelope sender address can also be specified, with at least **EAS 4.2.30**. If this is not set, `EAS_EMAIL_FROM_ADDRESS` is used.

    EAS_EMAIL_ENVELOPE_SENDER=admin@example.com

Zoomer configuration (from EAS 4.2.36)
====================================

The EAS includes a new implementation for the zoomer from **version 4.2.36**.

Janitor settings of the zoomer
---------------------------------

### EAS\_ZOOMER\_MAX\_CACHE\_TIME

### EAS\_ZOOMER\_MIN\_FREE\_SPACE

The EAS-Janitor periodically clears the temporary files of the zoomer (See also `EAS_ZOOMER_TMP_DIR`). Some parameters can be applied to the resources:

The maximum age of temporary files, the default is one hour.

    EAS_ZOOMER_MAX_CACHE_TIME=2D

The following suffixes for time units can be used:
(Seconds), m (minutes), h (hours), D (days).

In addition, the oldest temporary files are deleted until the available space on the drive again reaches a certain value, if necessary. The default is one Gigabyte.

    EAS_ZOOMER_MIN_FREE_SPACE=24G

Available suffixes are K, M, G, T for the corresponding multipliers for bytes (1K stands for 1024 bytes).

Since the Janitor runs only every 60 minutes, it can still miss the violation of the limit several minutes.
The storage limit should therefore be generously dimensioned.

Other parameters
=================

### EAS\_JANITOR

The cleanup process of the EAS can be disabled. By default it is active.

    EAS_JANITOR=false

### EAS\_JSON\_INDENT

The data exchange format of the EAS is mainly JSON (JavaScript Object Notation). If this option is active (the default), the data will be formatted into a more readable shape.

    EAS_JSON_INDENT=1

### EAS\_EXIFTOOL\_PATH

Exiftool is a central component for metadata treatment. Because the distribution version of this software is too old, The easydb provides a newer version whose path is configured here. Normally this setting should not be changed. 

    EAS_EXIFTOOL_PATH=/opt/easydb/common/exiftool/exiftool 

### EAS\_CONVERT\_LIMIT\_\*

 For ImageMagick calls, various restrictions can be specified with `EAS_CONVERT_LIMIT_ *` (see [ImageMagick-Documentation about limits](http://www.imagemagick.org/script/command-line-options.php#limit)),

Examples:

    EAS_CONVERT_LIMIT_THREAD=1 
    EAS_CONVERT_LIMIT_MAP=512MB

### EAS\_SOFFICE\_MAX\_WAIT

(from EAS 4.2.48.7) Maximum wait time for office processes in seconds. The default is 30 minutes. When this time has elapsed, all office processes are aborted and restarted. 

    EAS_SOFFICE_MAX_WAIT=900 

&nbsp;

> The mentioned paths on this page refer to paths inside the easydb-eas container, so not to paths directly on your server that is running the docker container.
