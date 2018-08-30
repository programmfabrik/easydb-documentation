---
title: "22 - /query"
menu:
  main:
    name: "/query"
    identifier: "sysadmin/eas/api/query"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /query

The `query`-quest allows you to retrieve information from the EAS independently of specific assets. Currently, this includes:

* Available color profiles (`/query/profiles`)
* Type-dependent options for creating versions (`/query/params/<fileclass>/<mimetype>`)
* File classes and extensions used for this instance (`/query/distinct/extension`)
* Metadata keywords used for this instance (`/query/distinct/keyword/<group>/<item>`)

##  Example

```url
http://eas.example.com/eas/query/profiles?instance=example
http://eas.example.com/eas/query/params/video/video/mpeg?instance=example
http://eas.example.com/eas/query/distinct/extension?instance=example
http://eas.example.com/eas/query/distinct/keyword/EAS::Custom/produced_user?instance=example
```


##  Parameter


|key|value|
|---|---|
|`instance`         |Name of the Instance|


 

