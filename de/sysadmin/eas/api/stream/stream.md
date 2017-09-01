#  EAS-API: /stream

Mit dem `stream`-Request kann eine Datei aus dem EAS abgerufen werden. Anders als der "partitions-Request":../partitions kann hierbei aber ein Start-Offset angegeben werden und es gibt Spezialbehandlung zum FLV-Streaming.

##  Beispiel

~~~
 http://eas.example.com/eas/stream/123/a8fdc205a9f19cc1c7507a60c4f01b13d11d7fd0?instance=example
~~~


##  Parameter


|---|---|
|`instance`          |Name der Instanz|
|`start`             |Byte-Offset innerhalb der Datei|




