#  EAS-API: /status

Mit dem `status`-Request kann der aktuelle Status des EAS abgefragt werden.

##  Beispiel

~~~
http://eas.example.com/eas/status?instance=example
~~~


##  Beispielausgabe

~~~
{
"janitor-enabled": false,
"jobs-recent-interval": "1 day",
"jobs": {
"failed": 3422,
"done": 300194,
"recent-done": 235,
"pending": 702
},
"current-server-timestamp": 1305803904,
"partitions": [
{
"auto_disabled_at": null,
"used": 385136467968,
"name": "orig",
"free": 177439236096,
"disabled": false,
"path": "/var/lib/eas/pool/orig",
"id": 1
},
{
"auto_disabled_at": null,
"used": 385136467968,
"name": "dest",
"free": 177439236096,
"disabled": false,
"path": "/var/lib/eas/pool/dest",
"id": 2
},
]
}
~~~

##  Parameter


|---|---|
|`instance`          |Name der Instanz|




