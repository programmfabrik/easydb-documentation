---
menu:
  main:
    name: "5.61"
    identifier: "5.61"
    parent: "releases569"
    weight: -561
---

# Version 5.61.1

*Veröffentlicht am 08.01.2020*

### Webfrontend

*Behoben*

* Fehler bei Bestätigung von Meldungen korrigiert

### Server

*Behoben*

* Upload von Videos korrigiert

# Version 5.61.0

*Veröffentlicht am 18.12.2019*

### Webfrontend

*Neu*

* Nutzungsbedingungen beim Download darstellbar

*Behoben*

* Status in Objekttyp-/Pool-Selektor verbessert

### Server

*Neu*

* XML-Mapping kann zusätzliche XML-Attribute setzen, im Typo3-Plugin verwendet
* Format für `date_range`-Aggregationen eingeschränkt, keine beliebigen Werte mehr möglich
* Die Container-Basis wurde von Stretch auf Buster angehoben, dies hat eine neue Kernel-Abängigkeit eingeführt. Der Kernel 3.17 ist nun Mindestvoraussetzung.

*Behoben*

* Objekttyp-ACLs werden aufgeräumt, wenn Objekttyp auf Pool (und damit Pool-Rechte) umgestellt wird
* Sprachen für Ad-Hoc-Nutzer werden aus der Session initialisiert
* Fehlerbehandlung beim Aufruf externer Programme verbessert
* korrekter Name des Collection-Besitzers bei Fehlermeldungen
