# Eigene Bilder oder andere Medien einbinden
Um eigene Medien einzubinden müssen diese relativ zu der in der Basis Konfiguration angegeben SCSS Datei URL liegen (siehe [Schnelleinstieg](../quickstart)).
Mittels der EasyDB eigenen SCSS Variable $urlBase kann dann ein Link zu der eigenen Medien-Datei erstellt werden.  

Beispiel: 
```
background-image: url($__urlBase+"/custom_image.png")
```  


