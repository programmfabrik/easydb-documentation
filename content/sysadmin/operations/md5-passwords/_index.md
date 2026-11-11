---
title: "12 - MD5-Passwörter aus easydb 4 ablösen"
menu:
  mainWEG:
    name: "MD5-Passwörter ablösen"
    identifier: "sysadmin/operations/md5-passwords"
    parent: "sysadmin/operations"
---
# MD5-Passwörter aus easydb 4 ablösen

Passwörter, die bei der Migration aus einer easydb 4 übernommen wurden, speichert die easydb 5 als **ungesalzene MD5-Hashes**. Alle anderen Passwörter sind gesalzene SHA-512-Hashes. Gelangen MD5-Hashes in fremde Hände, lassen sich schwache und mittelstarke Passwörter daraus schnell ermitteln.

Diese Anleitung entwertet alle MD5-Passwörter auf einmal, meldet die betroffenen Benutzer ab und lässt sie über „Passwort vergessen" ein neues Passwort vergeben. Das neue Passwort wird als SHA-512-Hash gespeichert.

[English version](/en/sysadmin/operations/md5-passwords/)

## Was danach gilt

* **Ein ermitteltes altes Passwort führt nicht mehr zur Anmeldung.** Die easydb prüft eine Anmeldung nur gegen aktive Passwörter des Benutzers. Ein archiviertes Passwort ist nicht mehr aktiv; die Anmeldung schlägt fehl wie bei einem falschen Passwort.
* **Bestehende Sitzungen der betroffenen Benutzer werden beendet.** Wer bereits angemeldet ist, auch ein Angreifer, wird abgemeldet.
* **Benutzer mit E-Mail-Adresse** setzen ihr Passwort selbst neu: auf der Anmeldeseite „Passwort vergessen" wählen, Login oder E-Mail-Adresse eingeben, dem Link in der E-Mail folgen. Der Link geht an die primäre E-Mail-Adresse des Benutzers, ein Angreifer bräuchte also Zugriff auf dieses Postfach.
* **Benutzer ohne E-Mail-Adresse** brauchen einen Administrator: Er vergibt in der Benutzerverwaltung ein neues Passwort oder trägt eine E-Mail-Adresse ein, danach kann der Benutzer „Passwort vergessen" selbst nutzen.
* **Gesperrte Benutzer** („Login gesperrt") erhalten keine „Passwort vergessen"-E-Mail.
* **Benutzer mit LDAP- oder SSO-Anmeldung** sind nicht betroffen, ihre Anmeldung verwendet keine easydb-Passwörter.

Das Setzen von „Passwort ändern erforderlich" an den Benutzern genügt **nicht**: Die Anmeldung mit dem alten Passwort gelingt dann weiterhin, erst danach wird ein neues Passwort verlangt – das könnte auch ein Angreifer vergeben.

## 1. Basis-Konfiguration vorbereiten

In der easydb als Administrator unter *Administration → Basis-Konfiguration → [Login](/de/webfrontend/administration/base-config/login/)*:

* **„Anfordern vergessener Passwörter erlauben"** und **„Anfrage-Dialog im Login anzeigen"** einschalten. „Anfordern vergessener Passwörter erlauben" ist ab Werk **aus**; ohne diese Einstellung lehnt der Server „Passwort vergessen" ab.
* **„Wiederholte Passwörter erlauben"** auf **Niemals** setzen. Die alten MD5-Passwörter bleiben archiviert erhalten, und mit dieser Einstellung kann ein Benutzer sein altes (möglicherweise bekanntes) Passwort nicht erneut vergeben. Mit _Immer_ (der Voreinstellung) prüft der Server wiederholte Passwörter nicht.

## 2. Betroffene Benutzer ansehen

Alle folgenden Befehle laufen auf dem easydb-Server als root, für die Standardinstallation mit den Containern `easydb-pgsql` und `easydb-server` und der Datenbank `easydb5`.

Liste der Benutzer mit aktivem MD5-Passwort, Benutzer ohne E-Mail-Adresse zuerst:

```bash
docker exec -i easydb-pgsql psql -U postgres easydb5 <<'EOF'
SELECT u.login, u.type, u.login_disabled,
       EXISTS (SELECT 1 FROM "ez_user:email" e
               WHERE e."ez_user:id" = u."ez_user:id"
                 AND (e.is_primary OR e.intended_primary)) AS hat_email
FROM ez_user u
JOIN "ez_user:password" p USING ("ez_user:id")
WHERE p.type = 'authenticate'
  AND p.date_archive IS NULL
  AND p.password LIKE '$1pf$$%'
ORDER BY hat_email, u.login;
EOF
```

Nur die Anzahlen:

```bash
docker exec -i easydb-pgsql psql -U postgres easydb5 <<'EOF'
SELECT EXISTS (SELECT 1 FROM "ez_user:email" e
               WHERE e."ez_user:id" = p."ez_user:id"
                 AND (e.is_primary OR e.intended_primary)) AS hat_email,
       count(*)
FROM "ez_user:password" p
WHERE p.type = 'authenticate'
  AND p.date_archive IS NULL
  AND p.password LIKE '$1pf$$%'
GROUP BY 1;
EOF
```

**Steht Ihr eigenes Administrator-Login in der Liste**, vergeben Sie ihm zuerst in der easydb ein neues Passwort (oder halten Sie ein anderes Administrator-Login bereit). Sonst können Sie sich nach Schritt 3 ebenfalls nicht mehr anmelden.

## 3. MD5-Passwörter archivieren und Sitzungen beenden

Beides geschieht in einer Transaktion. Die Anweisungen entsprechen denen, mit denen die easydb selbst Passwörter archiviert und Benutzer aus Sitzungen entfernt.

```bash
docker exec -i easydb-pgsql psql -U postgres -v ON_ERROR_STOP=1 easydb5 <<'EOF'
BEGIN;
CREATE TEMP TABLE md5_users AS
  SELECT DISTINCT "ez_user:id" FROM "ez_user:password"
  WHERE type = 'authenticate' AND date_archive IS NULL AND password LIKE '$1pf$$%';
UPDATE "ez_user:password"
  SET date_archive = NOW()
  WHERE type = 'authenticate' AND date_archive IS NULL AND password LIKE '$1pf$$%';
UPDATE ez_session
  SET "ez_user:id" = NULL, time_updated = NOW(), time_expire = NOW(), time_deauth = NOW()
  WHERE "ez_user:id" IN (SELECT "ez_user:id" FROM md5_users);
COMMIT;
EOF
```

psql meldet die Anzahl der geänderten Zeilen (`UPDATE …`) für Passwörter und Sitzungen.

## 4. easydb-Server neu starten

```bash
docker restart easydb-server
```

## 5. Prüfen

Beide Abfragen müssen `0` ergeben:

```bash
docker exec -i easydb-pgsql psql -U postgres easydb5 <<'EOF'
SELECT count(*) AS aktive_md5_passwoerter
FROM "ez_user:password"
WHERE type = 'authenticate' AND date_archive IS NULL AND password LIKE '$1pf$$%';

SELECT count(*) AS offene_sitzungen_betroffener_benutzer
FROM ez_session s
WHERE (s.time_expire IS NULL OR s.time_expire > NOW())
  AND s."ez_user:id" IN (SELECT "ez_user:id" FROM "ez_user:password"
                         WHERE password LIKE '$1pf$$%');
EOF
```

Melden Sie sich danach mit einem betroffenen Test-Login und dem alten Passwort an: Die Anmeldung muss fehlschlagen. „Passwort vergessen" muss eine E-Mail mit Link senden.

## 6. Benutzer informieren

Teilen Sie den betroffenen Benutzern mit, dass ihr altes Passwort nicht mehr gilt und sie über „Passwort vergessen" auf der Anmeldeseite ein neues vergeben. Benutzer ohne E-Mail-Adresse wenden sich an ihren easydb-Administrator.
