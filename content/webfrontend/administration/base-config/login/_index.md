---
title: "70 - Anmelden"
menu:
  main:
    name: "Anmelden"
    identifier: "webfrontend/administration/base-config/login"
    parent: "webfrontend/administration/base-config"
---
# Anmelden {#login}

Unter diesem Reiter können Einstellungen für den Login vorgenommen werden.

## Cookies

|Einstellung | Erläuterung |
|-----|----|
|Cookies für Session-Absicherung aktivieren| Für den Session-Token kann zusätzlich das Setzen eines Cookies aktiviert werden. Das erschwert die Kopierbarkeit von Links zu Sessions, da die HTTP-Anfrage zum Token auch den Cookie benötigt. [*Zum Eintrag in der Technischen Dokumentation*](https://docs.easydb.de/en/technical/api/session)|

## Zugriff

|Einstellung  | Erläuterung |
|-----|-----|
|Anonym über Internet erlaubt| Bei Aufruf der Haupt-easydb-URL (http://<easydb-server>/) wird mit dieser Einstellung festgelegt, dass ein unbekannter Benutzer als anonymer Benutzer am System angemeldet wird. Jeder anonyme Benutzer ist automatisch in der Gruppe `Anonymer Benutzer` und kann darüber mit Rechten ausgestattet werden. easydb hinterlegt beim Benutzer einen Browser-Cookie, mit dem er beim nächsten Mal wiedererkannt wird und intern derselben Benutzer-ID zugeordnet wird. Für den Benutzer können dadurch Benutzer-Einstellung usw. gespeichert werden. Ob ein Benutzer aus dem Internet kommt oder nicht, wird über _Intranet-Konfiguration_ festgelegt. |
|Anonym über Intranet erlaubt| Wie *Anonym über Internet erlaubt* nur dass sich diese Einstellung auf Benutzer bezieht, die als Intranet-Benutzer erkannt wurden.|

## Vergessene Passwörter

|Einstellung | Erläuterung |
|-----|-----|
|Anfordern vergessener Passwörter erlauben (API).| Wenn aktiv, können Benutzer über ihre hinterlegte E-Mail-Adresse ein neues Passwort anfordern. Um den Anfrage Dialog im easydb Frontend nutzen zu können, muss zudem noch *Anfrage-Dialog im Login anzeigen" gesetzt werden. Über API können auch andere Anmeldeformulare genutzt werden, für die diese Einstellung gilt.|
|Anfrage-Dialog im Login anzeigen.|Wenn das *Anfordern vergessener Passwörter erlaubt* ist, kann im Login ein Anfrage-Link angezeigt werden, der dem Benutzer auf der Anmeldeseite die Möglichkeit bietet, über seine hinterlegte E-Mail-Adresse ein neues Passwort zu setzen (beide Checkboxen müssen dafür aktiv sein).|

> HINWEIS: Diese Einstellung gilt systemweit für alle Benutzer und kann nicht individuell entzogen werden.

## Hintergrundbild

|Einstellung | Erläuterung |
|-----|-----|
|Dateiupload für Hintergrundbild|Für die Login-Seite kann ein Hintergrund-Bild hochgeladen werden. Ein Standard-Bild wird in der .ini-Variable `[default-pics]background` festgelegt. Achten Sie darauf, dass das Bild groß ist, so dass für große Bildschirme keine Artefakte sichtbar werden.|

> Das Hintergrund-Bild wird nur bei der Login-Seite verwendet die erscheint, wenn Ihre easydb über /login aufgerufen wird oder kein anonymer Zugriff möglich ist (siehe oben). Beim anonymen Zugriff wird beim Aufruf bzw. beim Klick auf "Anmelden" lediglich die Login-Box eingeblendet.

## Informationstexte

|Einstellung | Erläuterung |
|-----|-----|
|Information neben dem Login| Hier kann ein Hinweis für den Benutzer hinterlegt werden. Der Text wird im Anmeldedialog neben dem Login angezeigt. Hier ist nur Text (Markdown) erlaubt, kein HTML.|
|Begrüßungstext| Der Begrüßungstext kann für die Login-Seite mehrsprachig hinterlegt werden. Hier ist nur Text (Markdown) erlaubt, kein HTML.|

## Passwort-Überprüfung

|Einstellung |Eingabe |Erläuterung |
|-----|---|----|
| Hinweis||Der mehrsprachige Text erklärt dem Benutzer, was er bei seinem Passwort beachten muss.|
|Bestimmungen||Legen sie mit _Minimum_ und _Maximum_ Regeln zur Überprüfung von Passwörtern fest. Über ein Regulären-Ausdruck wird das Passwort geprüft. Mit _Minimum_ und _Maximum_ legen sie fest wie oft der Reguläre Ausdruck mindestens gefunden werden muss und maximal gefunden werden darf. Es können mehrere reguläre Ausdrücke festgelegt werden. Die Überprüfung findet nicht für bestehende, sondern nur für neue Passwörter statt.|
|Wiederholte Passwörter erlauben| |easydb speichert alle vom Benutzer benutzen Passwörter (verschlüsselt). Für wiederverwendete Passwörter kann festgelegt werden, wie alt ein Passwort sein darf.|
| | _Immer_ | Ein Passwort darf niemals wiederverwendet werden. |
| | _Älter als ein Monat_ | Ein Passwort darf im selben Monat nicht wiederverwendet werden. |
| | _Niemals_ | Der Server schaltet die Überprüfung nach wiederholten Passwörtern ab.|
|Sperrung nach mehrfachen Fehlversuchen |Anzahl der Fehlversuche|Einfache Zahl, für die Anzahl der erlaubten Fehlversuche. Bleibt das Feld leer, gibt es keine Begrenzung für Fehlversuche.|
||Dauer der Sperre (in Sekunden)|Dauer der Sperrung, bis der Benutzer einen neuen Eingabeversuch starten kann. Zahl 60 = 60 Sekunden.|

## Hinweise für Benutzer

|Einstellung |Erläuterung |
|-----|----|
|Einleitungstext für eigene Einstellungen (Markdown)|Nach dem Login erscheint oben rechts das Benutzerprofil. Über das Menü können Benutzer Ihre Einstellungen ändern. Oben in diesen Einstellungen kann der Administrator einen Text für den Benutzer anzeigen lassen. |

## Selbstregistrierung für Benutzer erlauben
|Einstellung |Erläuterung |
|-----|----|
|Selbstregistrierung akivieren|Neben dem Button für den Login erscheint ein Button für die Registrierung, über den Benutzer selbst einen Account in easydb anlegen können. Eine Anleitung zur Einrichtung der Selbstregistrierung ist im Kapitel [Benutzerverwaltung](../../../userprefs/selfregister) zu finden. |
|Einleitungstext für Selbstregistrierung (Markdown)|Im oberen Bereich des Registrierungsformulars kann ein Text für den Benutzer hinterlegt werden.|
|Bestätigungstext für Selbstsegistrierung (Markdown)| Hier kann eine Bestätigungsnachricht für den Benutzer hinterlegt werden, die nach erfolgreichem Absenden des Registrierungsformulars in einem Pop-Up erscheint.  |


## Intranet-Konfiguration

Hier werden IP-Adressen (172.16.0.2) und Netze (zb. 192.168.0.0/16) hinterlegt, die als _Intranet_ gelten. Beim Aufruf des Servers wird die IP-Adresse des Aufrufes festgestellt und eine entsprechende Einordnung vorgenommen.

## Anmeldedienste: SSO

|Einstellung |Erläuterung |
|-----|----|
|Beschriftung für den Button um zum easydb-Login-Screen zu wechseln |Text der auf dem Button angezeigt werden soll, um vom SSO-Login-Screen zum easydb-Login-Screen zu wechseln. Dort werden Eingabefelder für Login und Passwort angezeigt. Wird nur verwendet, wenn die easydb standardmäßig mit der SSO-Login-Seite startet (Server-YML: visually_preferred: true) |
|Beschriftung für den Button um zum SSO-Dienst zu wechseln |Text der auf dem Button angezeigt werden soll, über den der Nutzer zum SSO-Dienst weitergeleitet wird. |
|Beschriftung für den Button um zum SSO-Login-Screen zu wechseln |Text der auf dem Button angezeigt werden soll, um vom easydb-Login-Screen zum SSO-Login-Screen zu wechseln. Dort werden keine Eingabefelder mehr für Login und Passwort angezeigt. Wird nur verwendet, wenn die easydb standardmäßig mit der SSO-Login-Seite startet und man manuell zur easydb-Login-Seite gewechselt ist (Server-YML: visually_preferred: true) |
