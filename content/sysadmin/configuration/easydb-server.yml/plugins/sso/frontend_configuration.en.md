---
title: "SSO Frontend Configuration"
menu:
  main:
    name: "SSO Frontend Configuration"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/sso/frontend_configuration"
    weight: -938
    parent: "sysadmin/configuration/easydb-server.yml/plugins/sso"
---

As part of the [SSO](../) plugin, you may tailor the user experience of the easydb.

# SSO Frontend configuration

There are several variables available for configuring the web frontend, which are set in the `easydb-server.yml`.

The location of `easydb-server.yml` is chosen during the [install](../../../../../installation).

## List of frontend settings

| Variable <div style="width:200px"></div> | Type | Obligation | Explanation | Default Value |
| ------------------------------------------------- | --------------- | --------- | ----------- | -------------- |
| `login:` | | | Settings for calling the SSO login from the login dialog. Without this block, the SSO login is not visible in the login dialog ||
| &#8193;`timeout:` | Integer | No | Number of milliseconds before the single-sign-on iframe is automatically terminated if not previously authenticated. The value 0 turns off the timeout. The timeout is only considered if `visible = false` | 5000 |
| &#8193;`window_open:` | String | No | If set, the SSO system is opened when the login page is opened in a separate browser window. The browser window is started with the specified window.open parameters. The parameter is the *strWindowFeatures* as described in [window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open). *StrWindowName* is always `\ _blank`. If set to **self**, the URL is opened inside the main window. | - |
| &#8193;`visible:` | Boolean | No | If set, the Iframe call is displayed visibly in a modal dialog. | True |
| &#8193;`show_errors:` | Boolean | No | If set, iframe errors are visible. | True |
| &#8193;`visually_preferred:` | Boolean |  No | If set, the login dialog has a design with the SSO login in the foreground. | False |
| `logout:`                                      |               |         | Configure what happens after Logout. | |
| &#8193;`url:`                             | String       | No    | URL which is called as soon as the user logs out. By default this is done in a new browser window. | |
| &#8193;`window_open:`                              | String       | No    | Parameters for the window.open call. Configures the new browser window. This is *strWindowFeatures* as described in [window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open). If this is set to **self**, then no new window is opened but the current one is used instead. | |
| autostart | | | Settings for automatically starting the SSO logon. Without the block, Autostart is inactive | |
| &#8193;`timeout:` | Integer | No | Number of milliseconds before the single-sign-on iframe is automatically terminated if not previously authenticated. The value 0 turns off the timeout. The timeout is only considered if **visible = false** | 5000 |
| &#8193;`visible:` | Boolean | No | If set, the Iframe call is displayed visibly in a modal dialog. | True |
| &#8193;`show_errors:` | Boolean | No | If set, iframe errors are visible. | True |
| &#8193;`anonymous_fallback:` | Boolean | No | If set, attempts are made to log the user anonymously. | False |

> From the login, you can force CTRL-mouse click: `visible = true`,` show_errors = true` and `timeout = 0`. The settings for window_open are ignored with ALT mouse click.

## Frontend Configuration Examples

> Only add those lines which are missing in your configuration.

Example 1:

```yaml
easydb-server:
  sso:
    auth_method:
      client:
        login:
          visible: true
          show_errors: true
          window_open: ""
```

In example 1 the login dialog appears. In the login dialog, clicking "Use logon service" displays a window with the login dialog of your Single Sign-On System. We recommend to start with these settings.

Example 2:

```yaml
easydb-server:
  sso:
    auth_method:
      client:
        login:
          visible: true
          show_errors: true
          window_open: ""
          visually_preferred: true
```

Example 2 replaces the easydb login dialog with the one of your Single Sign-On System. We recommend to use this configuration once the login has been successfully set up and tested.

Example 3:

```yaml
easydb-server:
  sso:
    auth_method:
      client:
        autostart:
		  timeout: 5000
          visible: false
          show_errors: false
          anonymous_fallback: false
        login:
          visible: true
          window_open: "height=600, width=400"
          show_errors: true
        logout:
          url: https://www.testshib.org/Shibboleth.sso/Logout
          window_open: "width=640,height=400"
```

In example 3, an automatic login is explicitly configured, so the Kerberos ticket or Shibboleth token is tried first. If this does not succeed within 5 seconds, the login dialog will appear with the "Use logon service" link. Clicking on this link opens an iframe by default, but in the example a separate browser window in the size 600 x 400 pixels is opened instead. Also there is a window opened after logout.
