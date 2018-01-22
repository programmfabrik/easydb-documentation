# Metadaten-Mapping (Profile)

Das Metadaten-Mapping wird genutzt, um den Import und Export von Metadaten zu definieren. Es wird dabei zwischen Import- oder Exportprofilen unterschieden. Ferner werden Mappings in drei Typen gegliedert, wovon jeder anderen Bereichen zur Verfügung steht:

- exiftool_export (Herunterladen, Export)
- exiftool_import (Neue Datensätze, Objekttypen-Management, Pool-Management)
- xml_export (Export)

Aktuell können Mappings für **EXPORT**, **IMPORT**, **Dublin Core** und **TYPO3 Metadaten** standardmäßig erstellt werden.

## Mapping einrichten und anwenden

Für jeden Typ können mehrere Mappings definiert werden. Um ein neues Mapping einzurichten, klicken Sie in der Liste der Typen unten auf das Plus-Zeichen und wählen Sie den Typ, für den Sie ein Mapping einrichten möchten.

![Neues Mapping](profiles_neu.png)

Vergeben Sie einen Namen für das Mapping. Die Felder der easydb werden den Feldern des Mappings per Drag & Drop zugeordnet. Im nachstehenden Beispiel wurde beispielsweise das Feld "Titel" von links nach rechts in das Feld "Dokumententitel" gezogen.

Um die Feldauswahl wieder zu entfernen ziehen Sie den Eintrag etwas neben das Feld.

![Neues Mapping einrichten](profiles_interface.png)

Je nach Typ gibt es im Mapping sehr viele Zielfelder, in die die easydb Felder gemappt werden können. Es können mehrere easydb Felder in ein Mapping Feld gemappt werden.

Nachdem die Feldzuordnung abgeschlossen ist, wird das Mapping mit dem Button <code class="button">Speichern</code> gesichert und steht ab sofort als Auswahl z.B. im Exporter zur Verfügung. Der nachstehende Screenshot zeigt den Exporter mit dem neu angelegten Mapping.

![Exporter und Mapping-Auswahl](profiles_exporter.png)

Beim Hochladen neuer Datensätze kann das Mapping im "Neue Datensätze Editor" gewählt werden. Vorhandene Metadaten werden dann direkt mit dem gewählten Profil gemappt. Der nachstehende Screenshot zeigt den "Neue Datensätze Editor". Es wurde bereits eine Datei hochgeladen und im Mapping-Pulldown das Mapping "Grundinformationen" ausgewählt.

Nach Klick auf den Button <code class="button">weiter</code> gelangt man in den Editor. Wird nun die soeben hochgeladene Datei angewählt, zeigt der Inhalt der Felder eine Vorschau des durchgeführten Mappings. In diesem Beispiel wurden die Informationen für "Titel" und "Beschreibung" gemappt.

![Vorausgefüllte Felder](profiles_uploader.png)

## Metadaten-Mapping für TYPO3 Exporte

Nach erfolgreicher Installation des TYPO3 Plugins, können an dieser Stelle eigene Metadaten-Mappings für den Export zu TYPO3 erstellt werden.

![Beispielmapping für TYPO3](mapping_cms.jpg)