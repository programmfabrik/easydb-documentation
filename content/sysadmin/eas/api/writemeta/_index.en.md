---
title: "30 - /writemeta"
menu:
  main:
    name: "/writemeta"
    identifier: "sysadmin/eas/api/writemeta"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /writemeta

Returns a version of an asset with specific metadata.

##  Example

```url
http://eas.example.com/eas/writemeta/123/f1d2d2f924e986ac86fdf7b36c94bcdf32beec15?target_metadata=["-title=Test","-date=2012-04-23T12:00:00+02"]&instance=example
```


##  Parameter


|key|value|
|---|---|
|`instance`          |Name of the Instance|
|`target_metadata`   |JSON list of rows for Exiftool for writing metadata (see Option `-` from Exiftool)|

 

