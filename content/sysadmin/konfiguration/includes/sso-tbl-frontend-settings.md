| Variable | Type | Obligation | Explanation | Default Value |
| ------------------------------------------------- | --------------- | --------- | ----------- | -------------- |
| `login` | | | Settings for calling the SSO login from the login dialog. Without this block, the SSO login is not visible in the login dialog ||
| `login.timeout` | Integer | No | Number of milliseconds before the single-sign-on iframe is automatically terminated if not previously authenticated. The value 0 turns off the timeout. The timeout is only considered if `visible = false` | 5000 |
| `login.window_open` | String | No | If set, the SSO system is opened when the login page is opened in a separate browser window. The browser window is started with the specified window.open parameters. The parameter is the *strWindowFeatures* as described in [window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open). *StrWindowName* is always `\ _blank`. If set to **self**, the URL is opened inside the main window. | - |
| `login.visible` | Boolean | No | If set, the Iframe call is displayed visibly in a modal dialog. | True |
| `login.show_errors` | Boolean | No | If set, iframe errors are visible. | True |
| `login.visually_preferred` | Boolean |  No | If set, the login dialog has a design with the SSO login in the foreground. | False |
| logout                                      |               |         | Configure what happens after Logout. | |
| `logout.url`                             | String       | No    | URL which is called as soon as the user logs out. By default this is done in a new browser window. | |
| `logout.window_open`                              | String       | No    | Parameters for the window.open call. Configures the new browser window. This is *strWindowFeatures* as described in [window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open). If this is set to **self**, then no new window is opened but the current one is used instead. | |
| autostart | | | Settings for automatically starting the SSO logon. Without the block, Autostart is inactive | |
| `autostart.timeout` | Integer | No | Number of milliseconds before the single-sign-on iframe is automatically terminated if not previously authenticated. The value 0 turns off the timeout. The timeout is only considered if **visible = false** | 5000 |
| `autostart.visible` | Boolean | No | If set, the Iframe call is displayed visibly in a modal dialog. | True |
| `autostart.show_errors` | Boolean | No | If set, iframe errors are visible. | True |
| `autostart.anonymous_fallback` | Boolean | No | If set, attempts are made to log the user anonymously. | False |