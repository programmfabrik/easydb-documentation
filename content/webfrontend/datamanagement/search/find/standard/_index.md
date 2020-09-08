---
title: "Standard"
menu:
  main:
    name: "Standard"
    identifier: "webfrontend/datamanagement/search/find/standard"
    parent: "webfrontend/datamanagement/search/find"
---
# Standard - In Bearbeitung

Die Card kann max. folgende Infos enthalten:

- Bild (sofern dies in der Maske eingerichtet ist)
- Pfad (sofern es ein hierarchischer Objekttyp ist)
- Standard 1 (sofern dies in der Maske eingerichtet ist)
- Standard 2 (sofern dies in der Maske eingerichtet ist)
- Objekttyp + ID (sofern dies in der Maske aktiviert ist)
- Pool (sofern dies in der Maske aktiviert ist)
- Tags (sofern dies in der Maske aktiviert ist)



Anzeige-Optionen in der Suche:

| View                                            | Größe  | Format              | Stil                          | Hier.      | Bild | Pfad | Standard 1                 | Standard 2                 | Tech. | SID                        | OT                         | Pool                       | Tag                        |
| ----------------------------------------------- | ------ | ------------------- | ----------------------------- | ---------- | ---- | ---- | -------------------------- | -------------------------- | ----- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| Standard (wenn Option "Standard-Info anzeigen") | Klein  | Füllen              | Überlagert                    | Dive       | x    | -    | x                          | x                          | -     | -                          | -                          | -                          | x                          |
|                                                 |        | Thumbnail/Ohne Rand | Überlagert (Option entfernen) |            |      |      |                            |                            |       |                            |                            |                            |                            |
|                                                 |        |                     | Unterlegt (Option entfernen)  |            |      |      |                            |                            |       |                            |                            |                            |                            |
|                                                 |        |                     | Seitlich                      |            | x    |      | x                          | x                          | -     | -                          | -                          | -                          | x                          |
|                                                 | Mittel | Füllen              | Überlagert                    | Dive       | x    | -    | x                          | x                          |       | ???                        | ???                        | x                          | x                          |
|                                                 |        | Thumbnail/Ohne Rand | Überlagert                    | Dive       | x    | -    | x                          | x                          |       | ???                        | ???                        | x                          | x                          |
|                                                 |        |                     | Unterlegt                     | Dive       | x    | -    | x                          | x                          |       | ???                        | ???                        | x                          | x                          |
|                                                 |        |                     | Seitlich                      | Dive       | x    | -    | x                          | x                          |       | x                          | x                          | x                          | x                          |
|                                                 | Groß   | Füllen              | Überlagert                    | Dive       | x    | -    | x                          | x                          | x     | x                          | x                          | x                          | x                          |
|                                                 |        | Thumbnail/Ohne Rand | Überlagert                    | Dive       | x    | -    | x                          | x                          | x     | x                          | x                          | x                          | x                          |
|                                                 |        |                     | Unterlegt                     | Dive       | x    | -    | x                          | x                          | x     | x                          | x                          | x                          | x                          |
|                                                 |        |                     | Seitlich                      | Dive       | x    | -    | x                          | x                          | x     | x                          | x                          | x                          | x                          |
| Text (wenn Option "Standard-Info anzeigen")     | -      | -                   | -                             | Dive       | x    | -    | x                          | x                          | x     | x                          | x                          | x                          | x                          |
| Tabelle                                         | -      | -                   | -                             | Aufklappen | x    | -    | Optional als eigene Spalte | Optional als eigene Spalte | -     | Optional als eigene Spalte | Optional als eigene Spalte | Optional als eigene Spalte | Optional als eigene Spalte |
| Liste                                           | Klein  | -                   | -                             | Aufklappen | -    | -    | x                          | -                          | -     | -                          | -                          | -                          | -                          |
|                                                 | Mittel | -                   | -                             | Aufklappen | x    | -    | x                          | x                          | -     | -                          | -                          | -                          | -                          |
|                                                 | Groß   | -                   | -                             | Aufklappen | x    | -    | x                          | x                          | -     | -                          | -                          | x                          | x                          |
| Hierachie-Browser (entspricht Liste "Mittel")   | -      | -                   | -                             | Aufklappen | x    | -    | x                          | x                          | -     | -                          | -                          | -                          | -                          |
| Neu Anlegen                                     |        |                     |                               |            |      |      |                            |                            |       |                            |                            |                            |                            |
| Gruppeneditor                                   |        |                     |                               |            |      |      |                            |                            |       |                            |                            |                            |                            |

Technische Infos enthalten max. folgende Informationen:

- Dateigröße (alle Dateiklassen)
- Abmessung (nur Bilder)
- Dateiendung (alle Dateiklassen)
- Seitenanzahl (nur Dokumente)
- Laufzeit (nur Audio & Video)



Anzeige von verlinkten Datensätzen in der Detailansicht, dem Editor, der Textansicht und Autovervollständigung:

| Modus    | Bild                                        | Standard 1  | Standard 2 | Pfad | SID                                         | OT                                          | Pool                                        | Tags                                        |
| -------- | ------------------------------------------- | ----------- | ---------- | ---- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| Standard | x                                           | x           | x          | x    | x, wenn in Maske aktiviert                  | x, wenn in Maske aktiviert                  | x, wenn in Maske aktiviert                  | x, wenn in Maske aktiviert                  |
| Text     | x, als eigenes Feld wenn in Maske aktiviert | -           | -          |      | x, als eigenes Feld wenn in Maske aktiviert | x, als eigenes Feld wenn in Maske aktiviert | x, als eigenes Feld wenn in Maske aktiviert | x, als eigenes Feld wenn in Maske aktiviert |
| Kurz     | -                                           | x, als Link | -          | -    | -                                           | -                                           | -                                           | -                                           |

