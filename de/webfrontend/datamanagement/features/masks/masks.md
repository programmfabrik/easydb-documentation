# Masken

Masken dienen dazu, die Veränderbarkeit und Sichtbarkeit von Feldern und Datensätzen zu steuern und zu kontrollieren. Eine ausführliche Beschreibung ist unter [Administration > Masken](administration/datamodel/mask/mask.html) zu finden.

Für die Anzeige von Feldern und Datensätzen muss mindestens eine Maske definiert werden. Dies ist die **Standard-Maske**. Es ist möglich mehrere unterschiedliche Masken zu definieren und einem Objekttyp zuzuweisen.

## Maskenfilter

Wenn einem Objekttyp neben der Standard-Maske weitere Masken und Tags zugewiesen sind, ist es möglich deren Verfügbarkeit über Filter zu steuern. Die Einstellung dafür wird unter Objekttypen-Konfiguration im Reiter "Ein- und Ausgabe" vorgenommen.

Anwendungsbeispiel: dem Objekttyp "Dokument" sind die Masken "Intern" (als Standard-Maske festgelegt) und "Extern" zugewiesen. Für den Objekttyp werden außerdem Tags definiert. Ein Tag heißt "freigegeben". Dieser Tag erhält eine Filterfunktion und aktiviert die Maske "Extern". Nur wenn ein Objekttyp mit diesem Tag gekennzeichnet wird, kann er mit der Maske "Extern" angezeigt werden. Ohne den Tag wird der Objekttyp nur mit der Standard-Maske "Intern" angezeigt.

## Masken-Präferenz

Für Masken kann eine **Reihenfolge** festgelegt werden. Damit wird die Präferenz der Masken ausgedrückt.

Bei Objekttypen, die nicht über Pools verwaltet werden, wird die Reihenfolge im Einstellungsbereich für das Datenmodell im Reiter "Ein- und Ausgabe" gesetzt.

Bei Objekttypen, die über Pools verwaltet werden, lässt sich diese Konfiguration auf Ebene der Pools vornehmen. Dies kann links in der Navigation auf übergeordneter Ebene für "Alle Pools" vorgenommen werden oder pro Pool, indem ein Pool ausgewählt wird. Im Reiter "Masken" ist die Liste von Objekttypen zu finden. Zu jedem Objekttyp sind daneben die Masken gelistet. Durch das Aktivieren der Checkbox, wird die Konfiguration des übergeordneten Pools übernommen. Ist die Checkbox nicht aktiv, kann Sie überschrieben werden. Dabei kann die Reihenfolge der Masken geändert oder aber Masken sogar ganz ausgeblendet werden. Unterhalb jeder Masken-Liste befindet sich eine waagerechte Linie. Auch die Position dieser Linie kann geändert werden. Masken, die sich oberhalb der Linie befinden, werden indiziert und somit dem Nutzer für den Pool angezeigt. Masken, die unterhalb der Linie liegen, werden nicht indiziert und dem Nutzer demnach für den Pool nicht angezeigt.

## Rechtemanagement und präferierte Maske

Über das [Rechtemanagement](../../rightsmanagement/rightsmanagement.html) kann die Verfügbarkeit der Masken für Nutzer gesteuert werden.

Die Steuerung über Tagfilter und Masken-Konfigurationen für Pools hat jedoch Priorität vor dem Rechtemanagement. Das bedeutet, dass die Zuweisung der Verfügbarkeit einer Maske für einen Nutzer unwirksam bleibt, wenn für die Maske Tagfilter oder Masken-Konfigurationen am Pool wirksam sind, mit denen die Maske nicht angezeigt wird.

Bei dem o. g. Beispiel der Masken "Intern" und "Extern" für den Objekttyp "Dokument" kann das wie folgt aussehen:

    Benutzer "Gast" hat `mask`-Recht für "Extern"
    Benutzer "Bearbeiter" hat `mask`-Recht für "Extern" und "Intern"

Wird für den Datensatz A der Tag "freigegeben" gesetzt und für den Datensatz B nicht, dann verhält es sich folgendermaßen:

    "Gast" sieht nur A (Maske "Extern")
    "Bearbeiter" sieht A (beide Masken) und B (nur "Intern")

Stehen einem Nutzer mehrere Masken zur Verfügung, steht die präferierte Maske an erster Stelle in der Auswahl. Die Präferenz und somit die Reihenfolge der Masken-Auswahl, wird durch die Konfiguration an den Objekttypen und Pools vorgenommen (siehe „Masken-Präferenz“). Wird keine Anpassung der Reihenfolge vorgenommen, steht die Standard-Maske an präferierter Stelle.

Die Zuweisung "Standard-Maske" ist eine Eigenschaft für Masken, die über das Rechtemanagement vergeben wird. Dieses Merkmal ist nicht singulär, sondern kann gleichzeitig auf mehrere Masken zutreffen. Wird einem Nutzer, der Zugriff auf mehrere Objekttypen/Pools hat, das Recht  "Standard-Maske" zugewiesen, bedeutet das, er sieht die jeweils präferierte Maske für einen Objekttyp oder einen Pool. Es handelt sich um ein dynamisches Recht. Wird die Konfiguration der Maske am Objekttyp oder Pool geändert, sieht der Nutzer eine andere Maske, obwohl sich sein Recht "Standard-Maske" nicht geändert hat.

Die Treffer der Suche werden mit der präferierten Maske angezeigt. In der Detail-Ansicht kann der Nutzer zwischen den verschiedenen Masken wechseln, die ihm zur Verfügung stehen.
