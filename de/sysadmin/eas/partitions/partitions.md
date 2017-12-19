> Die Pfadangaben beziehen sich auf Pfade im Container, nicht auf Pfade direkt auf Ihrem Server, der den docker-Container ausführt.

EAS-Partitionen
===============

Der EAS unterstützt mehrere sogenannte Partitionen. Diese werden in der
Datenbank verwaltet und durch folgende Eigenschaften spezifiziert:

-   eindeutiger Pfad
-   Einstellung, ob Originale, abgeleitete Originale bzw. Versionen
    gespeichert werden
-   außerdem: weitere Filter, Priorität

Auswahl der Zielpartition
=========================

Ausschlaggebend für die Auswahl der Zielpartition für eine Datei sind
o.g. Filter. Bleibt nach der Filterung mehr als eine Partition übrig,
wird zufällig eine ausgewählt.

Wenn zu wenig Platz auf dem unterliegenden Dateisystem zur Verfügung
steht wird die Partition automatisch deaktiviert. Die Grenze wird durch
[EAS\_PARTITION\_MIN\_FREE](../conf/conf.html##eas-partition-min-free) festgelegt. Sollten alle
gültigen Partitionen deaktiviert worden sein (`disabled = true` in der
Datenbank, siehe unten), müssen diese nachdem Platz geschaffen wurde
manuell wieder aktiviert werden.

Dateisystem-Layout
==================

Standardpartitionen liegen in `/var/opt/easydb/lib/eas/assets`. Werden
neue Partitionen in der Datenbank angelegt, werden sie beim Neustart des
Workers automatisch angelegt, sofern die Berechtigungen im
übergeordneten Verzeichnis ausreichend sind.

Für das Ausliefern über den Apache werden die Partitionen außerdem mit
ihrer ID in `/var/opt/easydb/lib/eas/partitions` verlinkt, in einer
Standardinstallation sieht das dann so aus:

    /var/opt/easydb/lib/eas/partitions/1 -> /var/opt/easydb/lib/eas/assets/orig
    /var/opt/easydb/lib/eas/partitions/2 -> /var/opt/easydb/lib/eas/assets/dest

Die symbolischen Links werden ebenfalls vom EAS-Worker verwaltet und bei
Bedarf angelegt bzw. geändert.

Anlegen neuer Partitionen
=========================

Momentan gibt es noch kein Werkzeug zum Anlegen neuer Partitionen, es
können aber auf Datenbankebene weitere Partitionen in die Tabelle
`eas.partition` eingetragen werden.

Diese Tabelle hat folgende Spalten:

  ---------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `partition`            ID (wird von PostgreSQL verwaltet)
  `partition_name`       eindeutiger Name der Partition
  `path`                 eindeutiger Pfad zur Datenablage
  `priority`             Priorität der Partition (Vorgabe `0`, je höher, desto unwichtiger)
  `store_original`       für “Originale” (hochgeladene Dateien)
  `store_derived`        für “abgeleitete Originale” (z.B. gedrehte Bilder)
  `store_version`        für “Versionen” (z.B. verschiedene Größen)
  `all_versions`         alle Versionen (Unterscheidung über Versionnamen) dürfen abgelegt werden (Vorgabe: `true`). Wenn `false`, wird die Link-Tabelle `eas.partition__version` verwendet.
  `all_classes`          alle Typklassen (`image`, `office`, etc.) dürfen abgelegt werden (Vorgabe `true`). Wenn `false`, wird die Link-Tabelle `eas.partition__fileclass` verwendet.
  `all_instances`        Assets aller Instanzen dürfen abgelegt werden (Vorgabe: `true`). Wenn `false`, wird die Link-Tabelle `eas.partition__instance` verwendet.
  `disabled`             Vorgabe `false`. Wenn `true` wird die Partition nicht benutzt. Dieses Flag wird auch automatisch gesetzt, wenn der freie Platz auf der Partition zu gering wird.
  `space_used`           verbrauchter Platz in Bytes (wird automatisch befüllt)
  `space_free`           freier Platz in Bytes (wird automatisch befüllt)
  `auto_disabled_time`   Zeit der automatischen Deaktivierung (wird automatisch befüllt, ab EAS 4.2.18)
  ---------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Reaktivieren von automatisch deaktivierten Partitionen
======================================================

Ist auf dem zugrundeliegenden Dateisystem wieder Platz geschaffen
worden, kann eine automatisch deaktivierte Partition nur durch Eingriff
in die Datenbank wieder aktiviert werden. Dazu verbinden Sie sich mit
den PostgreSQL-Kommandozeilen-Client `psql` zur
EAS-Datenbank, mit dem Nutzer **eas** und dem Datenbanknamen **easdb**
wäre der Aufruf z.B.:

    psql -U eas easdb

Anschließend führen Sie bitte das folgende SQL-Statement aus, ausgehend
davon, dass die zu aktivierende Partition **orig** heißt.

    UPDATE eas.partition SET disabled = false WHERE partition_name = 'orig';

Wenn Sie die Standardinstallation benutzen, werden die beiden
ursprünglich angelegten Partitionen auf dem selben Dateisystem liegen,
also auch gleichzeitig deaktiviert werden. Wiederholen Sie in diesem
Fall das obige Statement für den Partitionsnamen **dest**.
