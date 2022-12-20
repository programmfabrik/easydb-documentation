---
title: "Videos mit Untertitel"
menu:
  main:
    name: "Untertitel"
    identifier: "webfrontend/datamanagement/features/subtitles"
    parent: "webfrontend/datamanagement/features"
---

# Videos mit Untertiteln

Damit bei Videos im Video-Player Untertitel angezeigt werden können, müssen die Untertitel als separate VTT-Dateien vorliegen.

Stimmen die Dateinamen der Video-Datei und der VTT-Datei überein - also z.B. video.mp4 und video.vtt - so können beide Dateien in einem Schritt hochgeladen werden. Wichtig ist im Upload-Dialog "Versionen erkennen" zu aktivieren, sodass für beide Dateien nur ein Datensatz angelegt wird, in dem beide Dateien als Version abgelegt werden.

Alternativ kann wie gewohnt zunächst die Video-Datei hochgeladen werden und in einem zweiten Schritt über das 3-Punkte-Menü des Datei-Feldes die VTT-Dateien als zusätzliche Versionen hochgeladen werden.

Der Dateiname der Untertitel-Datei wird anschließend im Video-Player zur Auswahl angezeigt.