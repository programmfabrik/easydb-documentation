---
title: "Rechte Im-/Export"
menu:
  main:
    name: "Rechte Im-/Export"
    identifier: "tools/rightsimexport"
    parent: "tools"
---
# Rechte Im-/Export

easydb stellt im Frontend ein Migrationstool bereit, mit dem Rechte von easydb zu easydb übertragen werden können. Dies kann zum Beispiel der Fall sein, wenn für die Entwicklung ein Testsystem genutzt wird und Änderungen auf das Produktivsystem übertragen werden sollen. 


| Quelle      | Optionen                                                     | Beschreibung                                                 |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Gruppen     | - Berechtigungen und Systemrechte übertragen <br> - Ersetzen oder hinzufügen | Wählen Sie aus der Quelle **Gruppe**, um alle Gruppen zu übertragen oder öffnen Sie das Dropdown um einzelne Gruppen auszuwählen. Über Checkboxen kann festgelegt werden, ob Berechtigungen und/oder Systemrechte übertragen werden sollen. Bestehende Gruppen können ersetzt werden. Neue Gruppen können hinzugefügt werden. Sie werden in der Zielinstanz neu angelegt. |
| Tags        | - Berechtigungen übertragen <br> - Ersetzen oder hinzufügen  | Wählen Sie aus der Quelle **Tags**, um alle Tags zu übertragen oder öffnen Sie das Dropdown, um einzelne Tags auszuwählen. Aktivieren Sie die Checkbox, um die Berechtigungen zu übertragen. Bestehende Tags können ersetzt werden. Neue Tags können hinzugefügt werden. Sie werden in der Zielinstanz neu angelegt. |
| Workflows   | - Ersetzen oder hinzufügen                                   | Bestehende Workflows können ersetzt werden. Neue Workflows können hinzugefügt werden. Sie werden in der Zielinstanz neu angelegt. |
| Objekttypen | - Berechtigungen und Feldrechte übertragen <br> - Ersetzen oder hinzufügen | Wählen Sie aus der Quelle **Objekttypen**, um die Berechtigungen für alle Objekttypen zu übertragen oder öffnen Sie das Dropdown, um einzelne Objekttypen auszuwählen. <br><br> HINWEIS: auf Top-Level-Ebene sind nur die Objekttypen auswählbar, für die Berechtigungen definiert sind. Um auch die Feldrechte zu übertragen, müssen Sie die Objekttypen einzeln auswählen. |
| Pools       | - Berechtigungen übertragen <br> - Ersetzen oder hinzufügen  | Wählen Sie einen Pool. Aktivieren Sie die Checkbox für die Berechtigungen und wählen Sie den Zielpool, bei dem die Berechtigungen ersetzt oder hinzugefügt werden sollen. |

Um alle Berechtigungen zu übertragen, müssen die aktivierten Quellen mit dem Button <code class="button">Übertragen</code> bestätigt werden. Der Status zu den Übertragungen erscheint in der Konsole rechts.