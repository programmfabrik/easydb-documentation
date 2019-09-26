---
menu:
  main:
    name: "5.57"
    identifier: "5.57"
    parent: "releases"
    weight: -557
---

> **Neue Systemrechte:**
>
> *  **Zugriff auf Recherche** wurde um **Eigene Mappen verwalten** ergänzt. 
> * **Frontend-Funktionen** wurde um **CSV-Importer** und **JSON-Importer** ergänzt.

# Version 5.57.0

*Veröffentlicht am 26.09.2019*

### Webfrontend

*Neu*

* **Datenmodell**: Mehrfachfelder können jetzt `not_null`gesetzt werden. Dieses wird vom Server auf API-Level beim Speichern und Aktualisieren überprüft.
* **Rechtemanagement**: Ein neues Systemrecht **Zugriff auf Recherche** wurde um ein Parameter **Eigene Mappen verwalten** ergänzt. Benuzter und Gruppen für die vor dem Update **Zugriff auf Recherche** eingestellt ist, erhalten dieses Recht automatisch.
* **Filter**: Über eine Einstellung ist es möglich verlinkte Objekttypen in einem gemeinsamen Filter anzuzeigen oder nicht, wobei diese Einstellung standardmäßig deaktiviert ist. Bisher wurde das automatisch gemacht, sobald der verlinkte Objekttyp mindestens in zwei Feldern verlinkt wurde.
* **Listen**: Die Anzeige von **CSV-Importer** und **JSON-Importer** ist nun standardmäßig aus und muss über Parameter des Systemrechts **Frontend-Funktionen** für Benutzer und / oder Gruppen aktiviert werden.
* **Detailanzeige**: Textfelder zeigen neben **Web-Addressen** nun auch **Email-Addressen** als Link an.
* **Benutzermanagement**: Eine neue Spalte **Login** zeigt den Loginnamen des Benutzers an.

*Verbessert*

* **Mitteilungen**: Im Administrationsbereich und den Menüs werden Mitteilungen alphabetisch sortiert.
* **Benutzermanagement**: Gruppen werden aufsteigend nach ID sortiert, so dass sie eine nachvollziehbare Reihenfolge bekommen, das ist wichtig für die automatische Zuordnung von Einstellungen für neue Nutzer die auf Gruppen basieren können.
* **Editor**: Beim Speichern von Reverse-Objekten aus unterschiedlichen Objekttypen werden im Gruppenmodus beim Wechsel eines Pools auch die Reverse-Objekte in den neuen Pool geschoben. Das findet aber nur statt, wenn keine weiteren Felder aktualisiert weren. Ein entsprechender Hinweis wird unterhalb der Poolauswahl angezeigt.
* **Änderungshistorie**: Die Anzeige startet nun mit dem aktuellen Objekt.
* **Grafische Verbesserungen**: Das Eingabefeld für Email wurde verbreitert. Mehrzeilige Textfelder in Spalten werden niedriger angezeigt. 

*Behoben*

* **CSV-Importer**: Beim Laden von inkompatiblen Einstellungen werden einige Konflikten nun automatisch korrigiert.
* **Mitteilungen**: Unter bestimmten Umständen wurden Mitteilungen in Untermenüs nicht immer rechtzeitig geladen so dass sie nicht angezeigt wurden.
* **Benutzermanagement**: `Kopieren`wurde für Nutzer repariert die in Custom-Gruppen sind.
* **Drucken**: Das Drucken von verlinkten Objekten die im Textmodus angezeigt werden wurde repariert.