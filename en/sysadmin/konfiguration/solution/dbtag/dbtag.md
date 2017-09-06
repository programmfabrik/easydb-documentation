# Solution-specific documentation dbtag

To configure the base of LDAP searches:

~~~~
solution:
  config:
    auth:
      base_dn: DC=Parlament,DC=bundestag,DC=btg
~~~~


This configuration comes in the central file `easydb-server.yml`, whose location you set in [Installation](/sysadmin/installation/installation.md) .