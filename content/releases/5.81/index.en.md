---
menu:
  main:
    name: "5.81 (March 2021)"
    identifier: "5.81"
    parent: "releases"
    weight: -581
---

> A re-index is required for this release, please allow appropriate time to apply the update.

# Version 5.81.2

*Published on 29.03.2021*

## Web frontend

### Fixed

- **Group Edit Mode**: removed reverse-nested fields support, missing server support.

## Server

### Fixed

- fixed archiving of users with linked exports.
- better error handling in user archiving.

# Version 5.81.1

*Published on 24.03.2021*

## Web frontend

### Fixed

- **Collections**: fixed user handling for collections with links for eternal access
- **Plugins**: fixed `custom-mask-splitter-detail-linked` plugin for handling of nested tables inside nested tables
- **Group Edit Mode**: fixed displaying of standard info and preview images

## Server

### Fixed

- **Hotfolder**: fixed internal handling of database connections to avoid opening too many connections

# Version 5.81.0

*Published on 17.03.2021*

## Web frontend

### New

- **Export**: cover for images is now supported (image is zoomed into a fixed viewport).
- **Search**: Additional options for searching in hierarchical objects.
- **Editor**: Date ranges are closed automatically if only one value is entered.

### Improved

- **CSV importer**: Tags are now always visible.
- **Tags**: Colors are determined exclusively in the frontend, no longer in a server configuration.

### Fixed

- **Usermanager**: "undefined" is no longer displayed for new users.
- **Search**: Visibility of tags has been fixed.
- Graphical corrections in CSS.
- **Editor**: change of masks on tag changes fixed.
- **Search**: In search suggestions, hierarchical objects of the main object types were also searched by mistake.
- **Reverse Nested**: When changing the order, unchanged objects are now also reordered correctly.
- **Video**: In some browsers not all buttons could be reached (CSS fix).

## Server

### New

- New database language Turkish.
- Logging of additional user data can be set for events in base configuration.
- Images can be cropped with cover mode.
- Metadata mapping for image format (portrait / landscape).

### Improved

- Server can run without root privileges (system administration intervention required).
- File name generation improved.
- More fields available in Typo3 mapping.
- **/api/pool**: Output from all pools is allowed only for users with `system.root` right. This can be reset to the old behavior with the server configuration `server.api.pool.allow_non_root_list: true`.

### Fixed

- Rotating and flipping images has been stabilized.
- Search for non-existence of nested data now works for "nested index".
- User's emails are no longer output via API in short format.

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:7db0f038b92acb57d6628463035cbdec90d0fc7d89b207d5c8847db047d026d4
docker.easydb.de/pf/eas                  sha256:2dd23df39081a280d76255cae50f151a698e79b7bc1fce8a0898601e67851f19
docker.easydb.de/pf/elasticsearch        sha256:907b198deb124f06e6c825f94ee83e118494fdf5cfbe3ceb3b72f0e86d76c359
docker.easydb.de/pf/fylr                 sha256:72ce9843fe74f446712119231ec0f720cb8beebec9178c7aa453cda783f1a73b
docker.easydb.de/pf/postgresql-11        sha256:336ef532e4d215b264118a6d3a055035c8793e8f1f7daffe237688a6db723df8
docker.easydb.de/pf/server-base          sha256:2a9642a2b510877447399e4c384ecaa6ba3a61774f40a4d3bb35b741142d5b96
docker.easydb.de/pf/webfrontend          sha256:b1fe29c3220de03e7d2651e52a61ec27fe7c0f3356f64c8d7e8b5f3bfa35efe7
```



*Translated with www.DeepL.com/Translator*