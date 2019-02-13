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

Bitte prüfen Sie, ob Sie die Pflichtfelder ausgefüllt haben.

### Beim Hochladen bekomme ich eine Fehlermeldung bezüglich nicht erlaubter Formate?

Erscheint eine Meldung in der Art: "Der Upload der Datei apple_getamac_calmingteas_20080818_480x272.mov wurde abgelehnt. Der Dateityp mov aus der Klasse video ist nicht erlaubt.", handelt es sich um eine Einschränkung, die im System eingerichtet wurde. Wenden Sie sich ggfs. an Ihren Systemadministrator.

### Wie kann ich mich für easydb registrieren?

Eine Registrierung für easydb erfolgt nach den Regularien des Betreibers. Sofern nicht anders eingerichtet, legt der easydb Administrator neue Nutzer in der easydb an. Es besteht die Möglichkeit eine Selbstregistrierung in easydb bereit zu stellen. Eine Anleitung dafür finden Sie [hier](https://docs.easydb.de/de/webfrontend/userprefs/selfregister/#als-admin-selbstregistrierung-einrichten).

### Was ist der Unterschied zwischen "Herunterladen" und "Exportieren"?

Beim Herunterladen wird die Originaldatei oder eine Vorschauversion des Originals heruntergeladen. Beim Exportieren können zusätzlich zu den Originaldateien oder Vorschauversionen auch die in easydb eingetragenen Informationen als CSV, XML oder JSON exportiert werden.

### Wie kann ich mein (Test-)System vollständig leeren?

Sie können ihr (Test-)System in den Ursprungszustand zurücksetzen, indem Sie im Bereich [Server-Status](../webfrontend/administration/server-status) unten rechts über das Zahnradsymbol "Datenbank löschen" wählen. Beachten Sie aber, dass damit sämtliche Daten gelöscht werden, Sie anschließend ein leeres System vorfinden und die Aktion nicht rückgängig gemacht werden kann. Sollte die Funktion deaktiviert sein, so muss zunächst von einem Systemadministrator [api.settings.purgedata konfiguriert](../../en/sysadmin/konfiguration/easydb-server.yml) werden.

### Sie erhalten einen Fehler beim Import von CSV-Dateien?

Sollten Sie Fehler beim Import von CSV-Dateien erhalten, gehen Sie wie folgt vor um das Problem einzugrenzen:

- stellen Sie die Paket-Größe auf dem Reiter "Datei" auf "1 Zeile"
- führen Sie den Import erneut durch

Im rechten Bereich "Tabellen-Ansicht" sehen Sie nun in der Spalte "easydb|status" welcher Datensatz ein Problem verursacht hat. In den Spalten "easydb|status_text" und "easydb|warning_text" stehen ggfs. weitere Informationen.

Sollten Sie das Problem nicht identifizieren können, klicken Sie bitte unten links auf "CSV speichern" und schicken diese Datei mit der erschienenen Fehlermeldung an unser Support-Team.