---
title: "Standard"
menu:
  main:
    name: "Standard"
    identifier: "webfrontend/datamanagement/search/find/standard"
    parent: "webfrontend/datamanagement/search/find"
---
# Standard - In Bearbeitung

## Die Card

Die Card kann max. folgende Infos enthalten:

- Bild (sofern dies in der Maske konfiguriert ist)
- Pfad (sofern es ein hierarchischer Objekttyp ist)
- Standard 1 (wenn Standard 1 in der Maske nicht konfiguriert oder das Feld leer ist, wird die SID angezeigt)
- Standard 2 (sofern dies in der Maske konfiguriert ist)
- Objekttyp + ID (sofern dies in der Maske konfiguriert ist)
- Pool (sofern dies in der Maske konfiguriert ist)
- Tags (sofern dies in der Maske konfiguriert ist)



## Technische Informationen

Die technische Infos enthalten die folgenden Informationen:

|                 | Bilder | Videos | Audio | Office | 3D   | 2D   | Archive | Sonstiges |
| --------------- | ------ | ------ | ----- | ------ | ---- | ---- | ------- | --------- |
| **Dateigröße**  | x      | x      | x     | x      | x    | x    | x       | x         |
| **Abmessung**   | x      | -      | -     | -      | -    | -    | -       | -         |
| **Dateiendung** | x      | x      | x     | x      | x    | x    | x       | x         |
| **Seitenzahl**  | -      | -      | -     | x      | -    | -    | -       | -         |
| **Laufzeit**    | -      | x      | x     | -      | -    | -    | -       | -         |



## Anzeigeoptionen

Zur Verfügung stehende Anzeigeoptionen:

| Ansicht      | Anzeigeoption          | Optionen         | Bemerkung                                                    |
| ------------ | ---------------------- | ---------------- | ------------------------------------------------------------ |
| **Standard** | Standard-Info anzeigen |                  | Option bei Stil "Unterlegt" & "Seitlich" deaktivieren und Standard-Info immer anzeigen |
|              | Größe                  | Klein            |                                                              |
|              |                        | Mittel           | Default                                                      |
|              |                        | Groß             |                                                              |
|              | Format                 | Füllen           | Default                                                      |
|              |                        | Thumbnail        |                                                              |
|              |                        | Ohne Rand        |                                                              |
|              | Stil                   | Überlagert       | Default                                                      |
|              |                        | Unterlegt        | Option bei Format "Füllen" deaktivieren                      |
|              |                        | Seitlich         | Option bei Format "Füllen" deaktivieren                      |
|              | Flache Hierarchie      |                  |                                                              |
|              | Treffer pro Seite      |                  |                                                              |
| **Text**     | Standard-Info anzeigen |                  |                                                              |
|              | Flache Hierarchie      |                  |                                                              |
|              | Treffer pro Seite      |                  |                                                              |
| **Tabelle**  | Hierarchien aufklappen |                  |                                                              |
|              | Anzeigen               | Standard-Info    |                                                              |
|              |                        | System-Objekt-ID |                                                              |
|              |                        | Objekttyp        |                                                              |
|              |                        | Pool             |                                                              |
|              |                        | Pfad             |                                                              |
|              |                        | Tags             |                                                              |
|              | Treffer pro Seite      |                  |                                                              |
| **Liste**    |                        |                  |                                                              |



Auswirkungen der Anzeigeoptionen:

