# Links / Deep Links

Einzelne und mehrere Datensätze oder Dateien können in easydb per Link / Deep Link geteilt und freigegeben werden. Links / Deep Links sind in easydb an mehreren Stellen verfügbar.

## Suche

Sie können in easydb eine **Suche** über eine einfache Sucheingabe oder über die Expertensuche durchführen und die Treffer dieser Suche per Link teilen. Für diesen Link können keine besonderen Berechtigungen konfiguriert werden.

![Link zur Suche](link_search.png)

> Hinweis: Mit http://picshare.5.easydb.de/search/<suchwort> kann auch direkt eine Volltext-Suche gestartet werden.

**Gespeichert Suchen** können aus dem Schnellzugriff mit Benutzern und Gruppen geteilt und freigegeben werden. Über das Kontextmenü im Schnellzugriff wird die Freigabe konfiguriert. Im Tab <code class="tab">Teilen</code> können Benutzer und vorderfinierte oder eigene Berechtigungen (<i class="fa fa-bars"></i> Optionen) angelegt werden. Im Tab <code class="tab">Allgemein</code> können der Name der Mappe geändert und eine Beschreibung der Mappe angepasst werden.

![Link zu gespeicherter Suche](link_safed_search.png)

> HINWEIS: Beachten Sie, dass Sie die Einstellungen erst speichern müssen, um den Link anschließend teilen zu können.


## Pool

Über den <i class="fa fa-info-circle"></i> (Teilen-Button) in der Pool-Auswahl kann ein Link zum Pool und somit zu allen Datensätzen, die sich in diesem Pool befinden, aufgerufen und kopiert werden. Für diesen Link können keine besonderen Berechtigungen konfiguriert werden.

![Link zu den Datensätzen eines Pools](link_pool.png)

## Detailansicht / Editor {#sidebar}

Über den <i class="fa fa-share"></i>-Button in der Detailansicht kann ein Link zum **Datensatz** erzeugt werden. Der Weblink führt zum Datensatz in easydb. Der Deep-Link führt, wenn eingerichtet, zur Ausgabe des Datensatzes im XML Format. Wenn nicht anders angegeben, zeigt der Link die aktuellste Version des Datensatzes an. Unter Angabe der Version durch **version/< zahl >** kann auch eine ältere Version über den Link angesprochen werden. Weitere Optionen können der technischen Dokumentation zu [Deep Links](https://docs.easydb.de/en/technical/api/objects/objects.html) entnommen werden. Besondere Berechtigungen können für diese Art von Link nicht konfiguriert werden.

> HINWEIS: Wird beim Klick auf den Teilen-Button gleichzeitig `Strg` odr `Alt` gedrückt, wird für die Deep-Link-Url zu /api/objects eine Url mit der aktuellen Session erzeugt. Damit können zu Testzwecken Datensätze erreicht werden, die für den Deep-Link-User nicht oder noch nicht freigegeben sind.

![Link zum Datensatz](link_detail_asset.png)

Über das Optionen-Menü <i class="fa fa-ellipsis-v"></i> neben dem Dateifeld kann der Link zur **Datei** versendet werden. Diese Option ist aus der Detailansicht und dem Editor erreichbar. Die Links werden entsprechend der vorkonfigurierten Versionen und Formate erzeugt. Für diesen Link können keine besonderen Berechtigungen konfiguriert werden.

![Link aus Detailansicht zur Datei](link_detail_file.png)

> HINWEIS: Diese Links können aus der Detailansicht und dem Editor generiert werden.

Die Freigaben der Links erfolgen mit dem Deep-Link-Benutzer. Sollten einige URLs hier als nicht verfügbar erscheinen, liegt das daran, dass diese nicht freigegeben sind. Hinweise zum Einrichten von Deep Links sind unter [Basiskonfiguration](../../../administration/base-config/base-config.html) und im Rechtemanagement unter [Systemrechten](../../../rightsmanagement/rightsmanagement.html) zu finden.


## Mappen

Mappen können über das Kontextmenü im Schnellzugriff oder den <i class="fa fa-share"> </i> über der Detailansicht für die Mappe mit Benutzern/Gruppen geteilt und freigegeben werden. Im Tab <code class="tab">Teilen</code> können Benutzer und vordefinierte oder eigene Berechtigungen (<i class="fa fa-bars"> </i> Optionen) angelegt werden. Im Tab <code class="tab">Allgemein</code> können der Name der Mappe und die Beschreibung der Mappe angepasst werden. Im Tab <code class="tab">Hochladen</code> kann das Hochladen von Assets in diese Mappe aktiviert werden.

![Mappe freigeben und teilen](link_collection.png)

> HINWEIS: Eine freigegebene oder geteilte Mappe ist durch dieses Icon ![shared](collection_shared.png) auf der Mappe gekennzeichnet.

## Listen

Aus den Listen kann ein Link zum Datensatz erzeugt werden. Wird der Datensatz eines Objekttyps in der Detailansicht geöffnet, kann über den <i class="fa fa-share"></i>-Button ein Link zum **Datensatz** erzeugt werden. Der Weblink führt zum Datensatz in easydb. Für diesen Link können keine besonderen Berechtigungen konfiguriert werden.

![Link zu Datensatz aus Liste](link_list_keyword.png)

