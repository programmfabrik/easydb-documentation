---
title: "29 - /updatecustom"
menu:
  main:
    name: "/updatecustom"
    identifier: "sysadmin/eas/api/updatecustom"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /updatecustom

Custom-Daten sind Name-Wert-Optionen, die vom EAS für jedes Asset gespeichert werden. Diese werden vom EAS nicht verwendet. Mit dem `updatecustom`-Request können diese unabhängig von anderen Operationen gesetzt werden.

Diese Daten müssen immer komplett aktualisiert werden, das Setzen von einzelnen Werten innerhalb der Struktur ist nicht möglich.

##  Beispiel

```url
http://eas.example.com/eas/updatecustom/123?instance=example&custom={"foo": "bar"}
```


##  Parameter


|key|value|
|---|---|
|`instance`          |Name der Instanz|
|`custom`            |JSON-Objekt mit Custom-Daten|




