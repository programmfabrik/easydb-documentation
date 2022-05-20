---
menu:
  main:
    name: "5.100 (May 2022)"
    identifier: "5.100"
    parent: "releases"
    weight: -600
---

> This version **does not require a new index build**

> For this version **python 3** was introduced to repleace **python 2.7**. All plugins with a python version below **python 3.x** will not work anymore

# Version 5.100.0

*Released on 18.05.2022*


## Webfrontend

### New

* Added a new contact in workflows: **pool contact** (see below)

### Improved

* **Search**: Big improvements and bugfixes in the **filter**
* **Events**: Changed the way of getting the user types for the events (internal change)
* **Rights Management**: usability improvements in the field selector for rights
* **Export**: general bugfixes and improvements

### Fixed

* **Editor**: bugfix when closing the editor, sometimes there was a message saying "unsaved changes" more than one time
* **Smaller bugfixes in**:
  * Asset Detail View
  * Collection view
  * Main list count (sometimes it was in negative)
  * Detail view, where the mask was not being shown in the footer
  * Refresh button of collections

## Server

### New

* **Plugin Implementation**:
  * internal python implementation was upgraded **python 2.7** to **python 3.x**
  * all plugins with a python implementation have been upgraded as well
* **Workflows**: it is now possible to define user accounts, which are used as pool contact, as email recipients in workflows
* **User Management**: the right to edit or delete SSO users can now be granted to other users/groups
* **Rights Management**:
  * users can now remove their own read/write rights on objects
  * this allows the hiding of objects for yourself, instead of actually deleting objects

### Improved

* **Janitor**: performance improvement in statements to collect unused watermark versions of assets

### Fixed

* **Group edit mode**: don't try to update pools for objects where pool management is not enabled


# Checksums

Here are the checksums of our Docker images (latest version): 

```ini
docker.easydb.de/pf/chrome               sha256:02a6f3bf6d5b7932e98b46e60d878f07e0670730d10c9f804d07f266c3d2038a
docker.easydb.de/pf/eas                  sha256:f271316bc335e9cd8c3bc919bdba623f5493cbca9a31c5f094ce362b91bff498
docker.easydb.de/pf/elasticsearch        sha256:93cf92e964b6c25fe6acff8d0eb38a53935d0ec159c36038606ed9b6c4957bb3
docker.easydb.de/pf/fylr                 sha256:e59c504f7fad36c5da09fa558351293e710148f7fc10ed3f19fa1a8c566dcbeb
docker.easydb.de/pf/postgresql-11        sha256:a0800dfaf78ea5cef8df083677b7a842e9d6f629ed5aa2e060ec6b973d4648f4
docker.easydb.de/pf/server-base          sha256:53bb27ddcc5e3685d2bd9907b84ce5ee132a629264c975f5963424e895db1862
docker.easydb.de/pf/server-base-py3      sha256:ee5cc91b4f691fa4c6664cb96f13e80c802d44c213866e9e134ec6db9f74bb65
docker.easydb.de/pf/webfrontend          sha256:4df060fc228538ecdb90c62788d4b682cab0061055f79dda7b94d226e674a27d
```
