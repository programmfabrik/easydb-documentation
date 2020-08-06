---
title: "PDF-Templates"
menu:
  main:
    name: "PDF-Templates"
    identifier: "tutorials/pdf-templates"
    parent: "tutorials"
---
# PDF-Templates

Eine Beschreibung aller bereitstehenden Funktionen finden Sie unter ["Objekttypen"](/de/webfrontend/rightsmanagement/objecttypes/). Nachfolgend werden exemplarisch die Schritte erläutert, um ein PDF-Template zu erzeugen in dem pro Seite ein Bild und die dazugehörigen Metadaten angezeigt werden.

- Gehen Sie zu "Objekttypen"
- Klicken Sie den Objekttyp an, für den Sie ein PDF-Template erstellen wollen
- Wechseln Sie in den Reiter "PDF-Creator"
- Klicken Sie auf das Plus um ein neues Template hinzuzufügen
- Klicken Sie unten links auf "Datensätze auswählen" und wählen ein paar Beispieldatensätze aus, damit Sie die nachfolgenden Änderungen direkt in der Vorschau sehen
- Wählen Sie beim Element "Dokument" die Ausrichtigung "Querformat" und das Layout "Ein Datensatz"
- Geben Sie ggfs. im Bereich "Header" und "Footer" eine Dokumentüberschrift, Datum oder Seitenzahlen ein
- Fügen Sie unten links über das Plus ein DIV hinzu
- Geben Sie eine Breite von "50%" an
- Fügen Sie unter dem DIV über das Plus "Datei-Felder" hinzu
- Aktivieren Sie rechts das entsprechende Datei-Feld
- Fügen Sie unter dem Element "Dokument" ein weiteres DIV hinzu
- Geben Sie dort eine Breite von "470" an
- Fügen Sie unterhalb dieses DIVs "Felder" hinzu
- Wählen Sie unter "Felder" alle Felder aus, die Sie anzeigen möchten
- Klicken Sie zuletzt unten rechts auf "Anwenden" um das Template zu speichern



![](pdf_creator_example.png)



> TIPP: Passen Sie das Design der PDF-Datei mit Hilfe von CSS an, indem Sie eine eigene CSS-Datei einbinden oder direkt eigenes CSS im PDF-Creator schreiben.