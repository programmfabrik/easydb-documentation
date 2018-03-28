# Anmelden {#login}

Unter diesem Reiter können Einstellungen für den Login vorgenommen werden.

|Einstellung | | Erläuterung |
|-----|--|---|
|Cookie-Absicherung für Session aktivieren| ||
|Anonym über Internet erlaubt| |Bei Aufruf der Haupt-easydb-URL (http://<easydb-server>/) wir mit dieser Einstellung festgelegt, dass ein unbekannter Benutzer als anonymer Benutzer am System angemeldet wird. Jeder anonyme Benutzer ist automatisch in der Gruppe `Anonymer Benutzer` und kann darüber mit Rechten ausgestattet werden. easydb hinterlegt beim Benutzer einen Browser-Cookie mit dem er beim nächsten Mal wiedererkannt wird und intern derselben Benutzer-ID zugeordnet wird. Für den Benutzer können dadurch Benutzer-Einstellung usw. gespeichert werden. Ob ein Benutzer aus dem Internet kommt oder nicht, wird über _Intranet-Konfiguration_ festgelegt.|
|Anonym über Intranet erlaubt| |Wie *Anonym über Internet erlaubt* nur dass sich diese Einstellung auf Benutzer bezieht, die als Intranet-Benutzer erkannt wurden.|
|Intranet-Konfiguration| |Hier werden IP-Adressen (172.16.0.2) und Netze (zb. 192.168.0.0/16) hinterlegt, die als _Intranet_ gelten. Beim Aufruf des Servers wird die IP-Adresse des Aufrufes festgestellt und eine entsprechende Einordnung vorgenommen.|
|Prozess für vergessene Passwörter initiieren| |Wenn aktiv, wird dem Benutzer auf der Anmeldeseite eine Möglichkeit angeboten, über seine hinterlegte E-Mail-Adresse ein neues Passwort zu setzen. Diese Einstellung gilt systemweit für alle Benutzer und nicht deaktiviert entzogen werden.|
|Hintergrundbild| |Für die Login-Seite kann ein Hintergrund-Bild hochgeladen werden. Ein Standard-Bild wird in der .ini-Variable `[default-pics]background` festgelegt. Achten Sie darauf, dass das Bild groß ist, so dass für große Bildschirme keine Artefakte sichtbar werden.|
|Information neben dem Login| |Hier kann ein Hinweis für den Benutzer hinterlegt werden. Der Text wird im Anmeldedialog neben dem Login angezeigt. Hier ist nur Text (Markdown) erlaubt, kein HTML.|
|Begrüßungstext| |Der Begrüßungstext kann für die Login-Seite mehrsprachig hinterlegt werden. Hier ist nur Text (Markdown) erlaubt, kein HTML.|
|Passwort-Überprüfung|Policy|Legen sie mit +/- Regeln zur Überprüfung von Passwörtern fest. Über ein Regulären-Ausdruck wird das Passwort geprüft. Mit _Minimum_ und _Maximum_ legen sie fest wie oft der Reguläre Ausdruck mindestens gefunden werden muss und maximal gefunden werden darf.|
| |Hinweis|Der mehrsprachige Text erklärt dem Benutzer, was er bei seinem Passwort beachten muss.|
|Wiederholte Passwörter erlauben| |easydb speichert alle vom Benutzer benutzen Passwörter (verschlüsselt). Für wiederverwendete Passwörter kann festgelegt werden, wie alte ein Passwort sein darf.|
| | _Immer_ | Ein Passwort darf niemals wiederverwendet werden. |
| | _Monat_ | Ein Passwort darf im selben Monat nicht wiederverwendet werden. |
| | _Niemals_ | Der Server schaltet die Überprüfung nach wiederholten Passwörtern ab. |
|Anmeldedienste: SSO|Text für Anmeldelink |Eigenen Anmeldetext für den Link zum Authentifizierungsdienst hinterlegen. Beleibt das Feld leer wird standardmäßig "Anmeldedienst verwenden" angezeigt. |


