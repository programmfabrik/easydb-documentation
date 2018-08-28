---
title: "47 - Variants of filesize"
layout: config
menu:
  main:
    name: "Variants of filesize"
    identifier: "sysadmin/konfiguration/easydb-server.yml/produce"
    parent: "sysadmin/konfiguration/easydb-server.yml"
easydb-server.yml:
  - eas.rights_management.image.versions[].<class>.size_print
  - eas.rights_management.image.versions[].<class>.size_limit
  - eas.rights_management.image.versions[].<class>.export
  - eas.rights_management.image.versions[].<class>.rightsmanagement
  - eas.rights_management.image.versions[].<class>.group
  - eas.rights_management.image.versions[].<class>.zoomable
  - eas.rights_management.video.versions[].<class>.version
  - eas.rights_management.video.versions[].<class>.size_print
  - eas.rights_management.video.versions[].<class>.size_limit
  - eas.rights_management.video.versions[].<class>.export
  - eas.rights_management.video.versions[].<class>.group
  - eas.rights_management.video.versions[].<class>.rightsmanagement
  - eas.rights_management.video.versions[].<class>.standard
  - eas-rights_management.audio.versions[].<class>.version
  - eas-rights_management.audio.versions[].<class>.size_print
  - eas-rights_management.audio.versions[].<class>.export
  - eas-rights_management.audio.versions[].<class>.rightsmanagement
  - eas-rights_management.audio.versions[].<class>.group
  - eas-rights_management.audio.versions[].<class>.standard
  - eas-rights_management.office.versions[].<class>.version
  - eas-rights_management.office.versions[].<class>.size_print
  - eas-rights_management.office.versions[].<class>.export
  - eas-rights_management.office.versions[].<class>.rightsmanagement
  - eas-rights_management.office.versions[].<class>.standard
  - eas-rights_management.archive.versions[].<class>.version
  - eas-rights_management.archive.versions[].<class>.size_print
  - eas-rights_management.archive.versions[].<class>.group
  - eas-rights_management.archive.versions[].<class>.rightsmanagement
  - eas-rights_management.archive.versions[].<class>.limit
  - eas-rights_management.archive.versions[].<class>.standard
  - eas-rights_management.unknown.versions[]
  - eas-rights_management.vector2d.versions[]
  - eas-rights_management.vector3d.versions[]
---
# File size for download and preview

For each asset (picture, document, etc.) easydb provides automatically calculated variants of each asset, in order to be able to quickly display a small preview and to enable downloading in uniform image sizes.

These standard variants (or _versions_*) were chosen for user convenience. We recommend that you first check whether these variants are sufficient for you.

If your application requires other variants, additional variants can be configured as follows.

* _A version is created in easydb by editing the original application file, e. g. by copping. A data record can therefore have an original file with several versions. For a clear differentiation, the different file sizes for previews and downloads is called variants are._


## easydb5-master.yml

If not already contained, add the following lines to the central configuration file. The storage location of this file was defined during the [Installation](/en/sysadmin/installation).

```yaml
easydb-server:
  include_before:
    - /config/eas_rights_management.yml

  eas:
    produce_settings: /config/eas_produce.json
```

If not allready existing, add two new files to the configuration file.:

* eas_rights_management.yml
* eas_produce.json

## eas_rights_management.yml

This file contains configuration settings that are relevant for the rights management. The settings always refer to variants of file previews. The files are divided into file classes:

* **image**
* **video**
* **audio**
* **office**
* **archive**
* **vector2d**
* **vector3d**
* **unknown**

The **produce. conf** file class defines which variants are created after the upload.

Settings can be made for each variant to determine the behavior of the display and export. All variables are listed in the hierarchy under **eas. rights_management. \<class\>. version** (see example).

| Variable | Format | Description|
|---|---|---|
|version|string|Name of the variant, wich must match the variant in **produce. conf**.|
|size_print|string|Variant as displayed in the Download and Export Manager.|
|size_limit|int|Pixel limit for the rights management. If it is necessary to decide whether a download variant is allowed for the user during a mass download, this size is used and compared with the size of the preview. The variant is released if it is less than or equal to the limit in pixels.|
|export|boolean|If set, the variant is always available for download or export.|
|rightsmanagement|boolean|If set, this variant not allowed by the rights management and requires permission via the rights management.|
|group|string|Variants for the Export Manager can be gatherd in groups and are available in the URLs area, then. Group names can be chosen arbitrarily, but there are only following translations available in easydb: **thumbnail** (small), **preview** (preview), **huge** (large).|
|zoomable|boolean|If set, this variant is declared as zoomable. The frontend then displays the zoomer if desired. Only **PNG** and **JPEG** can be zoomed.|

Here is a complete example of the eas_rights_management. yml file:

