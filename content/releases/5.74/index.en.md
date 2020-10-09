---
menu:
  main:
    name: "5.74 (October 2020)"
    identifier: "5.74"
    parent: "releases"
    weight: -574
---

> This release does not require a re-index.
>
> Starting with version **5.76** (scheduled for release on **18.11.2020**) **easydb** will only start with the newer **PostgreSQL version 11**. This cut is necessary to be able to use new features of PostgreSQL without endangering old installations. In addition, the old PostgreSQL version does not get security updates anymore. More information in the **[PostgreSQL 11](../5.73#postgres-11)** section.

# Version 5.74.1

*Published on 08.10.2020*

## Webfrontend

*Fixed*

- Fixed displaying thumbnails during upload.

# Version 5.74.0

*Published on 07.10.2020*

## Webfrontend

*Improved*

- Search: In the table view, multiple fields of a parent element are hidden as soon as the children are opened.
- Search: More display sizes in searches.

*Fixed*

- Fixed hidden tag support. Hidden tags were erroneously deleted when saving in the editor.
- Folders: With certain rights settings it could happen that not all folders of a user were displayed correctly.
- Presentations: The display of connector objects has been fixed in some cases.

## Server

*New*

- Server-side sorting of nested fields.

*Improved*

- /api/schema: When saving the schema, the type conversion support is improved.

*Fixed*

- Error handling for SSO logins with double logins has been improved.

# Checksums

Here are the checksums of our docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:d5f7a58adaac58a12222938ef95187f0bbdac4700131b1c3bfae21cf3ee6421e
docker.easydb.de/pf/eas                  sha256:e9c9ac0ad4a7edd7a0404bace2cdf4da84491cb841b6dfb17ddb9eb7af68e99c
docker.easydb.de/pf/elasticsearch        sha256:dcdffe49347544254e438029bcd5e784287842dfb4324c0ec4f2d96784bc2e7c
docker.easydb.de/pf/fylr                 sha256:8ff9ecc5244a497d7b5ebd59f34fa8592a949a4c5d3463dbe20c9148b178cfb8
docker.easydb.de/pf/postgresql-11        sha256:3e4f3df062810da94ec2feb7d54fa6c8aa271c600b57330086fe9c4c0623f0ff
docker.easydb.de/pf/postgresql           sha256:ba51aac137b64a3f5b79f29af94b98114994a34757d0f16885027f78b60c778c
docker.easydb.de/pf/server-base          sha256:c1798798ebf3ae8f8115bc5dc6789019bef64f9524fc87bde53a8cd04a76c56e
docker.easydb.de/pf/webfrontend          sha256:51de622e0f6282cc9e656b8489615a954f189451dc533bce720ed9ef31b39a40
```



*Translated with www.DeepL.com/Translator*