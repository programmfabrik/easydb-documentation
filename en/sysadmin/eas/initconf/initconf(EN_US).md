Configuration variables for init script
=======================================

The configuration file for the init script, which start parameter and
Environment settings is located in
/ Etc/default/EasyDB-asset-server.

EAS\_CONFIG\_FILE
-----------------

Should only be set if a configuration file differs from
/etc/opt/easydb/eas/easydb-asset-server.conf should be used. in the
Normal case not necessary.

EAS\_EXEC\_DIR
--------------

Changes the code directory of the EAS. The default is/opt/easydb/eas,
Which is correct for all package installations.

EAS\_USER
---------

If the EAS is to run as a "www-data" under a different system user,
This variable must be set. In the EAS configuration,
[EAS\_EUID](../conf#eas_euid) correspondingly.

EAS\_GROUP
----------

Similar to EAS \ _USER, the group can also be changed. Specification
Also here "www-data". Correspondingly, [EAS\_EGID](../conf#eas_euid)
adapt.

EAS\_ULIMIT\_MAX\_OPEN\_FDS
---------------------------

This variable specifies the maximum number of open files and
Network connections for the EAS and all programs launched by the EAS
fixed. Default is 8192, which is also for a larger installation
Should be sufficient.

START
-----

Specifies whether the EAS should be started. Only if the variable is the
Value 1 (default), the EAS is started. It is only in
Exceptional cases, it is necessary to change the value.

&nbsp;

> The paths refer to paths in the container, not to paths directly on your server that is running the docker container.