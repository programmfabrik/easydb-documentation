---
title: "172 - Links / Deep Links"
menu:
  main:
    name: "Links / Deep Links"
    identifier: "webfrontend/datamanagement/features/deeplinks"
    parent: "webfrontend/datamanagement/features"
---
# Links / Deep links

Single and multiple records or files can be shared in easydb via Link/Deeplinks. Links/Deeplinks are available in easydb in several places.

## Search

In easydb you can perform a **search** via a simple search or the expert search and share the results of this search through a link. No special permissions can be configured for this link.

![Link to search](link_search_en.png)

> Note: http://picshare.5.easydb.de/search/ <search> can also be started directly with a full-text search.

**Saved Search** can be shared and shared with users and groups from the Finder. The share is configured via the context menu in the Finder. In the <code class="tab">Share</code> tab, you can create users and predefined or custom privileges (<i class =" fa fa-bars "> </i> options). The name of the folder can be changed in the <code class="tab">General</code> tab and a description of the folder can be adapted.

![Link to saved search](link_safed_search_en.png)

> NOTE: Note that you must save the settings before you can share the link.


Pool

A link to the pool and thus to all the records that are located in this pool can be called up and copied via the <i class = "fa fa-info-circle"> </i> button in the pool selection. No special permissions can be configured for this link.

![Link to the records of a pool](link_pool_en.png)

## Detail / Editor {#sidebar}

The <i class = "fa fa-share"> </i> (share-button) in the detail view can be used to create a link to the **record**. The weblink leads to the record in easydb. The deep link, if configured, leads to the output of the data record in XML format. The link displays the most recent version of the record. Older versions can also be accessed via this link when indicated with **version/< number >**. Further options for [Deep Links](https://docs.easydb.de/en/technical/api/objects) are listed in the technical part. No special permissions can be configured for this type of link. 

> Note: If you press `SHIFT` odr `Alt` at the same time as clicking on the share button, an url with the current session is created for the deep-link url to /api/objects. This way the record can be reached for test purposes, even if it is not or not yet released for the deep-link user.



![Link to the record](link_detail_asset_en.png)

The link to **file** can be sent via the <i class = "fa fa-ellipsis-v"> </i> options menu. This option is available from the detailed view and the editor. The links are generated according to the preconfigured versions and formats. No special permissions can be configured for this link.

![Link from detail view to the file](link_detail_file_en.png)

> NOTE: These links can be generated from the detailed view and the editor.

The links are shared with the Deep-Link user. If some URLs appear to be unavailable, this is because they are not shared. Please refer to [Basis Configuration](../../../administration/base-config) and the right-hand management under [System Rights](../../../rightsmanagement) for instructions on setting up deep links.


## Mappings

Folders can be shared and shared via the context menu in the Finder or the <i class = "fa fa-share"> </i> over the detail view for the user / group binder. In the <code class="tab">Share</code> tab, you can create users and predefined or custom privileges (<i class =" fa fa-bars "> </i> options). The name of the folder and the description of the folder can be adapted in the <code class="tab">General</code> tab. The uploading of assets into this folder can be activated in the <code class="tab">Upload</code> tab.

![Share and share folder](link_collection_en.png)

## Lists

A link to the record can be created from the lists. If the data set of an object type is opened in the detail view, a link to the **data set** can be created via the <i class = "fa fa-share"> </i> button. The weblink leads to the record in easydb. No special permissions can be configured for this link.

![Link to record from list](link_list_keyword_en.png)
