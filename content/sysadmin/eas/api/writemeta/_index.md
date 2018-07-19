---
title: "31 - /writemeta"
menu:
  main:
    name: "/writemeta"
    identifier: "sysadmin/eas/api/writemeta"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /writemeta

Gibt eine Version eines Assets mit bestimmten Metadaten zurück.

##  Beispiel

~~~
 http://eas.example.com/eas/writemeta/123/f1d2d2f924e986ac86fdf7b36c94bcdf32beec15?target_metadata=["-title=Test","-date=2012-04-23T12:00:00+02"]&instance=example
~~~


##  Parameter


|key|value|
|---|---|
|`instance`          |Name der Instanz|
|`target_metadata`   |JSON-Liste von Zeilen für Exiftool zum Schreiben von Metadaten (siehe Option `-`` von Exiftool)|



