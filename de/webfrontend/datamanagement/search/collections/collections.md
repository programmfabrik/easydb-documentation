# Schnellzugriff

Über den Schnellzugriff werden Zusammenstellungen von Datensätzen verwaltet. Das sind zum einen dynamische Mappen, wie gespeicherte Suchen und ad hoc Mappen für tagesaktuell bearbeitete Datensätze. Und zum anderen manuelle Zusammenstellungen, wozu eigene und freigegebene Mappen zählen. Mit <code class="button"> < </code> kann der Schnellzugriff ein- und ausgeblendet werden.

## Übersicht im Schnellzugriff

![Mappen](finder.png)

easydb bietet im Schnellzugriff folgende Speicheroptionen an:

|Mappe|Untergeordnet|Erklärung|
|--|--|--|
|<i class="fa fa-search"></i> Suche||Entsprich der aktuellen Anzahl von Datensätzen, die Ihnen in easydb zur Verfügung steht. Aus einer Mappe gelangen Sie über diesen Weg wieder direkt in der Hauptsuche. Die Zahl links zeigt die Anzahl |
||<i class="fa fa-search"></i> Heute bearbeitet|Enthält die von Ihnen heute bearbeiteten Datensätze. Hierfür wird das aktuelle Tagesdatum verwendet, d.h. 0:00 bis 23:59 des aktuellen Tages. Für komplexere Suchen, die zeitlich weiter zurückgehen, kann eine Abfrage der [Änderungshistorie](../../features/datatypes/datatypes.html#changelog-search) in der [Expertensuche](../../search/search.html#expert) durchgeführt werden.|
||<i class="fa fa-search"></i> Erstellt|Die heute von Ihnen erstellten Datensätze.|
||<i class="fa fa-search"></i>Geändert|Die heute von Ihnen geänderten Datensätze.|
|<i class="fa fa-search"></i> Gespeicherte Suchen||Die Treffer einer Suche können über das Optionen-Menü unter <i class="fa fa-floppy-o"></i> gespeichert und an dieser Stelle wieder erneut aufgerufen werden. Diese Mappe ist dynamisch. Hier werden alle Datensätze gezeigt, die für die Kriterien der gespeichert Suche passen.|
|<i class="fa fa-file-o"></i> Kategoriebrowser||Wenn aktiviert, erscheinen hier Listen von Nebenobjekttypen, über die ein schneller Zugriff auf verknüpfte Datensätze möglich ist. Der Kategoriebrowser ist eine Filtermethode, die als Schnellzugriffsvariante dient und entsprechend der Eingabe über die Expertensuche agiert. |
|Meine Mappen|| Vom Benutzer angelegte Zusammenstellungen von Datensätzen. |
|Freigegebene Mappen|| Zusammenstellungen von Datensätzen, die von anderen Benutzern freigegeben wurden. Es gelten die Berechtigungen an der Mappe, die der Ersteller zugewiesen hat.|

## Suchen im Schnellzugriff
![Suche nach Mappen](finder_suche.jpg)

Über das Suchfeld kann der Schnellzugriff nach Einträgen durchsucht werden. Durchsucht werden die Bezeichnungen der gespeicherten Suchen, der Einträge aus dem Kategoriebrowser sowie der Mappen (nicht aber die verknüpften Datensätze). Die Ergebnisse im Schnellzugriff werden zeigen nur übereinstimmende Einträge an. Nicht passende Einträge werden ausgeblendet. Die Übereinstimmungen für Mappen werden zusätzlich farbig hervorgehoben.

