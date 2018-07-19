---
title: "78 - Ereignisse"
menu:
  main:
    name: "Ereignisse"
    identifier: "webfrontend/administration/events"
    parent: "webfrontend/administration"
---
# Ereignisse

Hier können die Logs in easydb angezeigt und nach Typ und Zeitraum gefilter werden. Das Ereignisprotokoll kann als CSV heruntergeladen und ganz oder selektiv gelöscht werden.

![*Protokollierte Ereignisse*](events.png)

| Event | Bezeichnung im Frontend | Erläuterung |
|---|---|---|
|api_call |API-Call | Wird protokolliert, wenn ein Aufruf in easydb über API gemacht wird. |
|api_progress |Fortschrittsinformation | Ist eine Zustandsinformation bei laufenden Prozessen, z. B. beim Speichern von Datensätzen. |
|asset_download |Datei-Download | Asset wurde aus easydb heruntergeladen. |
|asset_export_download |Datei-Download über Export | Es wurde ein Export durchgeführt und hieraus ein Asset herunterladen. |
|asset_export_transport_copy |Datei-Kopie über Transport | Es wurde ein Transport durchgeführt. Dabei wurde die Kopie eines Assets gesendet. |
|asset_export_transport_copy_scheduled |Datei-Kopie über Transport mit Zeitplan | Es wurde ein Transport mit Zeitplan durchgeführt. Dabei wurde die Kopie eines Assets gesendet. |
|asset_export_transport_download |Download über Transport | Es wurde ein Transport durchgeführt und ein Asset heruntergeladen. |
|base_config_update |Aktualisierung der Basis-Konfiguration | Die Basis-Konfiguration wurde aktualisiert. |
|collection_owner_rights_error |Rechteverletzung bei Arbeitsmappen | Ein Vorgang für Mappen ist fehlgeschlagen, da er nicht konform mit den Rechteeinstellungen war. |
|detail_view |Aufruf Detailansicht | Ein Asset wurde in der Detailansicht aufgerufen |
|download_export |Download eines Exports | Ein Export wurde durchgeführt und heruntergeladen. |
|email_sent |E-Mail-Versand | Eine E-Mail wurde versendet. |
|export_asset |Datei-Export | Eine Asset wurde heruntergeladen. |
|export_failed |Export fehlgeschlagen | Ein Export ist fehlgeschlagen. |
|export_finish |Export abgeschlossen | Ein Export wurde fertig gestellt. |
|export_insert |Export angelegt | Ein Export wurde neu angelegt. |
|export_object |Information für Export | Wird generiert, wenn ein Datensatz exportiert wird. |
|export_start |Export gestartet | Ein Export wurde gestartet. |
|export_stopped |Export angehalten | Ein Export wurde angehalten. |
|export_update |Export aktualisiert | Ein Export wurde aktualisiert. |
|frontend_error |Frontend-Fehler | Es ist ein Frontend-Fehler während eines Vorgang aufgetreten. |
|login_failed |Login fehlgeschlagen | Ein Anmeldeversuch hat fehlgeschlagen. |
|object_deleted |Datensatz gelöscht | Ein Datensatz wurde gelöscht. |
|object_index |Datensatz indiziert | Ein Datensatz wurde indiziert, |
|object_insert |Datensatz angelegt | Ein Datensatz wurde neu angelegt. |
|object_update |Datensatz aktualisiert | Ein Datensatz wurde aktualisiert. |
|resource_not_available |Ressource nicht verfügbar | Ist z. B. der Fall, wenn eine nicht existierende URL aufgerufen wird oder Ressourcen, zu denen die Rechte fehlen. |
|schema_commit |Datenmodell-Aktualisierung | Das Datenmodell wurde aktualisiert. |
|search |Suche | Es wurde eine Anfrage über die Suche gesendet. |
|server_shutdown |Server-Stop | Der Server ist angehalten. |
|server_start |Server-Start | Der Server wurde gestartet. |
|session_invalid |Session ungültig | Es wurde versucht mit einer Session zu arbeiten, die bereits ungültig war. |
|user_accepted_message | Mitteilung akzeptiert | Wird generiert, wenn eine Nachricht gesendet wurde, die eine Bestätigung verlangt. |
|user_login |Nutzer-Login | Ein Benutzer hat sich angemeldet. |
|user_logout |Nutzer-Logout | Ein Benutzer hat sich abgemeldet |
|wordpress_sync |Wordpress-Synchronisation | Kopiervorgang von Assets zu Wordpress.|
| falconio_sync | Falconio-Synchronization | Kopiervorgang von Assets zu Falcon.io |
