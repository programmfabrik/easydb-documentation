---
title: "77 - Objekttypen"
menu:
  main:
    name: "Objekttypen"
    identifier: "webfrontend/administration/datamodel/objecttype"
    parent: "webfrontend/administration/datamodel"
---
# Objekttypen

## Objekttyp

![*Ansicht im Tab Objekttyp *](objekttyp.png)

| Einstellung | Option | Erläuterung |
| --- | --- | --- |
| Name | | Name des Objekttypen in der Datenbank. Hier sind nicht viele Zeichen erlaubt, da dieser Name ggfs. für Exporte usw. benutzt wird und deshalb keine komplexen Zeichen enthalten darf. [(siehe Regeln)](#objecttype_name_rules) |
| Bezeichnung | | Ist der Anzeigename des Objekttypen. Hier wird festgelegt unter welchem Namen der Objekttyp in der Anwendung erscheint. Dieses Feld ist mehrsprachig. |
| Kommentar (intern) | | Ein freier Kommentar, der nur hier angezeigt wird. |
| Datenbankoptionen | Pool-Verwaltung | easydb verwaltet diesen Objekttyp in der Pool-Hierarchie. D. h. die Datensätze dieses Objekttypen sind immer genau einem Pool zugeordnet. Über Pools kann Tag-Management, Rechte-Management und Transition-Management genutzt werden. Sie sollten ihre Haupt-Datensätze in Pools organisieren. |
| | Hierarchisch | easydb verwaltet diesen Objekttyp einer Hierarchie zugehörend. D. h. es kann jedem Datensatz genau ein übergeordneter Datensatz desselben Objekttypen zugeordnet werden. Datensätze ohne den Verweis auf eine übergeordnete Ebene werden als Top-Level-Datensätze bezeichnet. |
| | Editierbar in Verlinkung (Reverse Edit) | Bei hierarchische Objekttypen können alle untergeordneten Objekttypen (auch über mehrere Ebenen untergeordnet) direkt angezeigt und verändert werden. Für die untergeordneten Objekttypen kann über Masken eine andere Feld-Sichtbarkeit eingestellt werden, als für die Ebene des übergeordneten Objekttypen. Die Datensatz-Indizierung erfolgt mit dieser Einstellung immer inklusive aller untergeordneten Objekttypen. |
| Rechercheoptionen | Suche | Der Objekttyp ist damit in der Hauptsuche (Recherche) verfügbar. Dadurch kann der Objekttyp auch in Mappen verwaltet werden. |
| Berechtigungen | Individuelle Berechtigungen pro Datensatz | Wenn aktiv, können für diesen Objekttyp Rechte auch am einzelnen Datensatz verwaltet werden. Ohne diese Einstellung ist Rechtemanagement für die Datensätze dieses Objekttypen nur über Pools (bzw. Objekttypen direkt, wenn der Objekttyp kein Pool-Management unterstützt), Tags (wenn der Objekttyp Tag-Management unterstützt) und Mappen möglich. |
| | Vergabe von Tags | Mit aktiviertem Tag-Management können jedem Datensatz dieses Objekttypen Tags zugeordnet werden. Über Tags können Rechtemanagement und Workflow-Management durchgeführt werden. |

<a name="objecttype_name_rules"></a>
### Regeln für die Namen von Objekttypen

Um interne Konflikte mit den Namen von Objekttypen zu vermeiden, gelten für alle Objekttypnamen die folgenden Regeln:

- Kein Objekttyp darf mit dem Präfix `ez_` beginnen (Groß- und Kleinschreibung wird nicht beachtet)

- Ein Objekttyp muss den folgenden regulären Ausdruck erfüllen: `^[a-z][a-z0-9_]{0,61}[a-z0-9]$`
    - Nur kleine Buchstaben des englischen Alphabets (`a` - `z`), Zahlen oder Unterstriche `_` sind erlaubt
    - Mindestlänge 2 Zeichen, Höchstlänge 63 Zeichen
    - Muss mit einem Buchstaben beginnen

- Als Name für einen Objekttypen ist keine der folgenden geschützten Systemtabellen erlaubt:
    - `pool`
    - `collection`
    - `user`
    - `group`
    - `message`

## Felder

![*Ansicht im Tab Felder *](felder.png)

| Einstellung | Option | Erläuterung |
| --- | --- | --- |
| Feld | Feld | Name für das Datenbankfeld. Die Felder von Objekttypen werden direkt in der Datenbank als Tabellen-Feld angelegt. Es können nicht alle Zeichen verwendet werden, da dieser Name auch in Exporten usw. benutzt wird. |
| | Mehrfachfeld | Name des Mehrfachfeldes. Für Mehrfachfelder legt easydb in der Datenbank eine jeweils eigene Tabelle an. Mehrfachfelder können dadurch wiederum wieder eigene Felder definieren. Mehrfachfelder können verschachtelt werden. |
| Bezeichnung | | Anzeigename des Feldes wie ihn Benutzer in Anzeige und Editoren sehen. Bezeichnung ist mehrsprachig. Beachten Sie, dass nur in Objekttypen Bezeichnungen festgelegt werden können. Masken definieren nur die Sichtbarkeit der Felder, aber keine eigenen Anzeigenamen. |
| Datentyp | Einzeiliger Text | Der einzeilige Text erlaubt die Dateneingabe in einer Zeile, also Texte ohne Zeilenumbrüche. Die Länge ist nicht beschränkt. Texte werden im Index wortweise indiziert und können rechtstrunkiert gesucht werden. |
| | Einzeiliger Text (mehrsprachig) | Der mehrsprachige *einzeilige Text* erlaubt die Dateneingabe in mehreren Sprachen. Bei der Anzeige des Datensatzes wird bevorzugt die Sprache des Benutzers verwendet. Sollte diese Sprache nicht ausgefüllt sein, wird der Reihe nach geschaut, ob eine andere Sprache ausgefüllt ist. Nach welchen Sprachen der Benutzer sucht, kann er selber einstellen. |
| | Mehrzeiliger Text | Wie *Einzeiliger Text*, nur dass die Eingabe mit Zeilenumbrüchen erfolgen kann. Im Editor sind größere Eingabefelder zu sehen. |
| | Mehrzeiliger Text (mehrsprachig) | Der mehrsprachig einzeilige Text erlaubt die Dateneingabe in mehreren Sprachen. Bei der Anzeige des Datensatzes wird bevorzugt die Sprache des Benutzers verwendet. Sollte diese Sprache nicht ausgefüllt sein, wird der Reihe nach geschaut, ob eine andere Sprache ausgefüllt ist. Nach welchen Sprachen der Benutzer sucht, kann er selber einstellen. |
| | Einfacher Text (String) | Ein String wird verwendet für Bezeichnungen oder Referenz-IDs oder alles was links- und rechtstrunkiert durchsucht werden können soll. |
| *Datum + Zeit* | Datum | Der Datums-Typ unterstützt reine Jahreszahlen, Jahr+Monat und Jahr+Monat+Tag. Je nach eingestellter Frontend-Sprache unterscheiden sich die Ein- und Ausgabe-Formate. Beim Suchen werden die breiteren Datumsbereiche Jahr und Jahr+Monat wie ein Zeitraum behandelt, der beim Jahr vom 1. Januar bis zum 31. Dezember läuft und beim Monat vom 1. des Monats bis zum Letzten Tag des Monats. |
| | Datum (Bereich) | Mit diesem Typ kann eine untere und obere Datums-Grenze angegeben werden (Von+Bis). *Von* oder *Bis* ist bei der Eingabe optional. Wie *Datum* können auch hier reine Jahreszahlen, Jahr+Monat oder Jahr+Monat+Tag eingegeben werden. |
| | Datum + Zeit | Dieser Typ erlaubt bei der Datumseingabe zusätzlich die Eingabe einer Zeit mit Stunden und Minuten. Über die API lassen sich auch Sekunden und Zeitzone (als UTC Offset) speichern. Beim Speichern wird die aktuelle Zeitzone des Browsers des Benutzers gespeichert. |
| *Numerisch* | Zahl (ganzzahlig) | Dieser Typ speichert Zahlen ohne Nachkommastellen. Zahlen können beidseitig trunkiert in der Volltextsuche durchsucht werden |
| | Kommazahl (2 Stellen) | Dieser Typ kann für Geldbeträge genutzt werden und speichert eine Zahl mit zwei Nachkommastellen. |
| *Sonstige* | Datei | In diesem Typ speichert easydb Dateien. Jede Datei kann in verschiedenen Versionen gespeichert werden, so dass intern eine Liste von Dateien gepflegt wird. Eine Datei muss als bevorzugte Datei festgelegt sein. easydb generiert für Dateien Vorschaubilder und bietet für Formate wie Audio und Video Formatumwandlungen an, die ein direktes Anhören und Betrachten im Browser ermöglichen. |
| | Ja/Nein-Feld (Boolesch) | Dieser Typ speichert den Zustand gesetzt oder nicht gesetzt. In der Datenbank wird der Wert standardmäßig auf nicht gesetzt voreingestellt. Im Frontend wird dieser Datentyp als Checkbox dargestellt. |
| *Objekttypen* | Vorhandene Objekttypen | Mit diesem Typ werden sogenannte Vorwärts-Verlinkungen zu anderen Datensätzen angelegt. Intern wird dafür die easydb Datensatz-ID des verlinkten Datensatzes gespeichert. Durch das Vorwärts-Verlinken können die verlinkten Datensätze in den Masken für Ein- und Ausgabe und auch für die Suche berücksichtigt werden. Verlinkte Datensätze werden unabhängig von den verlinkenden Datensätzen eingegeben und gespeichert. Verlinkte Datensätze können jedoch nicht gelöscht werden. |
| *Zusätzliche Datentypen* | | Über Plugins können weitere Datentypen eingebunden und hier ausgewählt werden. |
| Überprüfung | | Eine Überprüfung kann für jedes Datenbankfeld hinterlegt werden und erfolgt bei jedem Speichervorgang. Die Optionen für Überprüfungen können sich je nach Datentyp unterscheiden. |
| | Keine Überprüfung | Bei dieser Einstellung wird keine Überprüfung durchgeführt. easydb akzeptiert alle Werte. Auf technischer Seite wird bei Textfeldern kein Leer-String (""), sondern eine Datenbank *null* gespeichert. Text-Felder werden automatisch getrimmt, d. h. Leerstellen am Anfang und am Ende werden automatisch entfernt. |
| | Nicht leer | Bedeutet es ist ein *Pflichtfeld*. In dieses Feld muss etwas eingetragen werden, vorher kann nicht gespeichert werden. Besteht das Pflichtfeld aus mehreren Feldern für Mehrsprachigkeit, muss obligatorisch nur eine Sprache mit einem Eintrag befüllt werden. |
| | Email | Es wird geprüft, ob es sich bei der Eingabe um eine E-Mail-Adresse handelt. Diese Überprüfung ist eine einfache Überprüfung von Zeichen und keine Garantie dafür, dass es sich um eine valide und zustellbare E-Mail-Adresse handelt. |
| | Regulärer Ausdruck (Regexp) | Ein regulärer Ausdruck prüft die Eingabe nach bestimmten Regeln: [Tcl Advanced Regular Expression](https://www.regular-expressions.info/tcl.html). Der Reguläre Ausdruck besteht aus *Regexp* und *Regexp Flags*. |
| | Datums-Bereich | Bei Datums-Feldern kann ein Datumsbereich hinterlegt werden, jeweils mit einer *Exklusive* Checkbox. |
| | Keine leeren Einträge (*NOT NULL*) | Hier wird in der Datenbank dafür gesorgt, dass das Feld nicht leer bleibt. Siehe unten die [ausführliche Erläuterung](#notnull). |
| | Keine doppelten Einträge | Mit diesem Check sorgt easydb dafür, dass keine doppelten Einträge für dieses Feld vorhanden sind. Ausnahme sind leere Felder, die bei diesem Check nicht berücksichtigt werden. Mit *`UNIQUE(A)`* bis *`UNIQUE(C)`* können UNIQUE-Checks definiert werden, die über mehrere Felder (in dem gleichen Objekttyp) funktionieren. Dabei wird überprüft, dass die Kombination von Eingaben einmalig über alle beteiligten Felder ist. |
| Editierbar in Verlinkung (Reverse Edit) | | Siehe unten die [ausführliche Erläuterung](#reverse-edit). |
| Bidirektional | | Siehe unten die [ausführliche Erläuterung](#bidirectional). |
| Bidirektional Reverse | | Siehe unten die [ausführliche Erläuterung](#bidirectional-reverse). |

### Datentypänderungen von existierenden Feldern {#typechange}

Der Datentyp von existierenden Feldern kann nur zwischen bestimmten Typen geändert werden. Die meisten Änderungen können in der Datenbank nicht sinnvoll verarbeitet werden und sind deshalb nicht erlaubt. Beim Speichern einer neuen Schemaversion werden mögliche Typänderungen geprüft und nicht erlaubte Typänderungen verursachen einen Fehler.

*Ausschließlich* die folgenden Typänderungen sind möglich:

| Alter Datentyp | Erlaubte neue Datentypen | Zusätzliche Änderungen in existierenden Daten |
|---|---|---|
| Einer dieser Typen: <ul><li>Einzeiliger Text<li>Einzeiliger Text (mehrsprachig)<li>Mehrzeiliger Text<li>Mehrzeiliger Text (mehrsprachig)<li>Einfacher Text (String)</ul> | Einer dieser Typen: <ul><li>Einzeiliger Text<li>Einzeiliger Text (mehrsprachig)<li>Mehrzeiliger Text<li>Mehrzeiliger Text (mehrsprachig)<li>Einfacher Text (String)</ul> | <ul><li>Änderungen von einsprachigem zu mehrsprachigem Text: der alte Wert wird für alle Datenbanksprachen im neuen Wert genutzt<li>Änderungen von mehrsprachigem zu einsprachigem Text: der erste nicht leere Wert in der Reihenfolge der Datenbanksprachen wird als neuer Wert genutzt</ul> |
| Einer dieser Typen: <ul><li>Datum<li>Datum (Bereich)<li>Datum + Zeit</ul> | Einer dieser Typen: <ul><li>Einzeiliger Text<li>Einzeiliger Text (mehrsprachig)<li>Mehrzeiliger Text<li>Mehrzeiliger Text (mehrsprachig)<li>Einfacher Text (String)</ul> | Wert wird in der Datenbank in Text umgewandelt. Für mehrsprachige Textfelder wird der Wert für alle Datenbanksprachen genutzt |
| Datum | Datum + Zeit | Die Zeit des neuen Werts ist `00:00:00` |
| Datum | Datum (Bereich) | Der Datumswert wird als Anfang und Ende des Bereichs genutzt |
| Datum + Zeit | Datum | Die Zeit des alten Werts wird verloren gehen |
| Datum + Zeit | Datum (Bereich) | Der Datumswert wird als Anfang und Ende des Bereichs genutzt |
| Zahl (ganzzahlig) | Einer dieser Typen: <ul><li>Einzeiliger Text<li>Einzeiliger Text (mehrsprachig)<li>Mehrzeiliger Text<li>Mehrzeiliger Text (mehrsprachig)<li>Einfacher Text (String)</ul> | Wert wird in der Datenbank in Text umgewandelt. Für mehrsprachige Textfelder wird der Wert für alle Datenbanksprachen genutzt |
| Kommazahl (2 Stellen) | Einer dieser Typen: <ul><li>Einzeiliger Text<li>Einzeiliger Text (mehrsprachig)<li>Mehrzeiliger Text<li>Mehrzeiliger Text (mehrsprachig)<li>Einfacher Text (String)</ul> | Dieser Währungswert wird im kleineren Währungsteil gespeichert, was bedeutet dass der Kommawert mit `100` mutlipliziert in der Datenbank gespeichert wird. Ein alter Wert von `1,56` wird als `156` gespeichert, und der Textwert wird `'156'` sein. Für mehrsprachige Textfelder wird der Wert für alle Datenbanksprachen genutzt |
| Zahl (ganzzahlig) | Kommazahl (2 Stellen) | Der alte Wert wird mit `100` multipliziert und mit zwei Nachkommastellen repräsentiert. Ein alter Wert von `156` wird als `15600` gespeichert und als `156,00` repäsentiert |
| Kommazahl (2 Stellen) | Zahl (ganzzahlig) | Der interne Wert wird nicht umgewandelt, aber mit zwei Nachkommastellen repräsentiert. Ein alter Wert von `156` wird `1.56` repräsentiert |

### Keine leeren Einträge (NOT NULL Constraint) {#notnull}

Ein *NOT NULL Constraint* kann für einfachen Feldern (auf Top Level Ebene und in Mehrfachfeldern), und ebenso auf Mehrfachfelder selbst gesetzt werden. Dabei wird *NOT NULL* unterschiedlich umgesetzt.

Für einfache Felder wird direkt in der Datenbank ein *NOT NULL Constraint* gesetzt. Das bedeutet, dass dieses Feld generell nicht leer sein kann. Dies sorgt u.a. auch dafür, dass ein Datenmodell nicht eingespielt werden kann, wenn ein *NOT NULL Constraint* neu gesetzt wird, und vom betroffenen Objekttyp bereits Objekte existieren, die dieses Constraint verletzen würden.

Im Gegensatz dazu wird das *NOT NULL Constraint* für Mehrfachfelder anders interpretiert: Es muss mindestens einen Eintrag in dieser Tabelle für jedes Objekt geben. Dies wird nur über die Import-API geprüft, also beim Speichern von Objekten. Dies gilt für den Editor, den Gruppeneditor und den JSON Importer.

Das Constraint wird in den folgenden Fällen **nicht** geprüft, so dass hier leere Mehrfachfelder möglich sind:

* Datenmodellaktualisierungen
* Löschen von verlinkten Objekten, die dann ein leeres Mehrfachfeld zurücklassen können

### Editierbar in Verlinkung {#reverse-edit}

Im Gegensatz zum vorwärts Verlinken, wobei eine easydb-ID des verlinkten Datensatzes am Hauptdatensatz gespeichert wird (als Verweis auf diesen Datensatz), wird beim Editieren in der Verlinkung, also beim rückwärts Verlinken, ein Datensatz als Teil eines anderen Datensatzes gespeichert.

```
Objecttype: Subject
Subject-ID    134
Title         Viele Bäume

  ^ Objekttyp: Term
  ^ Term-ID             89
  ^ Term-Subject-ID     134
  ^ Term-Title:         Wald

  ^ Objekttyp: Term
  ^ Term-ID             90
  ^ Term-Subject-ID     134
  ^ Term-Title:         Forest
```

In diesem einfachen Beispiel haben wir zwei Objekttypen angelegt: Subject und Term. Ein Benutzer kann im Subject-Editor an einem Subject mehrere Terms abspeichern. Im Term-Editor kann der vorwärts Link zum Subject genutzt werden, um genau ein Subject zu verlinken. Beim rückwärts Verlinken gehören die verlinkten Datensätze (2 Terms) fest zum Hauptdatensatz (Subject), d.h. wenn das Subject mit nur einem Term neu gespeichert wird, wird der nicht mehr verlinkte Term gelöscht. Beim vorwärts Verlinken würde nur die Verlinkung gelöst, nicht aber der Datensatz selbst. Rückwärts verlinkte Objekte verhalten sich wie Mehrfachfelder, die fest zum Datensatz gehören, können dabei aber auch separat bearbeitet und gesucht werden.

### Bidirektional {#bidirectional}

Beim Speichern von Verlinkungen zwischen zwei Datensätzen entsteht eine Richtung der Verlinkung (vorwärts oder rückwärts). Die Richtung ist entscheidend für die Sichtbarkeit der Datensätze, je nachdem von welcher Seite der Datensatz betrachtet wird. Um es an einem Beispiel zu verdeutlichen, soll Bild 198 mit Bild 166 und Bild 168 verlinkt werden. Beispiel 1: die Verlinkung wird über ein Mehrfachfeld *Andere Bilder* realisiert. Beispiel 2: die Verlinkung wird mit einem separaten Objekttyp *Bild-An-Bild* realisiert.

In beiden Fällen soll nun die Verlinkung von Bild 166 bzw. 168 zum Bild 198 sichtbar sein.

#### Bsp. 1: In einem Mehrfachfeld

Dafür wird im ersten Beispiel das Feld *Andere-Bild-ID* als *Bidirektional* markiert. Damit weiß easydb, dass eine Verlinkung in beide Richtungen funktionieren soll. In der Datenbank werden Einträge für jede Richtung erzeugt, d. h. beim Speichern von Bild 198 werden an den Bildern 166 und 168 jeweils die Mehrfachfeld-Einträge automatisch abgespeichert.

##### Objekttyp: Bild

| Feld | Datentyp | Editierbar in Verlinkung | Bidirektional |
| ------ | ------- | ------ | ---- |
| Titel | Text | | |
| Andere Bilder | Mehrfachfeld | | |
| &#8614; Anderes-Bild-ID | Bild | | X |

##### Daten:

| Bild-ID | Titel | Anderes-Bild-ID | |
| ----- | --- | --- | --- |
| 198 | Test-Bild 1 | 168 | |
| | | 166 | |
| 168 | Test-Bild 1 | 198 | Link in die andere Richtung (automatisch erzeugt) |
| 166 | Test-Bild 1 | 198 | Link in die andere Richtung (automatisch erzeugt) |

#### Bsp. 2: In einem separaten Objekttyp

Im zweiten Beispiel werden im separaten Objekttyp Datensätze, die den Link in die andere Richtung aufbauen, automatisch erzeugt. Durch die Einstellung *Editierbar in Verlinkung* werden die Bild-An-Bild Einträge des verlinken Bildes im Editor des Hauptdatensatzes editiert. Fügt man dort nun zwei Verlinkungen zum Bild 168 und 166 ein, werden automatisch zwei Datensätze für den Link in die andere Richtung geschrieben. Ruft man nun den Editor für Bild 166 bzw 168 auf, erscheint dort als Bild-An-Bild Eintrag die Verlinkung zum Bild 198.

##### Objekttyp: Bild

| Feld | Datentyp |
| --- | --- |
| Titel | Text |

##### Objekttyp: Bild-An-Bild

| Feld | Datentyp | Editierbar in Verlinkung | Bidirektional |
| ------ | ------- | ------ | ---- |
| Bild-From-ID | Bild | X | X |
| Bild-To-ID | Bild | X | X |

##### Daten:

**Objekttyp: Bild**

| Bild-ID | Titel |
| --- | --- |
| 198 | Test-Bild 1 |
| 168 | Test-Bild 2 |
| 166 | Test-Bild 3 |

**Objekttyp: Bild-An-Bild**

| Bild-An-Bild-ID | Bild-From-ID | Bild-To-ID | Bemerkung |
| ---- | --- | --- | ---- |
| 9898078 | 198 | 166 | |
| 9898079 | 198 | 168 | |
| 9898080 | 166 | 198 | Link in die andere Richtung (automatisch erzeugt) |
| 9898080 | 168 | 198 | Link in die andere Richtung (automatisch erzeugt) |

#### Bidirektional Reverse {#bidirectional-reverse}

Die Markierung eines Feldes als *Bidirectional Reverse* sorgt dafür, dass in einem bidirektionalen Kontext vorwärts Verlinkungen mit unterschiedlichen Attributen versehen werden und hierdurch typisierte bidirektionale Links entstehen. Im Falle bidirectional wird somit der Link 1 zu 1 kopiert und im Fall bidirectional reverse erhält der Link unterschiedende Attribut.

Die Einrichtung im Datenmodell ist für Bidirektional und Bidirektional Reverse gleich. In beiden Fällen wird bei der Verlinkung vorwärts auf die gleich Tabelle verwiesen.

> HINWEIS: Bei Einfachfeldern (Top-Level) müssen es zwei vorwärts Links sein, bei Mehrfachfeldern (Nested) reicht ein Link auf den Top-Level Objekttyp.

| objecttype: thing | type | example t1 | example t2 |
| --- | --- | --- | --- |
| id:pkey | primary key, internal | 1 | 2 |

| objecttype: thing_thing | type | example tt1 | example tt2 |
| --- | --- | --- | --- |
| id:pkey | primary key, internal | 12 | 13 |
| thing_from | forward link to thing, bidirectional | 1 | 2 |
| thing_to | forward link to thing, bidirectional | 2 | 1 |
| linktype | forward link to linktype | 8 | 9 |

| objecttype: linktype | type | example l1 | example l2 |
| --- | --- | --- | --- |
| id:pkey | primary key, internal | 8 | 9 |
| linktype_reverse | forward link to linktype, bidirectional_reverse | 9 | 8 |
| description | text | son of | parent of |

Beim Einfügen von *tt1* wird *tt2* automatisch erzeugt. *tt1* enthält als Linktyp *l1*, easydb schreib den Rücklink als *l2* in *tt2*.
