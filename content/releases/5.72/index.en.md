---
menu:
  main:
    name: "5.72 (September 2020)"
    identifier: "5.72"
    parent: "releases"
    weight: -572
---

> This release does **not** require a **re-index**.

# Version 5.72.0

*Released on 27.08.2020*

## Webfrontend

*New*

- Loading of multiple versions during **download** is supported.
- Standard design removed from the mask editor.
- Collections: **Selection of pool** when creating new objects after upload is supported.

*Improved*

- Loading of images is now only done when it is necessary (Lazy Loading).
- Table view now shows the **hierarchy** if desired.

*Fixed*

- Improvement in the menu for loading an image in the preview.
- Fixed display of localized names in **CSV user importer**.
- Bug fixes for the new **table view**.
- **Collections**: In some rights management settings the `+` button could behave incorrectly.
- **Detail**: In some rights management settings an error could occur when loading the detail.

## Server

*New*

- **/api/mask**: `standard_design` parameter has been removed from the API This parameter was not used by the easydb web frontend.
- **/api/collection**: new parameter `linked_pool_id`. This parameter sets the pool for linked objects used when creating within the folder.

*Fixed*

- Fixed a bug in the **group editor** in connection with Tags & Pool.

# Checksums

Here are the checksums of our docker images (latest version):

```ini
docker.easydb.de/pf/chrome              sha256:268fc098104f2ae58f234df2abda856f7c2fe2ae9f0ac36e689ca3a3ada16d0a
docker.easydb.de/pf/eas                 sha256:c918d1320423f6adcd9f2ae438537966e225c643a6f6521c81cd5bd4daa45c33
docker.easydb.de/pf/elasticsearch       sha256:96136e2cf3440534f8ffc111888b08bae64c02fc5558ec114f0064b9b19e1372
docker.easydb.de/pf/fylr                sha256:6b435119b593be668dc91e6479af390e8d02f8ba7ef99faeeb553e86af9c71c9
docker.easydb.de/pf/postgresql-11       sha256:fe6fd87ace569e9f30f3e1b4c6eb89744fb2691fa651e89c0b6bdcd804bba43a
docker.easydb.de/pf/postgresql          sha256:6be6074fec5abb39400dbbbf12bdcac48beb92e3b1292027f91eebfdfe40209c
docker.easydb.de/pf/server-base         sha256:ec9eb2cab24ef6014f8adcca1aae39f9582b3539724311cb933071011a8d5790
docker.easydb.de/pf/webfrontend         sha256:885485270ebd444bcdbabe790d113e22845e752bfb6c983c8d7beb2164a1ef38
```

*Translated with www.DeepL.com/Translator*