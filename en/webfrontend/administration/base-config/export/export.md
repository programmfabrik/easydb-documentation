# Export and OAI / PMH

Easydb provides several types of unauthenticated access to the files and data. For the accesses, on the one hand deep links and on the other OAI / PMH are available.

Use deep links when accessing a resource from the easydb directly, OAI / PMH can be used to monitor and load several resources as well as changes to resources.

## Deep-Link

The deep link releases are technically solved via the API interface [/api/objects](../../../technical/api/objects/objects.html). There you will find explicit information about the structure of the URL. In the front-end, you will find the deep links [Detail]() and the [EAS-Column (parts)]() in various places. Deep links are always authenticated by the user *DeepLink*. Give this user the necessary rights to the data to allow access from outside.


| Settings |  Explanation |
| ------ | -------- |
| Allow | Turning the deep link on and off. |
| Including visible reference to ID | Allows direct access by object ID, because these object IDs are continually assigned, it can be a security risk to unblock this option. A user who is made aware of a deep link can guess further deep links guess. For all deep links, however, the *DeepLink* user must have access to the objects for them to work. |
| Including visible reference to a unique field | Like the ID reference, they specify whether or not one-to-one data fields can be deep-linked |
| Show EAS URLs | This option allows direct file links in the. XML output of the deep links written. These links point directly to a file and are no longer right-managed. These URLs never lose their validity. Without this option, there are other URLs for accessing files in the XML. |

## OAI / PMH

The OAI / PMH interface is a harvesting interface. For more information, see the [Protocol Description](../../../technical/protocols/oai-pmh/oai-pmh.html) and [Open Archives](http://www.openarchives.org/).

The searches that perform the interface are performed with the system user *OAI / PMH*. Give this user the rights data to see.

| Settings |  Explanation |
| ------ |  -------- |
| Share | Switching the OAI / PMH interface on and off. |
| Repository Name | Name of the OAI / PMH repository. |
| Administrator email | Email specified in OAI responses.
| Namespace | Freely definable OAI Identifier Namespace. Objects can be requested using `oai:<namespace>:<uuid>` in the URL. |
| Tag Sets | Define tag filters to create new OAI / PMH sets. They may be e.g. All objects that have the tag *Internet*. |
| Show EAS URLs | As with the deep links, this determines whether the direct file links will be output in the XML or not. See Deep link. |
| Embed linked objects | As for the XML Export, linked objects are not loaded and embedded in the XML Document. If "Not included in main search" option is selected, all linked objects that are not included in the main search are loaded and embedded during the export. If "None" is selected, no linked objects are loaded, but only the standard is exported. |

### XSLT Formats

In addition to the standard easydb format and [Dublin Core](http://dublincore.org/) (which is mandatory for OAI-PMH), the OAI/PMH interface can provide custom formats (e. g. LIDO). To use Dublin Core, a Dublin Core mapping must be set up in [Metadata Mapping](../../profiles/profiles.html). Then it must be also linked to the corresponding [object type](../../datamodel/objecttype/objecttype.html). For these formats, an XSLT must be created that converts the standard easydb format. The OAI/PMH interface provides a metadata format for each uploaded XSLT.


| Settings |  Explanation |
| ------ |  -------- |
| OAI / PMH prefix | Technical name of the format in the OAI / PMH interface. |
| Display Name | Display name of the format in the XML of the OAI / PMH interface. |
| Description | Description of the format in the XML of the OAI / PMH interface. |
| XSLT | XSLT file for transforming the data. |



