---
title: "42 - HTTPS"
menu:
  main:
    name: "HTTPS"
    identifier: "sysadmin/konfiguration/global/apache2/https"
    parent: "sysadmin/konfiguration/global/apache2"
    weight: 1
---
# HTTPS

The data traffic with the easydb can be encrypted at any time via HTTPS.

In fact, the easydb does not have to be changed, but is only protected by an additional web server running outside the docker container.

HTTPS is therefore not considered as part of the easydb; But to make your work easier, we show the example implementation by Apache webserver.

> An existing certificate is required.

## Configuration of the HTTPS web server


For this purpose, a reduced configuration of Apache is sufficient.

If you still want to allow unencrypted traffic, you must ensure that Apache does not use port 80 where the easydb is already listening.

Here are the most important lines of the configuration:

{{< getFileContent file="/content/sysadmin/konfiguration/includes/apache2/enable-https.md" markdown="true" >}}

Under Debian 8, you enable the necessary modules. With:

{{< getFileContent file="/content/sysadmin/konfiguration/includes/apache2/enable-ssl-modules.md" markdown="true" >}}

## Prevent traffic without HTTPS

If you want to prevent unencrypted access, only a few changes are necessary.

### easydb startup

When you start the easydb-webfrontend, you can specify the local network interface, which can not be reached directly from outside the server.

Compared to the start in chapter [Installation](../../installation), only the penultimate row changes: It is supplemented by `127.0.0.1:`:

{{< getFileContent file="/content/sysadmin/konfiguration/includes/docker/docker-https.md" markdown="true" >}}

### easydb configuration

In the central `easydb5-master.yml`, whose location you set in [install](../../installation), you should change the URL from http to https:

```yaml
easydb-server:
  server:
    external_url: https://hostname.as.in.certificate.example.com
```

If you allow both http and https access, you can only specify a protocol here.

## Redirect HTTP accesses

So that requests are not rejected by HTTP but converted into HTTPS requests, e.g. The following information is required:

Apache:

{{< getFileContent file="/content/sysadmin/konfiguration/includes/apache2/redirect-http-to-https.md" markdown="true" >}}

When using port 80 through both easydb and apache, the `Listen` directive must ensure that Apache uses different IP addresses than the easydb. In this example, the easydb only uses the address of the local interface, ie 127.0.0.1.

Please replace "example.com" and "1.2.3.4" with the hostname and IP address of your server. The hostname should match the certificate.
