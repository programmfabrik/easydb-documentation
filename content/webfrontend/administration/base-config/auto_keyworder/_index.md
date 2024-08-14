---
title: "64 - Auto Keyworder"
menu:
  main:
    name: "Auto Keyworder"
    identifier: "webfrontend/administration/base-config/auto_keyworder"
    parent: "webfrontend/administration/base-config"
---

# Auto Keyworder

> **Hinweis**: Dieses Plugin wird als separates Modul lizensiert. Bitte überprüfen Sie im Zweifel Ihren Lizenzvertrag.

Das Auto Keyworder Plugin ist ein Prozess-Plugin (im Hintergrund), das periodisch Bilddaten von Objekten an Online-KI-Dienste sendet, um den Bildinhalt zu erkennen und Objekte mit automatisch generierten Schlagwörtern und Themen zu aktualisieren.

Derzeit sind die folgenden KI-Dienste implementiert:

|  | Homepage | Externe API Dokumentation |
|---|---|---|
| **Cloudsight** | https://cloudsight.ai | https://cloudsight.docs.apiary.io |
| **DeepVA** | https://deepva.ai | https://docs.deepva.com |
| **Imagga** | https://imagga.com | https://docs.imagga.com |


## Basiskonfiguration

Alle KI-Dienste in der Basiskonfiguration unter 'Auto Keyworder' konfiguriert.

Das Plugin prüft die Basis-Konfiguration auf Veränderungen. Dies geschieht mit einer Verzögerung von `baseconfig_poll_interval_sec` Sekunden, nachdem ein momentan laufender Prozess beendet wurde. Dieser wird in der Server-Konfiguration definiert.

Folgende Einstellungen stehen zur Verfügung:

