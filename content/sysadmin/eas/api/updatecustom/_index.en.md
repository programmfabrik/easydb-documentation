---
title: "28 - /updatecustom"
menu:
  main:
    name: "/updatecustom"
    identifier: "sysadmin/eas/api/updatecustom"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /updatecustom

Custom data is name value options that are stored by the EAS for each asset. These are not used by the EAS. With the `updatecustom`-Request, these can be set independently of other operations.

This data must always be updated completely, it is not possible to set individual values within the structure.

##  Example

```url
http://eas.example.com/eas/updatecustom/123?instance=example&custom={"foo": "bar"}
```


##  Parameter


|key|value|
|---|---|
|`instance`          |Name of the Instance|
|`custom`            |JSON-Object with Custom-Data|


 

