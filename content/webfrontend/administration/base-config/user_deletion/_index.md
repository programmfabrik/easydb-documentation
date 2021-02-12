---
title: "Löschen & Pseudonymisierung"
menu:
  main:
    name: "Löschen & Pseudonymisierung"
    identifier: "webfrontend/administration/base-config/user_deletion"
    parent: "webfrontend/administration/base-config"
---
# Löschen & Pseudonymisierung

Die easydb unterstützt ein Archivieren und das endgültige Löschen von Benutzern, sowie eine Pseudonymisierung archivierter Benutzer.



## Benutzer-Löschmethode

Wählen Sie hier die Lösch-Methode, die angewendet werden soll, wenn ein Benutzer in der Benutzerverwaltung über das Minus gelöscht wird.

| Option      | Erläuterung                                                  |
| ----------- | ------------------------------------------------------------ |
| Nachfragen  | Klickt ein Administrator auf das Minus um einen Benutzer aus dem System zu löschen, wird bei dieser Option nachgefragt, ob der Benutzer archiviert oder endgültig gelöscht werden soll. |
| Archivieren | Klickt ein Administrator auf das Minus um einen Benutzer aus dem System zu löschen, wird dieser bei dieser Option lediglich archiviert. Er ist aber nicht mehr in der Benutzerverwaltung auffindbar und kann sich nicht mehr anmelden. |
| Löschen     | Klickt ein Administrator auf das Minus um einen Benutzer aus dem System zu löschen, wird dieser bei dieser Option endgültig gelöscht. Die Mappen die dieser Benutzer angelegt hat, werden ebenfalls dauerhaft gelöscht. Datensätze in denen er als "Verantwortlicher" hinterlegt ist, werden dem Systembenutzer "deleted_user" zugeschrieben. Gleiches gilt für die Ereignisse des gelöschten Benutzers. |



## Automatisches Löschen oder Archivieren von Benutzern

Die easydb unterstützt das automatische Archivieren von inaktiven Benutzern und das automatische Löschen von archivierten bzw. anonymen Benutzern. Standardmäßig werden Benutzer weder automatisch archiviert noch gelöscht.

| Option                                  | Erläuterung                                                  |
| --------------------------------------- | ------------------------------------------------------------ |
| Nach n Tagen Inaktivität archivieren    | Benutzer die sich nach n Tagen nicht bei der easydb angemeldet haben, werden archiviert und können sich anschließend nicht mehr am System anmelden. |
| Archivierte Nutzer nach n Tagen löschen | Archivierte Benuzter werden nach n Tagen endgültig gelöscht. |
| Anonyme Nutzer nach n Tagen löschen     | Anonyme Benutzer werden nach n Tagen endgültig gelöscht.     |

