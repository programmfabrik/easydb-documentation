---
title: "17 - /commit"
menu:
  main:
    name: "/commit"
    identifier: "sysadmin/eas/api/commit"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /commit

##  Beispiel

```url
http://eas.example.com/eas/commit/123?instance=example&custom={"producer": "admin"}
```


##  Parameter


|key|value|
|---|---|
|`instance`          |Name der Instanz|
|`custom`            |JSON-Objekt mit Name-Wert-Optionen (wird gespeichert und ausgeliefert, aber nicht ausgewertet oder verändert)|
|`keep_temporary`    |`1`: weiterhin als "temporär" betrachten|
|`unlogged`          |`1`: keinen Eintrag in das dateibasierte Wiederherstellungs-Log schreiben. Unter I/O-Last beschleunigt das den Zugriff auf `/commit`. Für den normalen Betrieb und auch die Wiederherstellung bei existierendem Datenbank-Backup ist dieses Log nicht notwendig, andernfalls können die an `/commit` übergebenen Custom-Informationen verloren gehen. |


