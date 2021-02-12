---
title: "206 - Ereignisse"
menu:
  main:
    name: "Ereignisse"
    identifier: "webfrontend/administration/base-config/event_logging"
    parent: "webfrontend/administration/base-config"
---
# Ereignisse

Wählen Sie aus, welche Ereignisse geloggt werden sollen, und ob diese Ereignisse personenbezogene Daten speichern dürfen.

## Benutzer-Aktivität loggen

Die folgenden Ereignisse und Ereignisgruppen loggen Benutzer-Aktivitäten. Falls eine Ereignisgruppe nicht aktiviert ist, wird keines der Ereignisse geloggt, selbst wenn das einzelne Ereignis aktiviert ist (s.u.).

|Einstellung | Erläuterung | Ereignistypen |
|---|---|---|
| Suchanfragen loggen | Protokolliert die Suchanfragen der Benutzer. | `SEARCH` |
| Detailansicht loggen | Protokolliert die Aufrufe einer Detailansicht. | `DETAIL_VIEW` |
| Loggen, wenn ein Benutzer eine Datei hochlädt | Protokolliert das Hochladen eines Assets durch einen Benutzer. | `UPLOAD_ASSET` |
| Export-Ereignisse loggen | Protokolliert das Anlegen, Starten, Ändern oder den Abschluss eines Exports. | `EXPORT_ASSET`, `EXPORT_FINISH`, `EXPORT_INSERT`, `EXPORT_OBJECT`, `EXPORT_START`, `EXPORT_STOPPED`, `EXPORT_UPDATE` |
| Loggen, wenn ein Benutzer einen Export herunterlädt | Protokolliert das Herunterladen eines Exports durch einen Benutzer. | `DOWNLOAD_EXPORT` |
| Loggen, wenn ein Benutzer eine Datei herunterlädt | Protokolliert das Herunterladen eines Assets aus einem Export durch einen Benutzer. | `ASSET_DOWNLOAD`, `ASSET_EXPORT_DOWNLOAD`, `ASSET_EXPORT_TRANSPORT_DOWNLOAD`, `ASSET_EXPORT_TRANSPORT_COPY`, `ASSET_EXPORT_TRANSPORT_COPY_SCHEDULED` |
| Login / Logout loggen | Protokolliert Login- und Logout-Ereignis eines Benutzers. | `USER_LOGIN`, `USER_LOGOUT` |
| Webfrontend-Probleme loggen | Protokolliert die Fehler, die bei der Verwendung der Benutzeroberfläche auftreten. | `FRONTEND_ERROR` |

## Persönliche Daten loggen

Für alle folgenden Ereignistypen können Sie einstellen, ob in den Ereignisdetails personenbezogene Daten gespeichert werden dürfen (**Personenbezogene Daten loggen**).

Ein Ereignis wird nicht geloggt, falls es in einer der Gruppen für Benutzer-Aktivitäten enthalten ist, und die Gruppe nicht aktiviert ist.

Falls das Speichern von personenbezogenen Daten deaktiviert ist, werden vor dem Speichern des Ereignisses die Benutzer-ID und die Session-ID entfernt, um das Ereignis zu anonymisieren. Zudem werden bestimmte Inhalte aus dem optionalen JSON-Objekt mit Zusatzinformationen entfernt.

| Einstellung                     | Erläuterung                                                  |
| ------------------------------- | ------------------------------------------------------------ |
| Ereignisse beim Suchen          | (De-)aktivieren Sie für die Ereignisse `SEARCH` und `DETAIL_VIEW`, ob diese personenbezogene Daten speichern dürfen. |
| Export- und Download-Ereignisse | (De-)aktivieren Sie für die Gruppe der Ereignisse `EXPORT_OBJECT`, `EXPORT_ASSET`, `EXPORT_STOPPED`, `EXPORT_FINISH`, `EXPORT_START`, `EXPORT_INSERT`, `EXPORT_UPDATE`, `ASSET_EXPORT_DOWNLOAD`, `ASSET_EXPORT_TRANSPORT_DOWNLOAD`, `ASSET_DOWNLOAD`, `ASSET_EXPORT_TRANSPORT_COPY`, `ASSET_EXPORT_TRANSPORT_COPY_SCHEDULED`, `DOWNLOAD_EXPORT`, ob diese personenbezogene Daten speichern dürfen. |



## Zusätzliche Benutzerdaten in den Ereignissen loggen

Standardmäßig werden in den Ereignissen nur Verknüpfungen zu Benutzern geloggt die die protokollierte Aktion durchgeführt haben. Wird ein Benutzer gelöscht, ist auch in den Ereignissen kein Rückschluss mehr auf den Benutzer möglich. Bei der Archivierung von Benutzern verbleibt der Benutzer im System und ist in den Ereignissen weiterhin sichtbar. Wurden ausgewählte Daten allerdings pseudonymisiert, sind die Originalwerte auch nicht mehr in den Ereignissen zu finden. Damit in den Ereignissen trotz Löschung oder Pseudonymisierung von Benutzern weiterhin Informationen zu den Benutzern erhalten bleiben, können hier ausgewählte Felder aktiviert werden, die als Text in das jeweilige Ereignis kopiert werden und somit auch nach der Löschung oder Pseudonymisierung in den Ereignissen erhalten bleiben.



## API-Call

Ereignistyp: `API_CALL`

| Einstellung | Erläuterung |
|---|---|
| aktiv | Hier wird festgelegt ob und welche Logs in easydb gemacht werden. Optionen: "keine", "nur Schreiboperationen", "alle" |
| folgende Calls loggen	| Durch Aktivieren der Checkboxen werden die Calls definiert, die geloggt werden sollen. |

> **Hinweise:**
>
> - Nähere Informationen zu den einzelnen Logs sind in der [Technischen Dokumentation](https://docs.easydb.de/en/technical/api) unterhalb des Kapitels API zu finden.
