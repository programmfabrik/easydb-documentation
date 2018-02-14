# E-Mail Versand
Die easydb sendet an Ihre Nutzer E-Mails, z.B. um eine Bestätigung zu bekommen oder um über bestimmte Änderungen zu informieren.

In Folge des Missbrauchs der E-Mail-Infrastruktur im Internet erfordern die meisten Netzwerke unserer Kunden dass E-Mails an einen zentralen Server in diesem Netzwerk übergeben werden.

Die easydb geht davon aus dass es immer solch einen E-Mail-Server gibt, auch relay genannt. Damit E-mails versendet werden können muss dieser daher in der easydb konfiguriert werden.

## Konfigurationsbeispiel

In den folgenden Beispielen nehmen wir an, dass das relay die Adresse 172.18.0.1 hat. Wir nehmen an, dass E-Mails von diesem weitergeleitet werden, falls der easydb-Server sich als easy.example.com ausgibt und falls die Absende-Adresse noreply@example.com ist.

Außerdem nehmen wir an dass während der [Installation](/sysadmin/installation/installation.html#datenablage-bestimmen) als Datenablage "/srv/easydb" bestimmt wurde und dass Sie unter you@example.com per E-Mail erreichbar sind. Bitte passend Sie diese Annahmen an Ihre Situation an.

- Ergänzen Sie /srv/easydb/config/easydb5-master.yml mit:  *(allerdings ohne z.B. eine zweite "easydb-server:" Zeile zu erzeugen)*

~~~
easydb-server:
  server:
    mailer:
      enabled: true
common:
  email:
    server: 172.18.0.1
    hostname: easy.example.com
    from-address: noreply@example.com
~~~

- In der Web-Oberfläche der  easydb:
Wählen Sie '''Basiskonfiguration''' im Menü, scrollen Sie herunter bis zu den Absende-Adressen und füllen Sie beide Felder mit (in diesem Beispiel) noreply@example.com.

- Starten Sie den docker container "easydb-server" neu (oder die ganze easydb):

~~~
docker restart easydb-server
~~~

## E-Mail Versand testen

### Per SMTP testen

~~~
docker exec -ti easydb-server bash

apt-get install telnet
telnet 172.18.0.1 25

mail from:<noreply@example.com>
rcpt to:<you@example.com>
data
Subject: test via SMTP
.

quit
~~~

### Mit der E-Mail Software im container testen

~~~
docker exec -ti easydb-server bash

echo "Subject: testing sSMTP"|ssmtp -v -fnoreply@example.com -Fnoreply you@example.com
~~~

Optional: Lesen Sie die Konfiguration, die für die SMTP-Software ("SSMTP") übernommen wurde, aus Ihrer Konfiguration in easydb5-master.yml:

~~~
docker exec easydb-server cat /etc/ssmtp/ssmtp.conf
~~~

### Mit der Web-Oberfläche testen
1. In der oberen rechten Ecke ist Ihr Kontoname zu sehen. Beim Klick darauf erscheint die Option "Einstellungen".
2. Ändern Sie die E-Mail Addresse zu einer Adresse, die Sie empfangen - denn dorthin wird nun eine Bestätigungsanfrage versendet.

## E-Mails die sofort versendet werden
Bei bestimmten Operationen werden E-Mails vom Server verschickt. Folgende E-Mails werden sofort (1) verschickt:

| Name                    | Wann wird die E-Mail verschickt?                                 | An welche Adressen wird die E-Mail verschickt?                                          |
|-------------------------|------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| welcome_new_user        | Ein Benutzer wird angelegt                                       | An die "beste" (2) E-Mail-Adresse des neu angelegten Benutzers                          |
| updated_self_service    | Ein Benutzer ändert seine eigene Daten                           | An die "beste" (2) E-Mail-Adresse des Benutzers                                         |
| updated_record          | Die Daten eines Benutzers werden bearbeitet (von jemand anderem) | An die "beste" (2) E-Mail-Adresse des Benutzers                                         |
| forgot_password         | Ein Benutzer initiiert den Forgot-Password-Prozess               | An die angegebene E-Mail-Adresse, oder wenn das Login benutzt wurde, an die "beste" (2) |
| confirm_email           | Eine E-Mail braucht Bestätigung,                                 | An die zu bestätigende E-Mail-Adresse                                                   |
|                         | - weil sie vom Benutzer selbst geändert bzw. neu angelegt wurde  |                                                                                         |
|                         | - weil der Administrator es so eingestellt hat                   |                                                                                         |
| require_password_change | Ein Benutzer wird angefordert, sein Passwort zu ändern           | An die "beste" (2) E-Mail-Adresse des Benutzers                                         |
| login_disabled          | Ein Benutzer wird gesperrt (3)                                   | An die "beste" (2) E-Mail-Adresse des Benutzers                                         |
| share_collection        | Ein Benutzer wurde zu einer Collection eingeladen                | An die "beste" (2) E-Mail-Adresse des Benutzers                         |
| transition_resolve      | Eine Transition wurde ausgelöst und die E-Mail ist immediate     | Mailer entscheidet                                                                      |
| transition_reject       | Eine Transition wurde abgewiesen und die E-Mail ist scheduled    | Mailer entscheidet                                                                      |
| transport               | Ein Export ist fertig und der Benutzer erhält die Daten per E-Mail (transport "email") | An die "beste" (2) E-Mail-Adresse des Benutzers   |
| export                  | Ein Export ist fertig (Nachricht für den Export-Erzeuger)        | An die erste E-Mail-Adresse des Benutzers, die `send_email` hat                         |

Anmerkungen:

(1) "sofort" bedeutet, dass sie beim nächsten Lauf des Prozess "mailer" bearbeitet und verschickt werden. Die Frequenz
kann man in der Konfiguration einstellen (mailer.interval) setzen und ist Defaultmäßig eine Minute.

(2) Die "beste" E-Mail-Adresse ist die bevorzugte E-Mail-Adresse, wenn sie gesetzt ist. Andernfalls ist sie die erste E-Mail-Adresse des Benutzers.
Wenn der Benutzer keine E-Mail-Adresse eingestellt hat, wird die E-Mail nicht verschickt.

(3) Wenn ein Benutzer gesperrt wird (`login_disabled`), wird eine E-Mail verschickt. Während er gesperrt ist, werden keine weiteren E-Mails verschickt.

Zusätzlich gibt es eine E-Mail, die "scheduled" verschickt wird. Das bedeutet, dass sie zu den Zeitpunkten verschickt wird, die der Benutzer in seinem
"schedule" eingestellt hat:

| Name                    | Wann wird die E-Mail generiert?                                                                        | An welche Adressen wird die E-Mail verschickt?                  |
|-------------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| transition_resolve      | Eine Transition wurde ausgelöst und die E-Mail ist scheduled                                           | Mailer entscheidet                                              |
| transition_reject       | Eine Transition wurde abgewiesen und die E-Mail ist scheduled                                          | Mailer entscheidet                                              |

Die Transitions kann man konfigurieren, sodass die E-Mails einzeln oder zusammengefasst verschickt werden können (`batchable`). Im letzteren Fall werden Operationen für
die gleiche Transition (d.h. mit der gleichen Transition-ID) in der Transition-Tabelle (siehe unten) zusammengefasst.

## E-Mail-Templates

Der Server bastelt die E-Mails aus Templates zusammen. Templates sind E-Mails in mbox-Format, die Platzhalter enthalten können. Um eine E-Mail in
mbox-Format zu generieren, kann man ein Mail-Programm benutzen, sich die E-Mail selbst verschicken und sich den Quelltext der empfangenen E-Mail
anzeigen lassen. Es gibt Beispiele in `base/email/`.

Die E-Mail-Templates können Platzhalter für Variablen enthalten. Ein Platzhalter sieht so aus:

**%(**\<name\>**)**\<type\>

\<name\> ist der Name der Variable, die ersetzt wird. \<type\> bestimmt das Format für den Wert:

| Type | Bedeutung         |
|------|-------------------|
| s    | Text              |
| i    | Ganzzahl          |
| ui   | Positive Ganzzahl |
| d    | Datum + Zeit      |
| D    | Datum             |

Wenn die E-Mail gebaut wird, wird der Platzhalter durch den Wert der Variable in dem gewünschten Format ersetzt. Die Werte und die Datum- und Zeitformate sind lokalisiert. Das heißt,
der Benutzer erhält eine E-Mail in seiner Sprache.

Variablen vom Typ "s" können auch Platzhalter enthalten. Der Server erlaubt verschachtelte Platzhalter, solange sie sich nicht wiederholen.

Ein Beispiel:

~~~~
@@include:template@@
~~~~

~~~~
"server.email.subject","E-Mail für %(_generated_displayname)s","E-mail for %(_generated_displayname)s"
"server.email.welcome_new_user.greeting","Willkommen an Bord, %(_generated_displayname)s","Welcome aboard, %(_generated_displayname)s"
~~~~

Und `_generated_displayname` wird vom Server selbst angeboten.

Angenommen der Benutzer hat ein Displayname "Hans" und Deutsch als Sprache, würde er eine E-Mail mit dem Betreff: "E-Mail für Hans" bekommen.

### E-Mail-Template anpassen

- Kopieren Sie sich eine Vorlage aus dem container nach draußen: (Beispiel hier: Vorlage für E-Mails falls ein Zugang gesperrt wurde)

~~~
docker exec easydb-server cat /easydb-5/base/email/login_disabled.mbox > /srv/easydb/config/login_disabled.mbox
~~~

    Wie bereits angesprochen ist /srv/easydb nur ein Beispiel-Pfad für Ihre Datenablage, der bei der Installation der easydb festgelegt wurde.

    Der andere Pfad jedoch (/easydb/...) befindet sich im docker container und muss typischerweise genau so angegeben werden. Der Dateiname allerdings ("login_disabled.mbox") muss zu der Vorlage passen, die Sie anpassen wollen. Eine Liste von Vorlagen sehen Sie mit folgendem Befehl:

~~~
docker exec easydb-server ls /easydb-5/base/email
~~~

- Konfigurieren Sie, dass Ihre angepasste Vorlage verwendet werden soll, in easydb5-master.yml:

~~~
easydb-server:
  email:
    login_disabled:           /config/mail/login_disabled.mbox
~~~

Der Pfad /config/[...] befindet sich im container und sollte deshalb nicht um "/srv/easydb" ergänzt werden. Statt dessen kümmert sich docker darum, dass /srv/easydb/config im container als /config zur Verfügung steht. (Stichwort "mapped volume")

- Starten Sie den docker container "easydb-server" neu (oder die gesamte easydb):

~~~
docker restart easydb-server
~~~

### Variablen

Die Variablen, die als Quelle in den E-Mail-Templates benutzt werden können sind:

| Variable                        | Wert                                             |
|---------------------------------|--------------------------------------------------|
|`_generated_displayname`         | ein Darstellungsname des Benutzers, der je nach Verfügbarkeit aus dem Namen, dem Login oder der E-Mail-Adresse des Benutzers erstellt wird |
| `_login_or_email`               | der Login-Name des Benutzers oder, wenn nicht verfügbar, dessen E-Mail-Adresse |
| `first_name`                    | der Vorname des Benutzers |
| `last_name`                     | der Nachname des Benutzers |
| `login`                         | der Login-Name des Benutzers |
| `easydb_url`                    | die URL der easydb |
| `easydb_name`                   | der Name der easydb |
| `lang`                          | die ausgewählte Sprache des Benutzers |

Je nach E-Mail-Typ sind andere Variablen auch verfügbar:

| E-Mail-Typ                  | Variable                             | Wert |
|-----------------------------|--------------------------------------|------|
| updated_self_service        | self_service_fields_table            | HTML-Tabelle mit den Daten, die der Benutzer bearbeitet hat (vorher/nachher) |
| updated_record              | updated_fields_table                 | HTML-Tabelle mit den Daten, die bearbeitet wurden (vorher/nachher) |
| forgot_password             | task_link                            | URL zum Neusetzen des Passworts |
| require_password_change     | task_link                            | URL zum Ändern des Passworts |
| confirm_email               | task_link                            | URL zur E-Mail-Bestätigung |
| share_collection            | collection_name                      | Name der Collection |
| share_collection            | collection_description               | Beschreibung der Collection |
| share_collection            | collection_link                      | URL zur Collection |
| transport                   | export_id                            | Export-ID |
| transport                   | export_name                          | Name des Exports |
| transport                   | downloads                            | HTML-Tabelle mit den Dateien des Exports und Links zu den Downloads |
| transport                   | server.email.export.message (\*)     | Vom Benutzer konfigurierter Nachricht |
| transition_resolve & transition_reject | transitions                          | HTML-Tabelle mit Information über die Operationen, die die Transition ausgelöst haben |
| transition_resolve & transition_reject | server.email.transition.subject (\*) | Vom Benutzer konfigurierter Betreff |
| transition_resolve & transition_reject | server.email.transition.body (\*)    | Vom Benutzer konfigurierter Body |

Die Variablen, die mit (\*) markiert sind, kann der Benutzer mit eigenen Texten überschreiben, wenn eine Transition bzw. ein Export konfiguriert wird.
