---
title: Webfrontend
layout: config
menu:
  main:
    name: "Webfrontend"
    identifier: "sysadmin/configuration/easydb-server.yml/config_webfrontend"
    parent: "sysadmin/configuration/easydb-server.yml"
    weight: -995
easydb-server.yml:
  - default_client.debug
  - default_client.tag_icons
  - default_client.tag_colors
  - default_client.asset_browser_max_preview_filesize
  - default_client.video_player_use_original
  - default_client.audio_player_use_original
  - default_client.webdvd_player_open_window_parameter
  - default_client.print_limit
  - default_client.collection_refresh_rate_seconds
  - default_client.suggest_disable
  - default_client.database.level
  - default_client.database.server
  - default_client.database.uid
  - default_client.database.instance
  - default_client.download_zip.url
  - default_client.index_html_head_include
  - default_client.index_html_body_include
  - default_client.sso_authentication_required_html
---

# Webfrontend

This article describes the configuration for the webfrontend which can be done in the server. All configuration for the webfrontend are inside a **default_client** map.

## default_client

The following table describes each key in the map.

| <div style="width:325px">Config</div> | Format  | Description                                                  | Default |
| -------                                 | ------- | ------------------------------------------------------------ | ------- |
| `default_client` | List | Is the parent element which contains client related settings |
| &#8193;`asset_browser_max_preview_filesize`    | Integer | Up to this size, preview images for the display in the asset browser are considered. If not set to *`-1`*, the *Original* is never taken into account. If set to *`0`*, all sizes and the original are taken into account | - |
| &#8193;`audio_player_use_original`             | Boolean | If set, the audio player also uses the original as source for the HTML5 audio tag. | *false* |
| &#8193;`collection_refresh_rate_seconds`       | Integer | Number of seconds waited until the fixed searches in the Finder are updated. | *30* |
| &#8193;`datamodel`                              |         | | |
| &#8193;&#8193;`instance`                       | String  | Optional overwrite to the the identifier for the storage client on Fylr. If not set, the instance name of **easydb** is used. | - |
| &#8193;&#8193;`level`                          | String  | Overwrites the highest permitted database rights level. Allowed values are: *development* (the dev datamodel is visible and changeable), *current* (the current datamodel is visible), *commit* (both data models are visible and changeable). | - |
| &#8193;&#8193;`server`                         | Url     | Url of the [**Fylr** server](/en/sysadmin/configuration/fylr.yml/) to store a common datamodel among multiple **easydb** servers. | - |
| &#8193;&#8193;`uid`                            | String  | UID of the Fylr storage. | - |
| &#8193;`debug`                                 | Boolean | If set, the client is in debug mode, i.e. there are dump options in the context menu. | *false* |
| &#8193;`download_zip`                          |         | | |
| &#8193;&#8193;`url`                            | String  | Url of the [**Fylr** server](/en/sysadmin/configuration/fylr.yml/) ending in /zip to support ZIP downloads for certain customer solutions. | - |
| &#8193;`index_html_body_include`               | File    | Name of HTML file to be included in `body` part of `index.html`. It is recommended to put this file into the `config` directory next to the configuration files and reference it from the configuration using the `/config` prefix, e.g. `/config/include_body.html`. You can use this config to inject your own HTML into the main easydb webfrontend startpage. This can be used to serve a Sitemap. Since easydb is a single page app, the index.html is the only file loaded directly from the webserver. Afterwards, all changes in the DOM are done by Javascript. This is important to keep in mind when adding an analytics tool using this mechanism. | - |
| &#8193;`index_html_head_include`               | File    | Name of HTML file to be included in `head` part of `index.html`. See `index_html_body_include` for additional notes.| - |
| &#8193;`print_limit`                           | Integer | Limit the maximum number of objects that can be printed. | *250* |
| &#8193;`sso_authentication_required_html`      | File    | Name of HTML file to be used on SSO authentication errors. It is recommended to put this file into the `config` directory next to the configuration files and reference it from the configuration using the `/config` prefix, e.g. `/config/sso_authentication_required.html`. Added in version 5.62.0 |
| &#8193;`suggest_disable`                       | Boolean | If set, suggestions in input fields are disabled | *false* |
| &#8193;`tag_colors`                            | String  | Comma-separated list. Color clases for the tags. | *green, red, blue, yellow* |
| &#8193;`tag_icons`                             | String  | Comma-separated trick. Icon names for tag icons that can be stored for tags. Font-Awesome and CUI designations are allowed | *bolt, check, cloud, warning, legal* |
| &#8193;`video_player_use_original`             | Boolean | If set, the video player also uses the original as source for the HTML5 video tag. | *false* |
| &#8193;`webdvd_player_open_window_parameter`   | String  | HTML compliant string for [window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open). Settings for opening the new browser window to play a web DVD | - |

