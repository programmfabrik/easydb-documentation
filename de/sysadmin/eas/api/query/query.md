#  EAS-API: /query

Der `query`-Request erlaubt die Abfrage von Informationen aus dem EAS unabhängig von speziellen Assets. Momentan umfasst das:

* verfügbare Farbprofile (`/query/profiles`)
* typabhängige Optionen für das Erstellen von Versionen (`/query/params/<fileclass>/<mimetype>`)
* für diese Instanz verwendete Datei-Klassen und -Erweiterungen (`/query/distinct/extension`)
* für diese Instanz verwendete Werte für Metadaten-Schlüsselwörter (`/query/distinct/keyword/<group>/<item>`)

##  Beispiel

~~~
http://eas.example.com/eas/query/profiles?instance=example
http://eas.example.com/eas/query/params/video/video/mpeg?instance=example
http://eas.example.com/eas/query/distinct/extension?instance=example
http://eas.example.com/eas/query/distinct/keyword/EAS::Custom/produced_user?instance=example
~~~


##  Parameter


|---|---|
|`instance`          |Name der Instanz|




