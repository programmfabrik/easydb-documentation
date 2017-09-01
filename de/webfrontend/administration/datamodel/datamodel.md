# Datenmodell

Beim Datenmodell kann das aktuellen Datenmodell <code class="tab">Aktuell</code> und wenn Zugriffrecht besteht die Entwicklungsversion <code class="tab">Entwicklung</code> angezeigt werden. Mit `Änderungen aktivieren`{.button} können Änderungen, die in der Entwicklungsversion vorgenommen wurden, übernommen werden. Hierdurch wird die aktuelle Version überschrieben.

> HINWEIS: Beachten Sie, dass dieser Vorgang serverseitig sehr viel Aktivität in Gang setzt, u.a. ein komplettes Neu-Indizieren aller Datensätze. Bis zur vollständigen Neu-Indizierung finden Benutzer ggfs. Datensätze im alten Format vor. In manchen Fällen, kann es auch passieren, dass von Änderungen betroffene Datensätze Benutzern nicht angezeigt werden, bis die Neu-Indizierung abgeschlossen ist.

Im Datenmodell werden Objekttypen und Masken definiert. Objekttypen beschreiben die Struktur der Daten in der Datenbank. Masken beschreiben die Aus- und Eingabesicht auf die Objekttypen und somit die Datensätze. Sind beispielsweise für einen Objekttyp insgesamt 20 Feldern definiert, können über Maskes unterschiedliche Feldkombinationen ausgegeben werden. Benutzer 1 könnte mit dem Recht auf Maske 1 z.B. 5 dieser Felder erhalten. Nutzer 2 könnte mit Maske 2 z.B. 5 andere Felder erhalten und mit  Maske 3 wiederum 15 Felder sehen.

* [Objekttypen](objecttype/objecttype.md)

* [Masken](mask/mask.md)

