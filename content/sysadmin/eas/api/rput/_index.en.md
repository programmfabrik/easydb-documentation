---
title: "23 - /rput"
menu:
  main:
    name: "/rput"
    identifier: "sysadmin/eas/api/rput"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /rput

Import assets by specifying a URL.


##  Example

```url
http://eas.example.com/eas/rput?instance=example&url=http%3A%2F%2Fexample.org%2Fimage.jpg
```


##  Parameter


|key|value|
|---|---|
|`instance`          |Name of the Instance|
|`url`               |Import-URL|
|`custom`            |JSON-Object with Name-Value-Options (Will be saved and delivered, but not evaluated or modified)|
|`thumbnailsize`     |If set, a thumbnail version with this size is created (e.g. `128x128`)|


 

