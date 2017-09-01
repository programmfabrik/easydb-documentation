#  EAS-API: /status

With the `status`-Request , the current status of the EAS can be queried.


##  Example 

~~~
 http://eas.example.com/eas/status?instance=example
~~~


##  Example output

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
|`instance`          |Name of the Instance|


 

