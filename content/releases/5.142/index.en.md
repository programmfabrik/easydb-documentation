---
menu:
  main:
    name: "5.142 (March 2025)"
    identifier: "5.142"
    parent: "releases"
    weight: -642
---

> This version **does not require** a new index build

# Version 5.142.0

*Released on 2025-03-26*

# Webfrontend

## Improved

- **Result View**: Enhanced rendering of dynamic objects in search results to minimize UI flickering during large list loads.
- **Download Manager**: Improved handling of filtered assets when downloading the current asset from the asset browser.


## Fixed

- **Search Suggestions**: Fixed autosuggestion exact match for multi-word queries, preventing incorrect results from word splitting.
- **Validation Error in Editor**: Fixed validation error display for custom fields without checkValue method during data saving.
- **Search Suggestions**: Fixed empty autocomplete suggestions for certain custom data types.
- **Objecttype Root Apps**: Fixed duplication of objecttype root menu apps after logout/login or anonymous user login.
- **Admin Messages**: Fixed min and max checked field processing in confirmation messages.
- **Expert Search**: Fixed error when opening expert search with initially invisible parent field, preventing getSearchFilter failure.
- **Change History View**: Fixed latest object loading when comparing versions, ensuring consistent data structures and accurate diff views.
- **Download Manager**: Fixed error when creating download manager for asset downloads without field information.
- **Download Manager**: Fixed bug in title of the popup when downloading only the current asset from the asset browser.


# Server

## Improved

* **/api/db**: `base_fields_only` optimization disabled when plugin update hooks are used. This allows more manipulation inside plugins.

## Fixed

* **/api/pool**: correct status for watermark assets

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.142.0            sha256:5b856bedc5f4a6c0a64345aa18ebd809fc6e06ad993b1b30fb6fbd892983cca9
docker.easydb.de/pf/elasticsearch:5.142.0  sha256:8a982e18886fdf68e10ba871563950e6849f28ed28012ace989bced0f63af7ed
docker.easydb.de/pf/fylr:5.142.0           sha256:8228eee009eb91da6687e153ff887280f27ac35f17ae62f28c3e92ad59b0caae
docker.easydb.de/pf/postgresql-14:5.142.0  sha256:832330ca0d818b07c4d904b84b53c3067c90f62a8fee8d7ff63e7c0e66da76fa
docker.easydb.de/pf/server-base:5.142.0    sha256:ce0e6d3940c24206194dd3982925f74c163c1751780d4df8055bff8ad90ece37
docker.easydb.de/pf/webfrontend:5.142.0    sha256:5feb815392a43807cb4ed1876388f5c83662d98a6fc3380ed98530370aeeefe2
```
