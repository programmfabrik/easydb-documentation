# YAML-Konfiguration

## Struktur und Ladereihenfolge

Der Easydb-Server wird durch YAML-Dateien konfiguriert. Die YAML-Dateien werden in der folgenden Reihenfolge geladen:

- `easydb5-master.yml` im Pfad, den Sie bei der [Installation](./sysadmin/installation/installation.md) festgelegt haben.
- Unter der Haube, also im docker container, wird zuerst `easydb-server.yml` im aktuellen Pfad geladen, falls vorhanden. Das sollte für Sie als Kunde nur in Ausnahmefällen relevant sein.
- Generell werden weitere Dateien geladen, die als Argument in der Kommando-Zeile angegeben werden (mit `--configfile`), in der Reihenfolge, mit der sie angegeben werden.

Eine YAML-Datei kann auch weitere Konfigurations-Dateien miteinbeziehen:

- Die Variable **include_before** ist eine Liste von Dateien, die vor der Datei geladen werden, in der sie definiert ist
- Die Variable **include_after** ist eine Liste von Dateien, die nach der Datei geladen werden, in der sie definiert ist

Die Dateien werden entweder mit absolutem Pfad definiert, oder relativ zu der YAML-Datei, in der sie angegeben wurden.

Außerhalb vom docker-container empfehlen wir alles in die eine YAML-Datei `easydb5-master.yml` mit-aufzunehmen.

## Typen

Variablen werden in Maps strukturiert, aber eine allgemeine Map ist kein gültiger Typ für eine Variable. Die unterstützten Typen sind:

| Easydb-Typ    | YAML-Typ                 | Kommentar |
|---------------|--------------------------|-----------|
| String        | String                   | |
| Integer       | Integer                  | |
| Boolean       | Boolean, String, Integer | true: true, "on", "1", 1 |
|               |                          | false: false, "off", "0", 0, null, nicht gesetzt |
| Datei         | String                   | entweder absolut oder relativ zu dem YAML-Datei, in dem die Variable definiert ist |
| Verzeichnis   | String                   | wie Datei |
| Dateien-Liste | Sequence of Strings      | nicht gesetzt = null = leere Liste |
|               |                          | jede Datei ist absolut oder relativ zu dem YAML-Datei, in dem sie definiert sind, d.h. eine Liste kann Dateien mit verschiedenen relativen Pfaden enthalten |

## Ersetzungen

Wenn eine Variable bereits definiert wurde, wird deren Wert ersetz, wenn sie zu einem späteren Zeitpunkt noch mal definiert wird. Weitere
möglichkeiten sind:

- variable+: fügt einen neuen Wert hinzu (gilt nur für Listen). Beispiel: Zwei weitere Plugins aktivieren mit der Liste "enabled":
```YAML
  plugins:
    enabled+:
      - base.custom-data-type-link
      - base.custom-data-type-gnd
```
- variable-:
    - wenn die Variable eine Liste ist, werden die angegebenen Werte aus der Liste gelöscht
    - wenn die Variable ein Scalar ist, wird sie undefiniert
    - wenn die Variable eine Map ist, werden alle Variablen darunter undefiniert
- variable-key: nur für Listen von Maps, entferne alle Einträge aus der Liste, deren Wert für "key" in der angegebenen Liste enthalten sind

## Liste der Variablen

**Easydb-Server**

