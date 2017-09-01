#  EAS-API: /bulkversions

Optimierte und limitierte Version des "/versions-Requests":../versions für mehrere Assets.

##  Beispiel

~~~
 http://eas.example.com/eas/bulkversions?instance=example&asset_ids=[1000,1001,1002]
~~~


##  Parameter


|---|---|
|`instance`          |Name der Instanz|
|`asset_ids`         |JSON-Liste mit Asset-IDs|

##  Antwort-Struktur

Bei einer Anfrage nach den Asset-IDs 1000, 1001 und 1002 wie im obrigen Beispiel sieht die Antwort in etwas so aus. Neben den angefragten Assets werden auch Informationen über das Root-Asset und die erste Seite bei Office-Dokumenten in der Antwort mitgeliefert. Die Versionsinformationen wurden teilweise gekürzt (…).

~~~
 {
    998: {
        "id": 998,
        "root_id": null,
        "versions": [
            …
        ]
    },
    1000: {
        "id": 1000,
        "root_id": 998,
        "versions": [
            …
        ]
    },
    1001: {
        "id": 1001,
        "root_id": null,
        "versions": [
            …
        ]
    },
    1002: {
        "id": 1002,
        "root_id": null,
        "versions": [
            {
                "hash": "005dff534a3a48be0feea384dfd7b0306d289691",
                "md5": "27ce49286ad9574dc31fa32f2cba28c3",
                "status": "done",
                "version": "original",
                "custom": {
                    "original_filename": "foo.pdf"
                },
                "type": {
                    "mimetype": "application/pdf",
                    "width": null,
                    "height": null,
                    "filesize": 12987,
                    "extension": "pdf",
                    "compiled": "pdf document, 2 pages",
                    "fileclass": "office"
                }
            }
        ],
        "children": [
            1010,
            1011
        ]
    },
    1010: {
        "id": 1010,
        "root_id": 1002,
        "versions": [
            {
                "hash": "292237f4fb469e372c886ca43d5b2d783aaada31",
                "md5": "30722adbbd687d1c72cee7a50abd4145",
                "status": "done",
                "version": "original",
                "custom": {
                    "original_filename": null
                },
                "type": {
                    "mimetype": "image/jpeg",
                    "width": 2300,
                    "height": 3800,
                    "filesize": 234545,
                    "extension": "jpg",
                    "compiled": "jpeg image, 2300x3800",
                    "fileclass": "image"
                }
            },
            {
                "hash": "10f8ad9f7c8ae59b019b6e2845421fc61cc1298c",
                "md5": "48b2351548822e87e2be344de72b4aae",
                "status": "done",
                "version": "thumbnail",
                "custom": {
                    "original_filename": null
                },
                "type": {
                    "mimetype": "image/png",
                    "width": 77,
                    "height": 128,
                    "filesize": 5678,
                    "extension": "png",
                    "compiled": "png image, 77x128",
                    "fileclass": "image"
                }
            }
        ]
    }
}
