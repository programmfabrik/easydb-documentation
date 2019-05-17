---
title: "EAS_Produce"
layout: config
menu:
  main:
    name: "EAS-Produce"
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

If your application requires other variants, additional variants can be configured as follows. To make the changes effective, just restart the `easydb-server` container.

* _A version is created in easydb by editing the original application file, e. g. by cropping. A data record can therefore have an original file with several versions. For a clear differentiation, the different file sizes for previews and downloads is called variants here._


## produce settings

Add the following lines to the configuration, e.g. `config/easydb-server.yml`. The storage location of the `config` directory was defined during the [Installation](/en/sysadmin/installation/#mount).

Make sure to not create duplicate lines. If a line already exists, e.g. `include_before:`, use it instead and add the missing line beneath it, with proper indentation. If in doubt use a linter tool or ask us for help. Problems of this kind can prevent the easydb from starting. We suggest to keep a backup of your previous configuration.

```yaml
include_before:
  - /config/eas_rights_management.yml

eas:
  produce_settings: /config/eas_produce.json
```

The file given for `produce_settings` defines which variants are created after the upload.

Get the default configuration of variants as a starting point and for editing:

```bash
docker cp easydb-server:/easydb-5/base/eas/rights_management.yml /srv/easydb/config/eas_rights_management.yml
docker cp easydb-server:/easydb-5/base/eas/eas-produce.json      /srv/easydb/config/eas_produce.json
```

Edit `eas_produce.json` and add the variants you desire.

Example: Adding a variant with maximum size of 500 pixels:

```json
[...]
        "image": {
                "__all": {
[...]
                        "500px": {
                                "target_size": "500x500",
                                "target_size_minimum": "251x251",
                                "target_format": "jpg",
                                "target_interlace": "1",
                                "target_quality": "80",
                                "target_no_enlarge": "1"
                        },
```

* Maximum size of 500 is implemented by `"target_size": "500x500",`.
* `500px` is the name of the variant. Names that only contain numbers are NOT VALID. Make sure to also include letters.
* `__all` is an existing paragraph. You may put your new variant into it, as in this example. Then your new variant is produced for assets no matter whether the format of the original file is png, jpg, tiff, etc..
* Putting your new variant into the `image` clause, as in this example, defines that this variant is only to be produced for assets which are an images in their original file. You could instead use the clauses `video`, `office`, etc. or the clause `__all` with the same indentation, to produce for all classes.
* `"target_size_minimum": "251x251",` defines that this preview is NOT to be generated for assets which are smaller than 251 pixels in both dimensions.
* The preview is generated as a jpg file. E.g. `png` and `tiff` are also possible.
* `target_interlace` and `target_quality` are for jpg only. For `png` and `tif` consider e.g. `"target_alpha": "on"` for transparency or `"target_dpi": "300"` for printing.
* Make sure to include all needed commas and to avoid any superflous commas. A superflous commma would be e.g. one at the end of a list. Note for example that there is no comma after `"target_no_enlarge": "1"` in the example above. Consider using a syntax checker and linter tool for json.

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

For the new variant `500px` (example shown above), you would include in `eas_rights_management.yml`:

```yaml
eas:
  rights_management:
    image:
      versions:
        - version: 500px
          size_print: 500px variant
          size_limit: 500
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
[...]
```

* The internal name of the variant is given as `version: 500px`. This must match the name in `eas_produce.json` above.
* The line `size_print: 500px variant` defines the name shown to the user in the frontend dialogs(`500px variant`).
* `export: true` defines that this version can be chosen in the dialogs of download and export.
* In this file, using `__all` is not valid.
* For bigger variants you would typically choose `group: huge` instead of `group: preview`, but this is arbitrary.

See further down for a bigger example.

Settings can be made for each variant to determine the behavior of the display and export. All variables are listed in the hierarchy under **eas. rights_management. \<class\>. version**.

| Variable | Format | Description|
|---|---|---|
|version|string|Name of the variant, wich must match the variant in `eas.produce_config`.|
|size_print|string|Variant as displayed in the Download and Export Manager.|
|size_limit|int|Pixel limit for the rights management. If it is necessary to decide whether a download variant is allowed for the user during a mass download, this size is used and compared with the size of the preview. The variant is released if it is less than or equal to the limit in pixels.|
|export|boolean|If set, the variant is always available for download or export.|
|rightsmanagement|boolean|If set, this variant not allowed by the rights management and requires permission via the rights management.|
|group|string|Variants for the Export Manager can be gatherd in groups and are available in the URLs area, then. Group names can be chosen arbitrarily, but there are only following translations available in easydb: **thumbnail** (small), **preview** (preview), **huge** (large).|
|zoomable|boolean|If set, this variant is declared as zoomable. The frontend then displays the zoomer if desired. Only **PNG** and **JPEG** can be zoomed.|

Here is a complete example of the eas_rights_management.yml file:

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

Here is the productively tested content of the eas_produce.json file matching the big `eas_rights_management.yml` example above:

```javascript
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
```

The hierarchy in the JSON file includes the file class (example `archive`), the file extension (example `webdvd. zip`) and the variant name (example `small`). For the file class and extension, the placeholder `__all` is allowed, which describes all classes and extensions. In this example, the variant `small` is always created.

For each variant, the EAS options used to calculate this variant are specified. A reference to these options can be found in the [EAS-API-Reference](../../eas/api/produce). All values for the options must be strings, i. e. enclosed in double quotation marks (e.g. `"1"`).

If a variant is configured under the variant placeholder `__all`, it can be excluded for a special extension by specifying `false` instead of the EAS options. In the example, `"pdf": false` deactivates the creation of the variant `pdf` for files with the extension `pdf`, because it is superfluous.

For Office files, `__pages` is allowed below the extension, which describes the individual pages. The described variants (example `small`) are calculated for all pages within the document, with `__source` the EAS options for the extraction of the page original are described.
