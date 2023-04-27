---
title: "CSV-Dateien importieren"
menu:
  main:
    name: "Dateien"
    identifier: "tools/csvimport/examples/files"
    parent: "tools/csvimport/examples"
---
# Dateien importieren

Dateien können auch über den CSV-Importer importiert werden. Wenn die Dateien bereits über das Web zugänglich sind, können Sie einfach diese URL in der CSV-Datei verwenden.

Wenn sich die Dateien lokal auf Ihrem Computer befinden, müssen sie zunächst über einen Webserver verfügbar gemacht werden, da Webbrowser keinen direkten Zugriff auf Dateien auf Ihrem Computer unterstützen. Sehen Sie sich zum Beispiel diese Liste von Webservern an: https://slashdot.org/software/p/Tiny-Web-Server/alternatives.

## Importverfahren
- Öffnen Sie zunächst den CSV-Importer 
- laden Sie Ihre CSV-Datei hoch 
- wählen Sie "1st Row" für "CSV Field Names" 
- wählen Sie den Zielobjekttyp, den Pool und die entsprechende Maske aus 
- Wechseln Sie auf die Registerkarte "Import Mapping" und wählen Sie das entsprechende Zielfeld für die Spalte, die die URLs enthält 
- wählen Sie bei "Typ" "url", um neue Dateien zu importieren 
- wechseln Sie zurück zur Registerkarte "Importeinstellungen" und wählen Sie "Feld aktualisieren", wenn sich bereits Datensätze in der Liste befinden, die ggf. aktualisiert werden sollen 
- Klicken Sie auf "Vorbereiten" und Sie erhalten eine Übersicht, wie viele Zeilen importiert bzw. aktualisiert werden sollen 
- dann kann der Import / die Aktualisierung gestartet werden