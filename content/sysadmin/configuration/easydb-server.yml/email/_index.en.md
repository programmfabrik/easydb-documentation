---
title: "Mail / SMTP"
menu:
  main:
    name: "Mail / SMTP"
    identifier: "sysadmin/configuration/easydb-server.yml/mail"
    weight: -996
    parent: "sysadmin/configuration/easydb-server.yml"
easydb-server.yml:
  - server.mailer.enabled
  - email.welcome_new_user
  - email.login_disabled
  - smtp.server
  - smtp.hostname
  - smtp.from-address
---

# Sending E-mails

The easydb sends emails to its users to ask for confirmation and to inform about certain changes.

Due to the abuse of the Internet's email infrastructure, most of our custumers' networks require that all outgoing email is handed over to a central email relay in that network.

The easydb assumes that there is always such a relay und thus this has to be configured in the easydb for emails to work.

## Configuration example

The examples below assume that the relay has the address 1.2.3.4, and that this mail server will relay mails coming from the easydb host if the easydb host is easydb-system.example.com and if the emails have the sender address noreply@example.com. 

Assuming that the base path choosen during the [installation](/en/sysadmin2/installation) is `/srv/easydb`, add into ...  *(but without creating e.g. a second `server` line)*:

`/srv/easydb/config/easydb-server.yml`:

```yaml
server:
  mailer:
    enabled: true
smtp:
  server: 1.2.3.4
  hostname: easydb-system.example.com
  from-address: noreply@example.com
```

`/srv/easydb/config/eas.yml`:

```yml
smtp:
  server: 1.2.3.4
  hostname: easydb-system.example.com
  from-address: noreply@example.com
```

Before the 2018-12-12 release there was a section `common` in `easydb5-master.yml`. This has been replaced by the server- and EAS-specific configuration seen above.

