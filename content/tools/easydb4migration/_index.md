---
title: "easydb 4 Migration"
menu:
  main:
    name: "easydb 4 Migration"
    identifier: "tools/easydb4migration"
    parent: "tools"
---
# Migration von easydb 4 auf 5

Zur Migration von easydb aus Version 4 zu Version 5 stehen auf Github [Migrations-Tools](https://github.com/programmfabrik/easydb-migration-tools) bereit. Die Tools können auch zur Migration anderer Daten verwendet werden. Eine Anleitung ist in der [Migrationsdoku](https://github.com/programmfabrik/easydb-migration-tools/blob/master/migration.md) zu finden. Nachstehend eine kurze Step-by-Step-Anleitung für das Vorgehen bei der Migration:

1. Öffnen des ezadmin der easydb 4
2. Backup mit Asset-URLs erstellen und anschließend das sqlite herunterladen
3. easydb 4 Migrationstool in easydb 5 aufrufen
4. Das eben heruntergeladene sqlite hochladen.
5. Nachdem das sqlite hochgeladen wurde, kann das Datenmodell als CSV heruntergeladen werden. Hierbei wird lediglich das Datenmodell heruntergeladen. Nicht die in easydb 4 eingestellten Masken.
6. easydb 4 Migrationstool schließen
7. Öffnen Sie das Datenmodell in easydb 5.
8. Upload des eben heruntergeladenen Datenmodells.
9. Anschließend können im Datenmodell die Masken entsprechen eingestellt und die Änderungen aktiviert werden.
10. easydb 4 Migrationstool erneut öffnen
11. Ggfs. muss das Mapping angepasst werden. Wenn Sie die Migration 1:1 durchführen, wird dies nicht nötig sein. Dies wird dann nötig, wenn z.B. aus einem Freitextfeld in eine Liste migriert werden soll.
12. Anschließend klicken Sie auf die Schaltfläche "Export JSON". Hierbei werden sämtliche Daten aus dem sqlite anhand des eingestellten Mappings in JSON-Files transferiert, die später beim Import verwendet werden.
13. Der Export-Vorgang kann je nach Größe der Datenbank und Größe des Datenmodells recht lange (auch mehrere Tage) andauern.
14. Ist der Export abgeschlossen, können Sie auf JSON-Importer klicken. Es öffnet sich ein neues Fenster.
15. Für gewöhnlich wird hier "rput" gewählt. Ggfs. muss hier noch die Adresse des easydb 4 Servers angegeben werden. Hier wird die Adresse eingetragen unter der, der easydb 4 Server dem easydb 5 Server bekannt ist.
16. Der Import wird mit "Import starten" gestartet.
17. Nachdem der Import abgeschlossen ist, werden die angelegten Datensätze indiziert und die Vorschauversionen berechnet. Das bedeutet, wenn der Import abgeschlossen ist, werden Sie vermutlich noch nicht alle Vorschauversionen im Frontend der easydb 5 sehen. Die Berechnung der Vorschauversionen läuft im Hintergrund und kann noch einige Zeit in Anspruch nehmen.