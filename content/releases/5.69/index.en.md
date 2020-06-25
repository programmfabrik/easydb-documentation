---
menu:
  main:
    name: "5.69 (June 2020)"
    identifier: "5.69"
    parent: "releases"
    weight: -569
---

> This release does not require a re-index.

# Version 5.69.0

*Published on 24.06.2020*

### Web frontend

*New*

- **Mask management**: Support of `|`-separators in the standard.

*Improved*

- Improved browser check at startup.

*Fixed*

- Fixed the display of **metadata fields** in deeply nested data models.
- Fixed display of available tags when **changing pools** in the new editor.
- The editor could no longer be used after displaying historical object information.
- **CSV importer**: Improved error handling in connection with hierarchical imports.
- Detail display of open date ranges was corrected.

### Server

*New*

- For rendering `_standard` there is a new option **pipe**. This connects terms by `|`.

*Improved*

- Support of `lookup:_id`in reverse objects.
- **/api/user**: Performance improvement when loading many users.
- Better error handling in the custom data type updater.
- Sorting of bidirectional links is now saved, previously the order of links was not predictable.

Fixed

- Elasticsearch errors could occur in the **OAI/PMH** interface for larger indexes (**uuid** search)
- **/api/export**: Bug fixing when exporting with fixed asset IDs.
- **SSO**: Improved error handling for visible display of login errors.
- **/api/pool**: The deletion of pools could not be performed in certain cases.
- Fix updates in index after group editor with reverse objects.

# Checksums

Here are the checksums of our docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:62ac9147529a03491b3edc35898b076fad86be181c96be9b2b701962688623f5
docker.easydb.de/pf/eas                  sha256:1eb9b08f107be72fc601753715441f4200c64653f42a8c7dabb6b9dbbd7edd5f
docker.easydb.de/pf/elasticsearch        sha256:023e67865e375cdfc475a34cc44b69cf0b2fc12a574c43e4fc7ecc0e9f8ecca3
docker.easydb.de/pf/fylr                 sha256:786ea3419e7c1395b0b720b94afdc8a6f85a697a91e9ce159e0fac44df856db7
docker.easydb.de/pf/postgresql-11        sha256:df579b5bae260a3755c3edc48fd2b94df8df9944acef46328c04195027939037
docker.easydb.de/pf/postgresql           sha256:17c8ac88d8d37e805083fa3311b93520d0488e0115b1faa33cf78ce56b63dc74
docker.easydb.de/pf/server-base          sha256:4c8f5deb812f560ca6a0e15a6821c8be1944b0a0abeb865575f705a0f62a05da
docker.easydb.de/pf/webfrontend          sha256:b43ebeef3261d8bd806083f27d8b7c73c6a2d3508c632cc632b7278253c47605
```

*Translated with www.DeepL.com/Translator*