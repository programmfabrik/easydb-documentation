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

*improved*

* click on background executes "close" action on non-fullscreen modal dialogs
* detail/export of single objects now uses the selected mask
* connector: support improved for downloads, and link share
* connector: log login and logout events remotely
* editor: honor show tags option for linked objects
* column filters: honor column filters also for users with system.root system right
* make metadata mapping more intuitive
* improved JSON logs
* improved usability when selecting & removing large quantity of objects
* object types and masks now show their database name next to the display name

*fixed*

* use Esc key to close layers
* several bug fixes in metadata mapping

### Fylr

* improved zip error checking
