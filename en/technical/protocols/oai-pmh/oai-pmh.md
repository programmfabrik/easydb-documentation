# OAI / PMH

The Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) was first developed in the late 1990's as a standard for harvesting metadata from distributed metadata/data repositories. The current version of the OAI-PMH standard is 2.0 as of June 2002, with minor updates in December 2008.

More information about the standard can be found here: [http://www.openarchives.org/](http://www.openarchives.org/OAI/openarchivesprotocol.html)

## Configuration

The OAI / PMH protocol is offered as base plugin ("oai"). Be sure to enable it in the YAML configuration in order to use it.

OAI / PMH is configured in the base configuration tab "Export and OAI / PMH". In order to use it, first enable it using the checkbox and then fill in the fields:

- repository name: information provided by [Identify](/technical/protocols/oai-pmh/oai-pmh.md#Repository) (repositoryName)
- adminitrator e-mail: information provided by [Identify](/technical/protocols/oai-pmh/oai-pmh.md#Repository) (adminEmail)
- namespace: namespace used in identifiers

## API

The OAI / PMH can be accessed under:

GET/POST /api/plugin/base/oai/oai

The parameters are defined in the [OAI / PMH standard](http://www.openarchives.org/OAI/openarchivesprotocol.html)).

## <a name="Repository"></a>Repository

The easydb provides the information configured in the base configuration tab "OAI / PMH" to identify the repository.
The granularity offered is "YYYY-MM-DDThh:mm:ssZ" and the deletedRecord policy is set to "no".

The repository consists of all user objects that can be seen by the system user "OAI/PMH".
That means, that the rights management settings allow to control which objects are offered via "OAI/PMH".

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
There is a column "OAI / PMH prefix" that is used to mark the format as available for "OAI / PMH". The prefix must be conform to the standard and unique.
Notice that "oai_dc" and "easydb" are already used.

These formats are shared between Export, which supports various output formats, and OAI / PMH, which only supports XML,
so make sure that you use XSLT files that output XML when activating them for OAI / PMH.

## Sets

The easydb supports the following sets:

- objecttypes: all objecttypes
- pools: all pools that the user "OAI/PMH" can see (`bag_read` right)
- collections: all collections that the user "OAI/PMH" can see (`bag_read` right)
