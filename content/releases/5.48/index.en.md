---
menu:
  main:
    name: "5.48"
    identifier: "5.48"
    parent: "releases"
    weight: -548
---

# Version 5.48.0

*Published on 20.03.2019*

### Server

*New*

* In the base configuration the **logging and saving of personal data** can be set for Export-, Search- and Detail-View-Events can be set

* Pools can save Custom Data 

* In the base configuration numbers with a maximum value of `2^64 − 1` (UINT64) can be used

* **Upload-Limits for files** can be set for each file class

* A **complete reindexing** can be started from the context menu of the server statusmanager

*Improved*

* **EAS Supervisor** will stop polling for failed assets and asset versions

* **Performance of deleting** collections and objects in collections improved

* **Performance of reindexing** of objects improved

* Upload-Limit for all files: maximum of 25 GB

*Fixed*

* Objects with tags are reindexed when the tags are deleted

* After **login per SSO** the state of the session will be updated

* Error during the deleting of objects that contain a link to themselves (self-references) fixed

* Inheriting of sticky pool rights was fixed