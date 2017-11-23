# Wordpress plugin

Plugin to easily transport media files to Wordpress CMS. Currently this supports
 creating of new media as well as updating media metadata. When media are update
d in easydb, a new media is created in Wordpress. There is no support for delete
s.

## Requirements

* Wordpress 4.7
* Wordpress needs to have the JSON-Rest-API enabled (which is the default) and a
uthentication set up.

## Setup (Wordpress)

* easydb supports **JSON Basic Authentication** and **WP REST API - OAuth 1.0a S
erver**
 * Install plugin(s) for authentication
 * Enable plugin(s)
 * Setup a user for oauth plugin, Callback URL: http://**easydb-server**/api/v1/plugin/base/easydb-wordpress-plugin/oauth1

## Install Plugin in easydb

* Make sure the plugin is correctly installed (paths are relative to the .yml);

Add the following lines to your server.yml:

```
base:
  plugins+:
    - name: wordpress
      file: easydb-wordpress-plugin/wordpress.yml

plugins:
  enabled+:
    - base.sso
    - base.simple-example
    - base.wordpress
```

(see FIXME)

### HTTP-Authentication

Use an admins login & password to connect.

### OAuth 1.0a

* Copy Client Key and Client Secret from the prepared applicatin user from Wordpress.
* Press "Generate Key" to connect to Wordpress, authenticate and retrieve a Token and Token Secret.
* Don't forget to save base config.

## Authenticate easydb users

Use system right "Wordpress" & "Wordpress transport" and authorize anybody who should be able to use easydb Wordpress Transport.

## Use in easydb

* In any export, use "Transport Wordpress" to transport all exported files to Wordpress.
* Pick the prepared and configured Wordpress instance for the transport.
* Optionally choose a schedule and incremental updates for regular updates.
