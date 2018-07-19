---
title: "50 - Varianten für Dateigröße"
menu:
  main:
    name: "Varianten für Dateigröße"
    identifier: "sysadmin/konfiguration/produce"
    parent: "sysadmin/konfiguration"
---
# Dateigrößen für Download und Vorschau

Für jedes Asset (Bild, Dokument, etc.) hält die easydb automatisch berechnete Varianten des Assets bereit, um schnell eine kleine Vorschau anzeigen zu können und um den Download in einheitlichen Bildgrößen zu ermöglichen.

Diese Varianten (oder _Versionen*_) wurden im Hinblick auf Benutzbarkeit ausgewählt und decken viele Nutzungsszenarien ab. Wir empfehlen, zuerst in der Praxis zu prüfen, ob diese Varianten für Sie ausreichen.

Falls Ihr Anwendungsfall andere Varianten erfordert, dann können zusätzliche Varianten wie folgt konfiguriert werden.

_*Eine Version entsteht in easydb durch Bearbeitung der Originaldatei, z.B. durch Zuschneiden. Ein Datensatz können folglich eine Originaldatei mit mehreren Versionen haben. Zur eindeutigen Unterscheidung ist daher bei den unterschiedlichen Dateigrößen für Vorschau und Download von Varianten die Rede._

## easydb5-master.yml

In der zentralen Konfigurationsdatei, deren Speicherort bei der [Installation](/de/sysadmin/installation) festgelegt wurde, ergänzen Sie die folgenden Zeilen, soweit noch nicht vorhanden:

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

In dieser Datei werden für das Rechtemanagement relevante Konfigurationseinstellungen vorgenommen. Die Einstellungen beziehen sich immer auf Varianten von Dateivorschauen. Die Dateien sind in Dateiklassen unterteilt:

* **image**
* **video**
* **audio**
* **office**
* **archive**
* **vector2d**
* **vector3d**
* **unknown**

Für die jeweilige Dateiklasse wird in der **produce.conf** festgelegt, welche Varianten nach dem Upload erzeugt werden.

Je Variante können Einstellung vorgenommen werden, die das Verhalten der Anzeige und des Exports bestimmen. Für alle Variablen gilt, dass sie in der Hierarchie unter **eas.rights_management.\<class\>.versions** aufgeführt sind (siehe Beispiel).

| Variable | Format | Beschreibung |
|---|---|---|
|version|string|Name der Variante, diese muss mit der Version in **produce.conf** übereinstimmen.|
|size_print|string|Variante wie sie im Download- und Export-Manager angezeigt wird.|
|size_limit|int|Limit in Pixeln für das Rechtemanagement. Wenn bei einem Massen-Download entschieden werden muss, ob eine Variante zum Download für den User erlaubt ist, wird diese Größe benutzt und mit der Größe der Vorschau verglichen. Die Variante wird freigegeben, wenn sie kleiner oder gleich des Limits in Pixeln ist.|
|export|boolean|Wenn gesetzt, steht die Variante für einen Download oder einen Export grundsätzlich zur Verfügung.|
|rightsmanagement|boolean|Wenn gesetzt ist diese Variante über das Rechtemanagement geschützt und braucht eine Freigabe im Rechtemanagement.|
|group|string|Für den Export-Manager können Varianten in Gruppen zusammengefasst werden, die dann im Bereich URLs zur Verfügung stehen. Gruppennamen können beliebig gewählt werden, es gibt allerdings nur für folgende Übersetzungen in der easydb: **thumbnail** (Klein), **preview** (Vorschau), **huge** (Groß).|
|zoomable|boolean|Wenn gesetzt wird diese Variante als zoomfähig deklariert. Das Frontend zeigt dann auf Wunsch den Zoomer an. Es können nur **PNG** und **JPEG** gezoomt werden.|

Hier ein vollständiges Beispiel der Datei eas_rights_management.yml:

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
    vector2d:
      versions: []
    vector3d:
      versions: []

~~~~

## eas_produce.json

Hier der zum obigen Beispiel passende produktiv getestete Inhalt der Datei eas_produce.json:

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

Die Hierarchie in der JSON-Datei umfasst die Dateiklasse (Beispiel `archive`), die Dateierweiterung (Beispiel `webdvd.zip`) und den Variantennamen (Beispiel `small`). Für die Dateiklasse und die Erweiterung ist der Platzhalter `__all` zulässig, der alle Klassen und Erweiterungen beschreibt. So wird im Beispiel die Variante `small` immer erstellt.

Für jede Variante werden die EAS-Optionen angegeben, die zur Berechnung dieser Variante verwendet werden. Eine Referenz dieser Optionen ist in der [EAS-API-Referenz](../../eas/api/produce) zu finden. Alle Werte für die Optionen müssen Zeichenketten sein, also in doppelten Anführungszeichen eingeschlossen sein (auch z.B. `"1"`).

Wenn eine Variante unter dem Variantenplatzhalter `__all` konfiguriert ist, kann sie für eine spezielle Erweiterung durch Angabe von `false` statt der EAS-Optionen wieder ausgeschlossen werden. Im Beispiel wird mit `"pdf": false` die Erstellung der Variante `pdf` für Dateien mit der Erweiterung `pdf` deaktiviert, da sie überflüssig ist.

Für Office-Dateien ist unterhalb der Erweiterung noch `__pages` zulässig, was die einzelnen Seiten beschreibt. Die beschriebenen Varianten (Beispiel `small`) werden für alle Seiten innerhalb des Dokuments berechnet, mit `__source` werden die EAS-Optionen für die Extraktion des Seiten-Originals beschrieben.
