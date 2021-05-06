---
menu:
  main:
    name: "5.73 (Mid September 2020)"
    identifier: "5.73"
    parent: "releases579"
    weight: -573
---

> There is a big version jump in the Elasticsearch container (**5.x to 7.x**). For this reason a **re-creation of the index** is necessary. Normally the upgrade does not require any additional steps, but in individual cases problems may occur. More information can be found in section **[Elasticsearch 7](#elasticsearch-7)**.
>
> Starting with version **5.76** (scheduled for release on **18.11.2020**) **easydb** will only start with the newer **PostgreSQL version 11**. This cut is necessary to be able to use new features of PostgreSQL without endangering old installations. In addition, the old PostgreSQL version does not get security updates anymore. More information in the **[PostgreSQL 11](#postgres-11)** section.

# Version 5.73.1

*Published on 24.09.2020*

## Webfrontend

*Improved*

- A configured **browser favicon** is now already loaded at login and not afterwards.

## Server

*Fixed*

- **/api/search**: Fixed search by date (year + year and month only)

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

* own **configuration** is used for Elasticsearch (block `config` in [elasticsearch.yml](/en/sysadmin/configuration/elastic/elasticsearch.yml/)). Some lines may prevent the `easydb-elasticsearch` container from starting successfully.

* a **index template** for Elasticsearch is used (`elasticsearch.default_template` in [easydb-server.yml](/en/sysadmin/configuration/easydb-server.yml/available-variables/)). This could cause errors when the easydb-server creates the index.

* especially if you still use the following configuration, you should remove this block and restart at least the server-container:

````yaml
  "store" : {
    "throttle" : {
      "type" : "merge",
      "max_bytes_per_sec" : "50mb
    }
  },
````

Typically this is found in the file `/srv/easydb/config/elastic_index_template.json`.

* check your **index template** also for the following line and remove it: (otherwise it will prevent the creation of the suggest-indexes)

````yaml
    "mappings" : { },
````

After removing this line the template must be transferred to Elasticsearch:

```
curl -H 'content-type: application/json' -XPOST $ES_URL/_template/default -d@elastic_index_template.json
```

Replace '$ES_URL' with for example http://localhost:9200 or wherever your Elasticsearch can be reached. Check the accessibility e.g. with the harmless listing of the indexes: `curl http://localhost:9200/_cat/indices`

* If `cluster.routing.allocation.disk.watermark.high` or `cluster.routing.allocation.disk.watermark.low` are set, you must now also configure `cluster.routing.allocation.disk.watermark.flood_stage`, otherwise Elasticsearch complains somewhat cryptically, because one value is absolute (in GB) and the other value is relative (default, in percent).

* For large data models you will reach the limits of the ES default configuration if the mapping is larger than the 100MB allowed per POST. ES7 now makes this more likely because there is no longer one mapping per mask, but the mapping for the entire data model is uploaded in one piece. Example for an increase ([elasticsearch.yml](/en/sysadmin/configuration/elastic/elasticsearch.yml/)):

````yaml
config:
  "http.max_content_length": "200mb"
````

* For installations with more than one node: (unusual for our customers, default is single-node): Here you have to set now, in [elasticsearch.yml](/en/sysadmin/configuration/elastic/elasticsearch.yml/):

````yaml
discovery-type: zen
config:
  "cluster.initial_master_nodes" [ "n1.example.com", "n2.example.com" ]
````

If these corrections are not sufficient, a look into the log of the Elasticsearch container (`docker logs easydb-elasticsearch') is necessary, the errors there should give hints how to proceed with the options used there. In case of doubt, the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/7.x/settings.html) should be consulted.

* For example the error message 'IndexNotAvailableException [...] Trying to create too many buckets' can be solved without restarting by:

```
curl -XPUT -H 'Content-Type: application/json' http://localhost:9200/_cluster/settings -d '{"persistent": { "search.max_buckets": 262144 }}'
```

    (http://localhost:9200 is an example address, but in many cases it works locally on the server).

Additionally this should be included in the configuration file: ([elasticsearch.yml](/en/sysadmin/configuration/elastic/elasticsearch.yml/)

````yaml
config:
  "search.max_buckets": 262144
````

### Postgres 11

PostgreSQL version 11 is available for all customers since early 2020 and can be installed with [this guide](https://docs.easydb.de/en/sysadmin/installation/postgres-upgrade/). Unfortunately the process is not automatic but requires a Linux administrator.

Starting with **5.76** (planned release date: **18.11.2020**) the server makes a check on the PostgreSQL version and will not start if it is smaller than 11.

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

