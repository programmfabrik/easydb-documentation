---
title: "E-Mail Configuration"
layout: config
menu:
  main:
    name: "E-Mail"
    identifier: "sysadmin/konfiguration/global/email"
    parent: "sysadmin/konfiguration/global"
    weight: 2
easydb-server.yml:
  - server.mailer.enabled
  - server.email.subject
  - server.email.welcom_new_user.greeting
  - email.server
  - email.hostname
  - email.from-address
  - email.login_disabled
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
common:
  email:
    server: 172.18.0.1
    hostname: easy.example.com
    from-address: noreply@example.com
```

- In the easydb web-frontend:
Choose '''base config''' in the menu, scroll down and fill both sender-address fields with (in this example) noreply@example.com.

- Restart the docker container "easydb-server" (or the whole easydb):

{{< getFileContent file="/content/sysadmin/konfiguration/includes/docker/restart-docker-be.md" markdown="true" >}}

## Test e-mail sending

### test using SMTP directly

{{< getFileContent file="/content/sysadmin/konfiguration/includes/bash/test-email-sending.md" markdown="true" >}}

### test using the mail program in the container

{{< getFileContent file="/content/sysadmin/konfiguration/includes/bash/test-email-sending-in-docker.md" markdown="true" >}}

Optional: Check the configration that was built for sSMTP, using your settings from easydb5-master.yml:

{{< getFileContent file="/content/sysadmin/konfiguration/includes/bash/check-ssmtp-configuration.md" markdown="true" >}}

### test using the easydb web-frontend
1. In upper right hand corner of the frontend: click on your '''user'''(e.g. root) and open '''settings'''.
2. Change '''e-mail address''' to an address that you receive - a confirmation request e-mail is sent.


## E-mails which are sent immediately

For certain operations, e-mails are sent from the server. The following e-mails are sent immediately (1):

{{< getFileContent file="/content/sysadmin/konfiguration/includes/email-tbl-sent.md" markdown="true" >}}

Remarks:

(1) "immediate" means that they will be processed and sent at the next run of the process "mailer". The frequency
Can be set in the configuration (mailer.interval) and is default one minute.

(2) The "best" e-mail address is the preferred e-mail address when it is set. Otherwise, it is the user's first e-mail address.
If the user has not set an e-mail address, the e-mail is not sent.

(3) When a user is locked (`login_disabled`), an e-mail is sent. While it is locked, no further e-mails will be sent.

In addition, there is an e-mail, which is sent "scheduled". This means that it will be sent at the time the user is in his or her home
"Schedule":

{{< getFileContent file="/content/sysadmin/konfiguration/includes/email-tbl-trantition.md" markdown="true" >}}

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
| S | Text |
| I | Integer |
| Ui | Positive integer |
| D | Date + Time |
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

{{< getFileContent file="/content/sysadmin/konfiguration/includes/docker/docker-change-mail-template-disabled-login.md" markdown="true" >}}

In the example above we use /srv/easydb as the base path. Please adjust to the one which was used during the installation of your easydb.

The first path in the command line above is inside the docker container and does not need to be adjusted in most cases. The filename however has to be chosen to among the existing templates. To list templates, use the following command:

{{< getFileContent file="/content/sysadmin/konfiguration/includes/docker/docker-list-email-templates.md" markdown="true" >}}

- Configure that your edited version shall be used from now on, in easydb5-master.yml:

```bash
easydb-server:
  email:
    login_disabled:           /config/mail/login_disabled.mbox
```

The Path /config/[...] is inside the docker container and should thus not be prefixed with "/srv/easydb". Instead, docker provides that /srv/easydb/config is usable inside the container as /config. (It is a "mapped volume".)

- Restart the docker container "easydb-server" (or the whole easydb).

{{< getFileContent file="/content/sysadmin/konfiguration/includes/docker/restart-docker-be.md" markdown="true" >}}

### Variables

The variables that can be used as source in the e-mail templates are:

{{< getFileContent file="/content/sysadmin/konfiguration/includes/email-tbl-variables.md" markdown="true" >}}

The variables that are marked with (\*) can be overwritten by the user with their own texts if a transition or export is configured.
