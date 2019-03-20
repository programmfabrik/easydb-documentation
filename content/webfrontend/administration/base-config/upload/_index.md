---
title: "73 - Hochladen"
menu:
  main:
    name: "Hochladen"
    identifier: "webfrontend/administration/base-config/upload"
    parent: "webfrontend/administration/base-config"
---
# Hochladen

In diesem Reiter werden globale Limits für Datei-Uploads definiert.

|Einstellung | | Erläuterung |
|----|---|---|
|Limit beim Hochladen | | Das Globale-Upload Limit in Bytes. Wenn eine Datei größer ist, wird sie in jedem Fall abgelehnt, auch wenn per Rechtemanagement andere Werte eingestellt sind. |
|_Dateityp_ | Alle Typen erlauben| Durch aktivieren der Checkbox werden alle Typen erlaubt, die über _Erweiterung_ für den jeweiligen Datei-Typ einzeln ausgewählt werden können. Für die Datei-Klasse _Sonstige_ werden immer alle Formate erlaubt, die nicht in einem der anderen Datei-Typen aufgelistet sind.|
| | Erweiterung | Es werden nur die Formate für einen Upload akzeptiert, die hier aktiviert sind. Ist *alle Typen erlauben* aktiviert, erübrigt sich die Auswahl in dieser Zeile. |
| |Limit (bytes) | Pro Dateityp kann ein eigenes Limit in bytes definiert werden. Wenn es größer ist, als das globale Upload-Limit ist, wird es ignoriert. |

> HINWEIS: Nähere Informationen zu den Dateitypen sind auch im Kapitel [Dateitypen](../../../../sysadmin/eas/filetypes) im Abschnitt Systemadministration zu finden.



