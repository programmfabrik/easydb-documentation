---
title: "206 - Events"
menu:
  main:
    name: "Events"
    identifier: "webfrontend/administration/base-config/event_logging"
    parent: "webfrontend/administration/base-config"
---
# Events

Wählen Sie aus, welche Events geloggt werden sollen, und ob diese Events personenbezogene Daten speichern dürfen.

## Benutzer-Aktivität loggen

Die folgenden Events und Eventgruppen loggen Benutzer-Aktivitäten. Falls eine Eventgruppe nicht aktiviert ist, wird keines der Events geloggt, selbst wenn das einzelne Event aktiviert ist (s.u.).

|Einstellung | Erläuterung | Eventtypen |
|---|---|---|
| Suchanfragen loggen | Protokolliert die Suchanfragen der Benutzer. | `SEARCH` |
| Detailansicht loggen | Protokolliert die Aufrufe einer Detailansicht. | `DETAIL_VIEW` |
| Loggen, wenn ein Benutzer eine Datei hochlädt | Protokolliert das Hochladen eines Assets durch einen Benutzer. | `UPLOAD_ASSET` |
| Export-Events loggen | Protokolliert das Anlegen, Starten, Ändern oder den Abschluss eines Exports. | `EXPORT_ASSET`, `EXPORT_FINISH`, `EXPORT_INSERT`, `EXPORT_OBJECT`, `EXPORT_START`, `EXPORT_STOPPED`, `EXPORT_UPDATE` |
| Loggen, wenn ein Benutzer einen Export herunterlädt | Protokolliert das Herunterladen eines Exports durch einen Benutzer. | `DOWNLOAD_EXPORT` |
| Loggen, wenn ein Benutzer eine Datei herunterlädt | Protokolliert das Herunterladen eines Assets aus einem Export durch einen Benutzer. | `ASSET_DOWNLOAD`, `ASSET_EXPORT_DOWNLOAD`, `ASSET_EXPORT_TRANSPORT_DOWNLOAD`, `ASSET_EXPORT_TRANSPORT_COPY`, `ASSET_EXPORT_TRANSPORT_COPY_SCHEDULED` |
| Login / Logout loggen | Protokolliert Login- und Logout-Events eines Benutzers. | `USER_LOGIN`, `USER_LOGOUT` |
| Webfrontend-Probleme loggen | Protokolliert die Fehler, die bei der Verwendung der Benutzeroberfläche auftreten. | `FRONTEND_ERROR` |

## Persönliche Daten loggen

Für alle folgenden Eventtypen können Sie einstellen, ob in den Eventdetails personenbezogene Daten gespeichert werden dürfen (**Personenbezogene Daten loggen**).

Ein Event wird nicht geloggt, falls es in einer der Gruppen für Benutzer-Aktivitäten enthalten ist, und die Gruppe nicht aktiviert ist.

Falls das Speichern von personenbezogenen Daten deaktiviert ist, werden vor dem Speichern des Events die Benutzer-ID und die Session-ID entfernt, um das Event zu anonymisieren. Zudem werden bestimmte Inhalte aus dem optionalen JSON-Objekt mit Zusatzinformationen entfernt.

### Events beim Suchen

(De-)aktivieren Sie für die Events `SEARCH` und `DETAIL_VIEW`, ob diese personenbezogene Daten speichern dürfen.

### Export- und Download-Events

(De-)aktivieren Sie für die Gruppe der folgenden Events, ob diese personenbezogene Daten speichern dürfen:

* `EXPORT_OBJECT`
* `EXPORT_ASSET`
* `EXPORT_STOPPED`
* `EXPORT_FINISH`
* `EXPORT_START`
* `EXPORT_INSERT`
* `EXPORT_UPDATE`
* `ASSET_EXPORT_DOWNLOAD`
* `ASSET_EXPORT_TRANSPORT_DOWNLOAD`
* `ASSET_DOWNLOAD`
* `ASSET_EXPORT_TRANSPORT_COPY`
* `ASSET_EXPORT_TRANSPORT_COPY_SCHEDULED`
* `DOWNLOAD_EXPORT`

## API-Call

Eventtyp: `API_CALL`

| Einstellung | Erläuterung |
|---|---|
| aktiv | Hier wird festgelegt ob und welche Logs in easydb gemacht werden. Optionen: "keine", "nur Scheiboperationen", "alle" |
| folgende Calls loggen	| Durch Aktivieren der Checkboxen werden die Calls definiert, die geloggt werden sollen. |

> **Hinweise:**
>
> - Nähere Informationen zu den einzelnen Logs sind in der [Technischen Dokumentation](https://docs.easydb.de/en/technical/api) unterhalb des Kapitels API zu finden.
