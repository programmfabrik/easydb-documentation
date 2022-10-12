---
menu:
  main:
    name: "5.84 (Late May 2021)"
    identifier: "5.84"
    parent: "releases589"
    weight: -584
---

> No re-index is required for this release.

# Version 5.84.0

## Web front end

### New

- **Geonames plugin**: Support from the PDF creator.
- **Mask management**: New option to not display the internally managed area in detail for date range fields.

### Improved

- **Accessibility** improvements.

### Fixed

- **Search**: Corrected display of the correct search view for older cookie settings.
- **Mask management**: Incorrect memory warning without changes has been corrected.

## Server

### Improved

- **Metadata mapping**: Base64 coded values are read.
- **User pseudonymization**: display name and email can be pseudonymized.

### Fixed

- **Metadata mapping**: The administration of profiles now deletes references in collections and exports.
- **Standard info**: sorting of assets remains stable and follows the mask sequence.
- **Database**: Improved error handling for linked objects.
- **Data model**: Creation of Boolean columns with UNIQUE has been fixed.
- **Database**: Output from older versions could lead to errors for object types with column names that were too long.

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:18099994c52753616a7a26b51873d88577c0f81a7825814dca04fbe302578673
docker.easydb.de/pf/eas                  sha256:6c8b18e12a94f4f01d7ab76eda7bea3dc1c1f88d0d2f23136e38c34460811417
docker.easydb.de/pf/elasticsearch        sha256:46de0c8ee8a42199a6804a80b22a875358b1152e9a385bb3a8abf307f6aad89d
docker.easydb.de/pf/fylr                 sha256:afdc4d3c39226800aa07d1dcbeea46d4612966dce91b2ac3748167533f85497f
docker.easydb.de/pf/postgresql-11        sha256:797bc55cc134c0e3f9d64692f9208755b4375dc260a1e258f9fa5eed6b67b4a9
docker.easydb.de/pf/server-base          sha256:ec0a7b623fab8443d183427baff69f43df4b7dc2f0a66b67f7671a47ea5a82e5
docker.easydb.de/pf/webfrontend          sha256:5eafc11466ec9761b38713e0c70545e96dc6953278fd6c49f95fab4c926258b4
```

