---
menu:
  main:
    name: "5.78 (January 2021)"
    identifier: "5.78"
    parent: "releases579"
    weight: -578
---

> A re-index is required for this release, please allow appropriate time to apply the update. 

# Version 5.78.0

*Published on 13.01.2021*

## Web frontend

*New*

- **CSV importer**: Replacing tags using CSV importer is supported.

*Improved*

- **Search**: Deep links into the search have been shortened slightly.
- Design: Improved output of standard info of objects.
- **HTML** Editor: Improvements and bug fixes.

*Fixed*

- Printing: fixed an error when creating the PDF.
- **Collections**: Selection of all elements was fixed.

## Server

*New*

- Permanent saving of configurable **user information** in the event log.

*Improved*

- **File name templates** can now contain date fields.
- Improved Error message when saving **circular references** in the group editor.

*Fixed*

- Possible unnecessary transaction consumption in the **Suggest index** avoided.
- Fixed indexing of **full text fields** in some cases.
- Saving multiple top-level **bidirectional** relations is now prevented.

# Checksums

Here are the checksums of our docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:3b0d0e3b97be2fc7129f29f56434608f6fcb3a213b2f7cfe042eccd6adbe6d0b
docker.easydb.de/pf/eas                  sha256:4765219fe3ac76a3bc05e27b28bbfab864e7db4bd2daaacd4c097397ea077bd7
docker.easydb.de/pf/elasticsearch        sha256:2c61c8d9096a741cadaa496861ae13bdc4ce808995710a2849c29e25160350c3
docker.easydb.de/pf/fylr                 sha256:efd5728211e52119f63f2d24e41abaa62692a310aa59857c801b1ad3e8db7a58
docker.easydb.de/pf/postgresql-11        sha256:98756185f6e1995f6cf64f46d1190968f771311967187dd5bf5c433157517290
docker.easydb.de/pf/server-base          sha256:967411bcc87aae646295a1c8b9dbe7152182232af8598676ef80c1addaf60ed0
docker.easydb.de/pf/webfrontend          sha256:ef2cc9c6a468200268cf569c5f010fe560a1b9efb9dee4cd39ea5425d5bacf95
```



*Translated with www.DeepL.com/Translator*

