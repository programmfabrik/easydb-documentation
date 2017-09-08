# Solution base

For this solution "base", the following customization must be made so that the service can start the easydb-server.

In the central configuration file `easydb5-master.yml`, whose folder has been set during the [installation](../../sysadmin/installation/installation.md#data)

~~~~~
easydb-server:
  [...]
  extension:
    external-user-schema: true
    
~~~~~


The last line must be completed; The others were given to demonstrate the correct indentation.

Also, the example shows the correct parent entry `extension`. If it is missing in your file, it must also be added now.