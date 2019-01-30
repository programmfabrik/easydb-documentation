---
title: "199 - Users"
menu:
  main:
    name: "Users"
    identifier: "webfrontend/rightsmanagement/users"
    parent: "webfrontend/rightsmanagement"
---
# User

There are several methods to create users in easydb. These are explained in detail below under *user types*. Users can be created, modified and deleted by the easydb Administrator or by users who have the system permission to manage users. To create a new user, you can copy an existing user (except for the user type *system*) and then modify it.


![](./rights_user_copy.jpg)

## General {#general}


| Setting | Description |
|---|---|
| Type | The different methods to create in easydb users correspond to different types. See the following table **User types**. |
| Login | The login for user must be unique to easydb-wide. However, it is optional. Users can be configured to use their login to login. Users can also log in using an e-mail address, which is why login is optional|
|First name| The first name of the user|
|Name |The last name of the user|
|Username|the name that other users see when they receive information about that user. Without an ad name, easydb automatically creates an ad name from the first name and name or login|
| Company | Field to deposit a company. Is currently displayed only in the user administration|
| Department | Field to deposit a department. Is currently displayed only in the user administration|
| Telephone | Phone. Is currently displayed only in the user administration|
|Image | For a user, an image can be stored. This image will be displayed to other users. If no image has been uploaded, a default image is displayed, which can be set in the config of the easydb. A uploaded image can be enlarged or reduced with drag and drop and drag and drop|
| Remarks | Internal Remark|

### User types

The distinction of user types refers to the method with which a user was created in easydb.

| Type | Description |
|---|---|
| System | The system user in the easydb. Currently, these are **root**, **oai_pmh** and **deep_link** (see [System rights](..)). These users are created automatically when easydb is set up and can not be deleted|
| Easydb | The normal easydb user. This user is set up and managed in the easydb by the administrator|
| Email | This user is created whenever an e-mail is used as a sharing target when releasing or exporting. By centrally managing the e-mail as a simple user, a later conversion to a full easydb user is possible|
| Anonymous | For each anonymous login in the easydb (call without login), an anonymous user is set up. This user is recognized by a cookie and can also save settings under his anonymous user account. Anonymous users are managed by easydb and are not visible in the frontend|
| Collection | When releasing folders (internally also collections), anonymous links can be set up, which can then be accessed directly on a folder. These users are automatically created and managed by easydb. They can not be reached via the frontend|

> NOTE: Typically only the types *easydb*, *system* and *email* are visible, the listing of the types also includes the internally managed types *anonymous* and *collection*.

## Emails

Easydb allows you to store any number of email addresses per user. E-mail addresses can fulfill various functions. For example, an e-mail address can be used by the user to log on, or e-mails can be sent as a sequence of transactions (workflow management).

The *Preferred e-mail* is the e-mail, which is communicated to the user as its e-mail address and which, if configured, it can also change by itself.

### Emails

| Setting | Description |
|---|---|
| E-mail | Is the e-mail address. The e-mail is unique|
| Requested |time when easydb sent an e-mail to request the user to confirm the e-mail|
| Confirmed | Time when the user has confirmed his / her e-mail address. |
| Request confirmation | Can be set to prompt the user (again) to confirm this e-mail address|
| Use for login  | If set the user can use this e-mail address to login. The user has only one current password, no matter what he uses to login|
| Use for E-mail | If set, this e-mail is used for workflow e-mails. The *schedule* allows you to set the number of times a user receives e-mails|
| Send Email | If set, changes to the user record are communicated to the user via e-mail. If the user himself changes his / her data in the User-Self-Management, an e-mail is always sent, this checkbox only refers to changes made in the administration area The system sends a welcome e-mail to this option|
| ... with password | If set, the password of the user is sent in the administration text. This happens only if the save action has changed or set the password|
| Preferred e-mail | Only one e-mail address is displayed to the user. If set, the user will see this e-mail address as his / her e-mail address. The preferred e-mail is the e-mail that other users get displayed by this user. If no preferred e-mail is configured, no e-mail is displayed for this user|
| Preferential e-mail | If a user changes his e-mail address via user settings and confirms the e-mail, the e-mail is set to *preferred*. The administrator can also set this checkbox manually and request a confirmation manually. After confirmation by the user, this e-mail address becomes the preferred user|

### <a name="school"> </a> Schedule

The schedule is used to provide the user with summarized workflow e-mails. Often it is not desired that an e-mail is sent immediately with every e-mail triggering workflow event. The schedule is used to summarize the e-mails and send them at the specified time. If no schedule is configured, workflow e-mails are sent out immediately at each event.

A filter is defined by checkboxes. If this filter fits, an e-mail will be sent. For example, You can configure that e-mails are always sent out on the 1st of the Monday at 10 o'clock: *day in the month*: 1 *hour*: 10.

| Setting | Description |
|---|---|
| Day a month | The days of the month used for the filter. |
| Weekday | The weekdays used for the filter. |
| Hours | Hours used for the filter. |


## Password management

| Setting | Description |
|---|---|
| Login blocked | Checkbox to lock a user's login. The user is informed of the blocking by e-mail
| User must set or change password at next login | To log on successfully, the user must assign a password during this login attempt|
| Set password | If set, the user password is set or deleted by the administrator. |
| Automatically generated password | If set, an automatically generated password is assigned to the user. This only makes sense in the connection of the options *Send e-mail* + *... with password*, otherwise no one can see the password. Passwords are stored encrypted in the easydb and can not be easily decrypted|
| Password | To set the password by the administrator, a password can be entered here. If it remains blank, the password is deleted and the user can not log in anymore|

## Groups

You use the checkbox to define in which groups the user is located. Note that a user can only be manually classified into non-system groups. The classification in [system groups](../groups) takes place automatically.

### Preferences for new users {#prefs}

It is possible to set preferences for new users by assigning them to groups. The user preferences include:

* the view for the search results
* the selection of active pools for the search
* the selection of active object types for the search
* the active database languages
* the active search languages
* Filter: active or hidden

The preferences are saved for the [Group](../groups) and can be taken over from an existing user or a pseudo-user, which was created especially for this purpose.

If the new user is assigned to several groups for which preferences have been set, he or she receives the settings of the first group (which is returned by the server).

## System rights

For a listing of the system rights, see [Rights Management](..). Note that context-dependent system rights may also be available, if any, not listed here.

## Authorizations

A list of all rights can be found under [Rights Management](..). Please note that not all of the listed rights are available depending on the context.
