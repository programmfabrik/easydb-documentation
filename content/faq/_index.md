---
title: "2 - FAQ"
menu:
  main:
    name: "FAQ"
    identifier: "faq"
    weight: -900
---
# FAQ

## Frequently Asked Questions - Häufig gestellte Fragen

> Hinweis: Verwenden Sie für easydb immer einen aktuellen Browser. Bei Problemen oder Fehlermeldungen prüfen Sie bitte zunächst, ob Sie Ihren Browser in der aktuellsten Version verwenden. Führen Sie ggfs. ein Update durch.

### Mein Account wurde gesperrt, weil ich zu oft das falsche Passwort eingegeben habe. Was muss ich jetzt tun?

Die Sperrung ist nur temporär. Warten Sie einen Tag oder wenden sich ggfs. an Ihren Administrator.

### Ich habe bei einigen Datensätzen keinen Download-Button?

Der Zugriff auf Datensätze wird über das Rechtemanagement gesteuert. Zugriffsrechte werden von Ihrem Administrator gesetzt und verwaltet.

### Der Speichern-Button bleibt inaktiv?

Bitte prüfen Sie, ob Sie die Pflichtfelder ausgefüllt haben. Diese sind mit einer roten Ecke am Eingabefeld gekennzeichnet.

### Beim Hochladen bekomme ich eine Fehlermeldung bezüglich nicht erlaubter Formate?

Erscheint eine Meldung in der Art:

> "Der Upload der Datei apple_getamac_calmingteas_20080818_480x272.mov wurde abgelehnt. Der Dateityp mov aus der Klasse video ist nicht erlaubt."

handelt es sich um eine Einschränkung, die in [Basiskonfiguration](/de/webfrontend/administration/base-config/) - [Upload](/de/webfrontend/administration/base-config/upload/) eingerichtet wurde. Wenden Sie sich ggfs. an Ihren Administrator.

### Die Berechnung einer Vorschauversion ist fehlgeschlagen. Was kann ich tun?

Dass Vorschauversionen nicht berechnet werden konnten, kann viele Gründe haben. Beispielsweise kann es sich um eine kaputte Originaldatei handeln oder um mangelndem Speicherplatz. Lösen Sie als erstes diese Ursache, wenden Sie sich dazu an Ihre Systemadministratoren und im Zweifelsfall an support@programmfabrik.de und stellen Sie uns eine Beispieldatei bereit, die wir untersuchen und testen können. Um sicher zu gehen, dass die Ursache behoben wurde, laden Sie eine Datei in Ihre easydb hoch und kontrollieren Sie dass nun Vorschauversionen generiert werden. Nun gilt es noch, die Versionen nachzuberechnen, die fehlgeschlagen sind, während das Problem bestand. Dies wird im [Sysadmin Manual](/en/sysadmin/eas/faq/#restart-all-failed-jobs) beschrieben.

### Wie kann ich mich für easydb registrieren?

Eine Registrierung für easydb erfolgt nach den Regularien des Betreibers. Sofern nicht anders eingerichtet, legt der easydb Administrator neue Nutzer in der easydb an. Es besteht die Möglichkeit eine Selbstregistrierung in easydb bereit zu stellen. Eine Anleitung dafür finden Sie [hier](./../tutorials/selfregister/#selbstregistrierung).

### Was ist der Unterschied zwischen "Herunterladen" und "Exportieren"?

Beim Herunterladen wird die Originaldatei oder eine Vorschauversion des Originals heruntergeladen. Beim Exportieren können zusätzlich zu den Originaldateien oder Vorschauversionen auch die in easydb eingetragenen Informationen als CSV, XML oder JSON exportiert werden.

### Wie kann ich mein (Test-)System vollständig leeren?

Sie können ihr (Test-)System in den Ursprungszustand zurücksetzen, indem Sie im Bereich [Server-Status](../webfrontend/administration/server-status) unten rechts über das Zahnradsymbol "Datenbank löschen" wählen. Beachten Sie aber, dass damit **sämtliche Daten gelöscht** werden, Sie anschließend ein leeres System vorfinden und die Aktion **nicht rückgängig** gemacht werden kann. Sollte die Funktion deaktiviert sein, so muss zunächst von einem Systemadministrator [api.settings.purgedata konfiguriert](../../en/sysadmin/configuration/easydb-server.yml) werden.

### Wie kann ich den Elasticsearch Index löschen und neu erzeugen?

Sie können den Elasticsearch Index löschenindem Sie im Bereich [Server-Status](../webfrontend/administration/server-status/#controls) unten rechts über das Zahnradsymbol "Reindex" wählen. Dies wird den Server neu starten und direkt nach dem Neustart den Index löschen. Der Index wird dann komplett neu erzeugt, bitte beachten Sie dass dies **sehr lange dauern** kann. Sollte die Funktion deaktiviert sein, so muss zunächst von einem Systemadministrator [api.settings.reindex konfiguriert](../../en/sysadmin/configuration/easydb-server.yml) werden.

Anstatt dies zu erlauben, kann der Systemadministrator die Re-Indizierung auch einmalig anstoßen mit nur dem folgenden SQL Befehl. Dieser muss in der SQL-Datenbank der easydb ausgeführt werden (also nicht in der Datenbank des EAS).

Den korrekten Datenbank-Namen erhalten sie als Ausgabe hinter `db-name:` auf der URL https://meineeasydb.example.com/api/v1/settings (ersetzen Sie myeasydb.example.com).

Verbinden Sie sich mit der Datenbank: (ersetzen Sie mein-db-name)

```bash
docker exec -ti easydb-pgsql psql -U postgres mein-db-name
```

Hier nun das SQL Kommando:

```sql
SELECT easydb_reindex();
```


### Sie erhalten einen Fehler beim Import von CSV-Dateien?

Sollten Sie Fehler beim Import von CSV-Dateien erhalten, gehen Sie wie folgt vor um das Problem einzugrenzen:

- stellen Sie die Paket-Größe auf dem Reiter "Datei" auf `"1 Zeile"`
- führen Sie den Import erneut durch

Im rechten Bereich "Tabellen-Ansicht" sehen Sie nun in der Spalte `"easydb|status"` welcher Datensatz ein Problem verursacht hat. In den Spalten `"easydb|status_text"` und `"easydb|warning_text"` stehen ggfs. weitere Informationen.

Sollten Sie das Problem nicht identifizieren können, klicken Sie bitte unten links auf "CSV speichern" und schicken diese Datei mit der erschienenen Fehlermeldung an unser Support-Team.



### Ich möchte meine Domain ändern. Was muss ich tun?

Um die primäre Domain der easydb zu ändern empfehlen wir die alte Domain in allen Dateien unterhalb von /srv/easydb/config zu ersetzen und dann die easydb neu zu starten.

Alle Erwähnungen finden:

```
grep -IRis 'old\.' /srv/easydb/config --color
```

Nach dem Ändern neu starten (hier nur die relevanten container):

```
docker restart easydb-eas easydb-server easydb-webfrontend easydb-fylr
```

Außerdem natürlich in /etc/apache2/sites-enabled/easydb-ssl.conf.
