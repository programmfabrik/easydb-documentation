---
title: "112 - Spracheinstellungen"
menu:
  main:
    name: "Spracheinstellungen"
    identifier: "webfrontend/userprefs/language"
    parent: "webfrontend/userprefs"
---
# Spracheinstellungen

Jeder Nutzer hat die Möglichkeit, Sprachen für die Anwendung (System), die Daten und die Suche zu wählen. Voraussetzung ist, dass die Mehrsprachigkeit vom Administrator in den Basis-Einstellungen bzw. im Datenmodell aktiviert wurde.

![Language Settings](language.png)

|Einstellung|Option|Erläuterung|
|---|---|---|
|Anwendung|*Sprachen*| Sofern vom Administrator mehrere Sprachen in der Basis-Konfiguration ausgewählt wurden, kann hier die Sprache des Systems gewählt werden. Alle Menüs und Buttons erscheinen dann in dieser Sprache. |
|Daten|*Sprachen*|Wählen Sie hier die Sprache(n) für die Eingabe und Anzeige der Daten. Bei der Auswahl mehrerer Sprachen, erscheint bei der Eingabe und Anzeige pro Sprache ein Feld. Die Reihenfolge der Sprachen kann verändert werden indem man die Sprachen per Drag & Drop verschiebt.|
|Suche|*Sprachen*| Aktivieren Sie diese Einstellung, um die Suche in einer oder mehreren Sprachen durchzuführen. Die Reihenfolge der Sprachen kann verändert werden indem man die Sprachen per Drag & Drop verschiebt. |
|Einstellungen||  |
||Rechtschreibprüfung| Durch Aktivieren der Rechtschreibprüfung werden die Texte bei der Eingabe überprüft. Hierfür wird die Rechtschreibprüfung des Browsers genutzt. Überprüfen Sie zunächst in Ihren Browsereinstellungen, ob die Rechtschreibprüfung aktiviert ist. |
|| Sprachauswahl je Feld im Editor             | Wenn aktiviert, werden im Editor nicht direkt alle aktivierten Datensprachen angezeigt, sondern nur die erste. Alle weiteren Sprachen können temporär pro Feld hinzugeschaltet werden, indem man beim Eingabefeld auf die Sprache klickt. |
|| Im Detail alle Sprachen mit Inhalt anzeigen | Wenn aktiviert, werden im Detail alle Sprachen angezeigt, für die etwas eingegeben wurde, auch wenn der Nutzer die Sprache nicht als Datensprache aktiviert hat. |



## Sortierung von Sprachen

Bei mehrsprachigen Daten kann es vorkommen, dass für einige Datensätze beide Sprachen eingegeben wurden und einige Texte nur in einer Sprache vorliegen. Da in der Standard- und Listen-Ansicht immer nur ein Wert angezeigt werden kann, greift die Reihenfolge der aktivierten Datensprachen.

Nehmen wir folgendes Beispiel:

    Datensatz 1: Wasser / Water
    Datensatz 2: Feuer / (nichts)
    Datensatz 3: (nichts) / Air

Je nachdem, ob die Reihenfolge der Datenbanksprachen hier z.B. Englisch-Deutsch oder Deutsch-Englisch eingestellt ist, sieht die Anzeige der Ergebnisse folgendermaßen aus:

    Englisch-Deutsch: Water, Feuer, Air
    Deutsch-Englisch: Wasser, Feuer, Air
