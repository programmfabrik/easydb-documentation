---
menu:
  main:
    name: "5.94 (January 2022)"
    identifier: "5.94"
    parent: "releases"
    weight: -594
---

> This version brings **accelerated loading time** of the application. In some tests **easydb** now loads up to **5x faster** than before. This acceleration could be achieved by massive parallelization during initial loading of required resources. 
>
> **5.94.1.** brings the latest Elasticsearch version [7.16.3](https://www.elastic.co/guide/en/elasticsearch/reference/current/release-notes-7.16.3.html), which solves the **log4j** security issue.

# Version 5.94.2

*Released on 18.01.2022*

## Webfrontend

### Fixed

- **Detail**: fixed render bug with certain nested data.

# Version 5.94.1

*Released on 14.0.12022*

## Webfrontend

### Fixed

- **Object type manager**: fixed error when saving.
- **Collection**: link for an anonymous user was fixed.
- **Detail**: Fixed a JS error when opening the asset version dialog.
- **PDF Printing**: The display of images was fixed again.

## Server

### Fixed

- **Elasticsearch Docker image** is now version  [7.16.3](https://www.elastic.co/guide/en/elasticsearch/reference/current/release-notes-7.16.3.html)  with a fix for the **log4j** security issue.

# Version 5.94.0

*Released on 12.01.2022*

## Webfrontend

### New

- **Fullscreen**: Display of detail information is in new design and to the right of the fullscreen display.
- **Editor**: When copying, it is now possible to select whether reverse nested objects are also copied or not.

### Improved

- **Optimization** of application loading time.
- **Filtertree**: Output of duplicate labels for multiple fields has been suppressed.
- **Search**: display of hierarchical objects with long names has been improved 

### Fixed

- **Detail**: Info > Version sometimes had problems displaying more complex version hierarchies.
- **PDF printing**: It could happen that some images were not displayed in the PDF.
- **Accessibility attributes** for some inputs were corrected.

## Server

### New

- **Easdb asset server:** SVG support in `vector2d`.
- **Group Edit Mode**: Update the pool in reverse nested objects.
- **Transitions**: Email from pool contact can be used for **transition emails**.

### Improved

- **Performance** improvements for **session requests**. 
- **Performance** improvements for type `message` searches.
- Elastic mapping optimizations with many configured languages and custom data types.

### Fixed

- Fixed an **indexing issue** when importing hierarchical objects.

# Checksums

Here are the checksums of our Docker images (latest version): 

```ini
docker.easydb.de/pf/chrome               sha256:159c4b4bc369dffa9751cbcc040a244bf5b2c6cc7856366afe5ba7a0c48b8b28
docker.easydb.de/pf/eas                  sha256:03bedfbf2b538ca64e4252fe90bafd98ef46ed3d48122eff94b81775b8793010
docker.easydb.de/pf/elasticsearch        sha256:4dcd768f26abab24ea894642619541b7993885521925130599b408991fbc1444
docker.easydb.de/pf/fylr                 sha256:2b10cafd9de76f064cc8b90afa9c5103fafd5baafd69912c6cb245ed172f632b
docker.easydb.de/pf/postgresql-11        sha256:8aa9ff8cbc673b2b1f234b9fe058a3bf1544ea8074cebef45d35dba8081f8afa
docker.easydb.de/pf/server-base          sha256:f6a6c64531032a385c254dcda2fd9f731ecacf9c40f1edbe501c9412b118ff12
docker.easydb.de/pf/webfrontend          sha256:6a194066a3ffc9de146ee7b0508d971942ca12fa9534bda956c6fb036bc6e345
```

*Translated with www.DeepL.com/Translator*

