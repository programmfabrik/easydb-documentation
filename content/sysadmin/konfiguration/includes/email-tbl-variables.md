| Variable | Value  |
| --------------------------------- | -------------------------------------------------- |
| `_generated_displayname` | A representation name of the user that is created from the user's name, login, or e-mail address, depending on availability |
| `_login_or_email` | The login name of the user or, if not available, the e-mail address of the user |
| `First_name` | The user 's first name |
| `Last_name` | The surname of the user |
| `Login` | The login name of the user |
| `Easydb_url` | The URL of easydb |
| `Easydb_name` | The name of the easydb |
| `Lang` | The selected language of the user |

Depending on the type of e-mail, other variables are also available:

| Email Type | Variable | Value |
| ----------------------------- | -------------------------------------- | ------ |
| Updated_self_service | Self_service_fields_table | HTML table with the data edited by the user (before / after) | 
| Updated_record |  Updated_fields_table | HTML table with the data edited (before / after) | 
| Forgot_password | Task_link | URL for resetting the password | 
| Require_password_change | Task_link | URL for changing the password | 
| Confirm_email | Task_link | URL for e-mail confirmation | 
| Share_collection | Collection_name  | Name of Collection | 
| Share_collection | Collection_description | Description of the collection | 
| Share_collection | Collection_link | URL to collection | 
| Transport | Export_id | Export ID |
| Transport | Export_name | Name of the export | 
| Transport  | Downloads | HTML table with the files of the export and links to the downloads | 
| Transport  | Server.email.export.message (\*) | User configured message | 
| Transition_ {resolve / reject} | Transitions HTML table with information about the operations that caused the transition | 
| Transition_ {resolve / reject} | Server.email.transition.subject (\*) | User-configured subject | 
| Transition_ {resolve / reject} | Server.email.transition.body (\*) | User configured body | 