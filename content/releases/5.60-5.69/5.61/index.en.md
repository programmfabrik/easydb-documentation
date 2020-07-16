---
menu:
  main:
    name: "5.61"
    identifier: "5.61"
    parent: "releases569"
    weight: -561
---

# Version 5.61.1

*Published on 08.01.2020*

### Webfrontend

*Fixed*

* Fixed error on pending message confirmation

### Server

*Fixed*

* Fixed upload of video files

# Version 5.61.0

*Published on 18.12.2019*

### Webfrontend

*New*

* Terms of use may be shown at download

*Fixed*

* Status improved in objecttype/pool selector

### Server

*New*

* XML mapping may set additional XML attributes, used in Typo3 plugin
* Format of `date_range` aggregations limited, no arbitrary values possible anymore
* The container base got raised from stretch to buster, thus the kernel dependencies changed. Kernel 3.17 is now a minimum requirement.

*Fixed*

* Objecttype ACLs get cleaned up when pool management is activated for objecttype
* Languages of ad-hoc users get initialized from session
* Error handling improved when executing external programs
* Correct name of collection owner in error messages
