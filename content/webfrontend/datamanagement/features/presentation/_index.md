---
title: "89 - Präsentationen"
menu:
  main:
    name: "Präsentationen"
    identifier: "webfrontend/datamanagement/features/presentation"
    parent: "webfrontend/datamanagement/features"
---
# Präsentationen

> HINWEIS: Die Funktionalität "Präsentationen" wird als separates Modul lizensiert. Bitte überprüfen Sie im Zweifel Ihren Lizenzvertrag.

easydb bietet für Mappen die Funktion, Präsentationen zu erstellen. Pro [Mappe](../../search/quickaccess/collection) kann eine Präsentation erstellt, für die Mappe gespeichert und auch exportiert werden.

Gespeicherte Präsentationen für Mappen werden durch <i class="fa fa-play"></i> an der Mappe im [Schnellzugriff](../../search/quickaccess) angezeigt und können durch Klick auf den Button im Präsentationsmodus gestartet werden. Zum Weiterbearbeiten öffnen Sie die Präsentation über das Kontextmenü.

## Präsentation erstellen

Wenn diese Funktion eingerichtet ist, können über das Kontextmenü für Mappen Präsentationen erstellt werden:
* Wird eine Präsentation geöffnet, erscheint links ein Überblick für die Folien. Die erste Folie (Titelfolie) ist voreingestellt und kann innerhalb von easydb nicht entfernt werden. Nach einem pptx-Export kann diese Folie lokal entfernt, ausgetauscht oder bearbeitet werden.
* Weitere Folien können mit <code class="button">+</code> über das Optionen-Menü unten im Überblick hinzugefügt werden. Markierte Folien können mit <code class="button">-</code> entfernt werden.
* Als Titel wird der Mappenname übernommen. Dieser kann manuell verändert werden.
* Neben der Übersicht wird die aktuelle Folie angezeigt. 
* Rechts stehen die Inhalte der Mappe zur Verfügung und können mit Drag & Drop in die Folien gezogen werden. 
* Sind mit einem Datensatz mehrere Bilder verknüpft, erscheint nach Drag & Drop in die Folie eine Auswahlleiste unten am Bild. Über die Pfeile kann das gewünschte Bild ausgewählt werden kann. Beim pptx-Export wird nur das ausgewählte Bild berücksichtigt.


![Präsentation erstellen](ppt_create.jpg)

|Button|Option|Erläuterung|
|---|---|---|
|<i class="fa fa-plus"> </i> <i class="fa fa-angle-down"> </i>||Auswahlmenü für das Hinzufügen neuer Folien|
||Freier Text|Erzeugt eine Folie für die Eingabe eines Texts mit Titel|
||Ein Datensatz|Folie für einen Datensatz. Der Datensatz kann aus der Übersicht für die Mappe auf der rechten Seite per Drag & Drop in die Folie gezogen werden. Mit <i class="fa fa-trash-o"></i> kann der Datensatz wieder von der Folie entfernt werden.|
||Zwei Datensätze|Folie für zwei nebeneinander stehende Datensatz. Die Datensätze können aus der Übersicht für die Mappe auf der rechten Seite per Drag & Drop in die Folie gezogen werden. Mit <i class="fa fa-trash-o"></i> können die Datensätze jeweils wieder von der Folie entfernt werden.|
||Alle fehlenden... |Fügt alle nicht verwendeten Datensätze der Mappe in Folien ein. Pro Datensatz wird eine Folie erzeugt. |
|<i class="fa fa-minus"></i>||Markierte Folie aus Übersicht löschen. |
|<i class="fa fa-search-plus"> </i> \ <i class="fa fa-search-minus"> </i>|Zoom|Für Folien mit Datensätzen steht ein Zoomer zur Verfügung. Er wird durch das Drehen am Mausrad (zoom-in) aktiviert. Der Datensatz kann ins Detail gezoomt oder als Vollbild dargestellt werden. Die Auswahl in dem kleinen Ansichtfenster kann mit Drag & Drop im Bild positioniert werden, um den gezoomten Ausschnitt zu wählen. |
||Doppelprojektion|Um die Reihenfolge von Datensätzen in Doppelprojektionen (Folie mit zwei Datensätzen) zu ändern, müssen die Datensätze jeweils entfernt und in der neuen Reihenfolge wieder eingefügt werden.|
||Reihenfolge|Die Reihenfolge der Folien kann mit Drag & Drop im Überblick geändert werden. Nur die Position der Titelfolie kann nicht geändert werden.|
|<i class="fa fa-cog"></i>| Standard-Info:                     | Für Folien mit Datensätzen kann eine Bildunterschrift hinzugefügt werden. Diese setzt sich automatisch aus Datenbank-Inhalten zusammen, die im Datenmodell als "Standard" definiert wurden. |
|| Keine Information                  | Es wird keine Bildunterschrift generiert. |
|| Titel                              | Es wird der Inhalt des Feldes eingeblendet, der im Datenmodell als "Titel" definiert wurde. |
||Titel und Untertitel| Es wird der Inhalt der Felder eingeblendet, die im Datenmodell als "Titel" und "Untertitel" definiert wurden. |
||Titel, Untertitel und Beschreibung| Es wird der Inhalt der Felder eingeblendet, die im Datenmodell als "Titel", "Untertitel" und "Beschreibung" definiert wurden. |
|<i class="fa fa-play"></i>|| Startet den Präsentationsmodus im Vollbild. Die Navigation in den Folien kann per Maus oder über die Pfeiltasten auf der Tastatur erfolgen.|

## Präsentation exportieren

Ihre Präsentationen können Sie aus easydb im Format pptx für Powerpoint exportieren. Im Auswahldialog können Format und Qualität für den Export gewählt werden.

![Präsentation exportieren](ppt_export.jpg)

>HINWEIS: Eine Präsentation wird durch das Löschen der Mappe gelöscht.
