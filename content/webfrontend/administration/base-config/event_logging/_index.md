---
title: "206 - Events loggen"
menu:
  main:
    name: "Events loggen"
    identifier: "webfrontend/administration/base-config/event_logging"
    parent: "webfrontend/administration/base-config"
---
# Events loggen

Wählen Sie aus, welche Events geloggt werden sollen, und ob diese Events personenbezogene Daten speichern dürfen.

## Benutzer-Aktivität loggen

<!-- These are general events and event groups that log user activity. If a event group is not enabled, none of the events is logged, even if the event is activated (see below).
 -->

Die folgenden Events und Eventgruppen loggen Benutzer-Aktivitäten. Falls eine Eventgruppe nicht aktiviert ist, wird keines der Events geloggt, selbst wenn das einzelne Event aktiviert ist (s.u.).

|Einstellung | Erläuterung | Eventtypen |
|---|---|---|
| Webfrontend-Probleme loggen. | Protokolliert die Fehler, die bei der Verwendung der Benutzeroberfläche auftreten. | `FRONTEND_ERROR` |
| Loggen, wenn ein Benutzer eine Datei aus einem Export herunterlädt. | Protokolliert das Herunterladen eines Assets aus einem Export durch einen Benutzer. | `ASSET_DOWNLOAD`, `ASSET_EXPORT_DOWNLOAD`, `ASSET_EXPORT_TRANSPORT_DOWNLOAD`, `ASSET_EXPORT_TRANSPORT_COPY`, `ASSET_EXPORT_TRANSPORT_COPY_SCHEDULED` |
| Loggen, wenn ein Benutzer eine Datei hochlädt. | Protokolliert das Hochladen eines Assets durch einen Benutzer. | `UPLOAD_ASSET` |
| Suchanfragen loggen. | Protokolliert die Suchanfragen der Benutzer. | `SEARCH` |
| Loggen, wenn ein Benutzer einen Export herunterlädt. | Protokolliert das Herunterladen eines Exports durch einen Benutzer. | `DOWNLOAD_EXPORT` |
| Detailansicht loggen. | Protokolliert die Aufrufe einer Detailansicht. | `DETAIL_VIEW` |
| Login / Logout loggen. | Protokolliert Login- und Logout-Events eines Benutzers. | `USER_LOGIN`, `USER_LOGOUT` |

## Loggen von spezifischen Events, Einstellungen für das Speichern personenbezogener Daten

<!--
For any of the following event types you can set if it will be logged (**Activated**), and if it is logged, if user specific data is included in the event details (**Save User Data**).

An event is not logged if it is part of any of the user activity groups (see above) and the group is not enabled.

If saving of user data is disabled for an event, the Session ID and the user ID is removed from the event before it is saved, as well as specific user data from the optional JSON object with additional information (see below). -->

Für alle folgendenn Eventtypen können Sie einstellen, ob die Events geloggt werden sollen (**Aktiviert**), und falls sie aktiviert sind, ob in den Eventdetails personenbezogene Daten gespeichert werden dürfen (**Personenbezogene Information speichern**).

Ein Event wird nicht geloggt, falls es in einer der Gruppen für Benutzer-Aktivitäten enthalten ist, und die Gruppe nicht aktiviert ist.

Falls das Speichern von personenbezogenen Daten deaktiviert ist, werden vor dem Speichern des Events die Benutzer-ID und die Session-ID entfernt, um das Event zu anonymisieren. Zudem werden bestimmte Inhalte aus dem optionalen JSON-Objekt mit Zusatzinformationen entfernt.

### Log API calls

Eventtyp: `API_CALL`

| Einstellung | Erläuterung |
|---|---|
| aktiv | Hier wird festgelegt ob und welche Logs in easydb gemacht werden. Optionen: "keine", "nur Scheiboperationen", "alle" |
| folgende Calls loggen	| Durch Aktivieren der Checkboxen werden die Calls definiert, die geloggt werden sollen. |
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

