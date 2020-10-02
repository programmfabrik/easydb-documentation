---
title: Fylr
layout: config
menu:
  main:
    name: "fylr.yml"
    identifier: sysadmin/configuration/fylr.yml
    parent: sysadmin/configuration
    weight: 70
fylr.yml:
  - server.accounts
  - server.addr
  - objectstore.dir
  - objectstore.uids[].uid
  - objectstore.uids[].name
  - objectstore.uids[].allowed_instances[].id
---

# Fylr

**Flyr** is a companion product for **easydb**. It serves as server for additional services which are not covered by the **easydb server**. More information on Fylr can be found on its website [**fylr.io**](https://fylr.io).

**easydb** optionally uses two features of Fylr:

* *Objectstore*: Used to keep datamodels among **easydb** in sync. This is useful for setups where **production** and **development** servers are separated.
* *Zip*: For users of the connector plugin, Fylr provides a service to zip files for download on the fly.

## Configuration

| Config                                        | Format  | Description                                                  |
| --------------------------------------------- | ------- | ------------------------------------------------------------ |
| `server`                                      | Map     |                                                              |
| &#8193;`addr`                                 | String  | Address of the server.                                       |
| &#8193;`hostname`                             | String  | In case the hostname is responded in any api response it is replaced with this one. If hostname is empty, the addr is used |
| &#8193;`accounts`                             | Map\<String\>String | Accounts defines a list of accounts that are allowed to login the easydbservices frontend. The api endpoints are not influenced by this accounts. Example: `root: "admin"` |
| &#8193;`assets_from_local_fs`                 | Boolean | The static assets are build into the binary. If you want to load them directly from the filesystem set this option to true. **DO NOT SET TO TRUE IN PRODUCTION** |
| &#8193;`log`                                  | Map | Configure the logging behavior                               |
| &#8193;&#8193;`level`                         | String  | Which log level should be logged. Available [`panic, fatal, error, warn, info, debug, trace`]. Default "info" |
| &#8193;&#8193;`file`                          | String  | Location of the sqlite file for the frontend log. Default "./log.db" |
| &#8193;`cert_file`                            | String  | If the server should be run with SSL enabled, both cert_file & key_file must be configured. |
| &#8193;`key_file`                             | String  | If the server should be run with SSL enabled, both cert_file & key_file must be configured. |
|                                               |         |                                                              |
| `pdf_creator`                                 | Map     | |
| &#8193;`chrome_addr`                          | String  | `chrome_addr` points to the headless chrome. 9222 is the standard port for the chrome remote debugging protocol |
| &#8193;`max_chrome_connections`               | int     | `max_chrome_connections` prevents running out of memory because to many chrome tabs are open at the same time. Defaults to 10 to many connections can cause a lot of memory in the headless chrome |
| &#8192;`chrome_back_channel_httpd`            | Map     | Local http server which serves the uploaded html for the access of the headless chrome |
| &#8193;&#8193;`addr`                          | String  | Address to run that second httpd on. **MUST BE ACCESSABLE FROM THE headless chrome container** |
| &#8193;&#8192;`hostname`                      | String  | Hostname for defining a docker-net internal dns name instead of using an IP. If not set, addr is used |
|                                               |         |                                                              |
| `link_shortener`                              | Map     | |
| &#8193;`domain`                               | String  | Base domain for the shortlinks. Is replied in the add link request. Should be public accessable |
| &#8193;`default_expire_days`                  | int     | If not set differently in the add link request, this expiry time is used. If default_expire_days is 0, the links never expire |
| &#8193;`min_length`                           | int     | Minimum length for a shortlink key |
| &#8193;`max_length`                           | int     | Maximum length for a shortlink key |
| &#8193;`db`                                   | String  | Path to the sqlite db where the short links are stored |
| &#8193;`allowed_urls`                         | String[] | Array of allowed shortlink targets. With a narrow configuration we can only allow the shorting of easyd urls |
|                                               |         |                                                              |
| `objectstore`                                 | Map    |                                                              |
| &#8193;`dir`                                  | String | Top-Level-Directory where Fylr stores its data.              |
| &#8193;`uids`                                 | Map[]  | Configured uuids for the store |
| &#8193;&#8193;`uid`                           | String | UID of the storage, this is a unique id for each storage group. |
| &#8193;&#8193;`name`                          | String | Name for the store |
| &#8193;&#8193;`allowed_instances`             | String | UID of the storage, this is a unique id for each storage group. |
| &#8193;&#8193;&#8193;`id`                     | String | Identifier of one of the clients for the storage.            |
| &#8193;&#8193;&#8193;`name`                   | String | Optional name for the client, as shown in the overview page on Fylr. |
|                                               |        |                                                              |
| `zip`                                         |        | If set, the *Zip*  service is enabled and allows Zipfiles to be created with files originating the given URLs. Each entry is endpoint |
| `allowed_urls`                                | String[] | URL bases that are allowed to get files for the zip from. |
| `max_concurrent_head_reqs`                    | int    | maximum parallel check if files are available. To big numbers could consume all system file descriptors or the remote resource blocks us because of DOS attack prevention |

## Configuration files

To show you more than just a few basics, we use an unusal elaborate example.

An elaborate main configuration file, `/srv/easydb/config/fylr.yml`, could look like this:

*(From now on we are assuming that `/srv/easydb` is your base directory where you installed easydb.)*

```yaml
hostname:
  fylr: easydb-fylr:4000

external_url: https://easydb-system.example.com
objectstore:
  uids: []

link_shortener:
  default_expire_days: 3650

root_password: my_secret

smtp:
  server: relay.example.com
  hostname: easydb-system.example.com
  from-address: noreply@easydb-system.example.com
```

In an additional configuration file, `/srv/easydb/config/fylr.d/objectstore_uids.yml`, you could provide a list of objectstores:


```yaml
objectstore:
  uids:
    # for project #12345
    - uid: 'e978560a-bd52-4a56-86d4-ed29d6041d21'
      name: 'objectstore1'
      allowed_instances:
        - id: '5fa800a5-0b08-4650-9ea4-7a566eb0dac3'
          name: access_by_production
        - id: 'abcdefghijklmnopqRSTUVWXYZ'
          name: access_by_internal
    - uid: 'f637ff9b-26ef-48a9-9019-a90deb254a70'
      allowed_instances:
        - id: '7e7896cb-2f4a-4b4d-9d72-34b7cf535c0c'
```


