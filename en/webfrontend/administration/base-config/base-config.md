# Basic configuration


## General


| Settings | | Explanation |
| ------ | - | -------- |
| Name of the easydb | | The easydb name is used as the directory name and ZIP prefix exports. Also, it is the name of the easydb as it appears in logs and administrator emails. |
| Display name | | Name of the easydb as it is displayed in the web browser (as document title). This field is multilingual. |
|Terms of Use | Frontend | The front-end languages ​​are the languages ​​available to end users. <br>_The listed languages ​​are fixed on the server side and can not be changed._ |
| | Database | The database languages ​​are the languages ​​available to end users for data modeling and input as well as search. <br>_The listed languages ​​are fixed on the server side and can not be changed._ |
| Administrator updates | | Administrator emails can be specified. Easydb sends such emails, at the following events: server_start, server_shutdown, ... |
|Permitted origin address || URLs from which third-party browser access is to be allowed. The URLs must be complete with log. For example "http://myown.easydb.api.example.com" |
|User Activity Logging |Search Logs|  Records user search requests. |
| | Login / Logout |  Records a user's login and logout events. |
| | Detail View Logs | Records the views of a detail view. |
| | Asset upload Logs | Records the upload of an asset by a user. |
| | Export download Logs  | Records the download of an export by a user. |
| | Asset download from an export Logs | Records the download of an asset from an export by a user. |
| Autocomplete | When ||
|| extent ||
| System addresses | sender ||
|| envelope sender ||
| API-Call Logs |||
|| active | here it is determined if and which logs are made in easydb |
|| log the following calls | the checkboxes can be used to define the calls that are to be logged |

## Upload

This tab defines global limits for uploads (uploading assets in easydb).

| Settings | | Explanation |
| ------ | - | -------- |
| Upload limit | | The global upload limit in bytes. If an upload is larger, it is rejected in any case, even if other values ​​are set by means of the management. |
| _File class_ | Limit | A separate limit can be defined per file class. If it is larger than the global upload limit, it is ignored. |
| | Type | Only the formats for an upload are accepted, which are activated here. For the file class _Sonstige_, all formats that are not listed in one of the other file classes are always allowed. |

## Log In

You can make settings for the login under this tab.

