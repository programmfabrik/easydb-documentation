---
menu:
  main:
    name: "5.73 (Mitte September 2020)"
    identifier: "5.73"
    parent: "releases"
    weight: -573
---

> There is a big version jump in the Elasticsearch container (**5.x to 7.x**). For this reason a **re-creation of the index** is necessary. Normally the upgrade does not require any additional steps, but in individual cases problems may occur. More information can be found in section **Elasticsearch 7**.

# Version 5.73.0

*Released on 09.16.2020*

## Webfrontend

*New*

- Search: Support of a **third sorting** level.
- Search: sorting for **string fields** with type numeric is now possible.

*Improved*

- Detail: It is no longer possible to select the **language settings** directly on the text field.
- Export: The custom field selection now works more precisely when showing and hiding fields.

*Fixed*

- **Detail view**: Update problems for the preview display have been fixed.
- **Table view**: Various minor fixes for displaying certain more complex data models.
- Metadata mapping: Minor inconsistencies between server and web frontend were fixed.
- Printing: A bug in the **print manager** in connection with various masks was fixed.
- Editor: The secondary search could only be opened once after using auto-complete.
- Workflows: The option to select system groups for email actions has been removed. 
- Folders: The automatic detection of series and versions has been fixed for some cases.
- Folders: Fixed **deep link** support for logged in and anonymous users. 
- Folders: Fixed a problem related to uploading objects where the file is created in a linked object with pool management.
- The user login is logged only once when logging in manually and not twice.
- Filters: The **faceting of date ranges** has been improved, now the same number is filtered as shown in the aggregation (both systems used the from field of the range).

# Server

*New*

- **/api/session/authenticate**: New parameter `log_event`. With this parameter an authentication without logging can be performed.
- /api/search: **sort** now supports *numeric* for fields of type string.
- /api/search: For **daterange** fields the appendix `.from` and `.to` is now supported for aggregation and search.
- Shibboleth: mapping of more user information at logins.

*Improved*

- Support of **Elasticsearch 7** (from 5)

*New*

- Fixed sorting of standard images for some cases related to linked objects.
- Memory leak in hot folder fixed.

### Elasticsearch 7

The update comes with Elasticsearch 7, normally there should be no problems, except if

- own **configuration** for Elasticsearch is used (block `config` in [elasticsearch.yml](/en/sysadmin/configuration/elastic/elasticsearch.yml/)). In this case the easydb-elasticsearch container will not start successfully.
- an **index template** for Elasticsearch is used (`elasticsearch.default_template` in [easydb-server.yml](/en/sysadmin/configuration/easydb-server.yml/available-variables/)). Here, errors could occur when the easydb-server creates the index.

- in particular if you have the following configuration, you should remove it and restart at least the server-container:

````yaml
  "store" : {
    "throttle" : {
      "type" : "merge",
      "max_bytes_per_sec" : "50mb"
    }
  },
````

Typically this is configured in the file `/srv/easydb/config/elastic_index_template.json`.

If the removal of the cited configuration is not solving your problems then you should have a look into the log of the Elasticsearch container (`docker logs easydb-elasticsearch`), the errors there should give hints how to proceed with the options used there. In case of doubt, the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/7.x/settings.html) should be consulted.

# Checksums

Here are the checksums of our docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:d5f7a58adaac58a12222938ef95187f0bbdac4700131b1c3bfae21cf3ee6421e
docker.easydb.de/pf/eas                  sha256:f8e2775ad3dd8edd307ae3727813f464a9fd7d448a1c3136c09de7d6fb388284
docker.easydb.de/pf/elasticsearch        sha256:6306674fb15197ddb371cbc63827891cf4be36b33338b92026b6f3b79f9ddc03
docker.easydb.de/pf/fylr                 sha256:9eefa5355209c9fdf288f8be42887a3096a24f8ce9ff03f14a8edc9bd355ccfa
docker.easydb.de/pf/postgresql-11        sha256:47a1737d6895da0b5fe2e2d41318283a6597489e1b0fa58e299bdef533958e28
docker.easydb.de/pf/postgresql           sha256:9a2e45b364c8e9b2f68f4f5a3d945c7ac1eef00fbe1b046f108dc6cebd2ac5f8
docker.easydb.de/pf/server-base          sha256:85bc26c8f0529ca7bfa28e1b35c4570fefe807dc55150fa9c8d6e5a48e8f65e1
docker.easydb.de/pf/webfrontend          sha256:d48c782dd4a857e0abd404b8374603a623ecbaa4548632d8cfb2a867de3ad155
```

*Translated with www.DeepL.com/Translator*

