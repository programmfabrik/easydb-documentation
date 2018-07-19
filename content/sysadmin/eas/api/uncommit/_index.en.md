---
title: "27 - /uncommit"
menu:
  main:
    name: "/uncommit"
    identifier: "sysadmin/eas/api/uncommit"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /uncommit

With the `uncommit`-Request you signal to the EAS that an asset is no longer used by the application. The EAS is then free to delete the complete asset tree after the expired `expires` time specified at "put":../put.

##  Example

~~~
 http://eas.example.com/eas/?instance=example
http://eas.example.com/eas/?instance=example
~~~


##  Parameter


|key|value|
|---|---|
|`instance`          |Name of the Instance|


 

