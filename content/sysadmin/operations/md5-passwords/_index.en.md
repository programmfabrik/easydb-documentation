---
title: "12 - Replace MD5 passwords from easydb 4"
menu:
  main:
    name: "Replace MD5 passwords"
    identifier: "sysadmin/operations/md5-passwords"
    parent: "sysadmin/operations"
---
# Replace MD5 passwords from easydb 4

Passwords that were migrated from an easydb 4 are stored by easydb 5 as **unsalted MD5 hashes**. All other passwords are salted SHA-512 hashes. If MD5 hashes get into the wrong hands, weak and medium-strength passwords can be recovered from them quickly.

This guide invalidates all MD5 passwords at once, logs the affected users out and lets them set a new password with "forgot password". The new password is stored as a SHA-512 hash.

[Deutsche Version](/de/sysadmin/operations/md5-passwords/)

## What applies afterwards

* **A recovered old password no longer logs anyone in.** easydb checks a login only against the user's active passwords. An archived password is not active; the login fails like a wrong password.
* **Existing sessions of the affected users are ended.** Anyone already logged in, an attacker included, is logged out.
* **Users with an email address** set a new password themselves: choose "forgot password" on the login page, enter login or email address, follow the link in the email. The link goes to the user's primary email address, so an attacker would need access to that mailbox.
* **Users without an email address** need an administrator: set a new password in the user management, or add an email address, after which the user can use "forgot password".
* **Blocked users** ("Login blocked") do not receive a "forgot password" email.
* **Users who log in via LDAP or SSO** are not affected; their login does not use easydb passwords.

Setting "password change required" on the users is **not** enough: logging in with the old password still succeeds, and only then a new password is requested – which an attacker could set as well.

## 1. Prepare the base configuration

In easydb as an administrator, under *Administration → Base configuration → [Login](/en/webfrontend/administration/base-config/login/)*:

* Switch on **"User can initiate a forgotten password process"**. It is **off** by default; without it the server rejects "forgot password".
* Set **"Repeat passwords"** to **Never**. The old MD5 passwords stay archived, and with this setting a user cannot set their old (possibly known) password again. With _Always_ (the default) the server does not check for repeated passwords.

## 2. Review the affected users

All following commands run on the easydb server as root, for the standard installation with the containers `easydb-pgsql` and `easydb-server` and the database `easydb5`.

Users with an active MD5 password, users without an email address first:

```bash
docker exec -i easydb-pgsql psql -U postgres easydb5 <<'EOF'
SELECT u.login, u.type, u.login_disabled,
       EXISTS (SELECT 1 FROM "ez_user:email" e
               WHERE e."ez_user:id" = u."ez_user:id"
                 AND (e.is_primary OR e.intended_primary)) AS has_email
FROM ez_user u
JOIN "ez_user:password" p USING ("ez_user:id")
WHERE p.type = 'authenticate'
  AND p.date_archive IS NULL
  AND p.password LIKE '$1pf$$%'
ORDER BY has_email, u.login;
EOF
```

Counts only:

```bash
docker exec -i easydb-pgsql psql -U postgres easydb5 <<'EOF'
SELECT EXISTS (SELECT 1 FROM "ez_user:email" e
               WHERE e."ez_user:id" = p."ez_user:id"
                 AND (e.is_primary OR e.intended_primary)) AS has_email,
       count(*)
FROM "ez_user:password" p
WHERE p.type = 'authenticate'
  AND p.date_archive IS NULL
  AND p.password LIKE '$1pf$$%'
GROUP BY 1;
EOF
```

**If your own administrator login is in the list**, give it a new password in easydb first (or keep another administrator login at hand). Otherwise you cannot log in either after step 3.

## 3. Archive the MD5 passwords and end the sessions

Both happen in one transaction. The statements are the ones easydb itself uses to archive passwords and to remove users from sessions.

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

psql reports the number of changed rows (`UPDATE …`) for passwords and sessions.

## 4. Restart the easydb server

```bash
docker restart easydb-server
```

## 5. Verify

Both queries must return `0`:

```bash
docker exec -i easydb-pgsql psql -U postgres easydb5 <<'EOF'
SELECT count(*) AS active_md5_passwords
FROM "ez_user:password"
WHERE type = 'authenticate' AND date_archive IS NULL AND password LIKE '$1pf$$%';

SELECT count(*) AS open_sessions_of_affected_users
FROM ez_session s
WHERE (s.time_expire IS NULL OR s.time_expire > NOW())
  AND s."ez_user:id" IN (SELECT "ez_user:id" FROM "ez_user:password"
                         WHERE password LIKE '$1pf$$%');
EOF
```

Then log in with an affected test login and its old password: the login must fail. "Forgot password" must send an email with a link.

## 6. Inform the users

Tell the affected users that their old password is no longer valid and that they set a new one with "forgot password" on the login page. Users without an email address contact their easydb administrator.
