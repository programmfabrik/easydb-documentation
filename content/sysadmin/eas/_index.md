---
title: "34 - easydb Asset Server"
menu:
  main:
    name: "easydb Asset Server"
    identifier: "sysadmin/eas"
    parent: "sysadmin"
    weight: 40
---
easydb-Asset-Server
===================

Der easydb-Asset-Server (auch EAS im Folgenden genannt) ist exklusiv für
die Berechnung und Verwaltung sämtlicher Assets (Bilder, Videos,
Office-Dokumente etc.) zuständig, die Sie mit der easydb verwalten.

[Hauptbestandteile](installation)

[Konfigurationsdatei](conf)

[Konfiguration bei Programmstart](initconf)

[Partitionen](partitions)

[API](api)

[Dateitypen](filetypes)

Dieser Dienst wird auch von der easydb4 verwendet, was die Migration zur
easydb5 an dieser Stelle wesentlich vereinfacht.

> Die weitere Dokumentation des EAS in den Unterkapiteln behandelt viele Interna, die nur innerhalb des EAS-Docker-Containers zugänglich sind.
>
> Dortige Pfadangaben beziehen sich also auf Pfade im Container, nicht auf Pfade direkt auf Ihrem Server, der den docker-Container ausführt.
