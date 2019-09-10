---
title: "207 - Janitor"
menu:
  main:
    name: "Janitor"
    identifier: "webfrontend/administration/base-config/janitor"
    parent: "webfrontend/administration/base-config"
---

# Janitor

Einstellungen zum endgültigen Löschen von Objekten, Benutzerdaten und Assets.

> Für allgemeine technische Informationen zum Janitor, klicken Sie [hier](/en/technical/janitor) (Dokumentation auf englisch).

Zeitintervalle können in Minuten (mit dem Suffix `'m'`), Stunden (mit dem Suffix `'h'`) oder Tagen (mit dem Suffix `'d'`) angegeben werden.

Zum Beispiel würde ein Intervall von 5 Minuten als `'5m'` angegeben werden, 24 Stunden können als `'24h'` oder `'1d'` angegeben werden.

### Allgemeine Janitor-Einstellungen

* **Janitor-Intervall**:
  * Wartezeit zwischen zwei Durchläufen des Janitors
  * Mindestdauer: 1 Minute (`'1m'`)
  * Standardwert: 10 Minuten (`'10m'`)

### Einstellungen zum Löschen von Sessions aus der Datenbank

* **Ablaufdauer für Sessions**:
  * Geben Sie an, nach welcher Zeit nach dem letzten Update der Session (dem Zeitpunkt des letzten authentifizierten API-Aufrufs mit dieser Session), die Session ablaufen soll.
      * Bitte beachten Sie, dass Eventpolling Requests (`/api/v1/event/poll`) ignoriert werden. Alle anderen Requests setzen die Ablaufzeit der Session zurück.
  * Mindestdauer: 1 Minute (`'1m'`)
  * Standardwert: 1 Woche (`'7d'`)

* **Abgelaufene Sessions endgültig aus der Datenbank löschen**:
  * Wählen Sie aus, ob abgelaufene Sessions endgültig aus der Datenbank gelöscht werden sollen.

### Einstellungen zum Löschen von Exporten und Downloads

* **Ablaufdauer für Exporte und Downloads**:
  * Geben Sie an, nach welcher Zeit Dateien für Exporte und Downloads vom System gelöscht werden sollen.
  * Mindestdauer: 1 Minute (`'1m'`)
  * Standardwert: 1 Woche (`'7d'`)
