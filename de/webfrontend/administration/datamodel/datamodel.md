# Datenmodell

Beim Datenmodell kann das aktuellen Datenmodell <code class="tab">Aktuell</code> und wenn Zugriffsrecht besteht die Entwicklungsversion <code class="tab">Entwicklung</code> angezeigt werden. Mit <code class="button">Änderungen aktivieren</code> können Änderungen, die in der Entwicklungsversion vorgenommen wurden, übernommen werden. Hierdurch wird die aktuelle Version überschrieben.

> HINWEIS: Beachten Sie, dass dieser Vorgang serverseitig sehr viel Aktivität in Gang setzt, u.a. ein komplettes Neu-Indizieren aller Datensätze. Bis zur vollständigen Neu-Indizierung finden Benutzer ggfs. Datensätze im alten Format vor. In manchen Fällen, kann es auch passieren, dass von Änderungen betroffene Datensätze Benutzern nicht angezeigt werden, bis die Neu-Indizierung abgeschlossen ist.

## Definition von Feldern

Im Datenmodell werden Objekttypen und Masken definiert. Objekttypen beschreiben die Struktur der Daten in der Datenbank. Masken beschreiben die Aus- und Eingabeansicht auf die Objekttypen und somit die Datensätze. Sind beispielsweise für einen Objekttyp insgesamt 20 Feldern definiert, können über Masken unterschiedliche Feldkombinationen ausgegeben werden. Benutzer 1 könnte mit dem Recht auf Maske 1 z. B. 5 dieser Felder erhalten. Nutzer 2 könnte mit Maske 2 z. B. 5 andere Felder erhalten und mit  Maske 3 wiederum 15 Felder sehen.

* [Objekttypen](objecttype/objecttype.html)

* [Masken](mask/mask.html)

> HINWEIS: Über die [Feldrechte](../../rightsmanagement/objecttypes/objecttypes.html#fieldrights) am Objekttyp ist es möglich einzelne Felder für bestimmte Benutzer oder Gruppen auszublenden und die Ansicht eines Objekttyps und entsprechender Masken zu verfeinern.  

## Datenmodell exportieren/importieren

easydb bietet die Möglichkeit das Datenmodell der easydb Instanz herunterzuladen und es als JSON-Datei zu sichern oder wiederzuverwenden. Der Export enthält die Konfiguration aller Objekttypen und dazugehöriger Masken.

Ebenfalls ist es möglich ein extern gesichertes Datenmodell in easydb zu importieren. 

Der Download und Uplaod des Datenmodells wird im Hauptmenü über das Datenmodell erreicht und ist unterhalb der Liste der Objekttypen in der Entwicklungsumgebung über das <i class="fa fa-cog"></i>-Menü zu finden. 

![](datamodel_load_de.jpg)

Ein bestehendes Datenmodell kann zurückgesetzt werden. In dem Fall werden alle Objekttypen und dazugehörigen Masken gelöscht.

## Datenmodellgrafik

Über das Auswahlmenü in den Bearbeitungsoptionen besteht die Möglichkeit die Strukturen des Datenmodells zu visualisieren. Das aktuelle Datenmodell kann dazu als svg-Grafik heruntergeladen werden.

![Grafikausgabe des Datenmodells](svg_datamodel.jpg)