| Konfiguration | Pflicht | Default | Beschreibung |
|---|---|---|---|
| Dienst aktiviert | ja | `False` | Aktiviert/Deaktiviert den Auto-Keyworder |
| Update-Prozess nach dem Speichern starten | | `False` | <ul><li>Aktivieren Sie dies, um den Update-Prozess direkt zu starten nachdem die Basis-Konfiguration gespeichert wurde. Alternativ wird bis zum nächsten konfigurierten Zeitpunkt gewartet.</li><li>Interne Representation: Wert `start_now`, welcher ebenso bei einem API-Aufruf gesetzt werden kann (siehe [Plugin API](/de/webfrontend/datamanagement/features/plugins/autokeyworder/#plugin-api))</li><li>Dieser Wert ist **nicht persistent** und greift nur einmalig. Jedes Mal wenn der Wert zu `True` geändert wird, setzt das Plugin danach den Wert wieder auf `False`. </li><li>Dieses Kontrollkästchen bleibt nach dem Speichern so lange aktiviert, bis die Basiskonfiguration im Frontend neu geladen wird.</li></ul> |
| easydb API Nutzer</br></br>easydb API Nutzer Passwort | ja | | <ul><li>Login und Passwort eines bestimmten Nutzers, der Suchen und Updates in easydb durchführen darf</li><li>Dieses Plugin nutzt die easydb-Endpunkte `/api/v1/search`, `/api/v1/db` und `/api/v1/event`</li><li>Der Nutzer benötigt mindestens eines der folgenden Rechte für Objekttypen (bzw. Pools):</li><ul><li>`write` Recht für alle Objekttypen, die zum Updaten konfiguriert wurden</li><li>`mask` Recht auf eine Maske, die das Bearbeiten von allen Feldern erlaubt</li><li>`asset_show` Recht für die ausgewählten Asset-Felder, sodass das Plugin die Bilddaten an den KI-Service übermitteln kann</li><li>`bag_read` für den Pool, wenn die Objekte Poolmanagement besitzen</li><li>wenn die Schlagwörter in verlinkten Objekttypen verwaltet werden, braucht der Nutzer darüber hinaus die folgenden Rechte für die verlinkte Objekttypen:<ul><li>`read` Recht, um nach existierenden verlinkten Objekten zu suchen</li><li>`mask` Recht für eine Maske, die das Schreiben und Lesen innerhalb des Schlagwort-Textfeldes erlaubt</li><li>`create` Recht, um neue verlinkte Objekte anzulegen</li></ul></li></ul> |
| Wiederholungen Statusabfragen | ja | `3` | Maximale Anzahl der wiederholten Versuche, den Status der Verarbeitung eines Bildes beim externen Dienst abzufragen, bevor die Verschlagwortung des Bildes verworfen wird |
| Pause zwischen Statusabfragen | ja | `5` | Mindestwartezeit in Sekunden zwischen wiederholten Statusabfragen eines Bildes |


### Gemeinsame Konfigurationen für alle KI-Dienste

Konfigurationen für verschiedene Dienste und Objekttypen werden in verschiedene Konfigurationsblöcken gespeichert. Die folgenden Einstellungen sind für alle Dienste gleich.

| Konfiguration | Pflicht | Default | Beschreibung |
|---|---|---|---|
| Diese Konfiguration aktivieren | ja | `False` | Aktiviert/Deaktiviert diese Konfiguration |
| Name dieser Konfiguration | | | Um das Debuggen zu erleichtern, kann man der Konfiguration einen bestimmten Namen geben |
| API URL | ja | | <ul><li>Die Basis-URL der API des Dienstes</li><li>Es sollte immer die vorgeschlagene URL genutzt werden</li><li>Wenn eine andere URL nötig ist, deutet das auf grundlegende Änderungen in der externen API hin. **Dieser Dienst sollte dann vorläufig nicht mehr genutzt werden!**</li></ul> |
| API Key | Je nach API kann dies obligatorisch sein | | Der optional API Key für den Dienst |
| Objekttyp | ja | | <ul><li>Objekttyp für die Schlagwort-Aktualisierung</li><li>Nur Objekttypen mit den folgenden Anforderungen können ausgewählt werden:</li><ul><li>Mindestens ein Asset (Bild)</li><li>Mindestens ein Feld, wo die generierten Schlagwörter gespeichert werden (entweder ein Textfeld innerhalb eines Mehrfachfeldes oder ein Textfeld innerhalb eines verlinkten Objekttyps in einem Mehrfachfeld)</li><li>Mindestens ein Datum&Zeit-Feld, in dem der Zeitpunkt des zuletzt erfolgreichen Updates des Objekts gespeichert wird</li></ul></li><li>Der Objekttyp sollte Tagverwaltung aktiviert haben, wenn ein Tagfilter genutzt werden soll (siehe unten)</li></ul> |
| Datei-Feld | ja | | <ul><li>Dateifeld, aus dem die Bilddatei geladen und hochgeladen wird</li><li>**Bitte beachten:** es ist wichtig dass dieses Feld in der Standardmaske für die Expertensuche aktiviert ist</li></ul> |
| Asset-Version | ja | `original` | <ul><li>Die hochgeladene Asset-Version kann eine beliebige existierende Version sein, muss aber ein gültiges Bildformat haben</li><li>eine Mindestgröße pro Seite wird empfohlen, kleinere Bilder können aufgrund der geringeren Auflösung zu Fehlern bei der Erkennung führen, daher sollten die Versionen `preview` oder `small` vermieden werden</li><li>**Bitte beachten:** die Asset-Versionen sind durch die Rechteverwaltung geschützt. Stellen Sie sicher, dass der Api-Nutzer mindestens `read`-Rechte für die ausgewählte Asset-Version hat. Andernfalls kann das Plugin das Asset in dieser Version **nicht** zum Dienst hochladen</li></ul> |
| Zielfeld für Zeitpunkt der Verschlagwortung | ja | | <ul><li>Es muss ein Datum&Zeit-Feld sein, um den Zeitpunkt zu speichern</li><li>Nachdem ein Datensatz erfolgreich aktualisiert wurde, wird der Zeitpunkt in diesem Feld gespeichert</li><li>Es werden nur Objekte gesucht, wo dieses Feld keinen Wert hat oder wo der Zeitpunkt älter als das bestimmte maximale Alter ist (siehe unten)</li><li>**Bitte beachten:** es ist wichtig dass dieses Feld in der Standardmaske für die Expertensuche aktiviert ist</li></ul> |
| Tagfilter, um Objekte für die automatische Verschlagwortung zu markieren | optional aber empfohlen | | <ul><li>Tag-Filter, um Datensätze zu markieren, die aktualisiert werden sollen</li><li>Es werden nur Datensätze gesucht, wo die Tags gesetzt wurden beziehungsweise nicht gesetzt wurden.</li></ul> |
| Mindestdauer seit der letzten automatischen Verschlagwortung | ja | `7` | <ul><li>Zeit, seitdem der Datensatz das letzte Mal aktualisiert wurde (in Tagen)</li><li>Es werden nur Datensätze gesucht, wo das Feld des Zeitpunktes keinen Wert hat oder wo der Zeitpunkt älter als diese Zeit ist</li><li>Wenn Daten in Datensätzen überschrieben werden sollen, die erst kürzlich geändert wurden, muss der Zeitpunkt manuell gelöscht werden</li></ul> |


### Konfigurationen für verschiedene KI-Dienste

#### Konfigurationen für Cloudsight

| Konfiguration | Pflicht | Default | Beschreibung |
|---|---|---|---|
| Zielfeld für Bildtitel (Subject) | | | Text-Feld, in dem der Bild-Titel gespeichert wird |
| Zielfelder für Schlagwörter:<ul><li>Ähnliche Objekte</li><li>Kategorie</li><li>Menge / Anzahl</li><li>Geschlecht</li><li>Material</li><li>Farbe</li></ul> | | | <ul><li>Felder, in denen verschiedene Teile der strukturierten Ergebnisse aus Responses aus der Cloudsight API gespeichert werden</li><li>Wenn eine dieser strukturierten Ausgaben in der Antwort vorhanden ist, werden diese spezifischen Felder ausgefüllt</li><li>Wenn das Feld ein Mehrfachfeld ist, wird jedes Schlagwort in einer neuen Reihe gespeichert, sonst werden die Schlagwörter mit einem Komma getrennt</li><li>Wenn das Feld ein mehrsprachiges Feld ist, werden die Schlagwörter in der definierten Sprache gespeichert (siehe unten)</li><li>Wenn das Feld ein verlinkter Objekttyp ist, sucht das Plugin einen Eintrag mit dem gleichen Namen. Wenn dies nicht der Fall ist, wird ein neuer Datensatz angelegt. Dies erfolgt bevor es mit dem Datensatz verlinkt wird, der aktualisiert wird.</li></ul> |
| Sprache für Bildtitel (Subject) und verlinkte Objekte | | englisch | <ul><li>Sprache, in der die Schlagwörter angefordert werden</li><li>Der Sprach-Parameter wird über die API geschickt</li><li>Der Titel (`name`) vom analysierten Bild wird in dieser Sprache zurückgesendet</li><li>Die Schlagwörter werden in der Sprache gesendet, die im Cloudsight-Projekt für den genutzten API Key konfiguriert wurde. **Diese Konfiguration ist getrennt und unabhängig von easydb!**</li><li>Für die besten Ergebnisse sollte die Sprache ausgewählt werden, die im Cloudsight-Projekt konfiguriert wurde. So werden die Schlagwörter und der Titel in derselben Sprache gespeichert.</li><li>Diese Sprachen sind verfügbar:<ul><li>deutsch: `de-DE`</li><li>englisch: `en-US`</li><li>spanisch: `es-ES`</li><li>italienisch: `it-IT`</li><li>arabisch: `ar`</li><li>tschechisch: `cs-CZ`</li><li>farsi (persisch): `fa`</li><li>französisch: `fr-FR`</li><li>japanisch (gemischte Schrift): `ja-Jpan`</li><li>georgisch: `ka-GE`</li><li>koreanisch (gemischte Schrift): `ko-Kore`</li><li>niederländisch: `nl-NL`</li><li>polnisch: `pl-PL`</li><li>russisch: `ru-RU`</li><li>chinesisch: `zh-Hans`</li></ul></li></ul> |

#### Konfigurationen für DeepVA

| Konfiguration | Pflicht | Default | Beschreibung |
|---|---|---|---|
| Zielfeld | | | <ul><li>Feld, in dem Labels aus Responses der DeepVA API als Schlagwörter gespeichert werden</li><li>Wenn das Feld ein Mehrfachfeld ist, wird jedes Schlagwort in einer neuen Reihe gespeichert, sonst werden die Schlagwörter mit einem Komma getrennt</li><li>Wenn das Feld ein mehrsprachiges Feld ist, werden die Schlagwörter in englischer Sprache gespeichert (es werden abhängig von den verwendeten Modellen verschiedene Sprachen zurückgegeben, aber es wird aus Kompatibilitätsgründen nur englisch genutzt)</li><li>Wenn das Feld ein verlinkter Objekttyp ist, sucht das Plugin einen Eintrag mit dem gleichen Namen. Wenn dies nicht der Fall ist, wird ein neuer Datensatz angelegt. Dies erfolgt bevor es mit dem Datensatz verlinkt wird, der aktualisiert wird.</li></ul> |
| Maximale Anzahl an Schlagwörtern | | `5` | Wenn die Antwort mehr Schlagwörter enthält, werden nur die ersten `n` Schlagwörtern verwendet. |
| Module und Modelle | | | <ul><li>DeepVA bietet verschiedene vortrainierte Modelle zur Beschriftung von Bildern</li><li>Mindestens ein Modul und Modell muss eingetragen werden</li><li>Alle Modelle und Module werden auf ein hochgeladenes Bild angewendet</li><li>Nutzen Sie dies, um den Inhalt und den Umfang der Label zu kontrollieren</li><li>**Verschiedene Modelle sind für unterschiedliche Zwecke vortrainiert. Achten Sie darauf, dass Sie die richtigen Modelle je nach dem erwarteten Inhalt der Bilder auswählen!**</li><li>Zu verfügbaren Modellen lesen Sie bitte die externe Dokumentation: <a href="https://docs.deepva.com/core-resources/model/#pre-trained-models">https://docs.deepva.com/core-resources/model/#pre-trained-models</a> </li></ul> |

#### Konfigurationen für Imagga

| Konfiguration | Pflicht | Default | Beschreibung |
|---|---|---|---|
| API Secret | ja | | Zusätzlich zum API Key benötigt die Imagga API auch ein API Secret |
| Zielfeld | | | <ul><li>Feld, in dem Tags aus Responses der Imagga API als Schlagwörter gespeichert werden</li><li>Wenn das Feld ein Mehrfachfeld ist, wird jedes Schlagwort in einer neuen Reihe gespeichert, sonst werden die Schlagwörter mit einem Komma getrennt</li><li>Wenn das Feld ein mehrsprachiges Feld ist, werden die Schlagwörter in der definierten Sprache gespeichert (siehe unten)</li><li>Wenn das Feld ein verlinkter Objekttyp ist, sucht das Plugin einen Eintrag mit dem gleichen Namen. Wenn dies nicht der Fall ist, wird ein neuer Datensatz angelegt. Dies erfolgt bevor es mit dem Datensatz verlinkt wird, der aktualisiert wird.</li></ul> |
| Maximale Anzahl an Schlagwörtern | | `5` | Wenn die Antwort mehr Schlagwörter enthält, werden nur die ersten `n` Schlagwörtern verwendet. |
| Minimale Konfidenz | ja | `75` | <ul><li>Die API liefert zu den erkannten Schlagwörtern einen Konfidenzwert (`1` - `100` als Prozentwert).</li><li>Schlagwörter, die nicht mindestens diesen Wert erreichen, werden ignoriert.</li></ul> |
| Sprache | | englisch | <ul><li>Sprache, in der die Schlagwörter angefordert werden</li><li>Der Sprach-Parameter wird über die API geschickt</li><li>Die Tags des analysierten Bildes werden in dieser Sprache zurückgegeben</li><li>Diese Sprachen sind verfügbar:<ul><li>englisch: `en-US`</li><li>deutsch: `de-DE`</li><li>arabisch: `ar`</li><li>katalanisch: `ca`</li><li>tschechisch: `cs-CZ`</li><li>spanisch: `es-ES`</li><li>farsi (persisch): `fa`</li><li>finnisch: `fi-FI`</li><li>französisch: `fr-FR`</li><li>hebräisch: `he`</li><li>hindi: `hi`</li><li>italienisch: `it-IT`</li><li>japanisch (gemischte Schrift): `ja-Jpan`</li><li>koreanisch (gemischte Schrift): `ko-Kore`</li><li>neiderländisch: `nl-NL`</li><li>polnisch: `pl-PL`</li><li>portugiesisch: `pt`</li><li>russisch: `ru-RU`</li><li>schwedisch: `sv-SE`</li><li>türkisch: `tr-TR`</li><li>ukrainisch: `uk`</li><li>urdu: `ur`</li><li>chinesisch (Kurzzeichen): `zh-Hans`</li><li>chinesisch (Langzeichen): `zh-Hant`</li></ul></li></ul> |
