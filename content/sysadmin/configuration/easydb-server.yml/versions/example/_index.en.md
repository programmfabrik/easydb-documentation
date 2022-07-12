---
title: "New image variant with watermark"
menu:
  main:
    name: "New image variant with watermark"
    identifier: "sysadmin/configuration/easydb-server.yml/versions/example"
    weight: -948
    parent: "sysadmin/configuration/easydb-server.yml/versions"
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
eas_rights_management.yml:
  - eas.rights_management.<class>
  - eas.rights_management.<class>.versions.version
  - eas.rights_management.<class>.versions.size_print
  - eas.rights_management.<class>.versions.size_limit
  - eas.rights_management.<class>.versions.export
  - eas.rights_management.<class>.versions.rightsmanagement
  - eas.rights_management.<class>.versions.group
  - eas.rights_management.<class>.versions.zoomable
  - eas.rights_management.<class>.versions.watermark
  - eas.rights_management.<class>.versions.standard
---

# Example

In the first example we would like to create a watermark version of maximum 500x500 pixels. Therefore we have to create the following `eas_produce.json` entry:

```json
"500px": {
	"target_size": "500x500",
	"target_size_min": "1",
	"target_format": "png",
	"target_alpha": "on",
	"target_no_enlarge": "1",
	"priority": "12"
},
```

To activate watermarks in this version, we also create the following `eas_rights_management.yml` entry:

```yaml
- version: 500px
  size_print: 500px variant
  size_limit: 500
  export: true
  rightsmanagement: true
  group: preview
  watermark: true
```

After the changes where made, your files should look like this:

**eas_produce.json:**
```json
{
	"__all": {
		"__all": {
			"small": {
				"target_size": "250x250",
				"target_size_min": "1",
				"target_format": "jpg",
				"target_quality": "80",
				"target_no_enlarge": "1",
				"target_no_fallback": "1",
				"priority": "12"
			}
		}
	},
	"image": {
		"__all": {
			"small": {
				"target_size": "250x250",
				"target_size_min": "1",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1",
				"priority": "12"
			},
      "500px": {
			  "target_size": "500x500",
			  "target_size_min": "1",
			  "target_format": "png",
			  "target_alpha": "on",
			  "target_no_enlarge": "1",
			  "priority": "12"
		  },
			"preview": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			},
			"preview_watermark": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			},
			"huge": {
				"target_size": "2000x2000",
				"target_size_minimum": "1001x1001",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			},
			"full": {
				"target_format": "png",
				"target_size_minimum": "2001x2001",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			}
		},
		"jpg": {
			"small": {
				"target_size": "250x250",
				"target_format": "jpg",
				"target_quality": "80",
				"target_interlace": "1",
				"target_size_min": "1",
				"target_no_enlarge": "1",
				"priority": "12"
			},
			"preview": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_interlace": "1",
				"target_quality": "80",
				"target_no_enlarge": "1"
			},
			"preview_watermark": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_interlace": "1",
				"target_quality": "80",
				"target_no_enlarge": "1"
			},
			"huge": {
				"target_size": "2000x2000",
				"target_size_minimum": "1001x1001",
				"target_format": "jpg",
				"target_quality": "80",
				"target_interlace": "1",
				"target_no_enlarge": "1"
			},
			"full": {
				"target_format": "jpg",
				"target_size_minimum": "2001x2001",
				"target_interlace": "1",
				"target_quality": "80"
			}
		}
	},
	"video": {
		"__all": {
			"preview": {
				"target_size": "720x720",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_interlace": "1",
				"target_quality": "80",
				"target_no_enlarge": "1"
			},
			"preview_watermark": {
				"target_size": "720x720",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_interlace": "1",
				"target_quality": "80",
				"target_no_enlarge": "1"
			},
			"huge": {
				"target_size": "1920x1920",
				"target_size_minimum": "721x721",
				"target_format": "jpg",
				"target_quality": "80",
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
				"target_size_minimum": "10000x361",
				"target_format": "mp4",
				"target_no_enlarge": "1",
				"target_audio_bitrate": "160k",
				"target_strip": "1",
				"target_video_bitrate": "840k"
			},
			"1920p": {
				"target_height": "1920",
				"target_size_minimum": "10000x721",
				"target_format": "mp4",
				"target_no_enlarge": "1",
				"target_audio_bitrate": "160k",
				"target_strip": "1",
				"target_video_bitrate": "840k"
			}
		}
	},
	"audio": {
		"__all": {
			"preview": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_quality": "80",
				"target_no_fallback": "1",
				"target_interlace": "1"
			},
			"preview_watermark": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_interlace": "1",
				"target_no_fallback": "1",
				"target_quality": "80",
				"target_no_enlarge": "1"
			},
			"aac": {
				"target_format": "aac",
				"target_no_fallback": "1",
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
					"target_size": "200x200",
					"target_format": "png"
				}
			},
			"preview": {
				"target_size": "1000x1000",
				"target_format": "png"
			},
			"preview_watermark": {
				"target_size": "1000x1000",
				"target_format": "png"
			}
		}
	},
	"archive": {
		"__all": {
			"thumb": false
		},
		"webdvd.zip": {
			"directory": {
				"target_format": "directory"
			},
			"small": {
				"target_size": "250x250",
				"target_extractsize": "1024x768",
				"target_format": "jpg",
				"target_quality": "80",
				"source_version": "directory",
				"priority": "12"
			},
            "preview": {
                "target_size": "1000x1000",
                "target_extractsize": "1024x768",
                "target_format": "jpg",
				"target_quality": "80",
                "source_version": "directory"
            }
		}
	},
	"unknown": {
        "__all": {
            "small": false
        }
	},
    "vector2d": {
		"__all": {
			"small": {
				"target_size": "250x250",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			},
			"preview": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			}
		}
    },
    "vector3d": {
        "__all": {
            "small": false
        }
    }
}
```

