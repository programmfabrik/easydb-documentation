---
title: "22 - /put"
menu:
  main:
    name: "/put"
    identifier: "sysadmin/eas/api/put"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /put

Mit dem `put`-request wird ein Asset in den EAS importiert.

##  Beispiel

~~~
 http://eas.example.com/eas/put?instance=example&filename=/tmp/some.jpg&custom={"producer": "admin"}
~~~


##  Parameter


|key|value|
|---|---|
|`instance`          |Name der Zielinstanz|
|`filename`          |Pfad zur zu vereinnahmenden Datei|
|`original_filename` |Originaldateiname der Datei|
|`symlink`           |Wert `1`, um Datei symbolisch zu verlinken, statt zu kopieren|
|`hardlink`          |Wert `1`, um Datei zu verlinken (hard-link), statt zu kopieren|
|`thumbnailsize`     |wenn gesetzt, wird eine *thumbnail*-Version mit dieser Größe erzeugt (z.B. `128x128`)|
|`thumbnailpriority` |Priorität der *thumbnail*-Version (ab EAS 4.2.31)|
|`thumbnail_target_*`|Optionen für implizite *thumbnail*-Version (alternativ zu `thumbnailsize`, ab EAS 4.2.40)|
|`custom`            |JSON-Objekt mit Name-Wert-Optionen (wird gespeichert und ausgeliefert, aber nicht ausgewertet oder verändert)|
|`parent_id`         |Asset-ID des Eltern-Assets (sollte normalerweise nicht benutzt werden, ist aber für Migrationszwecke vorhanden)|
|`no_fulltext_index` |Asset nicht in den Volltext-Index aufnehmen (ab EAS 4.2.12)|
|`expires`           |Ablaufintervall, z.B. 7d für 7 Tage|
|`reap`              |Asset-ID und -Hash einer Version eines anderen Assets, dass als Original importiert werden soll, beispielsweise `2364/f1d2d2f924e986ac86fdf7b36c94bcdf32beec15`. Von der Benutzung dieser Option wird abgeraten.|
|`dispose_source_asset`|Das Asset der mit `reap` übernommenen Version wird nach Extraktion gelöscht|
|`dispose_source_version`|Die mit `reap` übernommene Version wird nach Extraktion gelöscht|
|`url`               |die Verarbeitung wird durch "/rput":../rput übernommen, alle Optionen werden an diesen Handler weitergereicht|
|`zipasdirectory`    |Wert `1`, wenn ein hochgeladenes ZIP auf dem Server entpackt werden soll (ab EAS 4.2.49)|
|`webdvdasdirectory` |wie `zipasdirectory`, aber nur bei Endung `.webdvd.zip` (ab EAS 4.2.49)|

##  *thumbnail*-Version

Alternativ zu `thumbnailsize` können ab EAS 4.2.40 auch alle anderen Parameter der implizit erstellten *thumbnail*-Version bestimmt werden. Hier sind alle `target_*`-Optionen von [/produce](/de/sysadmin/eas/api/produce) möglich, die Optionen müssen allerdings das Präfix `thumbnail_` erhalten. Ausschlaggebend ist die Angabe von `thumbnail_target_format`, sehr sinnvoll ist das Setzen von `thumbnail_target_size`. `thumbnailpriority` ist auch bei der Verwendung von `thumbnail_target_*` weiterhin gültig.


##  Upload der Datei

Alternativ zur Angabe des Dateipfads über `filename` kann die Datei auch direkt hochgeladen werden. Das kann entweder direkt oder in einem Formular geschehen.

### Direkter Upload

Üblicherweise per HTTP PUT, Beispiel mit `curl`:

~~~
 curl -XPUT http://eas.example.com/eas/put -H 'Content-Type: image/png' -T test.png
~~~

### Upload im Formular

Auch bei dieser Art kann momentan immer nur eine Datei hochgeladen werden. Der Name des Formularfelds (im Beispiel `file`) ist egal. Beispiel mit `curl`:

~~~
 curl -XPOST http://eas.example.com/eas/put -F file=`test.png
~~~
