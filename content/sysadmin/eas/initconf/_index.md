---
title: "37 - Konfiguration beim Programmstart"
menu:
  main:
    name: "Konfiguration beim Programmstart"
    identifier: "sysadmin/eas/initconf"
    parent: "sysadmin/eas"
---
Konfigurationsvariablen für Init-Skript
=======================================

Die Konfigurationsdatei für das Init-Skript, welches Start-Parameter und
Umgebungseinstellungen enthält, liegt in
/etc/default/easydb-asset-server.

EAS\_CONFIG\_FILE
-----------------

Sollte nur gesetzt werden, wenn eine Konfigurationsdatei abweichend von
/etc/opt/easydb/eas/easydb-asset-server.conf benutzt werden soll. Im
Normalfall nicht notwendig.

EAS\_EXEC\_DIR
--------------

Ändert das Code-Verzeichnis des EAS. Die Vorgabe ist /opt/easydb/eas,
welche für alle Paketinstallationen korrekt ist.

EAS\_USER
---------

Soll der EAS unter einem anderen Systemnutzer als “www-data” laufen,
muss diese Variable gesetzt werden. In der EAS-Konfiguration sollte
[EAS\_EUID](../conf) entsprechend korrespondieren.

EAS\_GROUP
----------

Analog zu EAS\_USER kann auch die Gruppe geändert werden. Vorgabe ist
auch hier “www-data”. Entsprechend ist [EAS\_EGID](../conf)
anzupassen.

EAS\_ULIMIT\_MAX\_OPEN\_FDS
---------------------------

Diese Variable legt die maximale Anzahl der geöffneten Dateien und
Netzwerkverbindungen für den EAS und alle vom EAS gestarteten Programme
fest. Voreingestellt ist 8192, was auch für eine größere Installation
reichen sollte.

START
-----

Legt fest, ob der EAS gestartet werden soll. Nur wenn die Variable den
Wert 1 hat (Voreinstellung), wird der EAS gestartet. Es ist nur in
Ausnahmefällen notwendig, den Wert zu ändern.

&nbsp;

> Die Pfadangaben beziehen sich auf Pfade im Container, nicht auf Pfade direkt auf Ihrem Server, der den docker-Container ausführt.
