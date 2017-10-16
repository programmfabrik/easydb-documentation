# YAML configuration

Structure and load order

The Easydb server is configured by YAML files. The YAML files are loaded in the following order:

`easydb5-master. yml` in the path you defined during[Installation](. /sysadmin/installation/installation. md).
Under the hood, i. e. in the docker container, `easydb-server. yml` is first loaded in the current path, if available. This should only be relevant for you as a customer in exceptional cases.
Generally, other files are loaded that are specified as arguments in the command line (with `--configfile') in the order in which they are specified.

A YAML file can also include other configuration files:

The variable **include_before** is a list of files that are loaded before the file in which it is defined
The variable **include_after** is a list of files that are loaded after the file in which it is defined

The files are defined either with an absolute path or relative to the YAML file in which they were specified.

Outside of the docker-container we recommend to include everything in the one YAML-file `easydb5-master. yml`.

## Types

Variables are structured in maps, but a general map is not a valid type for a variable. The types supported are:

| Easydb-Typ    | YAML-Typ                 | Kommentar |
|---------------|--------------------------|-----------|
| String        | String                   | |
| Integer       | Integer                  | |
| Boolean       | Boolean, String, Integer | true: true, "on", "1", 1 |
|               |                          | false: false, "off", "0", 0, null, nicht gesetzt |
| Datei         | String                   | entweder absolut oder relativ zu dem YAML-Datei, in dem die Variable definiert ist |
| Catalogue  | String                   | wie Datei |
| Dateien-Liste | Sequence of Strings      | nicht gesetzt = null = leere Liste |
|               |                          | jede Datei ist absolut oder relativ zu dem YAML-Datei, in dem sie definiert sind, d.h. eine Liste kann Dateien mit verschiedenen relativen Pfaden enthalten |

## replacements

If a variable has already been defined, its value is replaced if it is redefined at a later time. Further further
opportunities are:

variable+: adds a new value (only valid for lists). Example: Activate two more plugins with the list "enabled":
```YAML
  plugins:
    enabled+:
      base. custom-data-type-link
      base. custom-data-type-gnd
````
- variable-:
    if the variable is a list, the specified values are deleted from the list
    if the variable is a scalar, it becomes undefined
    if the variable is a map, all variables below it are undefined
variable-key: only for lists of maps, remove all entries from the list whose value for "key" is included in the specified list

## List of variables

**Easydb-Server**

| Variable                                         | Typ           | Pflicht | Erklärung | Default-Wert |
|--------------------------------------------------|---------------|---------|-----------|--------------|
| **base**                                         |               |         | | |
| &#8614; plugins                                  | Dateien-Liste | No    | Liste der Base-Plugins | (leer) |
| **solution**                                     |               |         | Konfiguration der Solution | |
| &#8614; name                                     | String        | Yes      | Name der verwendeten Solution | |
| &#8614; plugins                                  | Dateien-Liste | No    | Liste der Solution-Plugins | (leer) |
| **server**                                       |               |         | Server-Einstellungen | |
| &#8614; **directory**                            |               |         | Dateien und Verzeichnisse | |
| &#8614; &#8614; imexporter                       | Catalogue  | Yes      | Imexporter-Verzeichnis | |
| &#8614; &#8614; pflib                            | Catalogue  | Yes      | Verzeichnis, wo die pflib liegt | |
| &#8614; &#8614; output                           | Catalogue  | Yes      | Output-Verzeichnis | |
| &#8614; &#8614; logfile                          | Datei         | Yes      | Log-Datei | /tmp/easydb-server.log |
| &#8614; &#8614; umask                            | Integer       | Yes      | umask | 022 |
| &#8614; &#8614; server_errors                    | Catalogue  | No    | Cataloguefür Server-Fehler-Information | <directory/logfile>.errors |
| &#8614; &#8614; l10n_dir                         | Catalogue  | Yes      | Cataloguefür die L10n-Konfiguration | |
| &#8614;  **exporter**                            |               |         | Exporter-Prozesse | |
| &#8614; &#8614;num_workers                       | Integer       | Yes      | Anzahl der Workers | 0 |
| &#8614; &#8614; batch_size                       | Integer       | Yes      | Batch-Größe | 100 |
| &#8614; **janitor**                              |               |         | Janitor-Prozess | |
| &#8614; &#8614; enabled                          | Boolean       | Yes      | Ob der Janitor läuft | true |
| &#8614; &#8614; interval                         | Integer       | Yes      | Wie häufig der Janitor läuft (alle X Sekunden) | 600 (10 Minuten) |
| &#8614; &#8614; max_age                          | Integer       | Yes      | Wann eine Datei abläuft (nach X Sekunden) | 259200 (3 Tage) |
| &#8614; **imexporter**                           |               |         | Imexporter-Prozesse | |
| &#8614; &#8614; socket                           | Datei         | Yes      | Socket | /tmp/easydb-server-imexporter.sock |
| &#8614; &#8614; num_services                     | Integer       | Yes      | Anzahl der Services | 2 |
| &#8614; **frontend**                             |               |         | Frontend-Prozesse | |
| &#8614; &#8614; socket                           | Datei         | Yes      | Socket | /tmp/easydb-server-frontend.sock |
| &#8614; &#8614; num_services                     | Integer       | Yes      | Anzahl der Services | 0 |
| &#8614; **upload-server**                        |               |         | Upload-Prozesse | |
| &#8614; &#8614; socket                           | Datei         | Yes      | Socket | /tmp/easydb-server-upload.sock |
| &#8614; &#8614; num_services                     | Integer       | Yes      | Anzahl der Services | 2 |
| &#8614; **indexer**                              |               |         | Indexer-Prozesse | |
| &#8614; &#8614; enabled                          | Boolean       | Yes      | Ob der Indexer läuft | true |
| &#8614; &#8614; num_processes                    | Integer       | Yes      | Anzahl der Prozesse | 1 |
| &#8614; &#8614; objects_pre_batch                | Integer       | Yes      | Anzahl der Objekte in einem Batch | 1000 |
| &#8614; **mailer**                               |               |         | Mailer-Prozess | |
| &#8614; &#8614; enabled                          | Boolean       | Yes      | Ob der Mailer läuft | true |
| &#8614; &#8614; interval                         | Integer       | Yes      | Wie oft der Mailer läuft (alle X Sekunden) | 60 (1 Minute) |
| &#8614; &#8614; max_attempts                     | Integer       | Yes      | Anzahl der Versuche, bevor eine E-Mail als unzustellbar eingetuft wird | 3 |
| &#8614; &#8614; sender_address                   | String        | Yes      | Sender-Adresse | easydb-server@localhost |
| &#8614; &#8614; envelope_address                 | String        | Yes      | Envelope-Adresse | |
| **schema**                                       |               |         | Schema-Einstellungen | |
| &#8614; base_dir                                 | Catalogue  | Yes      | Base-Schema-Verzeichnis | |
| &#8614; user_dir                                 | Catalogue  | Yes      | User-Schema-Verzeichnis | |
| &#8614; dsn                                      | String        | Yes      | DSN for the Database connection | |
| **eas**                                          |               |         | EAS-Konfiguration | |
| &#8614; url                                      | String        | Yes      | URL for the EAS-Anbindung | |
| &#8614; instance                                 | String        | Yes      | Name der EAS-Instanz | |
| &#8614; thumbnail_size                           | Integer       | Yes      | Thumbnail-Größe | 128 |
| &#8614; supervisor_enabled                       | Boolean       | Yes      | Ob der Supervisor läuft | true |
| &#8614; vhost                                    | String        | No    | V-Host | |
| &#8614; external_url                             | String        | No    | URL for the EAS-Anbindung von außerhalb der Easydb | |
| &#8614; produce_settings                         | Datei         | Yes      | EAS-Produce-Settings (JSON) | |
| &#8614; **rights_management**                    |               | Yes      | EAS-Rechtemanagement-Konfiguration | |
| &#8614; &#8614; *\<class\>*                    |               |         | Konfiguration für EAS-Klasse (image, video, audio, office, directory, unknown) | |
| &#8614; &#8614; &#8614; **versions**             |               | Yes      | EAS-Versionen ("original" ist nicht erlaubt) | |
| &#8614; &#8614; &#8614; &#8614; version          | String        | Yes      | Name der Version | |
| &#8614; &#8614; &#8614; &#8614; size_print       | String        | No    | Anzeigetext for the Version | |
| &#8614; &#8614; &#8614; &#8614; size_limit       | Integer       | No    | Versionsgröße (bestimmt die maximale Größe, die produziert werden kann, wenn man das Recht hat) | |
| &#8614; &#8614; &#8614; &#8614; export           | Boolean       | Yes      | Ob die Version für den Export verfügbar ist | |
| &#8614; &#8614; &#8614; &#8614; rightsmanagement | Boolean       | No      | Ob die Version rechtegemanagt wird | false |
| &#8614; &#8614; &#8614; &#8614; group            | String        | No    | Anzeigename for the Versionsgruppierung | |
| &#8614; &#8614; &#8614; &#8614; zoomable         | Boolean       | No    | Ob die Version für den Zoomer verfügbar ist | false |
| &#8614; &#8614; &#8614; &#8614; watermark        | Boolean       | No    | Ob die Version ein Wasserzeichen hat | false |
| &#8614; &#8614; &#8614; &#8614; standard         | Boolean       | No    | Ob die Version in "standard" enthalten ist | false |
| **config**                                       |               |         | Basis-Konfiguration | |
| &#8614; config_settings                          | Datei         | Yes      | Basis-Konfiguration | |
| **default_pics**                                 |               |         | Default-Bilder | |
| &#8614; background                               | Datei         | No    | für den Hintergrund | |
| &#8614; user_avatar                              | Datei         | No    | für User-Bilder | |
| &#8614; logo                                     | Datei         | No    | für das Easydb-Logo | |
| **plugins**                                      |               |         | Plugin-Konfiguration | |
| &#8614; url_prefix_internal                      | String        | No    | URL-Präfix für interne Anbindungen | Wert von "url_prefix" |
| &#8614; url_prefix_external                      | String        | No    | URL-Präfix für externe Anbindungen | Wert von "url_prefix" |
| &#8614; url_prefix                               | String        | No    | URL-Präfix für in- bzw. externe Anbindungen | (kein Präfix) |
| **elasticsearch**                                |               |         | Elasticsearch-Konfiguration | |
| &#8614; url                                      | String        | Yes      | URL | |
| &#8614; connect_timeout_ms                       | Integer       | Yes      | Verbindungs-Timeout (ms) | 30000 (30 Sekunden) |
| &#8614; transfer_timeout_ms                      | Integer       | Yes      | Übertragungs-Timeout (ms) | 300000 (5 Minuten) |
| &#8614; fielddata_memory                         | String-Liste  | No    | Index-Felder, die "memory" as Fielddata-Typ benutzen | |
| &#8614; settings                                 | Datei         | Yes      | Index-Settings (JSON) | |
| &#8614; begin_with_wildcards_allowed             | Boolean       | No    | Ob Suggest Wildcards am Anfang erlaubt | false |
| **email**                                        |               |         | E-Mail-Templates | |
| &#8614; welcome_new_user                         | Datei         | Yes      | | |
| &#8614; forgot_password                          | Datei         | Yes      | | |
| &#8614; require_password_change                  | Datei         | Yes      | | |
| &#8614; confirm_email                            | Datei         | Yes      | | |
| &#8614; updated_self_service                     | Datei         | Yes      | | |
| &#8614; updated_record                           | Datei         | Yes      | | |
| &#8614; login_disabled                           | Datei         | Yes      | | |
| &#8614; share_collection                         | Datei         | Yes      | | |
| &#8614; transition_resolve                       | Datei         | Yes      | | |
| &#8614; transition_reject                        | Datei         | Yes      | | |
| &#8614; transport                                | Datei         | Yes      | | |
| &#8614; export                                   | Datei         | Yes      | | |
| **ldap**                                         | Liste         |         | Liste von LDAP-Konfigurationen | |
| &#8614; **user**                                 |               |         | Nutzer-Authentifizierung | |
| &#8614; &#8614; protocol                         | String ("ldap" oder "ldaps") | No    | LDAP-Protokoll | ldap |
| &#8614; &#8614; server                           | String        | Yes      | LDAP-Server | |
| &#8614; &#8614; port                             | Integer       | No    | LDAP-Port | |
| &#8614; &#8614; basedn                           | String        | Yes      | Base-DN | |
| &#8614; &#8614; scope                            | String ("sub", "one" oder "base") | No | Such-Scope | sub |
| &#8614; &#8614; filter                           | String        | Yes      | LDAP-Such-Filter für Nutzer. Ersetzt werden: `%(login)s`, `%(Login)s` und `%(LOGIN)s` jeweils durch den Login-Namen. Dieser wird in entsprechend in Kleinbuchstaben umgewandelt, so beibehalten bzw. in Großbuchstaben umgewandelt. | |
| &#8614; &#8614; user                             | String        | No    | LDAP-Benutzer (DN), der verwendet wird, wenn eine anonyme Suche (ohne Anmeldung) im LDAP nicht möglich ist. | |
| &#8614; &#8614; password                         | String        | No    | Passwort für den zuvor mit `user` angegeben Benutzer. | |
| &#8614; **group**                                | Liste         |         | Liste mit Gruppen-Konfigurationen | |
| &#8614; &#8614; protocol                         | String ("ldap" oder "ldaps") | No    | LDAP-Protokoll | ldap |
| &#8614; &#8614; server                           | String        | Yes      | LDAP-Server | |
| &#8614; &#8614; port                             | Integer       | No    | LDAP-Port | |
| &#8614; &#8614; basedn                           | String        | Yes      | Base-DN | |
| &#8614; &#8614; scope                            | String ("sub", "one" oder "base") | No | Such-Scope | sub |
| &#8614; &#8614; filter                           | String        | Yes      | LDAP-Such-Filter für Gruppen. Ersetzt werden alle Attribute aus dem Benutzer-Eintrag, jeweils mit dem Präfix "user.", also z.B. `%(user.uid)s`. | |
| &#8614; &#8614; user                             | String        | No    | LDAP-Benutzer (DN), der verwendet wird, wenn eine anonyme Suche (ohne Anmeldung) im LDAP nicht möglich ist. | |
| &#8614; &#8614; password                         | String        | No    | Passwort für den zuvor mit `user` angegeben Benutzer. | |
| &#8614; **environment**                          |               |         | Abbildung der extrahierten LDAP-Informationen. Bezeichnung und Struktur kompatibel zu `sso.environment`. | |
| &#8614; &#8614; mapping                          |               |         | mit `mapping` können Variablen aus dem Umgebung extrahiert und umgeschrieben werden | |
| &#8614; &#8614; &#8614; *\<var\>*                |               |         | definierbarer Variablenname, dieser darf nur aus Buchstaben und Unterstrichen bestehen | |
| &#8614; &#8614; &#8614; &#8614; attr             | String        | Yes      | LDAP-Variable mit Wert der zu setzenden Variablen. Es kann auf Variablen aus dem Nutzer-Eintrag (mit Präfix "user.", z.B. `%(user.givenName)s`) und aus dem Gruppen-Eintrag (mit Präfix "group.", z.B. `%(group.cn)s`) zugegriffen werden. | |
| &#8614; &#8614; &#8614; &#8614; regex\_match     | String        | No    | Regulärer Ausdruck zum Finden von Teilen des Attributwerts. Ein Beispiel wäre `"@.*$"`zum Finden aller Zeichen ab dem "@" bis zum Ende (sog. "Scope"). | |
| &#8614; &#8614; &#8614; &#8614; regex\_replace   | String        | No    | Wert zum Ersetzen des durch `regex_match` gefundenen Teils. Den "Scope" aus dem Beispiel oben könnte man z.B. durch einen leeren String ersetzen (`""`) oder auch durch einen festen Wert (`":ldap"`) | |
| &#8614; &#8614; user                             |               |         | hier werden die Eigenschaften des Nutzers definiert. Über Format-Strings können aus LDAP-Variablen und über `mapping` definierten Variablen die finalen Werte for the Eigenschaften festgelegt werden. Neben variablen Werten können auch feste Texte verwendet werden. Ein Beispiel für den Wert von `displayname` wäre `"LDAP-Nutzer %(user.givenName)s %(user.sn)"`: dem Vornamen (`user.givenName`) und Nachnamen (`user.sn`) wird der feste Text "LDAP-Nutzer" vorangestellt. | |
| &#8614; &#8614; &#8614; login                    | Format-String | No    | Format für `login` des LDAP-Nutzers | "%(user.dn)s" |
| &#8614; &#8614; &#8614; displayname              | Format-String | No    | Format für `displayname` des LDAP-Nutzers | "%(user.dn)s" |
| &#8614; &#8614; &#8614; email                    | Format-String | No    | Format für primäre E-Mail des LDAP-Nutzers | |
| &#8614; &#8614; groups                           | Liste         |         | | |
| &#8614; &#8614; &#8614; attr                     | String        | Yes      | LDAP-Attribut oder im `mapping` gesetzte Variable mit Gruppenliste | |
| &#8614; &#8614; &#8614; divider                  | String        | No    | Trennzeichen für Gruppen-Liste | |
| **sso**                                          |               |         | Single-Sign-On-Konfiguration | |
| &#8614; auth_method                              |               |         | | |
| &#8614; &#8614; client                           |               |         | | |
| &#8614; &#8614; &#8614; login                    | Boolean       | No    | Wenn auf `true` gesetzt, wird die Single-Sign-On-Authentifizierung im Frontend aktiviert | |
| &#8614; environment                              |               |         | die meisten SSO-Systeme (z.B. Shibboleth) ermöglichen den Zugriff auf Eigenschaften des authentifizierten Nutzers über Umgebungsvariablen. Mit den folgenden Optionen können diese Variablen durch das `sso`-Plugin verwendet werden.| |
| &#8614; &#8614; mapping                          |               |         | mit `mapping` können Variablen aus dem Umgebung extrahiert und umgeschrieben werden | |
| &#8614; &#8614; &#8614; *\<var\>*                |               |         | definierbarer Variablenname, dieser darf nur aus Buchstaben und Unterstrichen bestehen | |
| &#8614; &#8614; &#8614; &#8614; attr             | String        | Yes      | Umgebungsvariable mit Wert der zu setzenden Variablen | |
| &#8614; &#8614; &#8614; &#8614; regex\_match     | String        | No    | Regulärer Ausdruck zum Finden von Teilen des Attributwerts. Ein Beispiel wäre `"@.*$"`zum Finden aller Zeichen ab dem "@" bis zum Ende (sog. "Scope"). | |
| &#8614; &#8614; &#8614; &#8614; regex\_replace   | String        | No    | Wert zum Ersetzen des durch `regex_match` gefundenen Teils. Den "Scope" aus dem Beispiel oben könnte man z.B. durch einen leeren String ersetzen (`""`) oder auch durch einen festen Wert (`":shibboleth"`) | |
| &#8614; &#8614; user                             |               |         | hier werden die Eigenschaften des Nutzers definiert. Über Format-Strings können aus Umgebungsvariablen und über `mapping` definierten Variablen die finalen Werte for the Eigenschaften festgelegt werden. Neben variablen Werten können auch feste Texte verwendet werden. Ein Beispiel für den Wert von `displayname` wäre `"SSO-Nutzer %(givenName)s %(sn)"`: dem Vornamen (`givenName`) und Nachnamen (`sn`) wird der feste Text "SSO-Nutzer" vorangestellt. | |
| &#8614; &#8614; &#8614; login                    | Format-String | No    | Format für `login` des SSO-Nutzers | "%(eppn)s" |
| &#8614; &#8614; &#8614; displayname              | Format-String | No    | Format für `displayname` des SSO-Nutzers | "%(displayName)s" |
| &#8614; &#8614; &#8614; email                    | Format-String | No    | Format für primäre E-Mail des SSO-Nutzers | |
| &#8614; &#8614; groups                           | Liste         |         | | |
| &#8614; &#8614; &#8614; attr                     | String        | Yes      | Umgebungsvariable oder im `mapping` gesetzte Variable mit Gruppenliste | |
| &#8614; &#8614; &#8614; divider                  | String        | No    | Trennzeichen für Gruppen-Liste | ";" |
| &#8614; ldap                                     |               |         | LDAP | |
| &#8614; &#8614; machine_bind                     |               |         | Konfiguration für den Server-Zugang zum LDAP-Server (SSO-Plugins können diese Variablen brauchen) | |
| &#8614; &#8614; &#8614; url                      | String        | No    | LDAP-Server-URL | |
| &#8614; &#8614; &#8614; who                      | String        | No    | login (zzt. nur AUTH_SIMPLE unterstützt: User) | |
| &#8614; &#8614; &#8614; cred                     | String        | No    | credential (zzt. nur AUTH_SIMPLE unterstützt: Passwort) | |
| **default_client**                               |               |         | Client-Konfiguration | |
| &#8614; debug                                    | Boolean       |         | Wenn gesetzt, ist der Client im Debug Modus, d.h. es gibt z.B. im Kontext-Menü Dump Optionen | false |
| &#8614; tag_icons                                | String        |         | Kommaseparierte Liste. Icon-Namen für Tag-Icons die für Tags hinterlegt werden können. Font-Awesome und CUI Bezeichnungen sind erlaubt | bolt, check, cloud, warning, legal |
| &#8614; tag_colors                               | String        |         | Kommaseparierte Liste. Color-Clases for the Tags. | green, red, blue, yellow |
| &#8614; asset_browser_max_preview_filesize       | Integer       |         | Bis zu dieser Größe werden Vorschaubilder for the Anzeige im Asset-Browser berücksichtigt. Wenn nicht oder auf *-1* gesetzt , wird das *Original* nie berücksichtigt. Wenn auf *0* gesetzt, werden alle Größen und auch das Original berücksichtigt | |
| &#8614; video_player_use_original                | Boolean       |         | Wenn gesetzt, benutzt der Video-Player auch das Original als Source für den HTML5-Video-Tag. | |
| &#8614; audio_player_use_original                | Boolean       |         | Wenn gesetzt, benutzt der Audio-Player auch das Original als Source für den HTML5-Audio-Tag. | |
| &#8614; webdvd_player_open_window_parameter      | String        |         | HTML konformer String für window.open. Einstellungen zum Öffnen des neuen Browser-Fensters um eine Web-DVD abzuspielen | |
| &#8614; print_limit      					  	   | Number        | No         | Limitierung der maximalen Objekte, die gedruckt werden können. | 250 |
| &#8614; collection_refresh_rate_seconds		   | Number        | No         | Anzahl Sekunden die gewartet wird bis die festen Suchen im Finder aktualisiert werden. | 30 |
| &#8614; suggest_disable                          | Boolean       |         | Wenn gesetzt, Vorschläge in Eingabefeldern sind deaktiviert | |
| &#8614; database                                 | Map           |         | | |
| &#8614; &#8614; level                            | String        | No    | Überschreibt das höchste erlaubte Database-Rechte-Level. Erlaubte Werte sind: "development","commit","current". | |
| **hotfolder**                               |               |         | 
| &#8614; enabled                              | boolean |  No |  True wenn Hotfolder verwendet werden soll |  
| &#8614; directory                              | file |  No |  Das Arbeitsverzeichnis des Hotfolders |  
| &#8614; number_of_workers        | integer |  No |  Anzahl der Worker Threads, die für den Upload der Objekte verwendet werden |  
| &#8614; upload_batch_size        | integer |  No |  Anzahl Objekte die maximal am Stück aus einen Hotfolder hochgeladen werden |  
| &#8614; delay        | integer |  No |  Zeit in Sekunden, die der Prozess nach einem Durchlauf wartet |  

Dateien-Liste ist eine Liste von Maps mit "name" (String) und "file" (Datei).

**Imexporter**

Diese Variablen werden nur für den Imexporter gebraucht:

| Variable                             | Typ           | Pflicht | Erklärung | Default-Wert |
|--------------------------------------|---------------|---------|-----------|--------------|
| **imexporter-database**              |               |         | Schema-Einstellungen | |
| &#8614; dsn                          | String        | Yes      | DSN for the Database connection | |
| &#8614; schema                       | String        | Yes      | Database Scheme | |
| **server**                           |               |         | | |
| &#8614; **directory**                |               |         | | |
| &#8614; &#8614; plans                | Catalogue  | Yes      | Plans | |

**Debug-Sachen**

| Variable                     | |
|------------------------------|---|
| **debug**                    | |
| &#8614; exporter_sleep       | |
| &#8614; exporter_fail        | |
| &#8614; exporter_warnings    | |
| &#8614; search_sleep         | |
