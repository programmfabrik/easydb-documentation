---
title: "53 - Requirements"
menu:
  main:
    name: "Requirements"
    identifier: "sysadmin/requirements"
    parent: "sysadmin"
---
# Requirements

## Software

Docker at least in version 1.11.

Versions with the newer version scheme (e.g., 17.03) are all recent enough.

The Community Edition (CE) is quite sufficient. We recommend the "stable" channel and assume the default architecture x86_64.

If we are installing the easydb for you then we will also install Docker ourselves. But please make sure that the requirements for Docker are met.

Here is a link to the [installation guide](https://docs.docker.com/engine/installation/linux/debian/#os-requirements) for Docker under e.g. Debian.

### Operating system

The selection of the operating system depends on Docker. There are, however, the following exceptions:

- If you want Programmfabrik to fullfill a maintenance contract on the server then only with Docker on a Debian server - without a graphical interface, 64 bit, in a version for which there are security updates.

- If you want Programmfabrik to do isolated tasks on the server (remote installation or troubleshooting) then only with Docker on a Debian server or Ubuntu server - without a graphical interface, 64 bit, in a version for which there are security updates.

- If you do not want Programmfabrik to take care of the server and want to use Windows as a further requirement, then you need the variant "[Docker for Windows](https://docs.docker.com/docker-for-windows/#step-one-install-docker-for-windows). " The easydb 5 does not work with its alternative "[native Docker](https://msdn.microsoft.com/en-us/virtualization/windowscontainers/quick_start/quick_start_windows_10)", which is also recognizable by it's "docker.exe".

We do not make separate tests for "Docker for Windows" or Docker on Mac OSX and have not measured the amount of performance degradation by the [additional virtualization](https://docs.docker.com/v1.11/engine/faq/#does-docker-run on Mac OS x-or-windows).

Are you interested in directly downloading a recommended operating system?

1. Go to [http://cdimage.debian.org/debian-cd/current/amd64/iso-cd](http://cdimage.debian.org/debian-cd/current/amd64/iso-cd )
2. Download the file that starts with `debian-9.` and ends with `-amd64-netinst.iso`.


## Hardware

4 processor cores. (Recommendation. Depending on your usage, more.)

16 GB of RAM. (Recommendation. Depending on your usage, more.)

Docker may have further requirements, e.g. 64 bit processor cores. These are mentioned in the Docker [installation guide](https://docs.docker.com/engine/installation/linux/debian/#os-requirements).

Storage space:

- 40 GB for the Docker files of the easydb. These grow slowly over time, starting from 8 GB.
- 50 GB for temporary files, such as intermediate conversion results or files for the zoom function.
- 30 GB for the operating system and log messages.
- 1 GB at least in /boot to accommodate the accumulating kernel versions. We recommend to not have /boot separately but instead as part of the root partition.
- 200% of the storage space of the assets which you want to manage with easydb. 100% is your assets and another 100% for preview versions. If you need additional large preview versions, more. Assets and preview versions can be stored on network storage (e.g. NFS). The other types of files should not be on network storage.
- 4% additional storage space for databases. The databases are the first to put on fast storage (e.g. SSDs). But this is optional.
- Summary: 120 GB plus 204% of the spaced used by your assets. If you got 1000 GB of assets, you need 120+2040=2160 GB storage space. 120+40 GB local storage and 2000 GB of local OR network storage.
- Here are two examples from production environments:

| Storage Requirements |            Assets | Preview Versions | SQL DB | Elasticsearch DB | easydb software |
|----------------------|-------------------|------------------|--------|------------------|-----------------|
| Small example        |             60 GB |            20 GB |   1 GB |          0,07 GB |            9 GB |
| Large example        |         15,000 GB |        15,000 GB | 200 GB |           170 GB |           22 GB |
| Rule of thumb        |    100% of assets |   100% of assets | 2% of assets | 2% of assets |         40 GB |

## Filesystem Layout

Assumptions: 1000 GB assets, base directory ("data store") is /srv/easydb

Example "separate only assets":

| storage space  | directory                     | cadidate for ...                             |
|----------------|-------------------------------|----------------------------------------------|
|  160 GB        | /                             | fast storage                                 |
| 2000 GB        | /srv/easydb/eas/lib/assets    | NFS / CIFS                                   |

Example "maximum separation":

| storage space  | directory                     | cadidate for ...                             |
|----------------|-------------------------------|----------------------------------------------|
| 30 GB          | /                             |                                              |
|  1 GB          | /boot                         |                                              |
| 40 GB          | /var/lib/docker               | fast storage (low priority)                  |
| 50 GB          | /srv/easydb/eas/tmp           | fast storage (low priority)                  |
| 20 GB          | /srv/easydb/pgsql/var         | fast storage (high priority)                 |
| 20 GB          | /srv/easydb/elasticsearch/var | fast storage (high priority)                 |
| 2000 GB        | /srv/easydb/eas/lib/assets    | NFS / CIFS                                   |

## Network

The domain name ("URL") of the easydb should be known during installation, so that it can be configured right away. It can be changed later and more addresses can be added later. One domain name is the primary, however, and is used for image URLs. If you use https at all then the primary domain must also have https.

easydb needs a domain or subdomain of its own. Or an IP address.

For example https://media.example.com or http://1.2.3.4 but not https://example.com/media. 

The "/media" part of the URL is called "path". A fixed path is not supported by easydb.

The easydb also communicates with its users via e-mail.

- An SMTP relay is specified in the easydb configuration.
- Also a sender address domain name, which must be accepted by the relay and by the receiving server (thus the domain usually has to be valid on the whole Internet).

&nbsp;


# Connections during installation

Specifically, if we are installing on one of your servers, the following connections should be allowed.

	Instead, you can install yourself; or we install on our servers (hosting contract).

## Connections to the server

For the installation, we need an SSH access to the server.

```
SSH is encrypted, secure and state of the art.
```

 - The account has to have administrative rights directly (root) or via e.g. "sudo bash".
 - Access can be granted by password or - preferred - by our public ssh key: 
   https://www.programmfabrik.de/files/sshkey4096.txt .
 - Optional: The access may be restricted to our IP address (starting point), which we will gladly inform you of.
 - Optional: The port can be configured by the customer. The default is 22.
 - Optional: The access can be secured via a customer operated SSH proxy (also known as Jumphost).
 - Optional: Additionally, a customer operated OpenVPN server can be used.

SSH access which is secured by key or IP address can be permanently accessible without risk ("port open").

 - Our accesses can then be carried out without any timely arrangements, and thus very promptly and effectively.
 - Optional: In addition, the server can be monitored by us (as part of a maintenance contract).

The installation takes several minutes or a few hours in case of complications.

We recommend a few working days before the installation an SSH access through us, whereby we check the access and the prerequisites of the server.

## Connections from the server to the Internet

- During the installation docker.easydb.de is being accessed via HTTPS.
- Also package sources of the Linux distribution (Debian or Ubuntu) are accessed via http and package sources of Docker at download.docker.com via https.
- Optional: Use of an HTTP (S) proxy is possible.
- The same information applies to updates.

----

# Integration

Further integration into your network is quite possible, but this is not treated as part of the installation. We recommend installation as a first step.

Examples for further integration:

- Storage connection via NFS or SMB ("network drive").
- [HTTPS](../konfiguration/https) with your certificate
- LDAP, [SSO](../konfiguration/sso), Active Directory
- Import directories that you can fill with Windows Explorer ("webdav"), network drive ("SMB") or NFS.

---

# Advanced

[Concrete steps of installation](../installation) of easydb 5.

&nbsp;
