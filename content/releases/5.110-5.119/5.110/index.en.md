---
menu:
  main:
    name: "5.110 (December 2022)"
    identifier: "5.110"
    parent: "releases5110"
    weight: -610
---


> This update requires a re-index, schedule appropriate downtime / update time


# Version 5.110.0

*Released on 14.12.2022*

# Webfrontend

## New

* **PDF Creator**: Use of variable substitutions in fields possible

## Improved

* **Detail Display**: Identifiers in file properties translated
* **Tag Filter Defaults plugin**: Pool filter now possible

## Fixed
* **Collection Settings**: Display of wrong field for uploading corrected
* **PDF Creator**: under certain circumstances PDF creation could fail when using assets from the default field
* **PDF Creator**: Field selection only worked on the first attempt
* **Export Manager**: Display of "Files" tab fixed
* **Video Player**: Improved display of quality selection in Safari
* **General**: Logo loading fixed
* **Expert Search**: API error when completing file names fixed.


# Server

## Improved

* **Hotfolder/Collection upload**: use of target fields in reverse nested tables possible
* **General**: new data language "Hebrew" added

## Fixed

* **Janitor**: Fixed asset cleanup, there were errors with outdated pool watermarks.
* **EAS**: `target_size_min` option now works correctly with video to image conversion


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:115035c8035906f90d7d6bacb52137f018c669b70274a364df05d112ad39bb6c
docker.easydb.de/pf/eas                  sha256:84866d95f5029327c6ca65cadcabb9185f820ea1495ac24a9cd2ea34099fb3d5
docker.easydb.de/pf/elasticsearch        sha256:88770255956de0170b45b02574201d0e8b1516dae5023b1ae6b268ff3c6af4d1
docker.easydb.de/pf/fylr                 sha256:e737f296f9839ec2c0ac56454ca9e23d0f39edc666725c423bdf16206eb9f992
docker.easydb.de/pf/postgresql-11        sha256:2d9cd4da24fd7bc4748b3ad9cacd9354783b7fc9c150f59525bb51f085e289af
docker.easydb.de/pf/postgresql-14        sha256:c208c18c792e6513b862c120da45948ac49aa87c83bbca9af3fab685e0124206
docker.easydb.de/pf/server-base          sha256:f35fd7c750da2771bbba59515f98e207dc29813bee362b070ec008d8627fdea7
docker.easydb.de/pf/webfrontend          sha256:1b9668287c8dc73e37f2e209ad3d8a92a509f2663f822b5aa6cf7bf0bb6fa585
```

Translated with www.DeepL.com/Translator (free version)
