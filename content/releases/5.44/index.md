---
menu:
  main:
    name: "5.44"
    identifier: "5.44"
    parent: "releases"
    weight: -544
---

> Mit dieser Version ist es möglich, die bisher gemeinsam für alle Dienste in `easy5-master.yml` gepflegte Konfiguration aufzuteilen (Link auf Dokumentation folgt). Durch die dazu notwendigen Änderungen sind Anpassungen in der Konfiguration notwendig. Die aufgezeigten Beispiele beziehen sich alle auf die schon vorhandene `easy5-master.yml`:
>
> **E-Mail-Konfiguration**. Sofern der Block `common.email` verwendet wird, muss dieser dupliziert als `easydb-server.smtp` und `eas.smtp` abgelegt werden. Der alte Block `common` kann nach dem Update entfernt werden. Siehe auch [E-Mail-Konfiguration](/en/sysadmin/konfiguration/recipes/email).
>
> alt:
>
> ````yaml
> common:
>   email:
>     server: 172.18.0.1
>     hostname: easy.example.com
>     from-address: noreply@example.com
> ````
>
> neu:
>
> ````yaml
> easydb-server:
>   smtp:
>     server: 172.18.0.1
>     hostname: easy.example.com
>     from-address: noreply@example.com
> eas:
>   smtp:
>     server: 172.18.0.1
>     hostname: easy.example.com
>     from-address: noreply@example.com
> ````
>
> **Host-Konfiguration**. Diese Änderung sollte nur in Ausnahmefällen notwendig sein, wenn die Installation vom Standard abweicht und z.B. auf mehrere Maschinen verteilt ist oder mehrere Instanzen auf einer Maschine laufen. In dem Fall, dass `docker-hostname` in `easy5-master.yml` vorkommt, sollte die Konfiguration erweitert werden. Dabei wird `easydb-server.docker-hostname` zu `easydb-server.hostnames.server`, `eas.docker-hostname` zu `easydb-server.hostnames.eas` sowie `fylr.docker-hostname` zu `easydb-server.hostnames.fylr`. Die bisherigen Konfigurationsvariablen sollten erhalten bleiben.
>
> alt:
>
> ````yaml
> eas:
>   docker-hostname: custom-eas
> easydb-server:
>   docker-hostname: custom-server
> fylr:
>   docker-hostname: custom-fylr
> ````
> neu:
>
> ````yaml
> eas:
>   docker-hostname: custom-eas
> easydb-server:
>   docker-hostname: custom-server
>   hostnames:
>     eas: custom-eas
>     server: custom-server
>     fylr: custom-fylr
> fylr:
>   docker-hostname: custom-fylr
> ````

# Version 5.44

*Veröffentlicht am 12.12.2018*

### Webfrontend

*Neu*

*Verbessert*

*Behoben*

### Server & Plugins

*Neu*

*Verbessert*

*Behoben*

