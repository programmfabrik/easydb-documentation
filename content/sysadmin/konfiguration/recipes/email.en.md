---
title: "E-Mail Configuration"
layout: config
menu:
  main:
    name: "E-Mail"
    identifier: "sysadmin/konfiguration/recipes/email"
    parent: "sysadmin/konfiguration/recipes"
    weight: 2
easydb-server.yml:
  - server.mailer.enabled
  - email.welcome_new_user
  - email.login_disabled
  - smtp.server
  - smtp.hostname
  - smtp.from-address
---
# Sending E-mails
The easydb sends e-mails to its users to ask for confirmation and to inform about certain changes.

Due to the abuse of the Internet's e-mail infrastructure, most of our custumers' networks require that all outgoing e-mail is handed over to a central e-mail relay in that network.

The easydb assumes that there is always such a relay und thus this has to be configured in the easydb for e-mails to work.

## Configuration example

The examples below assume that the relay has the address 172.18.0.1, and that this mail server will relay mails coming from the easydb host if the easydb host is easy.example.com and if the e-mails have the sender address noreply@example.com. 

Furthermore, the example assume that the base path choosen during the [installation](/en/sysadmin/installation) is /srv/easydb and that you e-mail address is you@example.com. Please adjust these to your situation.

- Add into /srv/easydb/config/easydb5-master.yml *(but without creating e.g. a second easydb-server line)*:

```yaml
easydb-server:
  server:
    mailer:
      enabled: true
  smtp:
    server: 172.18.0.1
    hostname: easy.example.com
    from-address: noreply@example.com

eas:
  smtp:
    server: 172.18.0.1
    hostname: easy.example.com
    from-address: noreply@example.com
```

Before the 2018-12-12 release there was a section `common` in `easydb5-master.yml`. This has been replaced by the server- and EAS-specific configuration seen above.

- In the easydb web-frontend:
Choose '''base config''' in the menu, scroll down and fill both sender-address fields with (in this example) noreply@example.com.

- Restart the docker container "easydb-server" (or the whole easydb):

```bash 
docker restart easydb-server
```

## Test e-mail sending

### test using SMTP directly

```bash
docker exec -ti easydb-server bash

apt-get install telnet
telnet 172.18.0.1 25

mail from:<noreply@example.com>
rcpt to:<you@example.com>
data
Subject: test via SMTP
.

quit
```

### test using the mail program in the container

```bash
docker exec -ti easydb-server bash

echo "Subject: testing sSMTP"|ssmtp -v -fnoreply@example.com -Fnoreply you@example.com
```

Optional: Check the configration that was built for sSMTP, using your settings from easydb5-master.yml:

```bash
docker exec easydb-server cat /etc/ssmtp/ssmtp.conf
```

### test using the easydb web-frontend
1. In upper right hand corner of the frontend: click on your '''user'''(e.g. root) and open '''settings'''.
2. Change '''e-mail address''' to an address that you receive - a confirmation request e-mail is sent.


## E-mails which are sent immediately

For certain operations, e-mails are sent from the server. The following e-mails are sent immediately (1):

| Name | When is the e-mail sent? | To which addresses is the e-mail sent? |
| ------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| welcome_new_user |  A user is created | To the "best" (2) e-mail address of the newly created user |
| updated_self_service | A user changes his own data | To the "best" (2) e-mail address of the user |
| updated_record | The data of a user is edited (by someone else) | To the "best" (2) e-mail address of the user|
| forgot_password | A user initiates the Forgot Password process | To the specified e-mail address, or if the login was used, to the "best" (2)|
| confirm_email | - An e-mail needs confirmation | To the e-mail address to be confirmed |
|  | - because it has been modified or newly created by the user | |
|  | - because the administrator has set it |  |
| require_password_change | A user is requested to change his password | To the "best" (2) e-mail address of the user |
| login_disabled | A user is locked (3)  | To the "best" (2) e-mail address of the user
| share_collection | A user was invited to a collection | To the "best" (2) e-mail address of the user |
| transition_resolve | A transition has been triggered and the e-mail is immediate | Mailer decides |
| transition_reject | A transition has been rejected and the e-mail is scheduled | Mailer decides |
| transport | An export is finished and the user receives the data by e-mail (transport "email") | To the "best" (2) e-mail address of the user |
| export | An export is finished (message for the export producer) | To the first e-mail address of the user who has `send_email` |

Remarks:

(1) "immediate" means that they will be processed and sent at the next run of the process "mailer". The frequency
Can be set in the configuration (mailer.interval) and is default one minute.

(2) The "best" e-mail address is the preferred e-mail address when it is set. Otherwise, it is the user's first e-mail address.
If the user has not set an e-mail address, the e-mail is not sent.

(3) When a user is locked (`login_disabled`), an e-mail is sent. While it is locked, no further e-mails will be sent.

