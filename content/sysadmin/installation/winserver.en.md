---
title: "40 - Installation under Windows Server"
menu:
  main:
    name: "Installation under Windows Server"
    identifier: "sysadmin/installation/winserver"
    parent: "sysadmin"
    weight: -999
---

This page is about a installation of a simplified easydb 5, under Windows Server 2019, which can store up to about 500 Gibibyte of uploads.

This installation method hides all Linux technology from you inside a prepared VM. If you have Linux knowledge, we advise you to instead use another installation method, as these allow to change the easydb later: Disk size, authentication mechanisms, etc..
* For Debian or Ubuntu Linux see [here](../).
* For RedHat Linux see [here](redhat).

# Requirements

- Windows Server 2019 (we tested these instructions with a fresh install)

- DHCP server, reachable by the below created VM. The VM automatically does client-side DHCP at startup. The DHCP server can be created with tools included in Windows Server 2019. For an example on how to do this, see further below: [DHCP-Server](#dhcp-server).

- A powershell with administrative Access. In this example we use the account "Administrator" and the current working directory is `C:\Users\Administrator` during the following commands.

- The download password and the frontend password from us.

More general requirements for hardware, like disk size: [prerequisites](../../requirements/#hardware) - but that page assumes a Linux installation.

# Installation

Commands to download (8,5 GB) and start the VM:

```
$secpasswd = ConvertTo-SecureString "download_password" -AsPlainText -Force
```

```
$cred = New-Object System.Management.Automation.PSCredential ("partner", $secpasswd)

Start-BitsTransfer -Source "https://download.easydb.de/easydb.vhdx.zip" -Destination "easydb.vhdx.zip" -Credential $cred -Authentication Basic

[void][System.Reflection.Assembly]::LoadWithPartialName("System.IO.compression.filesystem")

[System.IO.Compression.ZipFile]::ExtractToDirectory("easydb.vhdx.zip",".")

Install-WindowsFeature -Name Hyper-V -IncludeAllSubFeature -IncludeManagementTools -Restart

New-VM -Name easydb -MemoryStartupBytes 16GB -VHDPath C:\Users\Administrator\easydb.vhdx
```

Make the VM able to reach a DHCP server before the next command

```
Start-VM -VMName easydb
```

Make port 80 reachable for browsers. With our DHCP-example, a supported browser ( https://docs.easydb.de/en/#web-browser ), e.g. Chrome on the Windows Server itself would already be able to surf to the easydb, at http://10.3.1.2.

# Initial login

Log into the easydb webfrontend with login name `root` and the frontend password you need from us. The easydb should be ready for this in less than two minutes after starting the VM.

We strongly recommend that you change your password immediately after you have logged in.

---

# DHCP-Server

Here the promised example on how to make the VM reach an DHCP server - a local one, in this case:

During our testing we created a virtual switch of type `Internal`, in the "Hyper V Manager". We then added to the Windows Server the static IP `10.3.1.1`(netmask `255.255.0.0`), pointing at this new virtual switch. The feature "DHCP server" was then added to this Windows Server and bound to only listen at `10.3.1.1`. The DHCP server serves the IP `10.3.1.2` as a lease and informs clients that `10.3.1.1` is the Router IP and some DNS Server IP. The VM was connected to the virtual switch - all just before the `Start-VM` command.

---

# more optional remarks:

- To automatically download nightly updates for Debian Linux inside the VM and easydb: make the VM able to reach the Internet. (During our testing we used `New-NetNAT -Name “NATNetwork” -InternalIPInterfaceAddressPrefix 10.3.0.0/16`.) It will reach for several sources via http and https.
- The VM uses the account "partnertest" to download easydb updates. This will probably be disabled at some point in the future.

- If the IP address assigned via DHCP has a DNS name associated with it (a DNS reverse lookup is done), then the URL of the easydb is not configured as http://IP-ADDRESS but as https://DNS-NAME - note the "s" in https. To make this URL work correctly you have to put a reverse proxy in front of the easydb, which has a valid https-certificate matching that DNS name.

- The IP ranges `172.17.0.0/16` and `172.18.0.0/16` are already used inside the VM, so avoid using those.

- The vhdx file will be 19 GB big after unpacking and may grow up to about one terabyte (there are about 910 GibiBytes free inside linux, so roughly you can upload 500 GB of files into the easydb before filesystem has to be increased).

- The VM has a SSH server running at port 22. Login is allowed for user1 with the "linux password for user1" which you can get from us. It is not needed to get this easydb running. If you have linux knwoledge we recommend to use a linux installation instead, entirely.

