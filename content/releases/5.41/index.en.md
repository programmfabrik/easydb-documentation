---
menu:
  main:
    name: "5.41"
    identifier: "5.41"
    parent: "releases"
    weight: -541
---

# Version 5.41.0

*Published on Oct 10th 2018*

> This release needs to a full re-index, please consider appropriate update times.

### Server

* all emails searchable
* optimized suggest index generation
* slimmed down base type search results
* made available timeout of login locks
* `/api/buildsuggest` endpoint for test integration
* index all children and parent objects on changes
* fixed XSLT problem when exporting using newly uploaded XSL files
* better error handling

### EAS

* enforce UTF-8 for JS files
* strip NULL bytes from metadata values, fixing database errors

### Webfrontend

