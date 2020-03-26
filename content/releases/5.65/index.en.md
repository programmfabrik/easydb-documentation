---
menu:
  main:
    name: "5.65"
    identifier: "5.65"
    parent: "releases"
    weight: -565
---

> A re-index is required for this release, please allow adequate time for the update to be installed. 

# Version 5.65.0

*Published on 25.03.2020*

### Webfrontend

*New & Improved*

- Data model: **Nested fields** can be automatically **sorted** by **any sort criteria**. This sorting is only done in the web frontend and is done automatically before saving and before displaying.
- Exports can now embed object types for XML and CSV for linked objects that appear in the main search.
- **Messages**: Improved display in the form for confirmations.

Fixed

- **CSV importer**: Corrections when setting hierarchical information.

Plugins

- The **Geonames** and **GN250** **plugins** have been switched to [Mapbox](https://mapbox.com). For Mapbox it is mandatory to enter an API key in the base configuration, otherwise no maps will be displayed.

### Server

*New & Improved*

- **Export**: The export of language-dependent fields in CSV format has been improved.
- **Export**: `export.merge_linked_object=all` allows the embedding of linked objects in the export which are displayed in the main search. 
- **Export**: `mapping` is now only supported if xml_one_file_per_object=true.

*Fixed*

- **Index**: The pool facetting was corrected for objects linked to objects from other pools. A re-indexing is required for this and is automatically triggered at server startup.
- Export: The output of **assets in XML** was incorrect and has been corrected
- Export: **Saving ZIP files via FTP** has been corrected.

Checksums

- Here are the checksums of our docker images
```ini
  docker.easydb.de/pf/chrome               sha256:c1bdb8ed51116804abd49cc25d9bc13be5bbfe43d4f8c834c7d45c9ab0b673b2
  docker.easydb.de/pf/eas                  sha256:83d907500311166f28201c29d2663900f5c5fb61fbba66f6ddb64ba77e2eefff
  docker.easydb.de/pf/elasticsearch        sha256:3e7cd67fb1a4ee2e5cb2e78d79ee38661a98e99bb824413f2bbaa4238af6c60e
  docker.easydb.de/pf/fylr                 sha256:a90fc81cd5a2ce970f6a4fe13e674ded87b22cea3703201db6bdc0f42b95a81d
  docker.easydb.de/pf/postgresql-11        sha256:d7bca85db245478934ef3f8ccaaf3c13fcd6e7ff26728e344f70b0370c9d051b
  docker.easydb.de/pf/postgresql           sha256:c5de3a34289459f0d098bc64e36cb3308eaebbccab563ff5efb0667b8b539c0f
  docker.easydb.de/pf/server-base          sha256:cf56332fd0a751cbff93291b37cb4ffa5aa529e681c528acd459ef095a1d4185
  docker.easydb.de/pf/webfrontend          sha256:cd919adacdf5b00251badc09b773107e21afb6543d294936fccbf99dc124e507
```

*Translated with www.DeepL.com/Translator*

