---
title: "32 - /zoomer"
menu:
  mainWEG:
    name: "/zoomer"
    identifier: "sysadmin/eas/api/zoomer"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /zoomer

Gibt eine Kachel oder Thumbnail für den Zoomer zurück

##  Beispiel

```url
http://eas.example.com/eas/zoomer/123/d8e8fca2dc0f896fd7cb4cb0031ba249/zoom1920/part2x1.jpg?instance=example
http://eas.example.com/eas/zoomer/123/d8e8fca2dc0f896fd7cb4cb0031ba249/thumbnail.jpg?instance=example
```


Ab *Version 4.2.37* unterstützt der EAS für `/zoomer` auch folgende Syntax:

```url
 http://eas.example.com/eas/zoomer/123/d8e8fca2dc0f896fd7cb4cb0031ba249/zoom1920[/size320][/avoid_interpolation]/part2x1.jpg?instance=example
```

##  Struktur

Die Pfad-Teile nach `zoomer` sind wie folgt aufgebaut:

* Asset-ID
* Asset-Version (MD5)
* `zoom<destdim>`, wobei `destdim` die Zieldimension ist (Pixel, siehe unten)
* `size<size>`, wobei `size` die Kachelgröße ist (Pixel, wenn nicht gesetzt: `320`) (ab *Version 4.2.37*)
* `avoid_interpolation`: Interpolation nicht benutzen, wenn der Zoomfaktor eine natürliche Zahl ist (ab *Version 4.2.37*)
* `part<tile_x>x<tile_y>.jpg`, wobei `(tile_x, tile_y)` die Kachelkoordinaten sind. `(0,0)` ist oben links

Der Zoomfaktor wird anhand der Zieldimension angegeben. Das heißt: das Bild wird so gezoomt, dass die Breite des resultierenden Bildes so groß ist wie dieses Parameter. Der Zoomfactor beträgt: `destdim / image_width`.

In dem Beispiel, wenn das Originalbild `(3840x1200)` ist, ist der Zoomfaktor `1920/3840 = 0.5`. Das gezoomte Bild ist `(1920x600)`.

Wenn `avoid_interpolation` gesetzt ist, muss der Zoomfaktor entweder kleiner als `1` oder eine natürliche Zahl sein. Das heißt: `0.5` ist erlaubt, aber `1.5` nicht.

##  Parameter


|key|value|
|---|---|
|`instance`          |Name der Zielinstanz|



