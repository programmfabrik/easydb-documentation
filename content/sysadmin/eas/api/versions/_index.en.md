---
title: "29 - /versions"
menu:
  main:
    name: "/versions"
    identifier: "sysadmin/eas/api/versions"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /versions

##  Example

```url
http://eas.example.com/eas/versions/123?instance=example&metadata=.*
http://eas.example.com/eas/versions/123/thumbnail?instance=example
http://eas.example.com/eas/versions/123/4e1243bd22c66e76c2ba9eddc1f91394e57f9f83?instance=example
```


##  Parameter


|key|value|
|---|---|
|`instance`          |Name of the Target Instance|
|`metadata`          |Regular expression for filtering metadata field names (default: `^$`)|

 

