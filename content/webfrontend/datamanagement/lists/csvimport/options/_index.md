---
title: "99 - CSV-Importer Optionen"
menu:
  main:
    name: "Optionen"
    identifier: "webfrontend/datamanagement/lists/csvimport/options"
    parent: "webfrontend/datamanagement/lists/csvimport"
---
# Optionen - In Bearbeitung

easydb erlaubt den Import von Datensätzen und Benutzern über CSV (*UTF-8* oder *UTF-16*). Erreichbar ist der CSV-Importer im Menü unter *Listen* unten in der Sidebar über das <i class="fa fa-cog"></i>-Symbol.

![CSV-Importer](csv_importer.png)



## Vorbereitung

Die CSV-Datei wird hochgeladen und es werden folgende Einstellung vorgenommen:

| Einstellung                  | Beschreibung                                                 |
| ---------------------------- | ------------------------------------------------------------ |
| CSV-Feldnamen                | Zeile, in der die Spalten-Namen stehen.                      |
| Ziel-Feldnamen               | Zeile, in der die Ziel-Feld-Namen stehen.                    |
| Objekttyp                    | Objekttyp, der importiert werden soll.                       |
| Pool                         | Angabe des Pools. Der Pool wird nur beim Einfügen von Datensätzen gesetzt. |
| Maske                        | Maske, die für den Import verwendet werden soll.             |
| Feld zum Update              | Angabe eines Feldes, welches zum Suchen der Datensätze dient, wenn Sie ein Update machen möchten. Hier wählen Sie auch das Datei-Feld aus, wenn Sie Dateinamen in Ihrem CSV angegeben haben. |
| ---                          | Bei mehrsprachigen Feldern hat man dann die Möglichkeit den Abgleich über eine bestimmte Sprache zu machen (z.B. name#de-DE oder name#en-US). Um die Auswahl zu aktivieren, legen Sie im Reiter Mapping fest, für welche Felder, welche Sprachen zur Verfügung stehen sollen. |
| Mehrfachfelder anfügen       | Mit dieser Option werden angegebene Mehrfach-Felder hinzugefügt und nicht wie gewöhnlicherweise bei einem Update ersetzt. |
| Verlinkte Datensätze anlegen | Legen Sie fest, ob verlinkte Datensätze vor dem eigentlich Import angelegt werden sollen oder nicht. Ein Einfügen oder Aktualisieren von Datensätzen mit neuen verlinkten Datensätzen ist bei ausgeschalteter Option nicht möglich. |
| Kommentar                    | Kommentar zum Speichern der Datensätze.                      |
| Paket-Größe                  | Größe der Verarbeitungs-Pakete die nach und nach zum Server geschickt werden. |

### Aktionen

| Button                   | Beschreibung                                                 |
| ------------------------ | ------------------------------------------------------------ |
| Neu Einlesen             | Liest das CSV neu ein und verwirft alle bereits geladenen Informationen. |
| CSV speichern            | Beim Vorbereiten und nach dem Speichern entstehen Mehr-Informationen, die in das CSV zurückgeschrieben werden. Mit **CSV speichern** können Sie sich diese Informationen auf Ihren Desktop holen. Zum Beispiel werden die Datensatz-IDs in das CSV zurückgeschrieben, wenn Datensätze neu erzeugt wurden. |
| Vorbereiten...           | Bereitet den CSV-Import vor. Dazu gehören das Suchen von bereits bestehenden Datensätzen und verlinkten Datensätzen. Nach der Vorbereitung können Sie in der Tabellen-Ansicht überprüfen, welche Zeilen auf welche Art und Weise vereinnahmt werden. |
| Einfügen                 | Startet den CSV-Import und fügt neue Datensätze ein. Zuvor werden alle unbekannten verlinkten Datensätze neu angelegt. |
| Aktualisieren            | Startet den CSV-Import und aktualisiert bestehende Datensätze. Zuvor werden alle unbekannten verlinkten Datensätze neu angelegt. Beachten Sie, dass leere Spalten auch zum Server geschickt werden. |
| Einfügen + Aktualisieren | Führt beide Schritte direkt hintereinander durch.            |