|`system.login.internet`	   | boolean	| Clients considered on the internet (on an IP basis) are required to login. Default is true. |
|`system.login.intranet`	   | boolean	| Clients considered on the internet (on an IP basis) are required to login. Default: true. |
|`system.login.user.send_email`	 | boolean	| If set, send emails to the user with login information. Default to set in the user record when a user is created. Default: true. |
|`system.login.user.confirm_email`	| boolean	| If set, the user needs to confirm the email. Default to set in the user record when a user is created. Default: true. |
|`system.login.password_policy` | regexp | The default password policy. Defaults to `ini:system.login.user.password_policy`. |
|`system.login.password_policy.hint` | String-L10n | Text to explain the password policy to the user. Defaults to `csv:system.login.user.password_policy.hint`. |
|`system.login.forgotten_password_process` | Boolean | The system is allowed to support a forgotten password process. |
