---
title: "13 - /bulkfetch"
menu:
  main:
    name: "/bulkfetch"
    identifier: "sysadmin/eas/api/bulkfetch"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /bulkfetch

Queries information about multiple assets. Which information is required for each asset is defined by profiles. This request is used for the fetchassets step of the exporter, the XML notation used there is similar.

##  Example

```url
http://eas.example.com/eas/bulkfetch?instance=example&query=…
```


##  Parameter


|key|value|
|---|---|
|`instance`          |Name of the Instance|
|`query`             |JSON-Structure of the request, contains profile and requested assets|

##  Request and Response

For example, `query` might be:


```javascript
 {
    "profiles": {
        "example1": {
            "versions": [
                "original"
            ],
            "link": true
        },
        "example2": {
            "only-first": true,
            "versions": [
                "160",
                "thumbnail"
            ],
            "metadata": {
                "EAS::TypeInfo": [
                    "width",
                    "height"
                ],
                "Exif::Main": [
                    "*"
                ]
            }
        }
    },
    "assets": {
        "example1": [
            1000,
            1001,
            1002
        ],
        "example2": [
            1000
        ]
    }
}
```

The answer would look something like this:

```javascript
 {
    "example1": {
        1000: {
            "original": {
                "link": "/partitions/1/1000/1000/047595d0fae972fbed0c51b4a41c7a349e0c47bb/image/tiff",
                "ext": "tif"
            }
        },
        1001: {
            "original": {
                "link": "/partitions/1/1000/1001/296ce65c9a5c38d515b713bbb3fa42d0d027204c/image/jpeg",
                "ext": "jpg"
            }
        },
        1002: {
            "original": {
                "link": "/partitions/1/1000/1002/784a2a65aba22e001fd25a1b9e8544e058fbc703/image/jpeg",
                "ext": "jpg"
            }
        }
    },
    "example2": {
        1000: {
            "160": {
                "metadata": {
                    "EAS::TypeInfo": {
                        "width": 160,
                        "height": 120
                    },
                    "Exif::Main": {
                        "ExifIFD:ColorSpace": "uncalibrated",
                        "IFD0:ResolutionUnit": "inches"
                    }
                }
            }
        }
    }
}
```
