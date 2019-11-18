---
title: "54 - Migration"
menu:
  mainWEG:
    name: "Migration"
    identifier: "sysadmin/migration"
    parent: "sysadmin"
    weight: 8
---
# Migration

## Migration über CSV

Zum Import von Daten kann auch der [CSV-Importer](/de/webfrontend/datamanagement/lists/csvimport) genutzt werden.

## Frontend Migrationstool

easydb stellt im Frontend ein Migrationstool bereit, mit dem Rechte von easydb zu easydb übertragen werden können. Dies kann zum Beispiel der Fall sein, wenn für die Entwicklung ein Testsystem genutzt wird und Änderungen auf das Produktivsystem übertragen werden sollen. 


|Quelle|Optionen|Beschreibung|
|---|---|---|
|Gruppen|- Berechtigungen und Systemrechte übertragen <br> - Ersetzen oder hinzufügen| Wählen Sie aus der Quelle **Gruppe**, um alle Gruppen zu übertragen oder öffnen Sie das Dropdown um einzelne Gruppen auszuwählen. Über Checkboxen kann festgelegt werden, ob Berechtigungen und/oder Systemrechte übertragen werden sollen. Bestehende Gruppen können ersetzt werden. Neue Gruppen können hinzugefügt werden. Sie werden in der Zielinstanz neu angelegt. |
|Tags |- Berechtigungen übertragen <br> - Ersetzen oder hinzufügen| Wählen Sie aus der Quelle **Tags**, um alle Tags zu übertragen oder öffnen Sie das Dropdown, um einzelne Tags auszuwählen. Aktivieren Sie die Checkbox, um die Berechtigungen zu übertragen. Bestehende Tags können ersetzt werden. Neue Tags können hinzugefügt werden. Sie werden in der Zielinstanz neu angelegt. |
|Workflows|- Ersetzen oder hinzufügen| Bestehende Workflows können ersetzt werden. Neue Workflows können hinzugefügt werden. Sie werden in der Zielinstanz neu angelegt. |
|Objekttypen|- Berechtigungen und Feldrechte übertragen <br> - Ersetzen oder hinzufügen| Wählen Sie aus der Quelle **Objekttypen**, um die Berechtigungen für alle Objekttypen zu übertragen oder öffnen Sie das Dropdown, um einzelne Objekttypen auszuwählen. <br><br> HINWEIS: auf Top-Level-Ebene sind nur die Objekttypen auswählbar, für die Berechtigungen definiert sind. Um auch die Feldrechte zu übertragen, müssen Sie die Objekttypen einzeln auswählen. |
|Pools|- Berechtigungen übertragen <br> - Ersetzen oder hinzufügen| Wählen Sie einen Pool. Aktivieren Sie die Checkbox für die Berechtigungen und wählen Sie den Zielpool, bei dem die Berechtigungen ersetzt oder hinzugefügt werden sollen. |

Um alle Berechtigungen zu übertragen, müssen die aktivierten Quellen mit dem Button <code class="button">Übertragen</code> bestätigt werden. Der Status zu den Übertragungen erscheint in der Konsole rechts.



## Migration easydb 4 zu 5

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














