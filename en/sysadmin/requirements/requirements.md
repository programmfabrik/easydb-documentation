# Requirements

## Software

Docker at least in version 1.11.

Versions with the newer version scheme (e.g., 17.03) are all recent enough.

The Community Edition (CE) is quite sufficient. We recommend the "stable" channel and assume the default architecture x86_64.

If we are installing the easydb for you then we will also install Docker ourselves. But please make sure that the requirements for Docker are met.

Here is a link to the [installation guide](https://docs.docker.com/engine/installation/linux/debian/#os-requirements) for Docker under e.g. Debian.

### Operating system

The selection of the operating system depends on Docker. Based on this, Debian Server or Ubuntu Server can be used. There are, however, two exceptions:

- If you want Programmfabrik to work on the server (remote installation or maintenance or troubleshooting) then only with a Docker on a Debian server - without a graphical interface, 64 bit, in a version for which there are security updates.

- If you do not want Programmfabrik to take care of the server and want to use Windows as a further requirement, then you need the variant "[Docker for Windows](https://docs.docker.com/docker-for-windows/#step-one-install-docker-for-windows). " The easydb 5 does not work with its alternative "[native Docker](https://msdn.microsoft.com/en-us/virtualization/windowscontainers/quick_start/quick_start_windows_10)", which is also recognizable by it's "docker.exe". We do not make separate tests for "Docker for Windows" or Docker on Mac OSX and have not measured the amount of performance degradation by the [additional virtualization](https://docs.docker.com/v1.11/engine/faq/#does-docker-run on Mac OS x-or-windows).

Are you interested in directly downloading a recommended operating system?

1. Go to [http://cdimage.debian.org/debian-cd/current/amd64/iso-cd](http://cdimage.debian.org/debian-cd/current/amd64/iso-cd )
2. Download the file that starts with `debian-9.` and ends with `-amd64-netinst.iso`.


## Hardware

4 processor cores. (Recommendation, depending on usage more)

16 GB of RAM. (Recommendation, depending on usage more)

Docker may have further requirements, e.g. 64 bit processor cores. These are then mentioned in the Docker Installation Instructions.

space:

- 40 GB space for the Docker files of the easydb. These grow slowly over time, starting from 8 GB.
- 50 GB für temporäre Dateien wie Zwischenergebnisse der Bildumwandlung und Zoomer-Dateien (Lupenfunktion).
- 30 GB for the Operating system and Log messages.
- 1 GB for /boot with accumulating kernel versions. We recommend to not have /boot separately but instead use the root partition.
- 200% of the storage space of the assets you want to manage with easydb. (If you need additional large preview versions, more)
- 4% additional storage space for databases.
- Here are two examples from production environments:

| Storage Requirements |            Assets | Preview Versions | SQL DB | Elasticsearch DB | easydb software |
|----------------------|-------------------|------------------|--------|------------------|-----------------|
| Small example        |             60 GB |            20 GB |   1 GB |          0,07 GB |            9 GB |
| Large example        |         15,000 GB |        15,000 GB | 200 GB |           170 GB |           22 GB |
| Rule of thumb        |    100% of assets |   100% of assets | 2% of assets | 2% of assets |         40 GB |

## Network

The future address ("URL") of the easydb should be known, so that it can be configured during installation. (Can be changed later, several are possible.)

easydb needs a domain or subdomain of its own. Or an IP address. For example https://media.example.com or http://1.2.3.4 but not https://example.com/media. The part of URLs that is called "path", in this example "/media", is not supported.

The easydb also communicates with its users via e-mail.

- An SMTP relay is specified in the easydb configuration.
- Also for the sender address a domain, which is accepted by the relay and which is accepted by the supplying server (thus usually a domain valid on the Internet).

&nbsp;


# Connections during installation

Specifically, if we are installing on one of your servers, the following connections should be allowed.

	Instead, you can install yourself; Or we install on our servers so "host" easydb for you.

## Connect to the server

For the installation, we need an SSH access to the server. Docker does not need to be installed yet.

 - Access must have administrative rights.
 - SSH is encrypted and secure according to the state of the art.
 - Access restriction is by password or by key. We will be pleased to provide you with our public key.
 - Optional: The access may be restricted to our IP address (starting point), which we will gladly inform you.
 - Optional: The port can be configured by the customer; The default is 22.
 - Optional: The access can be secured via SSH proxy (also known as Jumphost) if the customer runs it.

SSH access which is secured by key or IP address can be permanently accessible without risk ("port open").

 - Our accesses can then be carried out without any timely arrangements, and thus very promptly and effectively.
 - Optional: In addition, the server can be monitored by us (as part of a maintenance contract).

The installation takes several minutes or a few hours in case of complications.

We recommend a few working days before the installation an SSH access through us, whereby we check the access and the prerequisites of the server.

## Connections from the server to the Internet

- During the installation, accesses from the server take place at docker.easydb.de, on TCP port 5000, via HTTPS.
- Also accesses to package sources of the Linux distribution (Debian or Ubuntu) and package sources of Docker (e.g. apt.dockerproject.org), via https and http.

- Optional: Use of an HTTP (S) proxy is possible.
- Optional: Access via ftp can be avoided by selecting the appropriate source of the package.

- The same information applies to updates.

----

# Integration

Further integration into your network is quite possible, but this is not treated as part of the installation. We recommend installation as a first step.

Examples for further integration:

- Storage connection via NFS or SMB ("network drive").
- [HTTPS](../konfiguration/https/https.html) with your certificate
- LDAP, [SSO](../konfiguration/sso/sso.html), Active Directory
- Import directories that you can fill with Windows Explorer ("webdav"), network drive ("SMB") or NFS.

---

# Advanced

[Concrete steps of installation](../installation/installation.html) of easydb 5.

&nbsp;
