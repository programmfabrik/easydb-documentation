#  EAS-API: /stream

With the `stream`-Request a file can be retrieved from the EAS. Unlike the "partitions-Request":../partitions, a start offset can be specified here and there is special treatment for FLV streaming.

##  Example

~~~
 http://eas.example.com/eas/stream/123/a8fdc205a9f19cc1c7507a60c4f01b13d11d7fd0?instance=example
~~~


##  Parameter


|key|value|
|---|---|
|`instance`          |Name der Instanz|
|`start`             |Byte-Offset innerhalb der Datei|


 

