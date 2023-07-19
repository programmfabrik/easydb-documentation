---
menu:
  main:
    name: "5.119 (July 2023)"
    identifier: "5.119"
    parent: "releases"
    weight: -619
---


> This version **does not require** a new index build


# Version 5.119.1

*Released on 2023-07-17*

All images have been regenerated to include latest security fixes. Especially [CVE-2023-36664](https://nvd.nist.gov/vuln/detail/CVE-2023-36664) has been handled by updating the Ghostscript package.

# Webfrontend

## Fixed

* **Startup**: avoid slow search request

# Version 5.119.0

*Released on 2023-07-12*

# Webfrontend

## Improved

* **Search**: Search is automatically executed when query is processed
* **easydb-editor-tagfilter-defaults plugin**: Date entries are supported
* **General**: Indicator when areas in quick access are empty.

## Fixed

* **CSV Importer**: Fixed issue when selecting a reverse link field as destination.
* **General**: Date formats for some languages added (fi, sv, fr).
* **Print**: Fixed CSS issue where all languages were displayed in multiple input fields.
* **Downloads**: Fixed display of messages before asset download
* **Linked-Object-Filter**: fixed bug
* **Tooltips**: Fixed issue with tooltips staying open.
* **Search**: Behavior of the resource button for new instances corrected

# Server

## Improved

* Server-side nested sorting: support for asset columns (sorting by original file name).
* New data language Nepali (`ne`).

## Fixed

* EAS Supervisor no longer tries to handle failed originals.
* Cropping of raw images fixed, target format becomes JPEG instead of the unsupported source format.

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.119.1         sha256:3897719774c5d49d06666b1e057a2eff53e8fec0d4fede7f2d6ad5f744ede7de
docker.easydb.de/pf/eas:5.119.1            sha256:a330e408fa83835912cb73cc6e026e432b5b5371ceef7d24d2a55a912508edad
docker.easydb.de/pf/elasticsearch:5.119.1  sha256:c0ff7ea49dacff828684df73ed9373911c5c65187e651234cfa51da8f02879b5
docker.easydb.de/pf/fylr:5.119.1           sha256:4bf9bee704a51c2ce69dfab3e45b841e70aed9ddddf9548b3788e59ad020cda2
docker.easydb.de/pf/postgresql-14:5.119.1  sha256:28aecee9c57724a9e25342f55c345fb5135b0439935b9228731c92cb5aed120b
docker.easydb.de/pf/server-base:5.119.1    sha256:c44da8b6466d63eb88daeb4200501c0c0bbdac3880bd0d144310b3913771ccfc
docker.easydb.de/pf/webfrontend:5.119.1    sha256:1ea14ce8e391881e514a560f0e7ff56072c50642e6ec5a4585f660e312236f85
```
