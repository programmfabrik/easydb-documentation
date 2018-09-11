---
title: "12 - /barcode"
menu:
  mainWEG:
    name: "/barcode"
    identifier: "sysadmin/eas/api/barcode"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /barcode

##  Beispiel

```url
http://eas.example.com/eas/barcode?value=Gute%20Nacht&target_code=Code128&target_size=512x384&target_quietzones=1&instance=example
```


##  Parameter


|key|value|
|---|---|
|`instance`          |Name der Instanz|
|`value`             |Wert des Barcodes, muss mit dem gewählten Barcode kompatibel sein|
|`target_code`       |Art des Barcodes, Vorgabe ist `Code128`. Unterstützt werden `Code128`, `EAN13`, `EAN8`.|
|`target_size`       |Größe des Barcodes. Ohne Angabe wird die kleinstmögliche Größe gewählt. Beispiel: `400x300`|
|`target_quietzones` |Wenn gesetzt (Wert `1`) wird links und rechts vom Barcode eine Ruhezone (weißer Bereich) ins Bild aufgenommen. Momentan nur für `Code128` möglich.|


