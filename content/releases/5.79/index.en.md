---
menu:
  main:
    name: "5.79 (February 2021)"
    identifier: "5.79"
    parent: "releases"
    weight: -579
---

> No re-index is necessary for this release. 

# Version 5.79.0

*Published 10.02.2021*

## Web frontend

### Improved

* **Search**: search type can be set for distinct parts when entering comma-separated list.

### Fixed

* **Export**: "Files" tab now always visible when there are files to export.
* **Datamodel editor**: removed invalid type selection for nested tables.

## Server

### Fixed

* Sessions of archived users are removed now. This also fixes a bug when querying such a session.
* Error on saving event after sensing e-mail removed.
* Collections of SSO and LDAP used are now removed when user is deleted (same as for easydb users).

# Version 5.79.0

*Published 03.02.2021*

## Web frontend

### New

- **Group management**: configuration of user pseudonymization added.

### Improved

- **Mask management**: option to display linked objects simplified.
- **User management**: Display of email for users without login in the table.
- **Search**: Accelerated display of linked objects in the search slot.
- 202-Process: Support of vertically arranged forms (currently only FYLR is used).
- **Rights management**: Contextual display of object type lists in pool, collections, system rights and workflows. 

### Fixed

- **Collections**: Deletion of connector objects that are no longer accessible is now possible.
- **Collections**: Improved alphabetical sorting of the display. 
- **Data model**: Saving multiple bidi pairs at top level is now prevented.
- **Search**: Double-clicking on a selected object with the sidebar closed could sometimes open the wrong object in detail.
- **Graphical fixes**: Editor, search display of linked objects with image, white tags on white background.
- Fixed loading error for databases with missing logo.
- **Tags**: fixed visibility in detail and editor depending on settings.
- **Search**: fixed bug with hierarchical objects display.
- **Detail**: display of deep links in the Parts menu in the Versions dialog was fixed.
- **Usermanager**: support of CSV down- and subsequent upload was fixed.

## Server

### New

- **User management**: Archived and anonymous users can be deleted time-controlled.
- **/api/user**: New parameter delete_policy. 
- **Events**: A lifetime is now configurable for automatic deletion of temporary events. 
- **Mapping**: PIN code entry is now enforced for email and collection type users for each new session.

### Improved

- **User management**: The configuration for pseudonymization is now with the groups, no longer in the base configuration.
- **Pool management**: speed up when saving with tags and many folders.

### Fixed

- **Indexer**: Archived users are no longer indexed (which caused an error in the log).

## Plugins

### GVK plugin

- The underlying service has been switched from the old GVK interface to the new k10plus interface. This means that now the latest database is used again. Otherwise nothing changes, but this is expressed in the labels and there is again the most current state and thus also again the most current books...

## Hotfolder

- Speed improvement by batching.

## Auto-Keyworder

- Memory leak on connections has been fixed.

# Checksums

  Here are the checksums of our docker images (latest version):

  ```ini
docker.easydb.de/pf/chrome               sha256:15e82b1a80281b83372c92b0ace52f343bc9eb8457497a76843f3ec8650af8d9
docker.easydb.de/pf/eas                  sha256:5fea450226eeccf8b3208795c5905dc45f1f4e0d78bcb8b553be2cc2d8002fe2
docker.easydb.de/pf/elasticsearch        sha256:34843553d665c05e684a5a8c65372c61f232bb3ff5de0767da769b6bb72f99e5
docker.easydb.de/pf/fylr                 sha256:7c1b6949957fa32c9dd90f0710b92b109dd2b298c03aa6d7f5f665eb68594602
docker.easydb.de/pf/postgresql-11        sha256:8c9ac649827eec7cdb080cd2ffb5fcc865066093e95c196f0e529e91a3b07ce5
docker.easydb.de/pf/server-base          sha256:9d92575b7bfdb5687a5cb7dacaf0ee1ca4ecab6de8739acd26cf4ff0d5b59f17
docker.easydb.de/pf/webfrontend          sha256:664ad1d569fc2c81fb8362cae9366bfbbd3335362b7108dec0fabf96d902719e
  ```

  

*Translated with www.DeepL.com/Translator*