| View                                          | Größe  | Format                | Stil               | Hier.      | Bild | Pfad              | Standard 1        | Standard 2        | Tech. | SID               | OT                | Pool              | Tag                |
| --------------------------------------------- | ------ | --------------------- | ------------------ | ---------- | ---- | ----------------- | ----------------- | ----------------- | ----- | ----------------- | ----------------- | ----------------- | ------------------ |
| Standard                                      | Klein  | Füllen                | Überlagert         | Dive       | x    | -                 | (x)               | -                 | -     | -                 | -                 | -                 | (x)                |
|                                               |        |                       | *Unterlegt (n/a)*  |            |      |                   |                   |                   |       |                   |                   |                   |                    |
|                                               |        |                       | *Seitlich (n/a)*   |            |      |                   |                   |                   |       |                   |                   |                   |                    |
|                                               |        | Thumbnail + Ohne Rand | *Überlagert (n/a)* |            |      |                   |                   |                   |       |                   |                   |                   |                    |
|                                               |        |                       | *Unterlegt (n/a)*  |            |      |                   |                   |                   |       |                   |                   |                   |                    |
|                                               |        |                       | Seitlich           | Dive       | x    | -                 | x                 | x                 | -     | -                 | -                 | -                 | x                  |
|                                               | Mittel | Füllen                | Überlagert         | Dive       | x    | -                 | (x)               | (x)               | (x)   | -                 | -                 | (x)               | (x)                |
|                                               |        |                       | *Unterlegt (n/a)*  |            |      |                   |                   |                   |       |                   |                   |                   |                    |
|                                               |        |                       | *Seitlich (n/a)*   |            |      |                   |                   |                   |       |                   |                   |                   |                    |
|                                               |        | Thumbnail + Ohne Rand | Überlagert         | Dive       | x    | -                 | (x)               | (x)               | (x)   | -                 | -                 | (x)               | (x)                |
|                                               |        |                       | Unterlegt          | Dive       | x    | -                 | x                 | x                 | x     | -                 | -                 | x                 | x                  |
|                                               |        |                       | Seitlich           | Dive       | x    | -                 | x                 | x                 | x     | x                 | x                 | x                 | x                  |
|                                               | Groß   | Füllen                | Überlagert         | Dive       | x    | -                 | (x)               | (x)               | (x)   | (x)               | (x)               | (x)               | (x)                |
|                                               |        |                       | *Unterlegt (n/a)*  |            |      |                   |                   |                   |       |                   |                   |                   |                    |
|                                               |        |                       | *Seitlich (n/a)*   |            |      |                   |                   |                   |       |                   |                   |                   |                    |
|                                               |        | Thumbnail + Ohne Rand | Überlagert         | Dive       | x    | -                 | (x)               | (x)               | (x)   | (x)               | (x)               | (x)               | (x)                |
|                                               |        |                       | Unterlegt          | Dive       | x    | x                 | x                 | x                 | x     | x                 | x                 | x                 | x                  |
|                                               |        |                       | Seitlich           | Dive       | x    | x                 | x                 | x                 | x     | x                 | x                 | x                 | x                  |
| Text                                          | -      | -                     | -                  | Dive       | x    | (x)               | (x)               | (x)               | (x)   | (x)               | (x)               | (x)               | (x)                |
| Tabelle                                       | -      | -                     | -                  | Aufklappen | x    | (x) eigene Spalte | (x) eigene Spalte | (x) eigene Spalte | -     | (x) eigene Spalte | (x) eigene Spalte | (x) eigene Spalte | (x)  eigene Spalte |
| Liste                                         | Klein  | -                     | -                  | Aufklappen | -    | -                 | x                 | -                 | -     | -                 | -                 | -                 | -                  |
|                                               | Mittel | -                     | -                  | Aufklappen | x    | -                 | x                 | x                 | -     | -                 | -                 | -                 | -                  |
|                                               | Groß   | -                     | -                  | Aufklappen | x    | -                 | x                 | x                 | -     | -                 | -                 | x                 | x                  |
| Hierachie-Browser (entspricht Liste "Mittel") | -      | -                     | -                  | Aufklappen | x    | -                 | x                 | x                 | -     | -                 | -                 | -                 | -                  |
| Neu Anlegen                                   |        |                       |                    |            |      |                   |                   |                   |       |                   |                   |                   |                    |
| Gruppeneditor                                 |        |                       |                    |            |      |                   |                   |                   |       |                   |                   |                   |                    |

**LEGENDE**: **x** = anzeigen, **(x)** = anzeigen, wenn Anzeigeoption aktiviert, **-** = nicht anzeigen



## Anzeige verlinkter Datensätze

Anzeige von verlinkten Datensätzen in der Detailansicht, dem Editor und der Textansicht:

| Modus    | Bild                                        | Standard 1  | Standard 2 | Pfad | SID                                         | OT                                          | Pool                                        | Tags                                        |
| -------- | ------------------------------------------- | ----------- | ---------- | ---- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| Standard | x                                           | x           | x          | x    | x, wenn in Maske aktiviert                  | x, wenn in Maske aktiviert                  | x, wenn in Maske aktiviert                  | x, wenn in Maske aktiviert                  |
| Text     | x, als eigenes Feld wenn in Maske aktiviert | -           | -          |      | x, als eigenes Feld wenn in Maske aktiviert | x, als eigenes Feld wenn in Maske aktiviert | x, als eigenes Feld wenn in Maske aktiviert | x, als eigenes Feld wenn in Maske aktiviert |
| Kurz     | -                                           | x, als Link | -          | -    | -                                           | -                                           | -                                           | -                                           |



## Autovervollständigung - TBD

Bei der Autovervollständigung in den Haupt- und Nebensuchen wird die Ansicht "Liste - mittel" verwendet. 





## Anzeige von Hierarchien - TBD

- Hierarchische Hauptobjekttypen
- verlinkte hierarchische Nebenobjekttypen
- Pool