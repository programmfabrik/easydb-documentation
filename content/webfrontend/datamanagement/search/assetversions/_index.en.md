---
title: "183 - Asset versions"
menu:
  main:
    name: "Asset versions"
    identifier: "webfrontend/datamanagement/search/assetversions"
    parent: "webfrontend/datamanagement/search"
---
# File Versions

easydb can manage multiple versions per file. For example, these can be sections of a file or retouched, improved versions. These are not the preview versions. These are automatically created and managed by easydb.

![](versions_menu_en.png)


## Display versions

![Displaying Versions](versionen_detail_en.png)

From the detail view you can view the versions created for this dataset by clicking on the <i class="fa fa-ellipsis-v"></i> Options button. The editor provides tools for creating versions.

## Create versions

![Show versions with zoom enabled](versionen_editor_en.png)

* Use <i class="fa fa-upload"></i> to upload new versions.
* Use <code class="button">-</code> to remove the selected version from the list.
* Use the mouse to change the order of the versions by drag & drop. The top version is the *preferred version*. This version is used in the detail view and in the file preview editor.
* You can give each version its own name. The name is only displayed here.
* Confirm your changes with <code class="button">Take over</code> to save them for the record.

## Asset Tools

|Button|Function | Explanation|
|---|---|
|<i class="fa fa-rotate-left"></i>|Turn left (each 90°)|Turn the image to the left. There's no stepless rotation planned at the moment.
|<i class="fa fa-rotate-right"></i>|Turn to the right (each 90°)|Turning the image to the right. There's no stepless rotation planned at the moment.
|<i class="fa fa-arrows-v"></i>|mirror vertical|mirror the image on the vertical axis. |
|<i class="fa fa-arrows-h"></i>|Mirror horizontally|Mirror the image on the horizontal axis. |
|<i class="fa fa fa-refresh"></i>|Reset|Resets the image back to its original state. |
|<i class="fa fa-crop"></i>|Crop|Start the Crop tool. With <code class="button">Create Version</code> you can create a new version of the file with your cut. It'll appear at the bottom of the list.


### Images

|Tool|Explanation|
|---|---|
|<code class="button">Zoom</code>|Starting Zoom View. |
|<code class="button">Metadata</code>|Display unchanged metadata from the file at the time of uploading. |

### Office & PDF

|Tool|Explanation|
|---|---|
|<code class="button">View</code>|Starts the overview view for the PDF. |
|<code class="button">Metadata</code>|Display unchanged metadata from the file at the time of uploading. |

### Video

|Tool|Explanation|
|---|---|
|<code class="button">Video</code>|Starts the video mode to play the file. |
|<code class="button">Metadata</code>|Display unchanged metadata from the file at the time of uploading. |

### Audio

|Tool|Explanation|
|---|---|
|<code class="button">Audio</code>|Starts the audio mode to play the file. |
|<code class="button">Metadata</code>|Display unchanged metadata from the file at the time of uploading. |

