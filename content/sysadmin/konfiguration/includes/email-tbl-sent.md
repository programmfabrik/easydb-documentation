| Name | When is the e-mail sent? | To which addresses is the e-mail sent? |
| ------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Welcome_new_user |  A user is created | To the "best" (2) e-mail address of the newly created user |
| Updated_self_service | A user changes his own data | To the "best" (2) e-mail address of the user |
| Updated_record | The data of a user is edited (by someone else) | To the "best" (2) e-mail address of the user|
| Forgot_password | A user initiates the Forgot Password process | To the specified e-mail address, or if the login was used, to the "best" (2)|
| Confirm_email | - An e-mail needs confirmation | To the e-mail address to be confirmed |
|  | - because it has been modified or newly created by the user | |
|  | - because the administrator has set it |  |
| Require_password_change | A user is requested to change his password | To the "best" (2) e-mail address of the user |
| Login_disabled | A user is locked (3)  | To the "best" (2) e-mail address of the user
| Share_collection | A user was invited to a collection | To the "best" (2) e-mail address of the user |
| Transition_resolve | A transition has been triggered and the e-mail is immediate | Mailer decides |
| Transition_reject | A transition has been rejected and the e-mail is scheduled | Mailer decides |
| Transport | An export is finished and the user receives the data by e-mail (transport "email") | To the "best" (2) e-mail address of the user |
| Export | An export is finished (message for the export producer) | To the first e-mail address of the user who has `send_email` |