```yaml
eas:
  rights_management:
    image:
      versions:
        - version: huge
          size_print: Pressebild
          size_limit: 1600
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
        - version: jpg1088
          size_print: 1088px
          size_limit: 1088
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: jpg808
          size_print: 808px
          size_limit: 808
          export: true
          zoomable: true
          rightsmanagement: true
          group: huge
        - version: jpg531
          size_print: 531px
          size_limit: 531
          export: true
          zoomable: true
          rightsmanagement: true
          group: huge
        - version: jpg252
          size_print: 252px
          size_limit: 252
          export: true
          zoomable: true
          rightsmanagement: true
          group: preview
        - version: jpg160
          size_print: 160px
          size_limit: 160
          export: true
          zoomable: true
          rightsmanagement: true
          group: preview
        - version: small
          size_print: 200px (small)
          size_limit: 200
          export: false
          group: thumbnail
          rightsmanagement: false
          standard: true
    video:
      versions:
        - version: 720p
          size_print: 720p
          size_limit: 1280
          export: true
          group: preview
          rightsmanagement: true
        - version: 360p
          size_print: 360p
          size_limit: 640
          export: true
          group: preview
          rightsmanagement: true
        - version: preview
          size_print: 640px
          size_limit: 640
          rightsmanagement: true
        - version: small
          size_print: 200px
          size_limit: 200
          rightsmanagement: false
          group: thumbnail
          standard: true
    audio:
      versions:
        - version: aac
          size_print: aac
          export: true
          rightsmanagement: true
        - version: preview
          size_print: 640px
          rightsmanagement: true
        - version: small
          size_print: 200px
          group: thumbnail
          rightsmanagement: false
          standard: true
    office:
      versions:
        - version: pdf
          size_print: pdf
          export: true
          rightsmanagement: true
        - version: huge
          size_print: 1600px
          rightsmanagement: true
        - version: preview
          size_print: 960px
          rightsmanagement: true
        - version: small
          size_print: 800px
          rightsmanagement: false
          standard: true
    archive:
      versions:
        - version: directory
          size_print: directory
          group: huge
          rightsmanagement: true
        - version: small
          size_print: 200px
          size_limit: 200
          rightsmanagement: false
          group: thumbnail
          standard: true
    unknown:
      versions: []
    vector2d:
      versions: []
    vector3d:
      versions: []
```

## eas_produce.json

Here is the productively tested content of the eas_produce.json file according to the example above:

```json
{
    "__all": {
        "__all": {
            "small": {
                "target_size": "1000x250",
                "target_format": "png",
                "target_alpha": "on",
                "target_no_fallback": "1",
                "priority": "12"
            }
        }
    },

    "image": {
        "__all": {
            "huge": {
                "target_size": "1600x1600",
                "target_format": "jpg",
                "target_interlace": "1",
                "target_no_enlarge": "1"
            },
            "jpg1088": {
                "target_size": "1088x1088",
                "target_format": "jpg",
                "target_interlace": "1",
                "target_no_enlarge": "1"
            },
            "jpg808": {
                "target_format": "jpg",
                "target_size": "808x808",
                "target_interlace": "1",
                "target_no_enlarge": "1"
            },
            "jpg531": {
                "target_format": "jpg",
                "target_size": "531x531",
                "target_interlace": "1",
                "target_no_enlarge": "1"
            },
            "jpg252": {
                "target_format": "jpg",
                "target_size": "252x252"
            },
            "jpg160": {
                "target_format": "jpg",
                "target_size": "160x160"
            }
        }
    },

    "video": {
        "__all": {
            "preview": {
                "target_size": "960x640",
                "target_format": "jpg",
                "target_interlace": "1",
                "target_no_enlarge": "1"
            },
            "360p": {
                "target_height": "360",
                "target_format": "mp4",
                "target_no_enlarge": "1",
                "target_audio_bitrate": "160k",
                "target_video_bitrate": "840k"
            },
            "720p": {
                "target_height": "720",
                "target_format": "mp4",
                "target_no_enlarge": "1",
                "target_audio_bitrate": "160k",
                "target_video_bitrate": "840k"
            }
        }
    },

    "audio": {
        "__all": {
            "preview": {
                "target_size": "640x640",
                "target_format": "jpg",
                "target_interlace": "1",
                "target_no_fallback": "1"
            },
            "aac": {
                "target_format": "aac",
                "target_audio_bitrate": "160k"
            }
        }
    },

    "office": {
        "__all": {
            "__pages": {
                "__source": {
                    "target_format": "png",
                    "target_size": "1000x1000"
                },
                "small": {
                    "target_size": "800x800",
                    "target_format": "png"
                }
            },
            "pdf": {
                "target_format": "pdf"
            },
            "preview": {
                "target_size": "960x960",
                "target_format": "jpg",
                "target_interlace": "1",
                "target_no_enlarge": "1"
            },
            "huge": {
                "target_size": "1600x1600",
                "target_format": "jpg",
                "target_no_enlarge": "1"
            }
        },
        "pdf": {
            "pdf": false
        }
    },

    "archive": {
        "__all": {
            "small": false
        },
        "webdvd.zip": {
            "directory": {
                "target_format": "directory"
            },
            "small": {
                "target_size": "200x200",
                "target_format": "png",
                "target_alpha": "on",
                "target_no_fallback": "1",
                "source_version": "directory",
                "priority": "12"
            }
        }
    },

    "unknown": {
    }
}
```json

The hierarchy in the JSON file includes the file class (example `archive`), the file extension (example `webdvd. zip`) and the variant name (example `small`). For the file class and extension, the placeholder `__all` is allowed, which describes all classes and extensions. In this example, the variant `small` is always created.

For each variant, the EAS options used to calculate this variant are specified. A reference to these options can be found in the [EAS-API-Reference](../../eas/api/produce). All values for the options must be strings, i. e. enclosed in double quotation marks (e.g. `"1"`).

If a variant is configured under the variant placeholder `__all`, it can be excluded for a special extension by specifying `false` instead of the EAS options. In the example, `"pdf": false` deactivates the creation of the variant `pdf` for files with the extension `pdf`, because it is superfluous.

For Office files, `__pages` is allowed below the extension, which describes the individual pages. The described variants (example `small`) are calculated for all pages within the document, with `__source` the EAS options for the extraction of the page original are described.