> HINWEIS: Nähere Informationen zu den einzelnen Logs sind in der [Technischen Dokumentation](https://docs.easydb.de/en/technical/api) unterhalb des Kapitels API zu finden.


### Aktualisierung Basis-Konfiguration

Eventtyp: `BASE_CONFIG_UPDATE`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Aufruf Detailansicht

Eventtyp: `DETAIL_VIEW`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Connector Asset Download

Eventtyp: `ASSET_CONNECTOR_DOWNLOAD`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

Personenbezogene Daten, die aus den Zusatzinformationen entfernt werden:

- `user_id`
- `user_displayname`
- `user_email`

### Connector Login

Eventtyp: `CONNECTOR_LOGIN`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

Personenbezogene Daten, die aus den Zusatzinformationen entfernt werden:

- `connector_user_id`
- `connector_user_displayname`

### Connector Logout

Eventtyp: `CONNECTOR_LOGOUT`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

Personenbezogene Daten, die aus den Zusatzinformationen entfernt werden:

- `user_id`
- `user_displayname`
- `user_email`

### Datei-Download

Eventtyp: `ASSET_DOWNLOAD`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Datei-Download über Export

Eventtyp: `ASSET_EXPORT_DOWNLOAD`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Datei-Kopie über Transport

Eventtyp: `ASSET_EXPORT_TRANSPORT_COPY`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Datei-Kopie über Transport mit Zeitplan

Eventtyp: `ASSET_EXPORT_TRANSPORT_COPY_SCHEDULED`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Dateiexport

Eventtyp: `EXPORT_ASSET`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Dateiinformationen aus Export

Eventtyp: `EXPORT_OBJECT`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Datenmodell-Aktualisierung

Eventtyp: `SCHEMA_COMMIT`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Datensatz aktualisiert

Eventtyp: `OBJECT_UPDATE`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Datensatz angelegt

Eventtyp: `OBJECT_INSERT`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Datensatz gelöscht

Eventtyp: `OBJECT_DELETE`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Datensatz indiziert

Eventtyp: `OBJECT_INDEX`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Download eines Exports

Eventtyp: `DOWNLOAD_EXPORT`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Download über Transport

Eventtyp: `ASSET_EXPORT_TRANSPORT_DOWNLOAD`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Drupal Dateikopie

Eventtyp: `DRUPAL_FILE_COPY`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Drupal Dateikopie: Fehler

Eventtyp: `DRUPAL_FILE_COPY_ERROR`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### E-Mail-Versand

Eventtyp: `EMAIL_SENT`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

Personenbezogene Daten, die aus den Zusatzinformationen entfernt werden:

- `recipients`
- `subject`
- `message`

### Export abgeschlossen

Eventtyp: `EXPORT_FINISH`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Export aktualisiert

Eventtyp: `EXPORT_UPDATE`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Export angehalten

Eventtyp: `EXPORT_STOPPED`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Export angelegt

Eventtyp: `EXPORT_INSERT`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Export fehlgeschlagen

Eventtyp: `EXPORT_FAILED`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Export gestartet

Eventtyp: `EXPORT_START`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Falcon.io Dateikopie

Eventtyp: `FALCONIO_FILE_COPY`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Falcon.io Dateikopie: Fehler

Eventtyp: `FALCONIO_FILE_COPY_ERROR`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Fortschrittsinformation

Eventtyp: `API_PROGRESS`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Frontend-Fehler

Eventtyp: `FRONTEND_ERROR`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Login fehlgeschlagen

Eventtyp: `LOGIN_FAILED`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

Personenbezogene Daten, die aus den Zusatzinformationen entfernt werden:

- `login`

### Mitteilung akzeptiert

Eventtyp: `USER_ACCEPTED_MESSAGE`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Neuer Nutzer angelegt

Eventtyp: `USER_CREATED`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Nutzer-Login

Eventtyp: `USER_LOGIN`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

Personenbezogene Daten, die aus den Zusatzinformationen entfernt werden:

- `root_login`

### Nutzer-Logout

Eventtyp: `USER_LOGOUT`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Rechteverletzung bei Arbeitsmappen

Eventtyp: `COLLECTION_OWNER_RIGHTS_ERROR`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Ressource nicht verfügbar

Eventtyp: `RESOURCE_NOT_AVAILABLE`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Server-Start

Eventtyp: `SERVER_START`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Server-Stop

Eventtyp: `SERVER_SHUTDOWN`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Session ungültig

Eventtyp: `SESSION_INVALID`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Suche

Eventtyp: `SEARCH`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Suggest Index fertig erstellt

Eventtyp: `SUGGEST_INDEX_DONE`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Suggest Index Fortschritt

Eventtyp: `SUGGEST_INDEX_PROGRESS`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Suggest Index konnte nicht erstellt werden

Eventtyp: `SUGGEST_INDEX_FAILED`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Suggest Index wird neu erstellt

Eventtyp: `SUGGEST_INDEX_START`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### TYPO3 Dateikopie

Eventtyp: `TYPO3_FILE_COPY`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### TYPO3 Dateikopie: Fehler

Eventtyp: `TYPO3_FILE_COPY_ERROR`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |

### Wordpress Synchronisation

Eventtyp: `WORDPRESS_SYNC`

| Einstellung | Erläuterung |
|---|---|
| Aktiviert | Events dieses Types loggen (Standard: `true`) |
| Personenbezogene Information speichern | Benutzerdaten in den Eventdetails speichern (Standard: `true`) |
