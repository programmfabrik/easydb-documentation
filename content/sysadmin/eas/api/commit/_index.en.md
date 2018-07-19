---
title: "16 - /commit"
menu:
  main:
    name: "/commit"
    identifier: "sysadmin/eas/api/commit"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /commit

##  Example

~~~
 http://eas.example.com/eas/commit/123?instance=example&custom={"producer": "admin"}
~~~


##  Parameter


|key|value|
|---|---|
|`instance`          |Name of the Instance|
|`custom`            |JSON-Object with Name-Value Option (Is stored and delivered but not evaluated or modified)|
|`keep_temporary`    |`1`: Continue to be considered "temporary"|
|`unlogged`          |`1`: Don't add entry to file-based recovery log. This speeds up the request when I/O load is high, but loses the information supplied to `/commit` when the database is lost. This functionality is not required for normal usage and backup/restore. |
 

