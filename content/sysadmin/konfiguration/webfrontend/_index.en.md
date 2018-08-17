---
title: Webfrontend
layout: config
menu:
  main:
    name: "Webfrontend"
    parent: "sysadmin/konfiguration"
    identifier: config_webfrontend
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
---

# Webfrontend

This article describes the configuration for the webfrontend which can be done in the server. All configuration for the webfrontend are inside a **default_client** map.

## default_client

The following table describes each key in the map.

| Config  | Format  | Description                                                  | Default |
| ------- | ------- | ------------------------------------------------------------ | ------- |
| `debug` | Boolean | If set, the client is in debug mode, i.e. there are dump options in the context menu. | *false* |
| `tag_icons` | String | Comma-separated trick. Icon names for tag icons that can be stored for tags. Font-Awesome and CUI designations are allowed | *bolt, check, cloud, warning, legal* |
| `tag_colors`  | String  | Comma-separated list. Color clases for the tags. | *green, red, blue, yellow* |
| `asset_browser_max_preview_filesize`       | Integer        | Up to this size, preview images for the display in the asset browser are considered. If not set to *`-1`*, the *Original* is never taken into account. If set to *`0`*, all sizes and the original are taken into account | - |
| `video_player_use_original`  | Boolean   | If set, the video player also uses the original as source for the HTML5 video tag. | *false* |
| `audio_player_use_original`  | Boolean   |  If set, the audio player also uses the original as source for the HTML5 audio tag. | *false* |
| `webdvd_player_open_window_parameter` | String         | HTML compliant string for [window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open). Settings for opening the new browser window to play a web DVD | - |
| `print_limit`                 | Integer         | Limit the maximum number of objects that can be printed. | *250* |
| `collection_refresh_rate_seconds` | Integer   | Number of seconds waited until the fixed searches in the Finder are updated. | *30* |
| `suggest_disable`    | Boolean       | If set, suggestions in input fields are disabled | *false* |
| `database.level`           | String     | Overwrites the highest permitted database rights level. Allowed values are: *development*, *commit*, *current*. | - |
| `database.server` | Url | Url of the [**Fylr** server](/en/sysadmin/fylr) to store a common datamodel among multiple **easydb** servers. | - |
| `database.uid` | String | UID of the Fylr storage. | - |
| `database.instance` | String | Optional overwrite to the the identifier for the storage client on Fylr. If not set, the instance name of **easydb** is used. | - |