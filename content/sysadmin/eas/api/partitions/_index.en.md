---
title: "19 - /partitions"
menu:
  main:
    name: "/partitions"
    identifier: "sysadmin/eas/api/partitions"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /partitions

With the `partitions`-Request, files from the EAS can be retrieved. The SHA1-Hash of the file must be known in addition to the asset ID.

##  Example

```url
http://eas.example.com/eas/partitions/1/0/0/123/4e1243bd22c66e76c2ba9eddc1f91394e57f9f83/image/jpg
http://eas.example.com/eas/partitions/1/0/0/123/4e1243bd22c66e76c2ba9eddc1f91394e57f9f83/image/jpg/sameFileButOtherName.jpg
```


##  Structure

The path parts to `partitions` are structured as follows:

* Partition ID (see also "Partitions": ../../partitions)
* Million block (asset ID by 1,000,000 times 1,000,000)
* Thousands block (asset ID by 1,000 times 1,000)
* Asset ID
* SHA1 hash
* MIME type (including slash, e.g., image/jpg)
* Download filename (optional)

##  Parameter

This request is processed directly by the Apache Web server and does not require any GET parameters.