| Variable                                         | Typ           | Pflicht | Erklärung | Default-Wert |
|--------------------------------------------------|---------------|---------|-----------|--------------|
| **base**                                         |               |         | | |
| &#8614; plugins                                  | Dateien-Liste | Nein    | Liste der Base-Plugins | (leer) |
| **solution**                                     |               |         | Konfiguration der Solution | |
| &#8614; name                                     | String        | Ja      | Name der verwendeten Solution | |
| &#8614; plugins                                  | Dateien-Liste | Nein    | Liste der Solution-Plugins | (leer) |
| **server**                                       |               |         | Server-Einstellungen | |
| &#8614; **directory**                            |               |         | Dateien und Verzeichnisse | |
| &#8614; &#8614; imexporter                       | Verzeichnis   | Ja      | Imexporter-Verzeichnis | |
| &#8614; &#8614; pflib                            | Verzeichnis   | Ja      | Verzeichnis, wo die pflib liegt | |
| &#8614; &#8614; output                           | Verzeichnis   | Ja      | Output-Verzeichnis | |
| &#8614; &#8614; logfile                          | Datei         | Ja      | Log-Datei | /tmp/easydb-server.log |
| &#8614; &#8614; umask                            | Integer       | Ja      | umask | 022 |
| &#8614; &#8614; server_errors                    | Verzeichnis   | Nein    | Verzeichnis für Server-Fehler-Information | <directory/logfile>.errors |
| &#8614; &#8614; l10n_dir                         | Verzeichnis   | Ja      | Verzeichnis für die L10n-Konfiguration | |
| &#8614;  **exporter**                            |               |         | Exporter-Prozesse | |
| &#8614; &#8614;num_workers                       | Integer       | Ja      | Anzahl der Workers | 0 |
| &#8614; &#8614; batch_size                       | Integer       | Ja      | Batch-Größe | 100 |
| &#8614; **janitor**                              |               |         | Janitor-Prozess | |
| &#8614; &#8614; enabled                          | Boolean       | Ja      | Ob der Janitor läuft | true |
| &#8614; &#8614; interval                         | Integer       | Ja      | Wie häufig der Janitor läuft (alle X Sekunden) | 600 (10 Minuten) |
| &#8614; &#8614; max_age                          | Integer       | Ja      | Wann eine Datei abläuft (nach X Sekunden) | 259200 (3 Tage) |
| &#8614; **imexporter**                           |               |         | Imexporter-Prozesse | |
| &#8614; &#8614; socket                           | Datei         | Ja      | Socket | /tmp/easydb-server-imexporter.sock |
| &#8614; &#8614; num_services                     | Integer       | Ja      | Anzahl der Services | 2 |
| &#8614; **frontend**                             |               |         | Frontend-Prozesse | |
| &#8614; &#8614; socket                           | Datei         | Ja      | Socket | /tmp/easydb-server-frontend.sock |
| &#8614; &#8614; num_services                     | Integer       | Ja      | Anzahl der Services | 0 |
| &#8614; **upload-server**                        |               |         | Upload-Prozesse | |
| &#8614; &#8614; socket                           | Datei         | Ja      | Socket | /tmp/easydb-server-upload.sock |
| &#8614; &#8614; num_services                     | Integer       | Ja      | Anzahl der Services | 2 |
| &#8614; **indexer**                              |               |         | Indexer-Prozesse | |
| &#8614; &#8614; enabled                          | Boolean       | Ja      | Ob der Indexer läuft | true |
| &#8614; &#8614; num_processes                    | Integer       | Ja      | Anzahl der Prozesse | 1 |
| &#8614; &#8614; objects_pre_batch                | Integer       | Ja      | Anzahl der Objekte in einem Batch | 1000 |
| &#8614; **mailer**                               |               |         | Mailer-Prozess | |
| &#8614; &#8614; enabled                          | Boolean       | Ja      | Ob der Mailer läuft | true |
| &#8614; &#8614; interval                         | Integer       | Ja      | Wie oft der Mailer läuft (alle X Sekunden) | 60 (1 Minute) |
| &#8614; &#8614; max_attempts                     | Integer       | Ja      | Anzahl der Versuche, bevor eine E-Mail als unzustellbar eingetuft wird | 3 |
| &#8614; &#8614; sender_address                   | String        | Ja      | Sender-Adresse | easydb-server@localhost |
| &#8614; &#8614; envelope_address                 | String        | Ja      | Envelope-Adresse | |
| **schema**                                       |               |         | Schema-Einstellungen | |
| &#8614; base_dir                                 | Verzeichnis   | Ja      | Base-Schema-Verzeichnis | |
| &#8614; user_dir                                 | Verzeichnis   | Ja      | User-Schema-Verzeichnis | |
| &#8614; dsn                                      | String        | Ja      | DSN für die Datenbank-Anbindung | |
| **eas**                                          |               |         | EAS-Konfiguration | |
| &#8614; url                                      | String        | Ja      | URL für die EAS-Anbindung | |
| &#8614; instance                                 | String        | Ja      | Name der EAS-Instanz | |
| &#8614; thumbnail_size                           | Integer       | Ja      | Thumbnail-Größe | 128 |
| &#8614; supervisor_enabled                       | Boolean       | Ja      | Ob der Supervisor läuft | true |
| &#8614; vhost                                    | String        | Nein    | V-Host | |
| &#8614; external_url                             | String        | Nein    | URL für die EAS-Anbindung von außerhalb der Easydb | |
| &#8614; produce_settings                         | Datei         | Ja      | EAS-Produce-Settings (JSON) | |
| &#8614; **rights_management**                    |               | Ja      | EAS-Rechtemanagement-Konfiguration | |
| &#8614; &#8614; *\<class\>*                    |               |         | Konfiguration für EAS-Klasse (image, video, audio, office, directory, unknown) | |
| &#8614; &#8614; &#8614; **versions**             |               | Ja      | EAS-Versionen ("original" ist nicht erlaubt) | |
| &#8614; &#8614; &#8614; &#8614; version          | String        | Ja      | Name der Version | |
| &#8614; &#8614; &#8614; &#8614; size_print       | String        | Nein    | Anzeigetext für die Version | |
| &#8614; &#8614; &#8614; &#8614; size_limit       | Integer       | Nein    | Versionsgröße (bestimmt die maximale Größe, die produziert werden kann, wenn man das Recht hat) | |
| &#8614; &#8614; &#8614; &#8614; export           | Boolean       | Ja      | Ob die Version für den Export verfügbar ist | |
| &#8614; &#8614; &#8614; &#8614; rightsmanagement | Boolean       | Nein      | Ob die Version rechtegemanagt wird | false |
| &#8614; &#8614; &#8614; &#8614; group            | String        | Nein    | Anzeigename für die Versionsgruppierung | |
| &#8614; &#8614; &#8614; &#8614; zoomable         | Boolean       | Nein    | Ob die Version für den Zoomer verfügbar ist | false |
| &#8614; &#8614; &#8614; &#8614; watermark        | Boolean       | Nein    | Ob die Version ein Wasserzeichen hat | false |
| &#8614; &#8614; &#8614; &#8614; standard         | Boolean       | Nein    | Ob die Version in "standard" enthalten ist | false |
| **config**                                       |               |         | Basis-Konfiguration | |
| &#8614; config_settings                          | Datei         | Ja      | Basis-Konfiguration | |
| **default_pics**                                 |               |         | Default-Bilder | |
| &#8614; background                               | Datei         | Nein    | für den Hintergrund | |
| &#8614; user_avatar                              | Datei         | Nein    | für User-Bilder | |
| &#8614; logo                                     | Datei         | Nein    | für das Easydb-Logo | |
| **plugins**                                      |               |         | Plugin-Konfiguration | |
| &#8614; url_prefix_internal                      | String        | Nein    | URL-Präfix für interne Anbindungen | Wert von "url_prefix" |
| &#8614; url_prefix_external                      | String        | Nein    | URL-Präfix für externe Anbindungen | Wert von "url_prefix" |
| &#8614; url_prefix                               | String        | Nein    | URL-Präfix für in- bzw. externe Anbindungen | (kein Präfix) |
| **elasticsearch**                                |               |         | Elasticsearch-Konfiguration | |
| &#8614; url                                      | String        | Ja      | URL | |
| &#8614; connect_timeout_ms                       | Integer       | Ja      | Verbindungs-Timeout (ms) | 30000 (30 Sekunden) |
| &#8614; transfer_timeout_ms                      | Integer       | Ja      | Übertragungs-Timeout (ms) | 300000 (5 Minuten) |
| &#8614; fielddata_memory                         | String-Liste  | Nein    | Index-Felder, die "memory" as Fielddata-Typ benutzen | |
| &#8614; settings                                 | Datei         | Ja      | Index-Settings (JSON) | |
| &#8614; begin_with_wildcards_allowed             | Boolean       | Nein    | Ob Suggest Wildcards am Anfang erlaubt | false |
| **email**                                        |               |         | E-Mail-Templates | |
| &#8614; welcome_new_user                         | Datei         | Ja      | | |
| &#8614; forgot_password                          | Datei         | Ja      | | |
| &#8614; require_password_change                  | Datei         | Ja      | | |
| &#8614; confirm_email                            | Datei         | Ja      | | |
| &#8614; updated_self_service                     | Datei         | Ja      | | |
| &#8614; updated_record                           | Datei         | Ja      | | |
| &#8614; login_disabled                           | Datei         | Ja      | | |
| &#8614; share_collection                         | Datei         | Ja      | | |
| &#8614; transition_resolve                       | Datei         | Ja      | | |
| &#8614; transition_reject                        | Datei         | Ja      | | |
| &#8614; transport                                | Datei         | Ja      | | |
| &#8614; export                                   | Datei         | Ja      | | |
| **ldap**                                         | Liste         |         | Liste von LDAP-Konfigurationen | |
| &#8614; **user**                                 |               |         | Nutzer-Authentifizierung | |
| &#8614; &#8614; protocol                         | String ("ldap" oder "ldaps") | Nein    | LDAP-Protokoll | ldap |
| &#8614; &#8614; server                           | String        | Ja      | LDAP-Server | |
| &#8614; &#8614; port                             | Integer       | Nein    | LDAP-Port | |
| &#8614; &#8614; basedn                           | String        | Ja      | Base-DN | |
| &#8614; &#8614; scope                            | String ("sub", "one" oder "base") | Nein | Such-Scope | sub |
| &#8614; &#8614; filter                           | String        | Ja      | LDAP-Such-Filter für Nutzer. Ersetzt werden: `%(login)s`, `%(Login)s` und `%(LOGIN)s` jeweils durch den Login-Namen. Dieser wird in entsprechend in Kleinbuchstaben umgewandelt, so beibehalten bzw. in Großbuchstaben umgewandelt. | |
| &#8614; &#8614; user                             | String        | Nein    | LDAP-Benutzer (DN), der verwendet wird, wenn eine anonyme Suche (ohne Anmeldung) im LDAP nicht möglich ist. | |
| &#8614; &#8614; password                         | String        | Nein    | Passwort für den zuvor mit `user` angegeben Benutzer. | |
| &#8614; **group**                                | Liste         |         | Liste mit Gruppen-Konfigurationen | |
| &#8614; &#8614; protocol                         | String ("ldap" oder "ldaps") | Nein    | LDAP-Protokoll | ldap |
| &#8614; &#8614; server                           | String        | Ja      | LDAP-Server | |
| &#8614; &#8614; port                             | Integer       | Nein    | LDAP-Port | |
| &#8614; &#8614; basedn                           | String        | Ja      | Base-DN | |
| &#8614; &#8614; scope                            | String ("sub", "one" oder "base") | Nein | Such-Scope | sub |
| &#8614; &#8614; filter                           | String        | Ja      | LDAP-Such-Filter für Gruppen. Ersetzt werden alle Attribute aus dem Benutzer-Eintrag, jeweils mit dem Präfix "user.", also z.B. `%(user.uid)s`. | |
| &#8614; &#8614; user                             | String        | Nein    | LDAP-Benutzer (DN), der verwendet wird, wenn eine anonyme Suche (ohne Anmeldung) im LDAP nicht möglich ist. | |
| &#8614; &#8614; password                         | String        | Nein    | Passwort für den zuvor mit `user` angegeben Benutzer. | |
| &#8614; **environment**                          |               |         | Abbildung der extrahierten LDAP-Informationen. Bezeichnung und Struktur kompatibel zu `sso.environment`. | |
| &#8614; &#8614; mapping                          |               |         | mit `mapping` können Variablen aus dem Umgebung extrahiert und umgeschrieben werden | |
| &#8614; &#8614; &#8614; *\<var\>*                |               |         | definierbarer Variablenname, dieser darf nur aus Buchstaben und Unterstrichen bestehen | |
| &#8614; &#8614; &#8614; &#8614; attr             | String        | Ja      | LDAP-Variable mit Wert der zu setzenden Variablen. Es kann auf Variablen aus dem Nutzer-Eintrag (mit Präfix "user.", z.B. `%(user.givenName)s`) und aus dem Gruppen-Eintrag (mit Präfix "group.", z.B. `%(group.cn)s`) zugegriffen werden. | |
| &#8614; &#8614; &#8614; &#8614; regex\_match     | String        | Nein    | Regulärer Ausdruck zum Finden von Teilen des Attributwerts. Ein Beispiel wäre `"@.*$"`zum Finden aller Zeichen ab dem "@" bis zum Ende (sog. "Scope"). | |
| &#8614; &#8614; &#8614; &#8614; regex\_replace   | String        | Nein    | Wert zum Ersetzen des durch `regex_match` gefundenen Teils. Den "Scope" aus dem Beispiel oben könnte man z.B. durch einen leeren String ersetzen (`""`) oder auch durch einen festen Wert (`":ldap"`) | |
| &#8614; &#8614; user                             |               |         | hier werden die Eigenschaften des Nutzers definiert. Über Format-Strings können aus LDAP-Variablen und über `mapping` definierten Variablen die finalen Werte für die Eigenschaften festgelegt werden. Neben variablen Werten können auch feste Texte verwendet werden. Ein Beispiel für den Wert von `displayname` wäre `"LDAP-Nutzer %(user.givenName)s %(user.sn)"`: dem Vornamen (`user.givenName`) und Nachnamen (`user.sn`) wird der feste Text "LDAP-Nutzer" vorangestellt. | |
| &#8614; &#8614; &#8614; login                    | Format-String | Nein    | Format für `login` des LDAP-Nutzers | "%(user.dn)s" |
| &#8614; &#8614; &#8614; displayname              | Format-String | Nein    | Format für `displayname` des LDAP-Nutzers | "%(user.dn)s" |
| &#8614; &#8614; &#8614; email                    | Format-String | Nein    | Format für primäre E-Mail des LDAP-Nutzers | |
| &#8614; &#8614; groups                           | Liste         |         | | |
| &#8614; &#8614; &#8614; attr                     | String        | Ja      | LDAP-Attribut oder im `mapping` gesetzte Variable mit Gruppenliste | |
| &#8614; &#8614; &#8614; divider                  | String        | Nein    | Trennzeichen für Gruppen-Liste | |
| **sso**                                          |               |         | Single-Sign-On-Konfiguration | |
| &#8614; auth_method                              |               |         | | |
| &#8614; &#8614; client                           |               |         | | |
| &#8614; &#8614; &#8614; login                    | Boolean       | Nein    | Wenn auf `true` gesetzt, wird die Single-Sign-On-Authentifizierung im Frontend aktiviert | |
| &#8614; environment                              |               |         | die meisten SSO-Systeme (z.B. Shibboleth) ermöglichen den Zugriff auf Eigenschaften des authentifizierten Nutzers über Umgebungsvariablen. Mit den folgenden Optionen können diese Variablen durch das `sso`-Plugin verwendet werden.| |
| &#8614; &#8614; mapping                          |               |         | mit `mapping` können Variablen aus dem Umgebung extrahiert und umgeschrieben werden | |
| &#8614; &#8614; &#8614; *\<var\>*                |               |         | definierbarer Variablenname, dieser darf nur aus Buchstaben und Unterstrichen bestehen | |
| &#8614; &#8614; &#8614; &#8614; attr             | String        | Ja      | Umgebungsvariable mit Wert der zu setzenden Variablen | |
| &#8614; &#8614; &#8614; &#8614; regex\_match     | String        | Nein    | Regulärer Ausdruck zum Finden von Teilen des Attributwerts. Ein Beispiel wäre `"@.*$"`zum Finden aller Zeichen ab dem "@" bis zum Ende (sog. "Scope"). | |
| &#8614; &#8614; &#8614; &#8614; regex\_replace   | String        | Nein    | Wert zum Ersetzen des durch `regex_match` gefundenen Teils. Den "Scope" aus dem Beispiel oben könnte man z.B. durch einen leeren String ersetzen (`""`) oder auch durch einen festen Wert (`":shibboleth"`) | |
| &#8614; &#8614; user                             |               |         | hier werden die Eigenschaften des Nutzers definiert. Über Format-Strings können aus Umgebungsvariablen und über `mapping` definierten Variablen die finalen Werte für die Eigenschaften festgelegt werden. Neben variablen Werten können auch feste Texte verwendet werden. Ein Beispiel für den Wert von `displayname` wäre `"SSO-Nutzer %(givenName)s %(sn)"`: dem Vornamen (`givenName`) und Nachnamen (`sn`) wird der feste Text "SSO-Nutzer" vorangestellt. | |
| &#8614; &#8614; &#8614; login                    | Format-String | Nein    | Format für `login` des SSO-Nutzers | "%(eppn)s" |
| &#8614; &#8614; &#8614; displayname              | Format-String | Nein    | Format für `displayname` des SSO-Nutzers | "%(displayName)s" |
| &#8614; &#8614; &#8614; email                    | Format-String | Nein    | Format für primäre E-Mail des SSO-Nutzers | |
| &#8614; &#8614; groups                           | Liste         |         | | |
| &#8614; &#8614; &#8614; attr                     | String        | Ja      | Umgebungsvariable oder im `mapping` gesetzte Variable mit Gruppenliste | |
| &#8614; &#8614; &#8614; divider                  | String        | Nein    | Trennzeichen für Gruppen-Liste | ";" |
| &#8614; ldap                                     |               |         | LDAP | |
| &#8614; &#8614; machine_bind                     |               |         | Konfiguration für den Server-Zugang zum LDAP-Server (SSO-Plugins können diese Variablen brauchen) | |
| &#8614; &#8614; &#8614; url                      | String        | Nein    | LDAP-Server-URL | |
| &#8614; &#8614; &#8614; who                      | String        | Nein    | login (zzt. nur AUTH_SIMPLE unterstützt: User) | |
| &#8614; &#8614; &#8614; cred                     | String        | Nein    | credential (zzt. nur AUTH_SIMPLE unterstützt: Passwort) | |
| **default_client**                               |               |         | Client-Konfiguration | |
| &#8614; debug                                    | Boolean       |         | Wenn gesetzt, ist der Client im Debug Modus, d.h. es gibt z.B. im Kontext-Menü Dump Optionen | false |
| &#8614; tag_icons                                | String        |         | Kommaseparierte Liste. Icon-Namen für Tag-Icons die für Tags hinterlegt werden können. Font-Awesome und CUI Bezeichnungen sind erlaubt | bolt, check, cloud, warning, legal |
| &#8614; tag_colors                               | String        |         | Kommaseparierte Liste. Color-Clases für die Tags. | green, red, blue, yellow |
| &#8614; asset_browser_max_preview_filesize       | Integer       |         | Bis zu dieser Größe werden Vorschaubilder für die Anzeige im Asset-Browser berücksichtigt. Wenn nicht oder auf *-1* gesetzt , wird das *Original* nie berücksichtigt. Wenn auf *0* gesetzt, werden alle Größen und auch das Original berücksichtigt | |
| &#8614; video_player_use_original                | Boolean       |         | Wenn gesetzt, benutzt der Video-Player auch das Original als Source für den HTML5-Video-Tag. | |
| &#8614; audio_player_use_original                | Boolean       |         | Wenn gesetzt, benutzt der Audio-Player auch das Original als Source für den HTML5-Audio-Tag. | |
| &#8614; webdvd_player_open_window_parameter      | String        |         | HTML konformer String für window.open. Einstellungen zum Öffnen des neuen Browser-Fensters um eine Web-DVD abzuspielen | |
| &#8614; print_limit      					  	   | Number        | Nein         | Limitierung der maximalen Objekte, die gedruckt werden können. | 250 |
| &#8614; collection_refresh_rate_seconds		   | Number        | Nein         | Anzahl Sekunden die gewartet wird bis die festen Suchen im Finder aktualisiert werden. | 30 |
| &#8614; suggest_disable                          | Boolean       |         | Wenn gesetzt, Vorschläge in Eingabefeldern sind deaktiviert | |
| &#8614; database                                 | Map           |         | | |
| &#8614; &#8614; level                            | String        | Nein    | Überschreibt das höchste erlaubte Database-Rechte-Level. Erlaubte Werte sind: "development","commit","current". | |
| **hotfolder**                               |               |         | 
| &#8614; enabled                              | boolean |  Nein |  True wenn Hotfolder verwendet werden soll |  
| &#8614; directory                              | file |  Nein |  Das Arbeitsverzeichnis des Hotfolders |  
| &#8614; number_of_workers        | integer |  Nein |  Anzahl der Worker Threads, die für den Upload der Objekte verwendet werden |  
| &#8614; upload_batch_size        | integer |  Nein |  Anzahl Objekte die maximal am Stück aus einen Hotfolder hochgeladen werden |  
| &#8614; delay        | integer |  Nein |  Zeit in Sekunden, die der Prozess nach einem Durchlauf wartet |  

Dateien-Liste ist eine Liste von Maps mit "name" (String) und "file" (Datei).

**Imexporter**

Diese Variablen werden nur für den Imexporter gebraucht:

| Variable                             | Typ           | Pflicht | Erklärung | Default-Wert |
|--------------------------------------|---------------|---------|-----------|--------------|
| **imexporter-database**              |               |         | Schema-Einstellungen | |
| &#8614; dsn                          | String        | Ja      | DSN für die Datenbank-Anbindung | |
| &#8614; schema                       | String        | Ja      | Datenbank-Schema | |
| **server**                           |               |         | | |
| &#8614; **directory**                |               |         | | |
| &#8614; &#8614; plans                | Verzeichnis   | Ja      | Plans | |

**Debug-Sachen**

| Variable                     | |
|------------------------------|---|
| **debug**                    | |
| &#8614; exporter_sleep       | |
| &#8614; exporter_fail        | |
| &#8614; exporter_warnings    | |
| &#8614; search_sleep         | |