| Settings | | Explanation |
| ------ | - | -------- |
| Anonymous over Internet allowed || When calling the main easydb URL (http://<easydb-server>/), this setting specifies that an unknown user is logged into the system as an anonymous user. Each anonymous user is automatically in the group `Anonymous user` and can be given rights. Easydb stores a browser cookie with the user, which he will be recognized the next time and assigned internally to the same user ID. This allows the user to save user settings, etc. Whether or not a user comes from the Internet is defined by _Intranet configuration_ |
| Anonymous over Intranet allowed || How *allows Anonymous over Internet* only that this setting applies to users who have been recognized as intranet users|
| Intranet configuration | | Here, IP addresses (172.16.0.2) and networks (eg 192.168.0.0/16) are stored, which are valid as _Intranet_. When the server is called, the IP address of the call is determined and a corresponding classification is made |
| Forgotten passwords can be requested || If active, the user is offered to log on to the login page via his registered email address a forgotten password. This setting is valid for all users. It can not be restricted (ugs) |
| Wallpapers | | For the login page, a background image can be uploaded. A default image is set in the .ini variable `[default-pics] background`. Make sure the image is large so that no artifacts are visible for large screens |
| Greeting | | The welcome text can be stored in multiple languages ​​for the login page. Here is only text allowed, no HTML |
| Password Verification | Policy | Set +/- rules to verify user passwords. The password is checked using a regular expression. With _Minimum_ and _Maximum_ they determine how often the regular expression must be found at least and can be found at most |
| | Note | The multilingual text tells the user what he has to do with his password |
| Repeat passwords | | Easydb saves all passwords (encrypted) used by the user. For reused passwords, you can specify how old a password may be |
| | _Immer_ | A password must never be reused. |
| | _Monat_ | A password can not be reused in the same month. |
| | _Niemals_ | The server turns off the check for repeated passwords. |

## Design {#design}

| Settings | | Explanation |
| ------ | - | -------- |
| Logo & Header |||
|| Logo | The logo can be uploaded. It is displayed in the original resolution and in the original format at the upper right. Use mouse wheel + move to adjust the logo. A path to a default image can be defined using the .ini variable `[default-pics] logo`. |
|| background color | Select background color for the logo. |
| CSS-Deteine ​​|| Create your own design for easydb. |
|Map settings|Show [map in detail](/webfrontend/datamanagement/search/detail/detail.html)|Displays the thumbnail of a file in a map, if the file contains geocoordinates.|

When the CSS plugin (default) is loaded, input fields for modifying the loaded CSS appear here. The CSS plugin detects when the specified URLs change and provides a new CSS for the application. Also use the [CSS-Developer] tool to get more overview of the loaded SCSS files.

The easydb's CSS is created in [SCSS](http://sass-lang.com/).

### CSS files

| Settings |  Explanation |
| ------ |  -------- |
| Header | Here you can specify URLs for SCSS files that are loaded before the header SCSS of the easydb. |
| Body | Here, URLs can be specified for SCSS files that are loaded after the body SCSS of the easydb. |
| Footer | Here, URLs can be specified for SCSS files that are loaded after the footer SCSS of the easydb. |


## Export and OAI / PMH

Easydb provides several types of unauthenticated access to the files and data. For the accesses, on the one hand deep links and on the other OAI / PMH are available.

Use deep links when accessing a resource from the easydb directly, OAI / PMH can be used to monitor and load several resources as well as changes to resources.

### Deep-Link

The deep link releases are technically solved via the API interface [/api/objects](../../../technical/api/objects/objects.html). There you will find explicit information about the structure of the URL. In the front-end, you will find the deep links [Detail]() and the [EAS-Column (parts)]() in various places. Deep links are always authenticated by the user *DeepLink*. Give this user the necessary rights to the data to allow access from outside.


| Settings |  Explanation |
| ------ | -------- |
| Allow | Turning the deep link on and off. |
| Including visible reference to ID | Allows direct access by object ID, because these object IDs are continually assigned, it can be a security risk to unblock this option. A user who is made aware of a deep link can guess further deep links guess. For all deep links, however, the *DeepLink* user must have access to the objects for them to work. |
| Including visible reference to a unique field | Like the ID reference, they specify whether or not one-to-one data fields can be deep-linked |
| Show EAS URLs | This option allows direct file links in the. XML output of the deep links written. These links point directly to a file and are no longer right-managed. These URLs never lose their validity. Without this option, there are other URLs for accessing files in the XML. |

### OAI / PMH

The OAI / PMH interface is a harvesting interface. For more information, see the [Protocol Description](../../../technical/protocols/oai-pmh/oai-pmh.html) and [Openarchives](http://www.openarchives.org/).

The searches that perform the interface are performed with the system user *OAI / PMH*. Give this user the rights data to see.

| Settings |  Explanation |
| ------ |  -------- |
| Share | Switching the OAI / PMH interface on and off. |
| Repository Name | Name of the OAI / PMH repository. |
| Administrator email | Email specified in OAI responses.
| Namespace | Freely definable OAI Identifier Namespace. Objects can be requested using `oai:<namespace>:<uuid>` in the URL. |
| Tag Sets | Define tag filters to create new OAI / PMH sets. They may be e.g. All objects that have the tag *Internet*. |
| Show EAS URLs | As with the deep links, this determines whether the direct file links will be output in the XML or not. See Deep link. |

#### XSLT Formats

In addition to the standard easydb format and [Dublin Core](http://dublincore.org/) (which is mandatory for OAI-PMH), the OAI/PMH interface can provide custom formats (e. g. LIDO). To use Dublin Core, a Dublin Core mapping must be set up in [Metadata Mapping](../profiles/profiles.html). Then it must be also linked to the corresponding [object type](../datamodel/objecttype/objecttype.html). For these formats, an XSLT must be created that converts the standard easydb format. The OAI/PMH interface provides a metadata format for each uploaded XSLT.


| Settings |  Explanation |
| ------ |  -------- |
| OAI / PMH prefix | Technical name of the format in the OAI / PMH interface. |
| Display Name | Display name of the format in the XML of the OAI / PMH interface. |
| Description | Description of the format in the XML of the OAI / PMH interface. |
| XSLT | XSLT file for transforming the data. |

## Cloud service provider

## CMS

Connecting CMS-Systems in easydb works via [Plugins](/webfrontend/datamanagement/features/plugins/plugins.html). The settings for the connection of CMS systems are made here.

| CMS | Input field | Description |
| - | - | - |
| Wordpress | Instance name | One or more instances can be created here. One name must be assigned per instance. |
|| URL | The URL of the WordPress instance to be transported to the media
|| Authentication | Authentication type, Loginname us password for Wordpress administration. |
| Falcon.io | Instance name | One or more instances can be created here. One name must be assigned per instance. |
|| API_Key | The generated unique key provided by Falcon.io for use of their RESTful API |
