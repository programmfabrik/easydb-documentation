---
title: "57 - Systemadministration"
# no German menu
# menu:
#  main:
#    name: "Systemadministration"
#    identifier: "sysadmin"
#    weight: -950
---
# Systemadministration

In diesem Abschnitt dokumentieren wir administrative Eingriffe außerhalb des Web-Interfaces.

* [Voraussetzungen](/de/sysadmin/requirements)
* [Installation](/de/sysadmin/installation)
* [Konfiguration](/de/sysadmin/configuration)
* [Betrieb](/de/sysadmin/operations)
* [Migration](/de/sysadmin/migration)
* [Instanziierung](/de/sysadmin/installation/instances) \(mehrere easydbs auf dem gleichen Server\)

### Begriffsklärung

Im Zweifelsfall bezieht sich "Systemadministration" auf dieses Kapital und ["Administration"](../webfrontend/administration) auf Eingriffe mithilfe des Web-Interfaces.

# Docker Integration

![Docker Integration](../sysadmin/easydb5_docker_architecture.png)

* Docker: 1 großer **hellgrau**er Kasten mit gepunkteter Linie
* Docker Container: 5 **grau**e Kästen
* Services: **weiß**e Rechtecke
* Speicher der in docker eingeblendet wird: **grün**
* Ports: **gelb**
* Optionale ports zum Netzwerk außerhalb des Servers zeigend: **gepunktet** \(ganz oben\)
* Optionaler Webserver für z.B. HTTPS oder Single Sign-On: **hellblau**es Rechteck \(ganz oben\)

### Weiterführendes

Für u.a. die Aufgaben der einzelnen Komponenten siehe bei Bedarf: [Technische Dokumentation](https://docs.easydb.de/en/technical).

