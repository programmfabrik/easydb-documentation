---
title: "167 - Messages"
menu:
  main:
    name: "Messages"
    identifier: "webfrontend/administration/messages"
    parent: "webfrontend/administration"
---
# Messages

The Messages section in easydb may perform various tasks. Here you may send a message that a user must confirm, e.g. To confirm usage conditions.

The Messages section may also be used to permanently display an imprint or make other information permanently accessible to the user.

It is possible to make certain messages visible only to certain user groups and to limit them temporarily.

Messages to the user are displayed when he has logged on or is calling easydb (for anonymous login).

> easydb remembers when which user has confirmed which message. This makes it comprehensible and provable that a user has accepted usage conditions. In a later version, we will also make this data available to the administrator.

## General {#general}

| Setting | Note |
|---|---|
|Usage|Type of message:<br><br> **System message after login**: After the user logged in (authenticated or unauthenticated), a message appears that needs to be confirmed in order to continue, e. g. terms of use. <br> **Permanent message in main menu**: Is the information in the Main Menu, e.g. easydb version, impressum <br> **Message before download**: When starting a download, the user receives a message and has to confirm this first before continuing.<br> **Welcome page in search**: Information for users in the search area. If no text is stored, the default setting is to display proposals for data records that have been released for the user. <br> **Permanent message in user menu**:The information appears as a button at the top right of the user menu. The button displays the title of the note, e.g. Terms of Use, and opens a pop-up in which the note appears. The button is also available without user login. <br> **Permanent message in self registration form**: Information, which appears in the [Self registration form](../../userprefs/selfregister). A link text is displayed. The message appears in a pop-up window when clicking on that link. If a confirmation note is also set, the link text must be read before the registration can be completed. The confirmation checkbox is automatically activated after opening the link text. |
|*Formatting*|*[Markdown](https://de.wikipedia.org/wiki/Markdown) can be used to insert your own text formatting or link texts.* |
| Title of the message. | Used for *Permanent Hint* as a link. Multilingual. |
| Type | Determines how the message is presented, but it has no effect on the functionality |
| Cosntant Reference | If the message is displayed, the message is displayed at the bottom right of the screen and is always available to the user at the click of the mouse. Use permanent references to create an imprint or information about your database |
| Confirmation Note | If entered, the user must select a checkbox and confirm the text. Multilingual field. |
| Confirm each new version | If set, all users will be prompted for confirmation once the message has been saved by the administrator |
| Valid from | Sets the first minute of validity. If the field remains free, the validity begins immediately |
| Valid to | Sets the last minute of validity. If the field remains free, it is valid without any restrictions |
| Message | The actual text of the message. Multilingual. |

## Groups

By default, messages are not visible to users. Here you define for which groups the message is to be displayed.
