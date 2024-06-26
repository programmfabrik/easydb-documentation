---
menu:
  main:
    name: "5.71 (August 2020)"
    identifier: "5.71"
    parent: "releases579"
    weight: -571
---

>This release **does not** require a re-index.

# Version 5.71.3

*Published on 14.08.2020*

## Web frontend

*Fixed*

* Various bug fixes for the new **table view**, especially in connection with hierarchies and reverse objects.
* With certain rights management settings the **detail view** was not loaded for some users. 

# Version 5.71.2

*Published on 10.08.2020*

## Web frontend

*Fixed*

- The new **table view** displayed too many fields in multiple fields.
- **Editor**: Display of errors in the form has been graphically fixed.

# Version 5.71.1

*Published on 06.08.2020*

## Web frontend

*Fixed*

- Fixed sharing collections when there are irregular **email** users.

## Server

*Fixed*

- Fixed error on database upgrade for quite old databases.

# Version 5.71.0

*Published on 05.08.2020*

## Web frontend

*New*

- **Search**: The table view of the search has been completely revised and redesigned.

*Improved*

- Opening and closing of the **Finder** is now done via a button.

*Fixed*

- Bug fixing in the **User-CSV-Importer** in connection with login names and upper and lower case.
- **Single-Sign-On**: Display of more information in case of login errors fixed.
- The display of saved searches was faulty for some users.
- Correct object selection when calling the editor within selected objects.
- Users without access to the search are no longer shown saved searches.

## Server

*New*

- When users log in via SSO (Single-Sign-On) or LDAP, the user information (email, name, groups) is updated. Previously, this information was only transferred during the first login.

*Improved*

- SSO: If there were errors while logging in, they are now better displayed on the SSO error page.
- **Acceleration of logins for connector** partners by parallelizing the requests.
- Preparations for new asset janitor.

*Fixed*

- Data model updates lead to less dead-locks in the database.
- Metadata mapping for data has been corrected for some cases.
- Improved re-indexing for updates in bi-directional top-level objects.
- **Email**: The configurable message stored in the workflow is now also written to the email.
- Bug fixes in the hotfolder.
- Improved UTF-8 handling in the Gazetteer plugin.

# Checksums

Here are the checksums of our docker images (latest version):

```ini
docker.easydb.de/pf/chrome        sha256:c797ded5694f320a2804eec746211ebb754c0506cd789063adcb4158a21e8a34
docker.easydb.de/pf/eas           sha256:2dc74cfe0e98999ef33016ff260a8817cc054e103a9d0215230b0de0a7a97568
docker.easydb.de/pf/elasticsearch sha256:bc1158ab95899270c04aa5e2e12fcfb6d386ac0db8ce90ce7cd68c0213ff25a3
docker.easydb.de/pf/fylr          sha256:f7edb6660514be738abf4b0c92cb3c605cce057be6b47475717b7de8b229643f
docker.easydb.de/pf/postgresql-11 sha256:28652aa27b33f768ca4faad084c65cea8fceddb274b99f93a1e583317c66241f
docker.easydb.de/pf/postgresql    sha256:4fa479c79d9d84553aa0c02a3c69ead4d1dbaed7567c01a662cf1717c101f4b2
docker.easydb.de/pf/server-base   sha256:4ae1067598b93196de7dacf422f8276027094fca8009251d5eae00ac44853220
docker.easydb.de/pf/webfrontend   sha256:0a29e6575a92b208ff6824109d51de93dc8de7f1f6eadfc061dee481404d6289
```



*Translated with www.DeepL.com/Translator*