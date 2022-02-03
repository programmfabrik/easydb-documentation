---
menu:
  main:
    name: "5.95 (February 2022)"
    identifier: "5.95"
    parent: "releases"
    weight: -595
---

> A **re-index is required** for this release, please allow appropriate time to apply the update.

# Version 5.94.0

*Released on 02.02.2022*

## Webfrontend
### New

* **Preview**: show SVG files directly in browser
* **Editor**: direct creation of children for hierarchical objects

### Improved

* **Asset share dialog**: new tab shows all available versions
* **Accessibility**: improvements for tooltips
* **Event manager**: allow change of column widths

### Fixed

* **Printing**: show configured maximum for search result entries to print
* **Table view**: fix search
* **Search result**: fix display of hierarchy when sorting by pool
* **Connector**: fix events
* **Editor**: better handling of circular links

## Server

### Improved

* Changed default value of client configuration `default_client.print_limit` from 250 to 1000
* Enabled asset cleanup preparation by default again

### Fixed

* Fix slowdown of `GET /api/v1/db` due to too many cache entries
* Search for empty fields inside nested tables now also works if "nested index" is enabled
* Maintain pool links for assets inside cascaded nested tables (important for watermarks)
* Migrate missing SHA2 checksums for assets (Were missing for `rput`, error already fixed)

# Checksums

Here are the checksums of our Docker images (latest version): 

```ini
docker.easydb.de/pf/chrome               sha256:cee0518bdf9ffcd5590b339326586af671bca47d16f74f4231017dc88faef939
docker.easydb.de/pf/eas                  sha256:3242292f7994c6901564430c3915d31cbc3759a4b83bcda8e0b5e0875ea995b7
docker.easydb.de/pf/elasticsearch        sha256:d616f0924d38e5594968243718f395e8fd9aab6b1151f23b8cf27f23903ef9fb
docker.easydb.de/pf/fylr                 sha256:999f2bfc6dcd8393f96ca80c626c7e1d9fe403f3e4323e3ebe4d97cb127d8484
docker.easydb.de/pf/postgresql-11        sha256:ea09de013916050d997f14c4ebde8976160850ade022b68d53359a5021eb5de3
docker.easydb.de/pf/server-base          sha256:add26b73e0706e7bc8b87b435d46a3da7ba5329bb4525f8c959879d6c3ef66e8
docker.easydb.de/pf/webfrontend          sha256:4d0da06ed26de76692776fb6f5fa93fbfab9691e098be645ee65bb3eb553c743
```