**eas_rights_management.yml:**
```yaml
eas:
  rights_management:
    image:
      versions:
        - version: small
          size_print: 250px
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: preview_watermark
          size_print: 1000px (watermark)
          size_limit: 1000
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: huge
          size_print: 2000px
          size_limit: 2000
          export: true
          rightsmanagement: true
          group: huge
          zoomable: true
        - version: full
          size_print: Original (formatiert)
          export: true
          rightsmanagement: true
          group: huge
          zoomable: true
        - version: 500px
          size_print: 500px variant
          size_limit: 500
          export: true
          rightsmanagement: true
          group: preview
          watermark: true
    video:
      versions:
        - version: small
          size_print: 250px
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 720px
          size_limit: 720
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: preview_watermark
          size_print: 720px (watermark)
          size_limit: 720
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: huge
          size_print: 1920px
          size_limit: 1920
          export: true
          group: huge
          rightsmanagement: true
          zoomable: true
        - version: 360p
          size_print: 360p
          size_limit: 360
          export: true
          group: preview
          rightsmanagement: true
        - version: 720p
          size_print: 720p
          size_limit: 720
          export: true
          group: preview
          rightsmanagement: true
        - version: 1920p
          size_print: 1920p
          size_limit: 1920
          export: true
          rightsmanagement: true
          group: huge
    audio:
      versions:
        - version: small
          size_print: 250px (small)
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: preview_watermark
          size_print: 1000px (watermark)
          size_limit: 1000
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: aac
          size_print: aac
          export: true
          rightsmanagement: true
    office:
      versions:
        - version: small
          size_print: 250px (small)
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: preview_watermark
          size_print: 1000px (watermark)
          size_limit: 1000
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: pages
          size_print: pages
          rightsmanagement: true
          use_for_pages: true
    archive:
      versions:
        - version: small
          size_print: 250px (small)
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
        - version: directory
          size_print: directory
          group: huge
          rightsmanagement: true
    unknown:
      versions: []
    vector2d:
      versions:
        - version: small
          size_print: 250px
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
    vector3d:
      versions: []
```

