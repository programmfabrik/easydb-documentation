---
menu:
  main:
    name: "5.101 (June 2022)"
    identifier: "5.101"
    parent: "releases5100"
    weight: -601
---

> This version **does not require a new index build**

# Version 5.101.0

*Released on 08.06.2022*

# Webfrontend

## New

* **Expert search**: Filter for file date

## Improved

* **Editor**: Output of object ID, etc. in the footer
* **Pools**: Comment field added

## Fixed

* **Data model**: checking of value range of decimal numbers corrected
* **Autocomplete**: entire input is completed
* **Editor**: limit of 1000 objects in editor is forced also for uploads
* **Collections**: display problem when searching without result fixed
* **CSV importer**: fixed problem with empty values for linked objects
* **PDF display**: no assumption that the original is readable

# Server

## Improved

* **/api/v1/db**: collection rights check less often and can be skipped
* **XML export**: option to output auxilliary objects as well as main objects that are reverse-linked
* **Search/XML mapping**: standard field of custom data types searchable
* **API logging**: events also configurable for /api/v1/objects
* **Database**: new index to speed up EAS supervisor when using many watermarked assets
* **/api/v1/db**: improvements for `all_versions=true` (bulk API in preparation for migration purposes)

## Fixed

* **XML export**: recursive loading of linked objects fixed
* **Group editor**: removing nested objects even with multiple occurrences
* **POST /api/v1/user**: empty language lists allowed
* **Plugin interface**: fixes for callbacks used in hotfolder
* **EAS**: fixed recognition of WMF files

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:8b0849bbb05834e0b273caf2d345f3635b7b61c74bc571960a5b70e5042ff869
docker.easydb.de/pf/eas                  sha256:1d78dbffc7ed68195799320876b86bb005840cc5c4ba99db9c05a95572d76c9b
docker.easydb.de/pf/elasticsearch        sha256:cfd775500615b26d4285fee1ff1914a85b51b4c54ed65972f92576cf212f66f0
docker.easydb.de/pf/fylr                 sha256:9e92b063deb5b4b44258eb669392fe6f4165e55e6fc4fad312037e72d04af8aa
docker.easydb.de/pf/postgresql-11        sha256:3b7fedc8dfa5fb4238005d7e859ec1e0b13173854b8a84490b2b9d0f20e60494
docker.easydb.de/pf/postgresql-14        sha256:14671871594cb6a62e506852ee3339e93d02c808918ee860f602f675d251c53d
docker.easydb.de/pf/server-base          sha256:1d6ad542d8eed44a3f1868ea5a4db01e52777957871d789e022c79a488f1c004
docker.easydb.de/pf/webfrontend          sha256:025b38c8f2292e791bcac6052b45c45c54eaf6a1ddea8c1cd47b9bbb6a7085c7
```

Translated with www.DeepL.com/Translator (free version)
