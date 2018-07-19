---
title: "13 - /batch"
menu:
  main:
    name: "/batch"
    identifier: "sysadmin/eas/api/batch"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /batch

##  Beispiel

~~~
 http://eas.example.com/eas/batch?instance=example&batch={"commands":[{"command":"put","args":{"filename":"/tmp/foo.png"}}]}
~~~


##  Parameter


|key|value|
|---|---|
|`instance`          |Name der Instanz|
|`batch`             |Stapelverarbeitungsanweisungen (Dokumentation folgt)|


