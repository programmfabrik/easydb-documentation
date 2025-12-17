---
menu:
  main:
    name: "5.151 (Dezember 2025)"
    identifier: "5.151"
    parent: "releases"
    weight: -651
---

> Diese Version benötigt **keinen neuen** Index-Aufbau


# Version 5.151.0

*Veröffentlicht am 17.12.2025*


# Webfrontend

## Behoben
* **Tags**: es wird jetzt die beste verfügbare Sprache für die Anzeige verwendet. Vorher wurden Tags nur in der ausgewählten Frontend-Sprache angezeigt und konnten deswegen leer sein.
* **Video-Player**: Bug behoben, der u.U. einen unsichtbaren Video-Player erstellte.
* **Filter**: Darstellung für Felder behoben, die "Rechtemanagement via Tags" verwenden
* **Tabellenansicht**: Problem behoben, bei dem die Objekthierarchie nicht angezeigt wurde, wenn nur ein Pool ausgewählt war. Wenn dieser Pool nicht der Root-Pool war, wurde die Anzeige unterdrückt.


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.151.0            sha256:d55d9f62d0d4878b18a557d584a3df7b5f8b623ebc83938edea4988e4a35c845
docker.easydb.de/pf/elasticsearch:5.151.0  sha256:ec332d919c26e1c42ad04698df5cdb4bdab5f6e32669f75cea19ab39881316a1
docker.easydb.de/pf/fylr:5.151.0           sha256:f4f07c2266b647051ef7205d97045fafe0589adbf042212551dacc423398a005
docker.easydb.de/pf/postgresql-14:5.151.0  sha256:85ba93a993a95581e57f9984041356d06473520e9b753fcbfeaab2e567d5e78c
docker.easydb.de/pf/server-base:5.151.0    sha256:5d3d7a04984a59fe5761c7b25c21f88afa42ceede82a8710bfb27d9ebcc5ada5
docker.easydb.de/pf/webfrontend:5.151.0    sha256:45efd4c55a8c7241bc7c1c010d90824f0c8069b0a1c37b4643b73554406278eb
```
