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

- Bild (nur bei linked objects sofern dies in der Maske konfiguriert ist)
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

| Ansicht      | Anzeigeoption                                   | Optionen         | Bemerkung                                                    |
| ------------ | ----------------------------------------------- | ---------------- | ------------------------------------------------------------ |
| **Standard** | Standard-Info anzeigen                          |                  | Option bei Stil "Unterlegt" & "Seitlich" deaktivieren und Standard-Info immer anzeigen |
|              | Größe                                           | Klein            |                                                              |
|              |                                                 | Mittel           | Default                                                      |
|              |                                                 | Groß             |                                                              |
|              | Format                                          | Füllen           | Default                                                      |
|              |                                                 | Thumbnail        |                                                              |
|              |                                                 | Ohne Rand        |                                                              |
|              | Stil                                            | Überlagert       | Default                                                      |
|              |                                                 | Unterlegt        | Option bei Format "Füllen" deaktivieren                      |
|              |                                                 | Seitlich         | Option bei Format "Füllen" deaktivieren                      |
|              | Flache Hierarchie                               |                  |                                                              |
|              | Treffer pro Seite                               |                  |                                                              |
| **Text**     | Standard-Info anzeigen                          |                  |                                                              |
|              | Flache Hierarchie                               |                  |                                                              |
|              | Treffer pro Seite                               |                  |                                                              |
| **Tabelle**  | Hierarchien aufklappen                          |                  |                                                              |
|              | Anzeigen                                        | Standard-Info    |                                                              |
|              |                                                 | System-Objekt-ID |                                                              |
|              |                                                 | Objekttyp        |                                                              |
|              |                                                 | Pool             |                                                              |
|              |                                                 | Pfad             |                                                              |
|              |                                                 | Tags             |                                                              |
|              | Treffer pro Seite                               |                  |                                                              |
| **Liste**    | Größe                                           | Klein            |                                                              |
|              |                                                 | Mittel           |                                                              |
|              |                                                 | Groß             |                                                              |
|              | Treffer pro Seite                               |                  |                                                              |
|              | Ergebnisse pro Seite in verschachtelten Feldern |                  | ???                                                          |



Auswirkungen der Anzeigeoptionen:

| View                                          | Größe  | Format                | Stil               | Hier.      | Bild inkl. Blättern | Pfad | Standard 1        | Standard 2 | Tech. | OT & SID           | Pool              | Tag                |                                                              |
| --------------------------------------------- | ------ | --------------------- | ------------------ | ---------- | ------------------- | ---- | ----------------- | ---------- | ----- | ------------------ | ----------------- | ------------------ | ------------------------------------------------------------ |
| Standard                                      | Klein  | Füllen                | Überlagert         | Dive       | x                   | -    | -                 | -          | -     | -                  | -                 | (x)                | Tag-Icons werden auf dem Bild angezeigt                      |
|                                               |        |                       | *Unterlegt (n/a)*  |            |                     |      |                   |            |       |                    |                   |                    |                                                              |
|                                               |        |                       | *Seitlich (n/a)*   |            |                     |      |                   |            |       |                    |                   |                    |                                                              |
|                                               |        | Thumbnail + Ohne Rand | *Überlagert (n/a)* |            |                     |      |                   |            |       |                    |                   |                    |                                                              |
|                                               |        |                       | Unterlegt          | Dive       | x                   | -    | x                 |            |       |                    |                   | x                  | einzeilig, die Tags werden unter Standard 1 angezeigt        |
|                                               |        |                       | Seitlich           | Dive       | x                   | -    | x                 | x          | -     | -                  | -                 | x                  | einzeilig, Tags werden unter Standard 1+2 angezeigt          |
|                                               | Mittel | Füllen                | Überlagert         | Dive       | x                   | -    | (x)               | (x)        | -     | -                  | -                 | (x)                | einzeilig, die Tags werden auf dem Bild angezeigt            |
|                                               |        |                       | *Unterlegt (n/a)*  |            |                     |      |                   |            |       |                    |                   |                    |                                                              |
|                                               |        |                       | *Seitlich (n/a)*   |            |                     |      |                   |            |       |                    |                   |                    |                                                              |
|                                               |        | Thumbnail + Ohne Rand | Überlagert         | Dive       | x                   | -    | (x)               | (x)        | -     | -                  | -                 | (x)                | einzeilig, die Tags werden auf dem Bild angezeigt            |
|                                               |        |                       | Unterlegt          | Dive       | x                   | -    | x                 | x          | -     | x                  | x                 | x                  | einzeilig, Tags werden unter Standard 1+2 angezeigt          |
|                                               |        |                       | Seitlich           | Dive       | x                   | -    | x                 | x          | -     | x                  | x                 | x                  | einzeilig, Tags werden unter Standard 1+2 angezeigt          |
|                                               | Groß   | Füllen                | Überlagert         | Dive       | x                   | -    | (x)               | (x)        | -     | (x)                | (x)               | (x)                | einzeilig, Tags werden auf dem Bild angezeigt                |
|                                               |        |                       | *Unterlegt (n/a)*  |            |                     |      |                   |            |       |                    |                   |                    |                                                              |
|                                               |        |                       | *Seitlich (n/a)*   |            |                     |      |                   |            |       |                    |                   |                    |                                                              |
|                                               |        | Thumbnail + Ohne Rand | Überlagert         | Dive       | x                   | -    | (x)               | (x)        | -     | (x)                | (x)               | (x)                | einzeilig, Tags werden auf dem Bild angezeigt                |
|                                               |        |                       | Unterlegt          | Dive       | x                   | x    | x                 | x          | x     | x                  | x                 | x                  | zweizeilig, Tags werden unter Standard 1+2 angezeigt, der Pfad wird über Standard 1 angezeigt, die technischen Infos werden auf dem Bild angezeigt |
|                                               |        |                       | Seitlich           | Dive       | x                   | x    | x                 | x          | x     | x                  | x                 | x                  | zweizeilig, Tags werden unter Standard 1+2 angezeigt, der Pfad wird über Standard 1 angezeigt, die technischen Infos werden auf dem Bild angezeigt |
| Text                                          | -      | -                     | -                  | Dive       | x*                  | (x)  | (x)               | (x)        | -     | (x)                | (x)               | (x)                |                                                              |
| Tabelle                                       | -      | -                     | -                  | Aufklappen | x                   | -    | (x) eigene Spalte | -          | -     | (x) eigene Spalten | (x) eigene Spalte | (x)  eigene Spalte |                                                              |
| Liste                                         | Klein  | -                     | -                  | Aufklappen | -                   | -    | x                 | -          | -     | -                  | -                 | -                  |                                                              |
|                                               | Mittel | -                     | -                  | Aufklappen | x                   | -    | x                 | x          | -     | -                  | -                 | x                  |                                                              |
|                                               | Groß   | -                     | -                  | Aufklappen | x                   | -    | x                 | x          | -     | -                  | x                 | x                  |                                                              |
| Hierachie-Browser (entspricht Liste "Mittel") | -      | -                     | -                  | Aufklappen | x                   | -    | x                 | x          | -     | -                  | -                 | -                  |                                                              |
| Neu Anlegen                                   | *tbd*  |                       |                    |            |                     |      |                   |            |       |                    |                   |                    |                                                              |
| Gruppeneditor                                 | *tbd*  |                       |                    |            |                     |      |                   |            |       |                    |                   |                    |                                                              |

