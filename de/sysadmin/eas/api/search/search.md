#  EAS-API: /search

##  Beispiel

~~~
http://eas.example.com/eas/search/keyword?instance=example&type.extension=jpg
http://eas.example.com/eas/search/keyword/ids?instance=example&type.width=RANGE(100,1000)
~~~


##  Parameter


|---|---|
|`instance`          |Name der Zielinstanz|
|`parent_id`         |Suche nach Kindern des mit dieser ID angegeben Assets|
|`*.*`               |Suchfeld und -wert für die Suche|

##  Erweiterte Suchfunktionen

Im Suchwert werden verschiedene Funktionen unterstützt, die die Suche beeinflussen. Pro Suchwert kann dabei nur eine Funktion verwendet werden.

Aus Effizienzgründen legt der EAS die Werte für alle Schlüsselwörter in drei verschiedenen Tabellen ab, um ein Ergebnis zu bekommen muss oft in der richtigen Tabelle gesucht werden. Ohne Angabe einer Suchfunktion wird nach Äquivalenz in Textfeldern gesucht.

|---|---|
|`int`|Ganzzahlen|alle ganzzahligen Werte|
|`text`|Text|kurze Zeichenketten, die keine Leerzeichen enthalten|
|`text_full`|Volltext|alle restlichen Zeichenketten|

Folgende Funktionen stehen zur Auswahl:

|---|---|
|`RANGE([<start>],[<end>])`|Bereichssuche auf Ganzzahlfeldern. Diese Funktion muss vor *(version)EAS 4.2.30* auch bei Äquivalenzsuche auf Zahlfeldern verwendet werden. Beispiele:|
type.colordepth=RANGE&#40;8,8)         |   # Farbtiefe genau 8 Bit|
type.height=RANGE&#40;,1000)           |   # Höhe bis 1000|
type.width=RANGE&#40;200,)             |   # Breite ab 200|
type.pages=RANGE&#40;4,8)              |   # zwischen 4 und 8 Seiten|
|`INT(<value>)`|Äquivalenzsuche auf Zahlfeldern ab *(version)EAS 4.2.30*. Beispiele:|
|type.height=INT&#40;1080)      |               # Höhe genau 1080|
|`REGEXP(<regexp>)`|Suche mit regulärem Ausdruck in Textfeldern. Beispiele:|
|type.fileclass=REGEXP&#40;^&#40;audi&#124;vide)o$)| # Fileclass "audio" oder "video"|
|`INLIST(<item1>[;<item2> ...])`|Äquivalenzsuche in Textfeldern nach verschiedenen Suchbegriffen. Mindestens ein Begriff muss gefunden werden (ODER-Verknüpfung). Beispiele:|
|type.extension=INLIST&#40;ppt;pptx;doc;docx)|  # Dateiendung eine aus der Liste|
|Achtung: das Semikolon ist ein reserviertes Zeichen innerhalb des HTTP-Query-Strings; es muss also URL-kodiert werden (%3b).||
|`FULLTEXT(<word>)`|Suche in Volltextfeldern (momentan `LIKE '%<word>%'`). Beispiele:|
|metadata.IPTC::ApplicationRecord.IPTC:Caption-Abstract=FULLTEXT&#40;Ente)|  # in der Bildbeschreibung nach Ente suchen|
|`FULLTEXTEXT(<word>)`|Wie `FULLTEXT()`, es wird aber auch in Textfeldern gesucht|




