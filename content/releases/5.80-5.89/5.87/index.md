---
menu:
  main:
    name: "5.87 (Ende Juli 2021)"
    identifier: "5.87"
    parent: "releases589"
    weight: -587
---

> Für dieses Release ist **kein Re-Index** nötig.

# Version 5.87.2

*Veröffentlicht am 02.08.2021*

## Webfrontend

### Verbessert

* **Detail**: Die Anzeige von verlinkten Objekten ohne Datei wurde verschlankt.

### Behoben

* **Suche**: Anzeigeproblem in der Tabellenansicht bei schnellem Wechsel von Objekttypen wurde behoben.
* **Benutzer** / Gruppensuchen: Archivierte Nutzer werden nicht mehr angezeigt.

## Server

* **/api/objects**: Format *xml_easydb* konnte in einigen Fällen nicht produziert werden und meldete eine Zeitüberschreitung.

# Version 5.87.1

*Veröffentlicht am 29.07.2021*

## Webfrontend

### Behoben

* **Suche**: Fehler beim Laden der Suche in Datenmodellen mit verlinkten Objekten für EAS Standard-Felder behoben.

# Version 5.87.0

*Veröffentlicht am 28.07.2021*

## Webfrontend

### Neu

* **Gruppenmanager**: Der IP-Filter versteht jetzt auch IPv6 (nur easydb 6).

### Verbessert

* **Plugin Typo3**: Kombinierte Felder werden jetzt nicht mehr mit einem `;` voneinander getrennt.
* **Exportmanager**: Die Event-Information wird in einem Tooltip komplett angezeigt.

### Behoben

* **Dialoge**: In einigen Dialogen wurde das HTML-Escaping korrigiert.
* **Datenmodell**: Beim Öffnen des Datenmodells wird ein Konsistenz-Check durchgeführt und eine Meldung ausgegeben wenn das Modell Probleme hat. Wir haben eine Inkonsistent bei reverse verlinkten Masken korrigiert die durch erneutes Speichern des Datenmodells (und anschließender Aktivierung) behoben werden kann.
* **Das konfigurierte Logo** wurde in eingen Fällen in Firefox nicht korrekt angezeigt.

## Server

### Neu

* **Maskenmanagement**: Eine neue Option erlaubt das Erstellen der Standard-Info mit nur dem ersten Eintrag in einem Mehrfachfeld.
* Dateien mit Endung `.obj` werden der Dateiklasse `vector3d` zugefügt.

### Verbessert

* **XML-Export**: Für hierarchische Objekte wird `_has_children` mit exportiert. Für reverse verlinkte Objekte wird die `_system_object_id` ausgegeben.
* **/api/settings**: Neues Feld `version`. Diese Version ist die einzige Version die wir in der API für easydb 6 belassen.
* **Export**: Einstellmöglichkeiten wieviel Exporte gleichzeitig im Hintergrund erstellt werden können. Das ermöglicht ein besseres Ressourcen-Management in größeren Installationen.
* Alle von Programmfabrik **ausgelieferten Plugins** sind jetzt in eigene Repositorien. Diese Änderung sollte keine sichtbare Auswirkung haben ist jedoch eine Vorbereitung zur Kompabilität mit easydb 6.

### Behoben

* **Datenmodell**: Potentielle interne Speicherfehler wurden korrigiert.

* **Suche**: Die Indzierung von Zeiträumen für Aggregationen kann jetzt mit Zeitzonen umgehen.

* **Benutzermanagement**: Verifizierung von erlaubten Zeichen in Benutzernamen.

* **/api/session**: Der Parameter `cookieauth wurde entfernt und wird nicht mehr unterstützt.

* **/api/mask**: Die Überprüfung für einige Fälle von falschen reverse verlinkten Feldern wurde verbessert.

* **/api/mask**: Umbenennung von reverse verlinkten Feldern wird jetzt korrekt durchgeführt.

* **Email**: Ein Problem mit dem Versenden von Emails wurde behoben.


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:ce4ccb312e12cdcb8daa9151e80081738b2612b1c109ecdcb39519e3f367c6ec
docker.easydb.de/pf/eas                  sha256:0f5b60d7aac9d6f3d832b62e2f02bdf2dda0519528ded041308ab29cbb3ee4b1
docker.easydb.de/pf/elasticsearch        sha256:2a9ca9620e35567d8ea6c666055e4377ca556d16b0a619f2198d9cc9fe9bc526
docker.easydb.de/pf/fylr                 sha256:153b381eb3bfdac633a3a119a69a3fc9f16806de0aa83c95e9d2e149fb19d665
docker.easydb.de/pf/postgresql-11        sha256:74a9fa8e0ee63bfe39f11adabbeaa141921fd2443e5735f85b73e249acf4e566
docker.easydb.de/pf/server-base          sha256:b882a3799463fb05c04b0967146d3372f5688c1594d15f205e1cb8944253a978
docker.easydb.de/pf/webfrontend          sha256:659c2ac11d3eed556b23a6ae1d20ee65ec63516855d96764dfbff9d74f670719
```