**LEGENDE**: **x** = anzeigen, **(x)** = anzeigen, wenn Anzeigeoption aktiviert, **-** = nicht anzeigen, ***** = wenn OT kein Bild haben kann, keinen Platz reservieren



## Anzeige verlinkter Datensätze

Anzeigeoptionen in Masken:

| Zwischenüberschrift  | Anzeigeoption             | Option     | Bemerkung                         |
| -------------------- | ------------------------- | ---------- | --------------------------------- |
| Editor               | Anzeige                   | Standard   |                                   |
|                      |                           | Verbergen  |                                   |
|                      |                           | Nur lesend |                                   |
|                      | Drop-Down-Liste verwenden |            |                                   |
| Detail, Editor, Text | Feldbreite                |            |                                   |
|                      | Anzeigeart                | Standard   |                                   |
|                      |                           | Text       |                                   |
|                      |                           | Kurz       |                                   |
|                      | Standard-Info anzeigen    |            | Nur bei Anzeigeart "Text" enabled |
|                      | Objekttyp + SID anzeigen  |            |                                   |
|                      | Pool anzeigen             |            |                                   |
|                      | Tags anzeigen             |            |                                   |
| Filter               | Feld in Filter ausblenden |            |                                   |



Anzeige von verlinkten Datensätzen in der Detailansicht, dem Editor und der Textansicht:

| Modus    | Bild | Standard 1                   | Standard 2                   | Pfad | OT + SID                     | Pool                         | Tags                         |
| -------- | ---- | ---------------------------- | ---------------------------- | ---- | ---------------------------- | ---------------------------- | ---------------------------- |
| Standard | x    | x                            | x                            | x    | x, sofern in Maske aktiviert | x, sofern in Maske aktiviert | x, sofern in Maske aktiviert |
| Text     | x    | x, sofern in Maske aktiviert | x, sofern in Maske aktiviert | x    | x, sofern in Maske aktiviert | x, sofern in Maske aktiviert | x, sofern in Maske aktiviert |
| Kurz     | -    | x, als Link                  | -                            | -    | -                            | -                            | -                            |



## Anzeigeoptionen für Objekttypen

Sofern die folgenden Informationen in der Maske auf "Anzeigen" stehen, werden sie wie folgt angezeigt:

| Systemfelder       | Editor                       | Detail        | Bemerkung |
| ------------------ | ---------------------------- | ------------- | --------- |
| Objekt-ID          | ???                          | ???           |           |
| Hierarchie         | Eigenes Feld + Card          | Card          |           |
| Tags               | Eigenes Feld + Card          | Card          |           |
| Verantwortlicher   | Eigenes Feld                 | Eigenes Feld  |           |
| Veröffentlichungen | Eigenes Feld                 | Eigenes Feld  |           |
| Berechtigungen     | Eigenes Feld                 | Eigenes Feld  |           |
| Mappen             | Footer                       | Footer        |           |
| Pool               | Eigenes Feld + Card + Footer | Card + Footer |           |





## Autovervollständigung - TBD

Autocompletion (Hauptsuche): ??? Einen bereits vorhandenen View wählen ???

Search Mini (Autocompletion bei linked objects): ??? Einen bereits vorhandenen View wählen ???





## Anzeige von Hierarchien - TBD

- Hierarchische Hauptobjekttypen
- verlinkte hierarchische Nebenobjekttypen
- Pool

??? An welchen Stellen rückwärts anzeigen ???