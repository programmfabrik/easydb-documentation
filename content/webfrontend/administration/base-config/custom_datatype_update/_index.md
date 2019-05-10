---
title: "Custom Datatype Update"
menu:
  main:
    name: "Custom Datatype Update"
    identifier: "webfrontend/administration/base-config/custom-datatype-update"
    parent: "webfrontend/administration/base-config"
---

# Update-Einstellungen für Custom Data Types

Wählen Sie für Custom Data Type Plugins, die ein automatisches Update unterstützen, in welchen Intervallen Objekte mit Daten des Custom Data Types automatisch aktualisiert werden sollen.

Alle Objekte, die einen der geänderten Custom Data Types enthalten, werden aktualisiert und neu indiziert. Bitte beachten Sie, dass dies viel Zeit in Anspruch nehmen kann.

| Einstellung | Erläuterung | Bereich | Default |
| --- | --- | --- | --- |
| Automatische Updates aktualisieren | Automatisch Aktualisierungen für alle Custom Types (de-)aktivieren | `true` / `false` | `false` |
| Update Stunde | Update aller Custom Data Types zur vollen Stunde pro Tag| `0..23` | `0` (0:00 Uhr) |
| Pause zwischen Updates | Nach der Aktualisierung aller Custom Types, warte so viele Tage bis zum nächsten Durchlauf | `> 0` | `1` (tägliche Updates) |

Custom Data Type Plugins mit eigenen Einstellungen für die Basis-Konfiguration können diese unter dieser Gruppe einfügen.