---
title: "21 - /produce"
menu:
  main:
    name: "/produce"
    identifier: "sysadmin/eas/api/produce"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /produce

##  Beispiel

```url
http://eas.example.com/eas/produce/123?instance=example&target_format=jpg&target_size=1024x1024
```


##  Parameter


|key|value|
|---|---|
|`instance`          |Instanzname (notwendig)|
|`version`           |Name der Zielversion (notwendig)|
|`custom`            |zusätzliche vom EAS zu verwaltende Daten|
|`priority`          |Priorität der Aufgabe, Vorgabe: `0`, höher ist wichtiger (ab 4.1.1)|
|`rebuild`           |`1`: die Version auch neu erstellen, wenn sie schon existiert|
|`new_original`      |`1`: die Version wird zu einem neuen abgeleiteten Asset|
|`no_link_to_orig`   |`1`: in Verbindung mit `new_original` wird die Version zu einem neuen Original ohne Referenz zur Quelle (ab 4.2.37)|
|`thumbnailsize`     |wenn gesetzt, wird eine Thumbnail-Version mit dieser Größe erzeugt (z.B. `128x128`)|
|--------------------|----------------------------------------------------|
|`target_format`     |Dateiformat der Version|
|`target_size`       |Größe (z.B. `128`, `640x480`, `x12` oder `45x`)|
|`target_page`       |eine Seite soll extrahiert werden (Zählung beginnt bei `0`)|
|`target_extractdpi` |Bei der Umwandlung von Office-Dokumenten in Bilder soll diese DPI-Zahl benutzt werden (Standard: `300`)|
|`target_metadata`   |JSON-Liste von Zeilen für Exiftool zum Schreiben von Metadaten (siehe Option `-` von Exiftool)|
|`target_rotate`     |Drehwinkel in Grad|
|`target_mirror`     |Spiegelung an der angegebenen Achse (`x` oder `y`)|
|`target_crop`       |Ausschneiden eines Bildbereiches (`<w>x<h>+<x>+<y>`, z.B. `400x300+100+30`)|
|`target_size_force` |`1`: Größe erzwingen (Seitenverhältnis missachten)|
|`target_size_limit` |`1`: Version nicht erstellen, wenn die Originalgröße kleiner als die angeforderte Größe ist|
|`target_size_min`   |`1`: Angegebene Größe ist gewünschte Minimal- und nicht Maximalgröße (ab *(version)Version 4.2.47*).|
|`target_no_enlarge` |`1`: Nicht vergrößern, wenn die Originalgröße kleiner als die angeforderte Größe ist (ab *(version)Version 4.2.34*).|
|`target_dpi`        |DPI-Einstellung für die Ausgabedatei (beeinflusst nicht die Größe)|
|`target_wm_image`   |Wasserzeichen-Bild, welches in die Version eingerechnet werden soll (wird mit absolutem Pfad, der für www-data lesbar ist, angegeben). |
|`target_wm_dissolve`|Wasserzeichen-Transparenz (von `0` - unsichtbar - bis `100` - deckend - die Voreinstellung ist `50`)|
|`target_wm_gravity` |Ausrichtung des Wasserzeichens (Himmelsrichtung), eine Option aus: `c` (Voreinstellung), `n`, `e`, `s`, `w`, `ne`, `nw`, `se`, `sw`|
|`target_wm_size`    |z.B. `100x100` oder `50%x50%` (Voreinstellung: `100%x100%`; Achtung: `10%x10%` statt `10%`; Wichtig: %-Zeichen URL-kodieren: `%25`)|
|`target_wm_tile`    |`1`: Wasserzeichen wird gekachelt. `target_wm_gravity` wird in diesem Fall nicht berücksichtigt. (ab *(version)Version 4.2.36*)|
|`target_colorspace` |Farbraum, getestet mit `rgb`, `cmyk` und `gray`|
|`target_numcolors`  |Anzahl der Farben, mögliche Werte: `2` .. `256`, `32k`, `64k`, `16m`. Die Farbtiefe wird entsprechend auf 8, 15, 16 bzw. 32 Bit angepasst. (ab 4.1.1)|
|`target_alpha`      |Transparenz-Einstellungen, eine Option aus `on`, `off`, `set` order `opaque` (Voreinstellung `off`; siehe auch "ImageMagick-Dokumentation":http://www.imagemagick.org/script/command-line-options.php#alpha)|
|`target_profile`    |Dateiname einer Farbprofil-Datei für `convert`. Ist nur ein Dateiname ohne Pfad angegeben, wird (ab 4.1.1) die Profil-Datei im Verzeichnis `eas/data` des EAS gesucht.|
|`target_quality`    |Qualität der Ausgabedatei von `0` bis `100` (abhängig vom Ausgabeformat)|
|`target_compress`   |Kompressionsmethode für Ausgabedatei (abhängig vom Format, z.B. `lzw`)|
|`target_strip`      |`1`: alle Metadaten entfernen|
|`target_no_rgb`     |`1`: keine automatische Konvertierung in RGB|
|`target_no_autorot` |`1`: keine automatische Drehung/Spiegelung anhand von EXIF-Tags|
|`target_zoomer`     |`1`: Version für den Zoomer vorbereiten (`target_format` muss `jpg` sein)|
|`target_duration`   |Anzahl der Sekunden ab Anfang, die für eine Video-Version berechnet werden sollen. Wenn nicht gesetzt, wird das komplette Video umgerechnet. (ab *(version)Version 4.2.32*)|
|`target_audio_bitrate` | Audio-Bitrate für Video- und Audio-Dateien, z.B. `160k` (ab *(version)Version 4.2.49*)|
|`target_audio_bitrate` | Video-Bitrate für Videos, z.B. `800k` (ab *(version)Version 4.2.49*)|
|--------------------|----------------------------------------------------|
|`target_commandfile`|Kommandodatei für Automator-Anfragen|
|`target_fail_on_error`|`1`: Schlägt das Hinzufügen einzelner Assets fehl, so wird die Abarbeitung der Kommandodatei abgebrochen (für `target_commandfile`, ab *(version)Version 4.2.33*).|

##  Reihenfolge

Transformationen werden in folgender Reihenfolge ausgeführt:
* `target_crop`
* `target_size`
* `target_mirror`
* `target_rotate`
