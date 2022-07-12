---
title: "Disable image variant"
menu:
  main:
    name: "Disable image variant"
    identifier: "sysadmin/configuration/easydb-server.yml/versions/example_disable"
    weight: -947
    parent: "sysadmin/configuration/easydb-server.yml/versions"
---

# disable image variant

To disable a specific version for a file-type, set that version in "eas_produce.json" to false. In this example there will be only a 250px version for dng-files:

```javascript
{
    ...
    "image": {
        "__all": {
            "small": {
                "target_size": "250x250",
                "target_format": "jpg",
                "target_quality": "80",
                "target_interlace": "1",
                "target_size_min": "1",
                "target_no_enlarge": "1",
                "priority": "12"
            },
            "preview": {
                "target_size": "1000x1000",
                "target_size_minimum": "251x251",
                "target_format": "jpg",
                "target_interlace": "1",
                "target_quality": "80",
                "target_no_enlarge": "1"
            },
            "preview_watermark": {
                "target_size": "1000x1000",
                "target_size_minimum": "251x251",
                "target_format": "jpg",
                "target_interlace": "1",
                "target_quality": "80",
                "target_no_enlarge": "1"
            }
        },
        "dng": {
            "preview": false,
            "preview_watermark": false
        }
    }
    ...
}
```
