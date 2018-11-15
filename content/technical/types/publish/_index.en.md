---
title: "133 - Publish"
menu:
  main:
    name: "Publish"
    identifier: "technical/types/publish"
    parent: "technical/types"
---
# Publish

An object containing publishing information.

| name | description |
|---|---|
| `_basetype` | base type name (string, r): always `publish` |
| `_timestamp_created` | date and time when published in ISO 8601 format (string, r) |
| `publish` | publish attributes |
| &#8614; `_id` | ID of publishing object (integer, unique, r) |
| &#8614; `system_object_id` | system object ID of record being published (integer, rw) |
| &#8614; `version` | version of the published record (integer, rw, optional) |
| &#8614; `collector` | name of the collector which triggered the publishing (string, rw) |
| &#8614; `publish_url` | external URL where the object is published (string, rw) |
| &#8614; `easydb_url` | easydb URL used for publishing the object (string, rw) |
