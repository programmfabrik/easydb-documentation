---
title: "177 - Publish"
menu:
  main:
    name: "Publish"
    identifier: "webfrontend/datamanagement/features/publish"
    parent: "webfrontend/datamanagement/features"
---
# Publishing with DOIs

DOIs (Digital Object Identifiers) are unique and permanent digital identifiers for physical or digital objects (in this case for easydb data records) that are assigned by so-called collectors. Collectors are registries that assign DOIs or URNs, such as [DataCite](https://doi.datacite.org/). 

In order to connect a DOI issuing authority such as DataCite, a so-called [workflow](../../../rightsmanagement/tags) must be configured, which calls a [webhook](../../../../../en/technical/plugins/webhooks/webhook) when a "Publish" tag is assigned, for example. The code of the webhook registers a URL with the DOI registry and uses [/api/publish](../../../../../en/technical/api/publish) to report the assigned DOI back to easydb.

The connected collectors must be defined in the [basic configuration](../../../administration/base-config/export).

If activated on the [mask](../../../administration/datamodel/mask) in the data model, these publications of a data set can then be viewed in the detailed view. 

The DOI allocation and the creation of the webhook are not carried out by Programmfabrik GmbH. An example plugin can be found on [GitHub](https://github.com/programmfabrik/easydb-publish-datacite).
