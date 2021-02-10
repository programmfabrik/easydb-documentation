---
menu:
  main:
    name: "5.75 (Late Oktober 2020)"
    identifier: "5.75"
    parent: "releases"
    weight: -575
---

> A **re-index is required** for this release, please allow adequate time for the update. 
>
> From this release on the **user history is no more written**, the existing history (only accessible via the database) will be deleted with this release.
>
> Starting with version **5.76** (scheduled for release on **18.11.2020**) **easydb** will only start with the newer **PostgreSQL version 11**. This cut is necessary to be able to use new features of PostgreSQL without endangering old installations. In addition, the old PostgreSQL version does not get security updates anymore. More information in the **[PostgreSQL 11](../5.73#postgres-11)** section.

# Version 5.75.3

*Released on 10.11.2020*

## Webfrontend

*Fixed*

* **Object View**: Sorting of hierarchical objects by parent objects was fixed.
* **Editor**: Saving of objects, where only the pool was changed, was fixed.
* **Editor**: Creating and changing of templates was fixed.

# Version 5.75.2

*Released on 06.11.2020*

## Webfrontend

*Fixed*

* **Connector**: Errors during downloads of objects from remote instances fixed.
* **Search**: Fixed expert search for empty date fields.

# Version 5.75.1

*Released on 04.11.2020*

## Webfrontend

*Fixed*

- **Search**: Expert search for date ranges in the format (minimum) searches the entire range between .fromand .to as before.
- **CSV importer**: Problem with double field display in mapping fixed.
- **Search**: Fixed expert search for reverse linked objects.

# Version 5.75.0

*Released on 28.10.2020*

## Webfrontend

*New*

- **Detail**: For reverse nested objects, **tags** can be displayed using the mask option.
- **Search**: Display options when grouping by linked objects.
- **PDF**: Integration of the browser-internal PDF viewer in addition to the easydb internal viewer.
- **Expert search**: The search for date ranges now has the possibility to distinguish between the lower and upper date in the search.

Improved

- A new display of **#New** and **#Copy** in the editor distinguishes whether a record is copied or newly created.
- **Search**: When displaying the number of hits, the name of the object type is now also specified if it is unique.

Fixed

- **Typo3 plugin**: Adaptation for Typo3 easydb plugin version [Version 1.4.0](https://docs.typo3.org/p/easydb/typo3-integration/1.4/en-us/AdministratorManual/). With this version the error message Request URI Too Long no longer appears.
- Fixed an error in the **table view** when displaying deeply nested hierarchies.
- Fixed an error in the editor when displaying **pools in reverse** linked objects.
- **Connector**: Display of previews for some cases fixed.
- Filter: Fixed filtering of date ranges for some cases.
- **Expert search**: Javascript errors could occur if fields were of different types but with the same localized field names.

# Server

*New*

- **/api/xmlmapping**: Events `MAPPING_INSERT`, `MAPPING_UPDATE` and `MAPPING_DELETE` are written.
- **/api/db**, **/api/search**: Output of _tag inside reverse-linked objects.

*Improved*

- **/api/db**: For date fields, years are accepted with a preceding `+`.
- **/api/search**: Date fields now also accept timestamps with milliseconds

*Behoben*

- Problems with **/api/suggest** after the Elasticsearch update to 7.x were fixed.
- **/api/collection**: When moving collections, the owner of the parent collection is taken over.
- **Index updates** when removing linked items have been improved.
- **/api/search**: Fixed aggregation of date without time.
- The system right `system.user.default_needs_confirmation` is now respected.
- **Welcome** mail is now also sent when Confirm mail is disabled.
- **/api/export**: Fixed version selection on export.
- **/api/search**: Search for non-existence of linked objects has been fixed for complex indexes

# Checksums

Here are the checksums of our docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:f24a68195f7215c5fba3ab3d0dca910ead74cc6659a5b2b3cdf8fe912d8d10e2
docker.easydb.de/pf/eas                  sha256:94266f584b75b6755a615ecb0141626c00265d7419747e883b7ab80878d715dc
docker.easydb.de/pf/elasticsearch        sha256:67891a41d3f83d0210607826957fc3f0469ab276b113fd49fd9911a28da451ab
docker.easydb.de/pf/fylr                 sha256:e25c897842ca3c3f4ea4699729655bd5b8aa2f5314d87b27c9e1c8520ffcf4b0
docker.easydb.de/pf/postgresql-11        sha256:f9018e12f629da8466e69bdf9ea01b17b1a73413b297ddf600bff7c5f8ad6b7e
docker.easydb.de/pf/postgresql           sha256:61bd66bd6734f316af5ae139946b83d085ebe1a310450805d5456201692f5fed
docker.easydb.de/pf/server-base          sha256:a8c71e833580c8ecb95df29fa2a55b2da82c3a6875711839beccc0fd97be1af4
docker.easydb.de/pf/webfrontend          sha256:0ab1bfc8e4f134cc15a2e92f3ef20e0a5facf0ba5ef5d114bd55b33e30396e42
```

*Translated with www.DeepL.com/Translator*