- In the easydb web-frontend:
Choose '''base config''' in the menu, scroll down and fill both sender-address fields with (in this example) noreply@example.com. More detail [here](/en/webfrontend/administration/base-config/general/#e-mail-addresses-of-the-system).

- Restart the containers for which you changed configuration, e.g.:

```bash 
docker restart eas easydb-server
```

## Mail Transfer

easydb will make [several attempts](/en/sysadmin/easydb-server.yml/server.mailer.max_attempts/) to send each email and then gives up if no attemps succeeded. Success is determined by the exit code of the `sendmail` program, which is provided by the mail transfer agent "dma" in the containers.

easydb just sends emails but does neither accept nor process emails, even error emails which are direct results of the sent emails. If you want to process answers to emails then set the smtp:from-address (see above) setting to an address where you receive the emails. Also fill all email settings in the [frontend](/en/webfrontend/administration/base-config/general/#e-mail-addresses-of-the-system).

If you want the easydb mail sending process to authenticate towards your smtp relay, we suggest to install postfix e.g. on the container host and do the configuration there. This postfix can then just trust the IP network of the containers. We recommend that the easydb configuration talks to postfix on the main IP address (1.2.3.4 in the example above), since this will reliably be up when postfix starts and thus postfix can listen there. The container network may not be up while postfix starts, so postfix might not listen there.

## Test E-mail sending

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

echo "Subject: testing dma"| dma you@example.com
```

Optional: Check the configration that was built for dma, using your settings from easydb5-master.yml:

```bash
docker exec easydb-server cat /etc/dma/dma.conf
```

### test using the easydb web-frontend
1. In upper right hand corner of the frontend: click on your '''user'''(e.g. root) and open '''settings'''.
2. Change '''email address''' to an address that you receive - a confirmation request email is sent.


## E-mails which are sent immediately

For certain operations, emails are sent from the server. The following emails are sent immediately (1):

| Name | When is the email sent? | To which addresses is the email sent? |
| ------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| welcome_new_user |  A user is created | To the "best" (2) email address of the newly created user |
| updated_self_service | A user changes his own data | To the "best" (2) email address of the user |
| updated_record | The data of a user is edited (by someone else) | To the "best" (2) email address of the user|
| forgot_password | A user initiates the Forgot Password process | To the specified email address, or if the login was used, to the "best" (2)|
| confirm_email | - An email needs confirmation | To the email address to be confirmed |
|  | - because it has been modified or newly created by the user | |
|  | - because the administrator has set it |  |
| require_password_change | A user is requested to change his password | To the "best" (2) email address of the user |
| login_disabled | A user is locked (3)  | To the "best" (2) email address of the user
| share_collection | A user was invited to a collection | To the "best" (2) email address of the user |
| transition_resolve | A transition has been triggered and the email is immediate | Mailer decides |
| transition_reject | A transition has been rejected and the email is scheduled | Mailer decides |
| transport | An export is finished and the user receives the data by email (transport "email") | To the "best" (2) email address of the user |
| export | An export is finished (message for the export producer) | To the first email address of the user who has `send_email` |

Remarks:

(1) "immediate" means that they will be processed and sent at the next run of the process "mailer". The frequency
Can be set in the configuration (mailer.interval) and is default one minute.

(2) The "best" email address is the preferred email address when it is set. Otherwise, it is the user's first email address.
If the user has not set an email address, the email is not sent.

(3) When a user is locked (`login_disabled`), an email is sent. While it is locked, no further emails will be sent.

In addition, there is an email, which is sent "scheduled". This means that it will be sent at the time the user is in his or her home
"Schedule":

| Name | When is the email generated? | To which addresses is the email sent? |
| ------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| transition_resolve | A transition has been triggered and the email is scheduled | Mailer decides |
| transition_reject | A transition has been rejected and the email is scheduled | Mailer decides |

The transitions can be configured so that the emails can be sent individually or together (`batchable`). In the latter case, operations for
The same transition (i.e., the same transition ID) in the transition table (see below).

## E-mail templates

The server creates the emails from templates. Templates are emails in mbox format.

To create your own template we suggest to ...

- use a built-in template as a starting point (we will show how to retrieve the built-in templates further below) and to
- send any email to yourself and view the "source code" of the email (we tested this with Mozilla Thunderbrid), for e.g. converting your own images to mbox format.

We added easydb specific placeholders and therefore we explain them in more detail below.

You only need a few header lines in a template, example:

```
X-Easydb-Message-Type: login_disabled
Subject: Uni Atlantis Mediathek - Benutzerkonto gesperrt
```

Each template must only contain one email.

But for the rest of the mbox format please refer to external sources, e.g.

- https://tools.ietf.org/html/rfc2049 shows an example with multiple parts inside one email, e.g. an image, in "Appendix A".

### Placeholders

The email templates may contain placeholders which easydb will later replace. A placeholder looks like this:

An example:

```bash
Subject: %(server.email.subject)s
```

Syntax:

**%(**\<name\>**)**\<type\>

\<name\>  is the name of the variable to be replaced. \<type\> determines the format for the value:

| Type | Meaning  |
| ------ | ------------------- |
| s | Text |
| i | Integer |
| ui | Positive integer |
| d | Date + Time |
| D | Date |

When the email is built, the placeholder is replaced by the value of the variable in the desired format. The values and the date and time formats are localized. This means,
The user will receive an email in his / her language.

Variables of type "s" can also contain placeholders. The server allows nested placeholders as long as they do not repeat.

And `server.email.subject` is provided by the server itself.

The server has an internal localization map with the following entry:

```bash
"server.email.subject","E-Mail für %(_generated_displayname)s","E-mail for %(_generated_displayname)s"
```

And again, `_generated_displayname` is provided by the server itself.

The localization map can only be changed by programming a plugin for the easydb or by a tailored solution by Programmfabrik.

But you can just copy an existing template and change that:

### Variables

These variables can be used in the email templates:

| Variable | Value  |
| --------------------------------- | -------------------------------------------------- |
| `_generated_displayname` | A representation name of the user that is created from the user's name, login, or email address, depending on availability |
| `_login_or_email` | The login name of the user or, if not available, the email address of the user |
| `first_name` | The user 's first name |
| `last_name` | The surname of the user |
| `login` | The login name of the user |
| `easydb_url` | The URL of easydb |
| `easydb_name` | The name of the easydb |
| `lang` | The selected language of the user |

Depending on the type of email, other variables are also available:

| Email Type | Variable | Value |
| ----------------------------- | -------------------------------------- | ------ |
| updated_self_service | self_service_fields_table | HTML table with the data edited by the user (before / after) | 
| updated_record |  updated_fields_table | HTML table with the data edited (before / after) | 
| forgot_password | task_link | URL for resetting the password | 
| require_password_change | task_link | URL for changing the password | 
| confirm_email | task_link | URL for email confirmation | 
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

### Change a template
Get a built-in template as a starting point: (example: The template used for emails in case of disabled login)

The filename has to be chosen among the existing templates. To list templates, use the following command:

```bash
docker exec easydb-server ls /easydb-5/base/email
```

Copy the chosen template, in our example, login_disabled.mbox:

```bash
docker exec easydb-server cat /easydb-5/base/email/login_disabled.mbox > /srv/easydb/config/login_disabled.mbox
```

In the example above we use /srv/easydb as the base path. Please adjust to the one which was used during the installation of your easydb.

The first path in the command line above is inside the docker container. The directories there do not need to be adjusted.

Configure that your edited version shall be used from now on, in easydb-server.yml:

```bash
email:
  login_disabled:           /config/mail/login_disabled.mbox
```

The Path /config/[...] is inside the docker container and should thus not be prefixed with `/srv/easydb`. Instead, docker provides that `/srv/easydb/config` is usable inside the container as `/config`. (It is a "mapped volume".)

Change the template, for exampe the subject line, into:

```bash
Subject: easydb login disabled for %(_generated_displayname)s
```

Restart the docker container "easydb-server" (or the whole easydb).

```bash 
docker restart easydb-server
```
