---
title: "JSON-Importer"
menu:
  main:
    name: "JSON-Importer"
    identifier: "tools/jsonimport"
    parent: "tools"
---
# JSON-Importer

Der JSON-Importer kann zum Massenimport von Daten im JSON Format verwendet werden.

Eine Schritt-für-Schritt-Anleitung, um aus beliebigen Datenquellen JSON-Payloads zu erstellen, finden Sie [hier](/de/tutorials/jsonimport/) (aktuell nur auf englisch verfügbar).

Den Importer finden Sie unter "Tools &gt; JSON-Importer".

Die Konfiguration für den JSON-Importer kann in einer Manifestdatei (`manifest.json`) hochgeladen werden. Das Manifest enthält Payloads und weitere Informationen, die als Voreinstellungen im Importer übernommen werden.

> Bitte beachten Sie, dass der Server, auf dem die manifest.json und die Payloads liegen, vom Frontend aus erreichbar sein müssen.

## Probleme mit Mixed Content Blocking (Blockierung gemischter Inhalte)

Da das Frontend die JSON Dateien als Client lädt, ist es möglich, dass Ihr Browser den Request zum anderen Server blockiert.

Bei **Mixed Content Blocking** handelt es sich um eine Sicherheitsmaßnahme, die in verschiedenen Browsern implementiert ist:

* Google Chrome: https://blog.chromium.org/2019/10/no-more-mixed-messages-about-https.html
* Mozilla Firefox: https://support.mozilla.org/de/kb/Wie-beeinflussen-Inhalte-die-nicht-sicher-sind-meine-Sicherheit
* Microsoft Edge: https://docs.microsoft.com/de-DE/deployedge/edge-learnmore-mixed-content-downloads
* In anderen Browsern kann es auf vergleichbare Art implementiert sein

Falls das `manifest.json` und die Payload-Dateien nicht geladen werden können, öffnen Sie den Developer Tab Ihres Browsers und suchen Sie nach Fehlermeldungen, die ähnlich wie die folgenden aussehen (es kann davon verschiedene Variationen geben):

    ... has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.

oder

    This request has been blocked; the content must be served over HTTPS.

Ist dies der Fall, blockiert Ihr Browser den Request. Abhängig vom Browser gibt es Möglichkeiten, das Blockieren zu umgehen und die Dateien trotzdem zu laden.

### CORS Plugin

> **Achtung:** Mixed Content Blocking ist ein Sicherheits-Feature. Deaktivieren Sie es nur, wenn sie dem anderen Server vertrauen. Dies ist ein mögliches **Sicherheitsrisiko!**

Für verschiedene Browser sind Plugins verfügbar, die es erlauben, das Mixed Content Blocking zu deaktivieren:

* Google Chrome: https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf?hl=de
* Mozilla Firefox: https://addons.mozilla.org/de-DE/firefox/addon/cors-everywhere/

Mit vielen dieser Plugins ist es möglich, Mixed Content Blocking an- und auszustellen. Bitte prüfen Sie die Verfügbarkeit für Ihren Browser.

## Felder

![](jsonimporter_de.png)

