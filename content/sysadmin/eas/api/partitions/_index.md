---
title: "20 - /partitions"
menu:
  main:
    name: "/partitions"
    identifier: "sysadmin/eas/api/partitions"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /partitions

Mit dem `partitions`-Request können Dateien aus dem EAS abgerufen werden. Dazu muss neben der Asset-ID der SHA1-Hash der Datei bekannt sein.

##  Beispiel

```url
http://eas.example.com/eas/partitions/1/0/0/123/4e1243bd22c66e76c2ba9eddc1f91394e57f9f83/image/jpg
http://eas.example.com/eas/partitions/1/0/0/123/4e1243bd22c66e76c2ba9eddc1f91394e57f9f83/image/jpg/sameFileButOtherName.jpg
```


##  Struktur

Die Pfad-Teile nach `partitions` sind wie folgt aufgebaut:

* Partitions-ID (siehe auch "Partitionen":../../partitions)
* Millionen-Block (Asset-ID durch 1.000.000 mal 1.000.000)
* Tausender-Block (Asset-Id durch 1.000 mal 1.000)
* Asset-ID
* SHA1-Hash
* MIME-Typ (incl. Slash, also z.B. image/jpg)
* Download-Dateiname (optional)

##  Parameter

Dieser Request wird direkt vom Apache-Webserver verarbeitet und benötigt keine GET-Parameter.
