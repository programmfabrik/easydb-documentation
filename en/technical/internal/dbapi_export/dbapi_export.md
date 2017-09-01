# dbapi_export

Für jede Maske und Version werden sog. "bare objects" exportiert und in ez_object_cache gecached. Bare objects enthalten keine linked objects, nur deren IDs. Das gleiche
gilt für verlinkte User, Gruppen und Pools.

Wenn ein Objekt exportiert wird, werden rekursiv die entsprechenden bare objects geladen - d.h. gesucht und wenn nicht gefunden, erzeugt und abgelegt - und das
Objekt wird zusammengebaut.

Beim Zusammenbauen werden:

- Felder gelöscht, die nicht zum Format passen
- Felder gelöscht, je nachdem ob das Objekt für den Index oder für den Client ist
- User und Gruppen ergänzt: Changelog, Owner (*)

(\*) Base-Objekte könnten auch als Datei abgelegt werden. Sie werden aber schon schnell bearbeitet. Man müsste sehen, ob es sich lohnt. Bereits generierte Base-Objekte werden
für die ganze Operation gecacht. Also, wenn beispielsweise der Owner im Changelog auftaucht, was normalerweise der Fall ist, wird er nur einmal generiert.

## Bare objects

### Meta-Info

Im Feld `_meta` befinden sich Infos für das Zusammenbauen von bare objects:

- Standard
- Move-To-All

#### Standard

Das Feld `_meta._standard` markiert, in wie weit Standard fertig ist oder noch mehr Information braucht, und enthält die nötigen Informationen, um "_standard" zu bauen,
falls nötig:

- Die Felder `text` uns `eas` nehmen folgende Werte an:

- "full": `_standard.text` bzw. `_standard.eas` ist vollständig, d.h. alle Infos, die das Objekt braucht, um Standard zu bauen, befinden sich im Objekt selbst
- "1": `_standard.text.1` bzw. `_standard.eas.1` ist vollständig, aber die anderen nicht
- "none": `_standard.text` bzw. `_standard.eas` fehlt komplett

- Das Feld `value` enthält eine JSON-Darstellung vom StandardResult, wobei bei LinkedObjects mask-ID und Object-ID gespeichert sind.

Wenn ein Objekt als Hauptobjekt gebaut wird und `_standard` "full" ist, muss der Server nichts mehr machen.
Wenn das Objekt ein Standard braucht (d.h. nicht "short"), müssen die Werte für Standard rekursiv gesammelt werden.

Wenn ein Objekt als LinkedObject gebaut wird und `_standard` "1" ist, muss der Server nichts mehr machen.

#### Move-To-All

Die Felder `_move_to_all_full` und `_move_to_all_standard` enthalten Werte, die direkt in `_all` geschrieben werden müssen, weil sie in fulltext gebraucht werden,
aber nicht in einem mit `copy_to_all` indizierten Feld sind.

Die Felder aus `_move_to_all_full` müssen nach `_all` kopiert werden, wenn das Objekt in einem fulltext-Kontext ist.

Wenn das Objekt in der Standard-Darstellung oder gar nicht gerendert wird, sollten auch die Werte aus `_move_to_all_standard` kopiert werden. Das betrifft Objekte im
Pfad und unsichtbare Linked Objects.

## Cache-Invalidierung

Der Cache ist am Anfang leer. Bei neu angelegten Objekten muss nichts besonderes gemacht werden.

Der Cache muss beim Bearbeiten bzw. Löschen invalidiert werden (siehe unten).

Darüber hinaus muss der Cache invalidiert werden, wenn eine Neuindizierung erforderlich ist, d.h. wenn das Base-Schema, das User-Schema oder die Index-Version
sich ändern.

### Objekt bearbeiten ###

Wenn ein Objekt bearbeitet wird, muss der Cache für das Objekt selbst geleert werden.
a die Version hochgezählt wird, ist das nicht unbedingt nötig, aber es ist gut, alte Dokumente aus dem Cache zu entsorgen.

Darüber hinaus müssen weitere Objekte invalidiert werden, deren Versionen sich nicht geändert haben:

#### Hierarchische Objekttypen:

Bei hierarchischen Objekttypen muss der Vater invalidiert werden. Wenn die Hierarchie noch rückverlinkt ist, müssen
alle Ahnen invalidiert werden.

Alle Nachfahren müssen invalidiert werden.

#### Rückverlinkte Objekte

Während ein bare object berechnet wird, werden alle rückverlinkte links gesammelt und in "ez_object_cache:dependencies" gespeichert.
Wenn ein Objekt bearbeitet wird, werden alle betroffene Objekte über diese Tabelle invalidiert, und zwar rekursiv.







