---
title: "24 - /rput"
menu:
  main:
    name: "/rput"
    identifier: "sysadmin/eas/api/rput"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /rput

Import von Assets durch Angabe einer URL.

##  Beispiel

~~~
 http://eas.example.com/eas/rput?instance=example&url=http%3A%2F%2Fexample.org%2Fimage.jpg
~~~


##  Parameter


|key|value|
|---|---|
|`instance`          |Name der Instanz|
|`url`               |Import-URL|
|`custom`            |JSON-Objekt mit Name-Wert-Optionen (wird gespeichert und ausgeliefert, aber nicht ausgewertet oder verändert)|
|`thumbnailsize`     |wenn gesetzt, wird eine Thumbnail-Version mit dieser Größe erzeugt (z.B. `128x128`)|




