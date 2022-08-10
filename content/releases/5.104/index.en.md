---
menu:
  main:
    name: "5.104 (August 2022)"
    identifier: "5.104"
    parent: "releases"
    weight: -604
---

> This update requires a re-index, schedule appropriate downtime / update time

# Version 5.104.0

*Released on 10.08.2022*

# Webfrontend

## New

* Added optional support for System ID in deeplink for objects

## Improved

* **User/Group Manager:**
  * Now the search always uses `wildcard` mode to search, it makes the search more user friendly
  * fixed a small problem where it was not possible to go back to the original list when removing the whole search text
* **Export manager:**
  * do not automatically load existing templates
  * added defaults for `batch size` for CSV export
* **Expert search:** fixed searching for filenames with wildcards
* **PDF Creator:** Reduce the amount of saved `custom_data` to avoid unnecessary large requests
* Added tooltips to dynamic objecttype list menu buttons

## Fixed

* **Daterange fields:** Do not auto-generate the textual representation when both `from` and `to` are set
* fixed the `/login` link
* **Asset browser:** fixed a corner case where images were not shown when no `standard` version available
* fix for some localization keys when the value was an encoded url
* **Presentation Download:** fixed download problems after slide layout was changed without saving

# Server

## New

* **Transitions/Workflows** now have a new comment field to describe the workflow
* **Detail URL:** format can be changed in the base config (between old format using the System ID and the new format using the UUID)
* **Expert Search:** behavior for searching for filenames was changed to allow right truncated searches with wildcards

## Improved

* **Extension Plugins**:
  * for plugins with API Callbacks, the url path now includes `plugin/extension/`, it was `plugin/base/` before
  * See also [API Callbacks](/en/technical/plugins/#api-callbacks)
* **Rights Management:** users/groups can be given the permission to view users from `sso`, `ldap` groups

## Fixed

* **Asset Upload:** use external EAS URL `eas.external_url` for asset urls
* **Change History:** do not try to load pools that have been deleted

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:2c0222ed258b40a21739b877e4684796bee62cca99a09bf74e668f40a1450327
docker.easydb.de/pf/eas                  sha256:e3350e816f03bb10f27f741d7124d287b0d943fd9e5e6b2f22d533ae28fcf621
docker.easydb.de/pf/elasticsearch        sha256:fc72ee8ec1ac3a27827a9b39b2cc921c0e659e0fc2d8e8126ad4d151c45b4624
docker.easydb.de/pf/fylr                 sha256:4a4feaf64f65a343be1e0de140b4470d53ebb7e7c723749fea79b53f17a32e63
docker.easydb.de/pf/postgresql-11        sha256:f2134eb9225dd2f7277f5c3d1d18b6bf76f7510828eb9eb9f5f194ee81625099
docker.easydb.de/pf/postgresql-14        sha256:459318519972b451bcefc425d04c9718e37bffd2c27130999744d4f696ee26d4
docker.easydb.de/pf/server-base          sha256:f5161d65d8fdb38b3c9439a83bb10e4377e292aa491c558ba17ff5f2f3de5be8
docker.easydb.de/pf/webfrontend          sha256:f4c5da770996b74b4ccaa329b94bfe4643d46fd6aef1a77bf42770b0000f2aad
```
