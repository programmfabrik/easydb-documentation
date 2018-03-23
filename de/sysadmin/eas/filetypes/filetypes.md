# Unterstützte Dateitypen {#unterstützte-dateitypen.top}


Der EAS kann <b>alle</b> Dateitypen vereinnahmen, unterstützt aber Vorschauen ( Thumbnails / Previews ) und Metadaten für folgende Formate:

## IMAGE

Bilder werden gut unterstützt. Grundlegende Unterstützung wird durch [ImageMagick](http://imagemagick.org/) bereitgestellt, für Anmerkungen zu einzelnen Formate kann die [Liste der unterstützten Formate](http://imagemagick.org/script/formats.php) herangezogen werden. Im EAS muss das Format allerdings auch bekannt sein, um als Bild (IMAGE) erkannt zu werden.

Die Unterstützung der Raw-Formate (dazu zählen **cr2**, **crw**, **nef**, **orf**, **raw** und teilweise **tiff**) ist von [dcraw](http://www.cybercom.net/~dcoffin/dcraw/) abhängig.

Sehr rudimentär werden Vektorformate in dieser Klasse verarbeitet. Dazu zählen **ai** und **eps**. Weitere Vektor-Grafikformate werden momentan nicht unterstützt.

Wenn die Unterstützung nicht gut ( **+++** ) ist, dann gibt es entweder einzelne Problemdateien (**++**) oder es gibt für das Format allgemein noch kleinere, bekannte Probleme (**+**).

|Extension|Umfang der Unterstützung|
|--|--|
|ai|+|
|bmp|+++|
|crw||
|cr2|+|
|eps|+|
|gif|+++|
|jpeg, jpg|+++|
|jp2|++|
|nef|+|
|orf|+|
|png|+++|
|ppm||
|psd|++|
|raw|+|
|tif, tiff|++|
|wmf||

## VIDEO

Videos werden durch [ffmpeg](http://ffmpeg.org/) verarbeitet. Dabei
können Vorschaubilder (IMAGE) oder wieder Videos in anderen Formaten und Größen
erstellt werden.

Zur Darstellung im Browser wird aus dem Video üblicherweise eine
FLV-Version erzeugt, die im integrierten Video-Player abgespielt werden
kann.

Die folgende Liste enthält die unterstützten Container-Formate. Diese
können die Nutzdaten wieder in unterschiedlichen Audio- und Video-Codecs
enthalten. Hierbei werden alle Codecs der installierten ffmpeg-Version
unterstützt. Ein Anhaltspunkt liefert die ffmpeg-Dokumentation für
[Audio](http://ffmpeg.org/general.html#Audio-Codecs)
und [Video](http://ffmpeg.org/general.html#Video-Codecs) Codecs, unten
werden die getesteten Audio- und Video-Codecs aufgelistet.

### Unterstützte Container-Formate

|Extension|Beschreibung|
|--|--|
|avi|AVI|
|flv|Flash Video|
|mov|QuickTime Video|
|mpg, mpeg|MPEG 1/2 PS/TS|
|mp4|ISO MPEG4|
|ogg, ogv|Ogg|
|rm |Real Media|
|ts||
|wmv||

### Getestete Video- und Audio-Codecs

|Video(V) / Audio(A)|Beschreibung|
|--|--|
|V|           FLV|
|V|           H.264|
|V|           MPEG 1|
|V|           MPEG 2|
|V|           MPEG 4|
|V|           Ogg Theora|
|V|           WMV1|
|V|           WMV3|
|A|           AAC|
|A|           AC3|
|A|           ADPCM|
|A|           MPEG Layer 2|
|A|          MPEG Layer 3|
|A|           Ogg Vorbis|
|A|           WMAv2|
|A|           WMA Voice|

## AUDIO

Die Behandlung von Audio-Dateien ist sehr ähnlich der von Videos. Auch
hier wird zur Anzeige im Browser üblicherweise eine FLV-Version erzeugt.
Durch eine Limitierung im Format ist es aber momentan nicht möglich, im
integrierten Video-Player innerhalb dieser FLVs bestimmte Zeiten
anzuspringen.

Momentan werden die folgenden Formate unterstützt:

|Extension|Beschreibung|
|--|--|
|flac     |   Free Lossless Audio Codec|
|mp3     |    MPEG Layer 3|
|m4a||
|wav     |    RIFF WAVE|
|wma     |    Windows Media Audio|

Da es sich hierbei meist um Containerformate handelt, kann es im
Einzelfall auch dazu kommen, dass sie nicht unterstützte Audio-Codecs
enthalten.

## OFFICE

Die Verarbeitung der meisten Office-Formaten erfolgt durch [OpenOffice.org](http://de.openoffice.org/).

### Textverarbeitungsformate

|Extension|Beschreibung|
|--|--|
|doc    |     MS Word|
|docx   |     MS Word 2003*|
|odt    |     OOo 2.x* Writer|
|ott    |     OOo 2.x+ Writer|
|rtf    |     Rich Text Format|
|sxw    |     OOo 1.x Writer|

### Tabellenkalkulationsformate

|Extension|Beschreibung|
|--|--|
|ods    |     OOo 2.x+ Calc|
|ots    |     OOo 2.x+ Calc|
|sxc    |     OOo 1.x Calc|
|xls    |     MS Excel|
|xlsx   |      MS Excel 2003+|

### Präsentationsformate

|Extension|Beschreibung|
|--|--|
|odp   |      OOo 2.x+ Impress|
|otp   |      OOo 2.x+ Impress|
|ppt  |       MS PowerPoint|
|pptx  |       MS PowerPoint 2003+|
|sxi  |       OOo 1.x Impress|

### Sonstige Formate

|Extension|Beschreibung|
|--|--|
|odf    |     OOo 2.x+ Formula|
|otf      |   OOo 2.x+ Formula|

### Formate, die nicht durch OpenOffice.org verarbeitet werden

|Extension|Beschreibung|
|--|--|
|pdf   |    Portable Document Format|
|txt    |   Plain Text|

## Andere




