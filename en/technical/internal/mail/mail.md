# E-Mail-Adressen

Ein User kann mehrere E-Mail-Adressen haben. Die Attribute sind [hier](/technical/types/user/user.md) zu sehen.

Eine valide E-Mail ist nicht abgelaufen und bestätigt (oder keine Bestätigung wurde angefordert):

```
valid = (NOT date_expire) AND (NOT date_request_confirm OR date_confirm)
```

Aus der Liste der E-Mails muss eine gewählt werden. Manchmal wird sie explizit angegeben und manchmal wird
die Entscheidung dem Mailer-Prozess überlassen.

Folgende E-Mails werden von der Easydb generiert (für Details, siehe [E-Mail-Konfiguration](/sysadmin/konfiguration/email/email.md)):

| Ursprung        | Template                | Typ                 | E-Mail explizit angegeben? |
|-----------------|-------------------------|---------------------|----------------------------|
| /api/user       | welcome_new_user        | immediate           | Ja                         |
| /api/user       | updated_self_service    | immediate           | Ja                         |
| /api/user       | updated_record          | immediate           | Ja                         |
| /api/user       | forgot_password         | immediate           | Ja                         |
| /api/user       | confirm_email           | immediate           | Ja                         |
| /api/user       | require_password_change | immediate           | Ja                         |
| /api/user       | login_disabled          | immediate           | Ja                         |
| /api/collection | share_collection        | immediate           | Ja                         |
| /api/db         | transition_resolve      | immediate/scheduled | Nein                       |
| /api/db         | transition_reject       | immediate/scheduled | Nein                       |
| export_worker   | transport               | immediate           | Ja                         |
| export_worker   | export                  | immediate           | Ja                         |

# Mailer

Der Mailer bearbeitet die Queue in einem in "server/mailer/interval" Sekunden und verwendet die konfigurierten "server/mailer/sender_address" und "server/mailer/envelope_address".

Die Schritte sind:

(1) immediate E-Mails bearbeiten
(2) scheduled E-Mails bearbeiten
(3) failed_delay E-Mails bearbeiten
(4) failed_delete E-Mails bearbeiten

## (1) immediate E-Mails bearbeiten

Der Mailer holt sich:

- immediate Einträge und
- scheduled Einträge, deren User kein Schedule hat,
- bei denen die Anzahl der Versuche <= "server/mailer/max_attempts" ist

Die Adresse kann entweder:

- explizit angegeben werden, oder
- vom User kommen: dann wird die erste valide Email mit use_for_mail genommen

Die E-Mail wird gebaut und verschickt:

- wenn alles OK läuft, wird der Eintrag gelöscht
- wenn keine Adresse gefunden wird, wird ein ERROR geloggt und der Eintrag als "failed_delete" markiert (siehe 4)
- wenn die E-Mail nicht gebaut werden kann, wird ein ERROR geloggt und der Eintrag als "failed_delete" markiert (siehe 4)
- wenn die E-Mail nicht zugestellt werden kann, wird der Eintrag also "failed_delay" markiert (siehe 3)

## (2) scheduled E-Mails bearbeiten

Der Mailer holt sich:

- scheduled Einträge, die nach dem User-Schedule bearbeitet werden sollten und
- bei denen die Anzahl der Versuche <= "server/mailer/max_attempts" ist

Die Adresse wird wie bei (1) ermittelt und:

- wenn der Eintrag nicht batchable ist, wird eine E-Mail gebaut und verschickt
- batchable Einträge werden pro Nutzer und Template gebaut und als einzige E-Mail verschickt

Die Fehlerbehandlung ist wie bei (1)

## (3) failed_delay E-Mails bearbeiten

Der Eintrag wird geupdated: Anzahl der Versuche, Fehler und Timestamp. Wenn die Anzahl der Versuche >= "server/mailer/max_attempts" ist, wird der Eintrag als failed_delete markeiert.

## (4) failed_delete E-Mails bearbeiten

Der Eintrag wird gelöscht.

**TODO**: der Administrator erhält eine E-Mail mit der Information.
