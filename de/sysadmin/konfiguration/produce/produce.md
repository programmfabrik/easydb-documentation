# Dateigrößen für Download und Vorschau

Für jedes Asset (Bild, Dokument, etc.) hält die easydb automatisch berechnete Varianten des Assets bereit, um schnell eine kleine Vorschau anzeigen zu können und um den Download in einheitlichen Bildgrößen zu ermöglichen.

Diese Varianten (oder "Versionen") wurden im Hinblick auf Benutzbarkeit ausgewählt und decken viele Nutzungs-Szenarien ab. Wir empfehlen, zuerst in der Praxis zu prüfen, ob diese Varianten für Sie ausreichen.

Falls Ihr Anwendungsfall andere Varianten erfordert, dann können zusätzliche Varianten wie folgt konfiguriert werden.

## easydb5-master.yml

In der zentralen Konfigurationsdatei, deren Speicherort bei der [Installation](/sysadmin/installation/installation.md) festgelegt wurde, ergänzen Sie die folgenden Zeilen, soweit noch nicht vorhanden:

~~~~
easydb-server:
  include_before:
    - /config/eas_rights_management.yml

  eas:
    produce_settings: /config/eas_produce.json

~~~~

Neben die zentrale Konfigurationsdatei legen Sie nun zwei neue Dateien, soweit noch nicht vorhanden:

* eas_rights_management.yml
* eas_produce.json

## eas_rights_management.yml

Hier ein vollständiges produktiv getestetes Beispiel:

~~~~
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
          size_print: 1088 px
          size_limit: 1088
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: jpg808
          size_print: 808 px
          size_limit: 808
          export: true
          zoomable: true
          rightsmanagement: true
          group: huge
        - version: jpg531
          size_print: 531 px
          size_limit: 531
          export: true
          zoomable: true
          rightsmanagement: true
          group: huge
        - version: jpg252
          size_print: 252 px
          size_limit: 252
          export: true
          zoomable: true
          rightsmanagement: true
          group: preview
        - version: jpg160
          size_print: 160 px
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
~~~~

## eas_produce.json

Hier das zum obigen Beispiel passende produktiv getestete Beispiel:

~~~~
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
~~~~

