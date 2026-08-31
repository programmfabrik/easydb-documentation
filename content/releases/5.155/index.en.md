---
menu:
  main:
    name: "5.155 (Late July 2026)"
    identifier: "5.155"
    parent: "releases"
    weight: -655
---

> This version **does not require** a new index build


# Version 5.155.1

*Released on 2026-08-31*

# Server

## Fixed

* fixed XSLT transformation of some objects.
* easydb server accidentially stopped other processes running under the same user (`www-data`, PID 33) under memory pressure.

# Version 5.155.0

*Released on 2026-07-29*


# Webfrontend

## Improved

- **Editor** — Moving a record to another pool removes the tags the new pool does not allow, with a warning before saving. `0272cddee` (#76965)
- **Metadata mapping** — Invalid tags are marked and block saving instead of being rejected silently. `742800b7a` (#76071)
- **Search results** — Large result pages render and scroll noticeably faster, and changing the view size no longer freezes the app. `9c92c648e` (#79956)
- **Reverse-linked fields** — Records with many reverse links open faster; their data is only loaded when the tool is opened. `0113a08b3` (#80067)
- **Editor** — Empty mandatory linked, nested and asset fields now say "… is required" instead of showing a generic error. `89a316fec` (#79359)
- **Asset browser** — After changing the preferred variant, the old asset is no longer shown until the record is saved. `521f1525f` (#79791)

## Fixed

- **Editor** — Tab titles and the preview column of the customize-templates dialog are translated. `b4238189d`, `8e01b4e6f`, `f339503ba` (#79659)
- **Search** — Linked-object suggestions find records again: indirectly linked object types match, suggestions that lead nowhere are no longer offered, and picking an entry from a hierarchy matches its whole subtree. `4fdf79361`, `74e841e71`, `467cf0f92`, `b2189c966` (#79876)
- **Search** — "Add to collection" is shown again for users who have no collection yet but may create one. `28dbc3754` (#80407)
- **Search** — Right-clicking a record no longer reloads the sidebar. `d08a4705e` (#79999)
- **Expert search** — Works again when no object type is selected in the search type selector. `80ec07815` (#80027)
- **Linked objects** — A value the user may not read is kept instead of being dropped on save. `504d8693f` (#79698)
- **Detail view** — Closing and reopening a root node no longer expands the whole hierarchy. `709d5a87b` (#79656)
- **Parent field** — The link to the parent record works again when the record is rendered as "Short". `ecb892abe` (#79656)
- **Result card list** — Fixed the placeholder label and the spacing for records without an asset. `c68372289` (#79656)
- **Text fields** — Overlong text no longer overflows its field. `f0705fe74` (#78555)
- **Datamodel** — New masks that are not the default one get the correct display name. `ffd620014` (#79405)
- **Tags** — Tag groups and tags can no longer be saved without a name; unnamed ones broke the facet panel. `1f573ff6a` (#80368)
- **Collections** — Firefox no longer offers to autofill the collection filter with a user name. `dc06478f1`

# Server

## Improved

* `debug/max_core_size` (default 0) also works in foreground mode (such as in Docker container), before the system default was in use. This prevents unwanted core files inside container.

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.155.0            sha256:09a2e335e68282c8d24d8d48282bd36ca2b969cc5f6c3e0bef0f2c115e56f58c
docker.easydb.de/pf/elasticsearch:5.155.0  sha256:8bbeee2e9f415f92bcab25ebc573ac3dea1dce6ad31e22925d91c93aa54e8507
docker.easydb.de/pf/fylr:5.155.0           sha256:be376566ba232aec17b8d66f100c1344b012ffcc03e0f19f1018bd3355f1a283
docker.easydb.de/pf/postgresql-14:5.155.0  sha256:5f4e214824d4136785d388dda438bd53c15ed03badd693ef66401542eb9b0af1
docker.easydb.de/pf/server-base:5.155.1    sha256:49ec91ce724ad4fa21d9f3fef4dbf5c340d922d4649aa75c738972bc83255c75
docker.easydb.de/pf/webfrontend:5.155.1    sha256:ccbc6a99acbd29c87f71051fa1cd5681ff9e5a47d9506492631dd0c06e7c1184
```
