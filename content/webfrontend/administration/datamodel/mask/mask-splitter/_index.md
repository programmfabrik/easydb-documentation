---
title: "Trenner"
menu:
  main:
    name: "Trenner"
    identifier: "webfrontend/administration/datamodel/mask/mask-splitter"
    parent: "webfrontend/administration/datamodel/mask"
---
# Trenner

In Masken können sogenannte Trenner verwendet werden, um die Felder zum Beispiel in Reitern oder Panels zu strukturieren. Über individuelle Trenner können darüber hinaus weitere Funktionen in Masken integriert werden (siehe "Plugin-Trenner").

Einige Trenner bestehen aus zwei Zeilen, die den Anfang und das Ende markieren. Dazugehörige Felder werden zwischen der Anfangs- und der Endzeile platziert.

> HINWEIS: Die Position aller Trenner und Felder in Masken kann per Drag & Drop verändert werden. Es kann sowohl der Anfang als auch das Ende des Trenners verschoben werden, um so den Bereich, den der Trenner definiert, zu variieren. Hierdurch können die Spaltenbreiten für die Eingabebereiche individuell angepasst werden.



## Standard-Trenner

Standardmäßig stehen Reiter, Panels, Blöcke und horizontale Teiler zur Verfügung.



### Reiter-System inkl. Reiter

Felder können in einem Reitersystem angezeigt werden. Für das Reitersystem kann ein Anzeigename vergeben werden, der über den Reitern angezeigt wird. Im Reitersystem muss mindestens ein Reiter angelegt werden, der mit dem Trenner *Reiter* hinzugefügt wird. Es können beliebig viele Reiter in dem Reitersystem angelegt werden. Felder, die unterhalb des Reitersystems angelegt werden, behalten ihre Position über alle Reiter hinweg.

Innerhalb von einem *Reitersystem* können mehrere Reiter definiert werden. Die Felder für einen Reiter werden dann unterhalb des Trenners *Reiter* platziert.



### Panel

Felder können innerhalb eines Panels gruppiert werden und sind als Einheit auf- und zuklappbar. Panels können wie auch Reiter dazu genutzt werden, komplexe Feldmodelle übersichtlicher anzuordnen. Ein Panel besteht, wie das Reitersystem aus einer Kopf- und einer Endzeile. In der Kopfzeile wird die Bezeichnung für das Panel eingetragen. Die Felder werden zwischen der Kopf- und Endzeile angelegt. Standardmäßig werden die Panel geschlossen angezeigt. Über die Optionen kann das Panel für die Detailansicht, den Editor und die Expertensuche auf standardmäßig geöffnet gesetzt werden. Für den Editor besteht darüber hinaus die Möglichkeit das Panel automatisch zu öffnen, sofern min. eines der Felder innerhalb des Panels ausgefüllt ist (Option "Im Editor öffnen, wenn Inhalt vorhanden ist").



### Block

Ähnlich wie beim Panel können Felder innerhalb eines Blocks als Einheit gruppiert werden. Blöcke können nicht geschlossen werden, sind aber dynamisch in der Darstellung. Mehrere Blöcke werden in der Sidebar untereinander angezeigt. Wird die Sidebar in die Breite gezogen oder das Vollbild gewählt, gleiten die Blöcke nebeneinander. Blöcke können im Gegensatz zu den anderen Trennern nicht innerhalb eines Reitersystems angelegt werden.



### Horizontaler Teiler

Dieser Trenner ist eine einfache Zwischenüberschrift zwischen Feldern.



## Plugin-Trenner

Über individuelle Plugins können weitere Trenner hinzugefügt werden. 



### Barcode

Mit Hilfe dieses Trenners kann ein Barcode generiert werden.



### Feldwerte anzeigen

Das Plugin display-field-values steht auf [Github](https://github.com/programmfabrik/easydb-display-field-values) zur Verfügung und eine Installationsanleitung ist [hier](../../../../../../en/sysadmin/configuration/easydb-server.yml/plugins/display-field-values/) zu finden. 

Folgende Optionen stehen zur Verfügung:

| Option                                                 | Beschreibung                                                 |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| Feldbreite                                             | Wählen Sie hier, ob die Ausgabe dieses Masksplitters die volle Breite im Editor und Detail einnehmen soll, oder nur 25, 50 oder 75 Prozent. |
| Ausgabe                                                | Geben Sie hier den Text ein, der angezeigt werden soll. Sie können die Markdown-Syntax verwenden um den Text zu formatieren und Links einzufügen. Mit Hilfe von Platzhaltern, wie z.B. %titel% können Sie auf die Inhalte von Freitextfeldern zugreifen. Sollten Sie einen Inhalt in einer URL verwenden, wählen Sie bitte die Ersetzungen mit :urlencoded (z.B. %titel:urlencoded%). |
| Text ausblenden, wenn keine Ersetzungen verfügbar sind | Aktivieren Sie diese Checkbox um den kompletten Text auszublenden, wenn keine Ersetzungen verfügbar sind (z.B. wenn ein verwendetes Feld keinen Inhalt hat). Andernfalls wird der Text trotzdem angezeigt (ist z.B. das Feld "Titel" nicht ausgefüllt, würde bei einer Ausgabe von "Das ist der %titel%." nur "Das ist der." angezeigt werden). |
| Auch die Feldinhalte als Markdown rendern              | Aktivieren Sie diese Checkbox, wenn der Inhalt eines Feldes bereits Markdown-Syntax enthält und dieser auch als Markdown gerendert werden soll. Andernfalls wird der Feldinhalt als Text ausgegeben. |



### Hijri to Gregorian converter

Dieses Plugin rechnet Hijri-Daten in Gregorianische Kalenderdaten um.



### Anzeige von Verlinkungen

Das Plugin custom-mask-splitter-detail-linked steht auf [Github](https://github.com/programmfabrik/custom-mask-splitter-detail-linked) zur Verfügung und eine Installationsanleitung ist [hier](../../../../../../en/sysadmin/configuration/easydb-server.yml/plugins/custom-mask-splitter-detail-linked/) zu finden.

Mit Hilfe dieses Plugins können in der Detailansicht von Datensätzen automatisch alle Einträge anderer Objekttypen die auf diesen verweisen, angezeigt werden. Haben Sie beispielsweise Bilder mit Schlagworten versehen, so können Sie in der Detailansicht eines jeden Schlagworts sehen, welche Bilder mit diesem verknüpft sind. 

Folgende Optionen stehen zur Verfügung:

| Option      | Beschreibung                                                 |
| ----------- | ------------------------------------------------------------ |
| Feldbreite  | Wählen Sie, ob das Feld 100%, 75%, 50% oder 25% der Breite in der Detailansicht einnehmen soll. |
| Anzeigeart  | Wählen Sie, ob die Einträge im Standard-, Text- oder Kurz-Format angezeigt werden sollen. |
| Objekttypen | Wählen Sie die Objektypen aus, dessen Verlinkungen angezeigt werden sollen. |