| Option                                       | Beschreibung                                                  |
| -------------------------------------------- | ------------------------------------------------------------ |
| URL zur manifest.json                        | Dies ist die URL, um das manifest.json zu erhalten (optional). Diese Datei kann die nachfolgenden Einstellungen enthalten, alternativ müssen diese im JSON-Importer-Formular eingegeben werden. |
| Quelle                                       | Name der Quell-Instanz \(optional). Kann frei gewählt werden. Diese Information wird nicht migriert, sondern dient nur der Identifikation. |
| Basis-URI für alle Payloads                  | Basis-URI für alle Payloads in der Liste. Sie wird jeder Payload vorangestellt. Der Standardwert ist die gleiche Basis-URL des manifest.json. Wenn die Payloads nicht im gleichen Ordner (oder auf einem anderen Server) wie das Manifest gespeichert sind, ist dies erforderlich, um aus den Payload-Dateinamen absolute Pfade zu erstellen. Dieser Wert muss der relative Pfad zum Payload-Ordner sein. |
| Stapelgröße                                  | Anzahl der Objekte die pro Anfrage zum Server geschickt werden. |
| Upload-Typ für Dateien                       | <ul><li>**Direkt**: Frontend lädt Dateien direkt zum EAS (`put`)</li><li>**URL (remote put)**: EAS lädt die Dateien von einer externen URL (`rput`)</li><li>**Dateien ignorieren**: keine Dateien werden hochgeladen</li></ul> |
| Metadaten-Mapping                            | Für den Import verwendetes Metadaten-Mapping, um Informationen aus den XMP-/IPTC-/EXIF-Daten auszulesen (optional). |
| Fehler beim Hochladen von Dateien ignorieren | Wenn diese Option aktiviert ist, werden alle Fehler beim Hochladen von Dateien ignoriert und der Importvorgang wird fortgesetzt. Alle Fehler sind in den Logs verfügbar. |
| Unique-Constraint-Fehler ignorieren          | Wenn diese Option aktiviert ist, werden alle Constraint-Fehler vom Server ignoriert. |
| EAS-URL-Ersetzung für Dateien                | Die URL unter der die Dateien aufrufbar sind kann hier verändert werden (optional). |

### Felder aus manifest.json ausfüllen

Einiger dieser Felder können mit Daten aus der `manifest.json` Datei vorausgefüllt werden:

| Option | Key | Typ | Beschreibung |
|---|---|---|---|
| Quelle | `"source"` | String | |
| Basis-URI für alle Payloads | `"payload_base_uri"` | String | |
| Stapelgröße | `"batch_size"` | Integer | min: `1`, max: `1000` |
| Upload-Typ für Dateien | `"eas_type"` | String | <ul><li>`direct`: Direkt</li><li>`url`: URL (remote put)</li><li>`ignore`: Dateien ignorieren</li></ul> |
| Fehler beim Hochladen von Dateien ignorieren  | `"eas_skip_errors"` | Boolean | |
| EAS-URL-Ersetzung für Dateien | `"eas_replace_url"` | String | Valide URL |
| Metadaten-Mapping | `"mapping"` | Integer | ID des Mappings |


## Payloads

Hier werden alle verfügbaren Payloads angezeigt. Durch Anklicken wird der Inhalt der Datei angezeigt.

| Header      | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| Status      | Aktueller Status (In Bearbeitung / Erfolgreich / Fehler).    |
| URL         | URL der Payload.                                             |
| Startstapel | Nummer des Stapels mit dem gestartet werden soll. Standardmäßig beginnt der Import bei 1, sodass alle Stapel verarbeitet werden. |
| Stapel      | Anzahl der Stapel (sie hängen von der Menge der Objekte und der gewählten Staplgröße ab). |
| Objekte     | Anzahl der Objekte.                                          |
| Objekttyp   | In der Payload enthaltener Objekttyp.                        |
| Aktion      | Öffnet die Payload-Datei in einem neuen Tab.                 |
| Aktiviert   | Aktivieren oder Deaktivieren Sie einzelne Payloads für den Import-Vorgang (Strg+Klick, um alle auf der ausgewählten Seite zu aktivieren oder zu deaktivieren, oder klicken Sie auf die Schaltfläche unten, um auf allen Seiten zu aktivieren oder zu deaktivieren). |



## Funktionen

| Function                | Description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| Log als CSV exportieren | Laden Sie das Log als CSV-Datei herunter.                    |
| Logs löschen            | Löschen Sie die Logs des letzten Durchlauf.                  |
| Letzten Report öffnen   | Öffnet den letzten Report.                                   |
| Vorbereitung            | Durch Klicken werden einige Validierungen durchgeführt, bevor der eigentliche Import gestartet werden kann. |
| Start                   | Startet den Importvorgang und importiert alle aktivierten Payloads. |