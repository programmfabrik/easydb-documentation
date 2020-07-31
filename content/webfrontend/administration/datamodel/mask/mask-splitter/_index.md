---
title: "Trenner"
menu:
  main:
    name: "Trenner"
    identifier: "webfrontend/administration/datamodel/mask/mask-splitter"
    parent: "webfrontend/administration/datamodel/mask"
---
# Trenner - In Bearbeitung

In Masken können sogenannte Trenner verwendet werden, um die Felder zum Beispiel in Reitern oder Panels zu strukturieren. Über individuelle Trenner können darüber hinaus weitere Funktionen in Masken integriert werden (siehe "Plugin-Trenner").

Einige Trenner bestehen aus zwei Zeilen, die den Anfang und das Ende markieren. Dazugehörige Felder werden zwischen der Anfangs- und der Endzeile platziert.

> HINWEIS: Die Position aller Trenner und Felder in Masken kann per Drag & Drop verändert werden. Es kann sowohl der Anfang als auch das Ende des Trenners verschoben werden, um so den Bereich, den der Trenner definiert, zu variieren. Hierdurch können die Spaltenbreiten für die Eingabebereiche individuell angepasst werden.



## Standard-Trenner

Standardmäßig stehen Reiter, Panels, Blöcke und horizontale Teiler zur Verfügung.

[SCREENSHOT EINFÜGEN]



### Reiter-System inkl. Reiter

Felder können in einem Reitersystem angezeigt werden. Für das Reitersystem kann ein Anzeigename vergeben werden, der über den Reitern angezeigt wird. Im Reitersystem muss mindestens ein Reiter angelegt werden, der mit dem Trenner *Reiter* hinzugefügt wird. Es können beliebig viele Reiter in dem Reitersystem angelegt werden. Felder, die unterhalb des Reitersystems angelegt werden, behalten ihre Position über alle Reiter hinweg.

Innerhalb von einem *Reitersystem* können mehrere Reiter definiert werden. Die Felder für einen Reiter werden dann unterhalb des Trenners *Reiter* platziert.



### Panel

Felder können innerhalb eines Panels gruppiert werden und sind als Einheit auf- und zuklappbar. Panels können wie auch Reiter dazu genutzt werden, komplexe Feldmodelle übersichtlicher anzuordnen. Ein Panel besteht, wie das Reitersystem aus einer Kopf- und einer Endzeile. In der Kopfzeile wird die Bezeichnung für das Panel eingetragen. Die Felder werden zwischen der Kopf- und Endzeile angelegt. Standardmäßig werden die Panel geschlossen angezeigt. Über die Optionen kann das Panel für die Detailansicht, den Editor und die Expertensuche auf standardmäßig geöffnet gesetzt werden.



### Block

Ähnlich wie beim Panel können Felder innerhalb eines Blocks als Einheit gruppiert werden. Blöcke können nicht geschlossen werden, sind aber dynamisch in der Darstellung. Mehrere Blöcke werden in der Sidebar untereinander angezeigt. Wird die Sidebar in die Breite gezogen oder das Vollbild gewählt, gleiten die Blöcke nebeneinander. Blöcke können im Gegensatz zu den anderen Trennern nicht innerhalb eines Reitersystems angelegt werden.



### Horizontaler Teiler

Dieser Trenner ist eine einfache Zwischenüberschrift zwischen Feldern.



## Plugin-Trenner

Über individuelle Plugins können weitere Trenner hinzugefügt werden. 



### Barcode





### Feldwerte anzeigen



Folgende Optionen stehen zur Verfügung:

| Option                                                 | Beschreibung                                                 |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| Feldbreite                                             | Wählen Sie hier, ob die Ausgabe dieses Masksplitters die volle Breite im Editor und Detail einnehmen soll, oder nur 25, 50 oder 75 Prozent. |
| Ausgabe                                                |                                                              |
| Text ausblenden, wenn keine Ersetzungen verfügbar sind |                                                              |
| Auch die Feldinhalte als Markdown rendern              |                                                              |



### Hijri to Gregorian converter



