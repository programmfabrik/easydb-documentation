# Editor {#editorplugin}

Diese Funktion wird über ein Plugin zu der Basis-Konfiguration hinzugefügt. Hier können Texte definiert werden, die beim Erstellen neuer Datensätze oder beim Aktualisieren bestehender Datensätze als Vorbelegung gesetzt werden. Das Plugin ist über [GitHub](https://github.com/programmfabrik/easydb-editor-tagfilter-defaults) frei verfügbar.

![](editorplugin_de.jpg)

|Einstellung|Detail|Erläuterung|
|---|---|---|
|Aktion|Aktualisieren|Der eingetragene Wert wird an bestehenden Datensätzen gesetzt. Die Option wird erst aktiv, wenn eine Maske gewählt wurde, für die Tags definiert sind, und mindestens ein Tag gesetzt wird. |
||Neue|Der eingetragenen Wert wird für neue Datensätze gesetzt.|
|Masken||Maske am Objekttyp, für die der Wert aus der Vorbelegung gesetzt werden soll.|
|Ersetzungen||Kann im Text der Vorbelegung genutzt werden, um auf einen bestimmten Wert zu verweisen. Bespeil: Wird für das Feld Lizenzrechte als Vorbelegung ein Verweis auf den Fotografen gemacht, kann der Fotograf über eine Ersetzung im Text angegeben werden.  |
|Tag-Filter||Die Vorbelegung kann an Tags geknüpft werden und wird gesetzt, wenn ein Datensatz entsprechenden Tag erhält. Dafür müssen für den Objekttyp Tags definiert sein. Für Aktualisierungen an bestehenden Datensätzen, muss ein Tag gesetzt werden. Bei neuen Datensätzen, kann der Wert auch Tags angegeben werden und wird beim Erstellen neuer Datensätze standardmäßig in das gewählte Felder der gewählten Maske gesetzt. *Beachten Sie: Wenn eine Vorbelegung generell für einen Objekttyp mit mehreren Masken greifen soll, muss diese Einstellung für jede Maske einzeln vorgenommen werden.* |
|Vorbelegung|Typ|Vorbelegung sind Werte, die beim Erstellen oder Aktualisieren eines Datensatzes automatisch als in ein Feld geschrieben werden. Aktuell steht nur der Typ *Vorbelegung* zur Verfügung. |
| | Feld |Feld, in das der Wert geschrieben werden soll. Je nach Auswahl der Maske erscheinen hier andere Felder zur Auswahl.|
||Wert| Hier kann ein Text, eine Ersetzung oder die Kombination aus beidem eingetragen werden.|