---
title: "109 - OAI/PMH"
menu:
  main:
    name: "OAI/PMH"
    identifier: "technical/protocols/oai-pmh"
    parent: "technical/protocols"
---
# OAI / PMH

The Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) was first developed in the late 1990's as a standard for harvesting metadata from distributed metadata/data repositories. The current version of the OAI-PMH standard is 2.0 as of June 2002, with minor updates in December 2008.

More information about the standard can be found here: [http://www.openarchives.org/](http://www.openarchives.org/OAI/openarchivesprotocol.html)

## Configuration

The OAI / PMH protocol is offered as base plugin ("oai"). Be sure to enable it in the Base Configuration in order to use it.

OAI / PMH is configured in the base configuration tab "Export and OAI / PMH". In order to use it, first enable it using the checkbox and then fill in the fields:

- Repository-Name: information provided by [Identify](/en/technical/protocols/oai-pmh) (repositoryName)
- Administrator-E-Mail: information provided by [Identify](/en/technical/protocols/oai-pmh) (adminEmail)
- Namespace: namespace used in identifiers

## API

The OAI / PMH can be accessed under:

    GET/POST /api/plugin/base/oai/oai

The parameters are defined in the [OAI / PMH standard](http://www.openarchives.org/OAI/openarchivesprotocol.html).

## <a name="Repository"></a>Repository

The easydb provides the information configured in the base configuration tab "OAI / PMH" to identify the repository.
The granularity offered is `"YYYY-MM-DDThh:mm:ssZ"` and the deletedRecord policy is set to `"no"`.

The repository consists of all user objects that can be seen by the system user "OAI/PMH".
That means, that the rights management settings allow to control which objects are offered via OAI/PMH.

The objects are identified by their UUID like this: `oai:<namespace>:<uuid>`

## Metadata Formats

The easydb always disseminates all available formats to all objects.

As per OAI / PMH standard, **Dublin Core (oai_dc)** is offered as Metadata format.
It is possible to define mapping profiles for Dublin Core under Profile > Dublin Core.
These mapping profiles work like any other easydb profile, so they can be configured per objecttype and pool.
The OAI / PMH will use the configured profile to generate the Dublin Core representation for the object.
If no profile is configured, a minimal representation is returned.

Another metadata format that is always provided by the easydb is the **easydb** export format.
This format is basically an XML representation of the object in the given mask and it is very similar to the JSON representation that is normally used by the API.

Besides those two formats, more formats can be defined using the base configuration, tab "Export and OAI / PMH", table "XSLT formats".
There is a column "Name (OAI/PMH prefix, name in Deep-Links with /api/objects)" that is used to identify the XSLT file. The prefix must be conform to the standard and unique.
Notice that `"oai_dc"` and `"easydb"` are already used.

To enable the XSLT file to be used as a Metadata Format for OAI / OMH, enable the Checkbox "Use for OAI/PMH". Make sure that you use XSLT files that output valid XML when activating them for OAI / PMH.

Optionally, you can specify a namespace and a schema for the Metadata Format.

## Sets

The easydb supports the following sets:

* Objecttypes:
  - all objecttypes
  - example: `<setSpec>objecttype:sample_object</setSpec>` for all objects of objecttype `sample_object`
- Pools:
  - all pools that the user "OAI/PMH" can see (`bag_read` right)
  - example: `<setSpec>pool:1:2</setSpec>` for all objects in the Standard Pool
- Collections:
  - all collections that the user "OAI/PMH" can see (`bag_read` right)
  - example: `<setSpec>collection:1:3</setSpec>` for the default user collection of the user "OAI/PMH"
- Pools and objecttypes:
  - all combinations of pool managed objecttypes and pools that the user "OAI/PMH" can see (`bag_read` right)
  - example: `<setSpec>objecttype_pool:sample_object:pool:1:2</setSpec>` for all objects of objecttype `sample_object` in the Standard Pool
