---
title: "28 - /uncommit"
menu:
  main:
    name: "/uncommit"
    identifier: "sysadmin/eas/api/uncommit"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /uncommit

Mit dem `uncommit`-Request signalisiert man dem EAS, dass ein Asset nicht mehr von der Anwendung benutzt wird. Dem EAS steht es dann frei, nach Ablauf der bei "put":../put angegebenen `expires`-Zeit den kompletten Asset-Baum zu löschen.

##  Beispiel

~~~
 http://eas.example.com/eas/?instance=example
http://eas.example.com/eas/?instance=example
~~~


##  Parameter


|key|value|
|---|---|
|`instance`          |Name der Instanz|