------------------------------------------------------------------------------------------------






For the new variant `500px` (example shown above), you would include in `eas_rights_management.yml`:



* The internal name of the variant is given as `version: 500px`. This must match the name in `eas_produce.json` above.
* The line `size_print: 500px variant` defines the name shown to the user in the frontend dialogs(`500px variant`).
* `export: true` defines that this version can be chosen in the dialogs of download and export.
* In this file, using `__all` is not valid.
* For bigger variants you would typically choose `group: huge` instead of `group: preview`, but this is arbitrary.

See further down for a bigger example.

Settings can be made for each variant to determine the behavior of the display and export. All variables are listed in the hierarchy under **eas. rights_management. \<class\>. version**.

See [eas_rights_management.yml](../eas_rights_management.yml) for more

Here is a complete example of the eas_rights_management.yml file:

```yaml
eas:
  rights_management:
    image:
      versions:
        - version: small
          size_print: 250px
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: 500px
          size_print: 500px variant
          size_limit: 500
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
        - version: preview
          size_print: 1000px
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: preview_watermark
          size_print: 1000px (watermark)
          size_limit: 1000
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: huge
          size_print: 2000px
          size_limit: 2000
          export: true
          rightsmanagement: true
          group: huge
          zoomable: true
        - version: full
          size_print: Original (formatiert)
          export: true
          rightsmanagement: true
          group: huge
          zoomable: true
    video:
      versions:
        - version: small
          size_print: 250px
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 720px
          size_limit: 720
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: preview_watermark
          size_print: 720px (watermark)
          size_limit: 720
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: huge
          size_print: 1920px
          size_limit: 1920
          export: true
          group: huge
          rightsmanagement: true
          zoomable: true
        - version: 360p
          size_print: 360p
          size_limit: 360
          export: true
          group: preview
          rightsmanagement: true
        - version: 720p
          size_print: 720p
          size_limit: 720
          export: true
          group: preview
          rightsmanagement: true
        - version: 1920p
          size_print: 1920p
          size_limit: 1920
          export: true
          rightsmanagement: true
          group: huge
    audio:
      versions:
        - version: small
          size_print: 250px (small)
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: preview_watermark
          size_print: 1000px (watermark)
          size_limit: 1000
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: aac
          size_print: aac
          export: true
          rightsmanagement: true
    office:
      versions:
        - version: small
          size_print: 250px (small)
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: preview_watermark
          size_print: 1000px (watermark)
          size_limit: 1000
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: pages
          size_print: pages
          rightsmanagement: true
          use_for_pages: true
    archive:
      versions:
        - version: small
          size_print: 250px (small)
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
        - version: directory
          size_print: directory
          group: huge
          rightsmanagement: true
    unknown:
      versions: []
    vector2d:
      versions:
        - version: small
          size_print: 250px
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
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
				"target_size": "250x250",
				"target_size_min": "1",
				"target_format": "jpg",
				"target_quality": "80",
				"target_no_enlarge": "1",
				"target_no_fallback": "1",
				"priority": "12"
			}
		}
	},

	"image": {
		"__all": {
			"small": {
				"target_size": "250x250",
				"target_size_min": "1",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1",
				"priority": "12"
			},
      "500px": {
			  "target_size": "500x500",
			  "target_size_min": "1",
			  "target_format": "png",
			  "target_alpha": "on",
			  "target_no_enlarge": "1",
			  "priority": "12"
		  },
			"preview": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			},
			"preview_watermark": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			},
			"huge": {
				"target_size": "2000x2000",
				"target_size_minimum": "1001x1001",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			},
			"full": {
				"target_format": "png",
				"target_size_minimum": "2001x2001",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			}
		},

		"jpg": {
			"small": {
				"target_size": "250x250",
				"target_format": "jpg",
				"target_quality": "80",
				"target_interlace": "1",
				"target_size_min": "1",
				"target_no_enlarge": "1",
				"priority": "12"
			},
			"preview": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_interlace": "1",
				"target_quality": "80",
				"target_no_enlarge": "1"
			},
			"preview_watermark": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_interlace": "1",
				"target_quality": "80",
				"target_no_enlarge": "1"
			},
			"huge": {
				"target_size": "2000x2000",
				"target_size_minimum": "1001x1001",
				"target_format": "jpg",
				"target_quality": "80",
				"target_interlace": "1",
				"target_no_enlarge": "1"
			},
			"full": {
				"target_format": "jpg",
				"target_size_minimum": "2001x2001",
				"target_interlace": "1",
				"target_quality": "80"
			}
		}
	},

	"video": {
		"__all": {
			"preview": {
				"target_size": "720x720",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_interlace": "1",
				"target_quality": "80",
				"target_no_enlarge": "1"
			},
			"preview_watermark": {
				"target_size": "720x720",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_interlace": "1",
				"target_quality": "80",
				"target_no_enlarge": "1"
			},
			"huge": {
				"target_size": "1920x1920",
				"target_size_minimum": "721x721",
				"target_format": "jpg",
				"target_quality": "80",
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
				"target_size_minimum": "10000x361",
				"target_format": "mp4",
				"target_no_enlarge": "1",
				"target_audio_bitrate": "160k",
				"target_strip": "1",
				"target_video_bitrate": "840k"
			},
			"1920p": {
				"target_height": "1920",
				"target_size_minimum": "10000x721",
				"target_format": "mp4",
				"target_no_enlarge": "1",
				"target_audio_bitrate": "160k",
				"target_strip": "1",
				"target_video_bitrate": "840k"
			}
		}
	},

	"audio": {
		"__all": {
			"preview": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_quality": "80",
				"target_no_fallback": "1",
				"target_interlace": "1"
			},
			"preview_watermark": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_interlace": "1",
				"target_no_fallback": "1",
				"target_quality": "80",
				"target_no_enlarge": "1"
			},
			"aac": {
				"target_format": "aac",
				"target_no_fallback": "1",
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
					"target_size": "200x200",
					"target_format": "png"
				}
			},
			"preview": {
				"target_size": "1000x1000",
				"target_format": "png"
			},
			"preview_watermark": {
				"target_size": "1000x1000",
				"target_format": "png"
			}
		}
	},

	"archive": {
		"__all": {
			"thumb": false
		},
		"webdvd.zip": {
			"directory": {
				"target_format": "directory"
			},
			"small": {
				"target_size": "250x250",
				"target_extractsize": "1024x768",
				"target_format": "jpg",
				"target_quality": "80",
				"source_version": "directory",
				"priority": "12"
			},
            "preview": {
                "target_size": "1000x1000",
                "target_extractsize": "1024x768",
                "target_format": "jpg",
				"target_quality": "80",
                "source_version": "directory"
            }
		}
	},

	"unknown": {
        "__all": {
            "small": false
        }
	},
    "vector2d": {
		"__all": {
			"small": {
				"target_size": "250x250",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			},
			"preview": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			}
		}
    },
    "vector3d": {
        "__all": {
            "small": false
        }
    }

}
```

The hierarchy in the JSON file includes the file class (example `archive`), the file extension (example `webdvd. zip`) and the variant name (example `small`). For the file class and extension, the placeholder `__all` is allowed, which describes all classes and extensions. In this example, the variant `small` is always created.

For each variant, the EAS options used to calculate this variant are specified. A reference to these options can be found in the [EAS-API-Reference](../../../../eas/api/produce). All values for the options must be strings, i. e. enclosed in double quotation marks (e.g. `"1"`).

/en/sysadmin2/eas/api/produce/

If a variant is configured under the variant placeholder `__all`, it can be excluded for a special extension by specifying `false` instead of the EAS options. In the example, `"pdf": false` deactivates the creation of the variant `pdf` for files with the extension `pdf`, because it is superfluous.

For Office files, `__pages` is allowed below the extension, which describes the individual pages. The described variants (example `small`) are calculated for all pages within the document, with `__source` the EAS options for the extraction of the page original are described.