In addition, there is an e-mail, which is sent "scheduled". This means that it will be sent at the time the user is in his or her home
"Schedule":

| Name | When is the e-mail generated? | To which addresses is the e-mail sent? |
| ------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| transition_resolve | A transition has been triggered and the e-mail is scheduled | Mailer decides |
| transition_reject | A transition has been rejected and the e-mail is scheduled | Mailer decides |

The transitions can be configured so that the e-mails can be sent individually or together (`batchable`). In the latter case, operations for
The same transition (i.e., the same transition ID) in the transition table (see below).

## E-mail templates

The server creates the e-mails from templates. Templates are e-mails in mbox format, which can contain placeholders. To send an e-mail in
Mbox format, you can use a mail program, get the e-mail itself and send out the source code of the received e-mail
Show. There are examples in `base/email/`.

The e-mail templates can contain placeholders for variables. A placeholder looks like this:

**%(**\<name\>**)**\<type\>

\<name\>  is the name of the variable to be replaced. \<type\> determines the format for the value:

| Type | Meaning  |
| ------ | ------------------- |
| s | Text |
| i | Integer |
| ui | Positive integer |
| d | Date + Time |
| D | Date |

When the e-mail is built, the placeholder is replaced by the value of the variable in the desired format. The values ​​and the date and time formats are localized. This means,
The user will receive an e-mail in his / her language.

Variables of type "s" can also contain placeholders. The server allows nested placeholders as long as they do not repeat.

An example:

```bash
@@include:template@@
```

```bash
"server.email.subject","E-Mail für %(_generated_displayname)s","E-mail for %(_generated_displayname)s"
"server.email.welcome_new_user.greeting","Willkommen an Bord, %(_generated_displayname)s","Welcome aboard, %(_generated_displayname)s"
```

And `_generated_displayname` is provided by the server itself.

If the user has a display name "Hans" and German as the language, he would receive an e-mail with the subject "E-Mail für Hans".

### Change a template
- Get the default template, to edit it: (example: The template used for e-mails in case of disabled login)

```bash
docker exec easydb-server cat /easydb-5/base/email/login_disabled.mbox > /srv/easydb/config/login_disabled.mbox
```

In the example above we use /srv/easydb as the base path. Please adjust to the one which was used during the installation of your easydb.

The first path in the command line above is inside the docker container and does not need to be adjusted in most cases. The filename however has to be chosen to among the existing templates. To list templates, use the following command:

```bash
docker exec easydb-server ls /easydb-5/base/email
```

- Configure that your edited version shall be used from now on, in easydb5-master.yml:

```bash
easydb-server:
  email:
    login_disabled:           /config/mail/login_disabled.mbox
```

The Path /config/[...] is inside the docker container and should thus not be prefixed with "/srv/easydb". Instead, docker provides that /srv/easydb/config is usable inside the container as /config. (It is a "mapped volume".)

- Restart the docker container "easydb-server" (or the whole easydb).

```bash 
docker restart easydb-server
```

### Variables

The variables that can be used as source in the e-mail templates are:

| Variable | Value  |
| --------------------------------- | -------------------------------------------------- |
| `_generated_displayname` | A representation name of the user that is created from the user's name, login, or e-mail address, depending on availability |
| `_login_or_email` | The login name of the user or, if not available, the e-mail address of the user |
| `first_name` | The user 's first name |
| `last_name` | The surname of the user |
| `login` | The login name of the user |
| `easydb_url` | The URL of easydb |
| `easydb_name` | The name of the easydb |
| `lang` | The selected language of the user |

Depending on the type of e-mail, other variables are also available:

| Email Type | Variable | Value |
| ----------------------------- | -------------------------------------- | ------ |
| updated_self_service | self_service_fields_table | HTML table with the data edited by the user (before / after) | 
| updated_record |  updated_fields_table | HTML table with the data edited (before / after) | 
| forgot_password | task_link | URL for resetting the password | 
| require_password_change | task_link | URL for changing the password | 
| confirm_email | task_link | URL for e-mail confirmation | 
| share_collection | collection_name  | Name of Collection | 
| share_collection | collection_description | Description of the collection | 
| share_collection | collection_link | URL to collection | 
| transport | export_id | Export ID |
| transport | export_name | Name of the export | 
| transport  | downloads | HTML table with the files of the export and links to the downloads | 
| transport  | server.email.export.message (\*) | User configured message | 
| transition_ {resolve / reject} | transitions | Transitions HTML table with information about the operations that caused the transition | 
| transition_ {resolve / reject} | server.email.transition.subject (\*) | User-configured subject | 
| transition_ {resolve / reject} | server.email.transition.body (\*) | User configured body | 

The variables that are marked with (\*) can be overwritten by the user with their own texts if a transition or export is configured.
