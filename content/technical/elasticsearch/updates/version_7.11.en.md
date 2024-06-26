---
title: "Elasticsearch update 7.11" 
menu:
  main:
    identifier: "technical/elasticsearch/update7.11"
    parent: "technical/elasticsearch/updates"
---

# Elasticsearch update to 7.11

With easydb version 5.85 we started shipping this elasticsearch version.

In most installations this is not causing any problems, but in some there is the setting `reclaim_deletes_weight` still present, which is not understood by elasticsearch any more. It prevents a re-index and thus many easydb operations.

This setting is part of the elasticsearch index template, not of the configuration files.

Symptoms:
- easydb frontend shows `An Elasticsearch error occurred.`
- In German: `Ein Fehler ist bei Elasticsearch aufgetreten.`
- The above error messages can have other causes (e.g. not enough reserved memory for elasticsearch) but the following cannot:
- Log messages (e.g. in the file `/srv/easydb/easydb-server/var/imexporter.log`) shows `unknown setting [index.merge.policy.reclaim_deletes_weight]`. If the Linux command `grep reclaim_deletes_weight /srv/easydb/easydb-server/var/imexporter.log` lists any found line, then you have confirmed that this easydb instance has (or had) this problem.

Solution:
- If you are a maintenance customer of Programmfabrik GmbH we have already done this on the maintained instances.
- Upload a minimal index template without old settings. In a typical installation, as Linux user `root`, you can do this with:

```
docker exec easydb-server curl -XPUT -H 'Content-Type: application/json' http://easydb-elasticsearch:9200/_template/default -d @/easydb-5/base/es_default_template.json
```

Caveats:
- If you are affected by the old setting then you may also have the following easydb configuration:

```
elasticsearch:
  default_template: elastic_index_template.json
```

 - The cited lines are usually found in `config/easydb-server.yml` or `config/easydb-server.d/*.yml`
 - This setting uploads an index template in case there is no index template in elasticsearch at all, yet. Since you already have an index template by now, this automatic upload will only happen again if you reset your elasticsearch to a very basic state, for example during disaster recovery. The referenced file `elastic_index_template.json` (usually in folder `config/`) may very well contain obsolete settings like `reclaim_deletes_weight`. Thus we recommend to prevent its future upload by removing the `default_template` setting in your easydb-server configuration. Removing it will cause the upload to fall back to an easydb-builtin minimal index template without obsolete settings.
 - Or, if you keep the setting, make sure that `elastic_index_template.json` does not contain `reclaim_deletes_weight` any more.

- The above recommended builtin minimal index template does of course not contain any adjustments you have made to your index template. That said, as far as we know, no customer adjusted this part of elasticsearch - except customers with more than one elasticsearch node. So only if you went out of your way to change the index template, then also incorporate your changes to the index template before uploading it into elasticsearch with curl.

If you have questions, please send them to support@programmfabrik.de or if you have a login to our ticket system: https://tickets.programmfabrik.de/newticket

