# LDAP

Wenn aktiviert und konfiguriert, wird LDAP als zusätzliche Authentifizierungsmethode verwendet, wenn Nutzername und Passwort eingegeben werden. LDAP wird grundsätzlich nach der easydb-eigenen Authentifizierung versucht und nur verwendet, wenn es keinen easydb-Nutzer mit dem eingegebenen Namen gibt.

## Aktivieren der LDAP-Unterstützung

LDAP ist als Plugin implementiert, das explizit aktiviert werden muss:
```
plugins:
  enabled+:
    - base.ldap
```

## Plugin-Konfiguration

Angegeben wird eine Liste mit Konfigurationen (im unten angegebenen Beispiel: eine Konfiguration, ab dem ersten "-"). Dabei wird die erste Konfiguration verwendet, bei der der Nutzer authentifiziert werden kann. Eine Konfiguration besteht jeweils aus einem Block für das Authentifizieren des Nutzers (`user`), einem Block für das Finden der verknüpften Gruppen (`group`) sowie einem Block für das Abbilden der LDAP-Informationen in der easydb (`environment`).

Beispiel-Konfiguration:
```
ldap:
  - user:
      protocol: ldap
      server: ldap.example.com
      basedn: dc=example,dc=com
      filter: '(&(objectClass=posixAccount)(uid=%(Login)s))'
    group:
      protocol: ldap
      server: ldap.example.com
      basedn: dc=example,dc=com
      filter: '(&(memberUid=%(user.uid)s)(objectClass=groupOfNames))'
    environment:
      mapping:
        u_login:
          attr: user.uid
          regex_match: '$'
          regex_replace: '@LDAP'
        g_ldap_prefixed:
          attr: group.cn
          regex_match: '^'
          regex_replace: 'ldap.'
      user:
        login: '%(u_login)s'
        displayname: '%(user.givenName)s %(user.sn)s'
        email: '%(user.mail)s'
      groups:
        - attr: g_ldap_prefixed
        - attr: group.cn
```

Anmerkungen:

- Das Schlüsselwort "Login" gilt so nur im Abschnitt "user", nicht im Abschnitt group (dort würde statt dessen "user.uid" verwendet werden, im obigen Beispiel).
- Die Prefixe "user.abc" und "group.abc" sind easydb-Syntax (nicht LDAP-Syntax) für: Nutze das Attribut "abc" von jedem LDAP-Objekt, welches mit den Regeln aus dem Abschnitt "user"(nicht environment.user) bzw. "group" gefunden wurde.

# Anwendungs-Szenarien

## Wer bekommt Login-Rechte?

Alle Konten im LDAP bekommen einen Login in die easydb. Wenn Sie statt dessen nur bestimmten Gruppen Login gewähren wollen dann kontaktieren Sie dazu gerne die Programmfabrik und wir besprechen die Umsetzung.
