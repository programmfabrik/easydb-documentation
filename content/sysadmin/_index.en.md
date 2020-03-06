---
title: "54 - System Administration"
menu:
  main:
    name: "System Administration"
    identifier: "sysadmin"
    weight: -950
---
# System Administration

In this section, we document administrative interventions outside the Web interface.


* [Prerequisites](requirements)
* [Install](installation)
* [Configuration](konfiguration)
* [Operation](operations)
* [Migration](migration)
* [Instantiation](installation/instances) (multiple easydbs on the same server)

&nbsp;

### Explanation of Terms

In case of doubt, "Systemadministration" refers to this chapter and ["Administration"](../webfrontend/administration) refers to interventions using the web interface.

&nbsp;

# Docker Integration
![Docker Integration](easydb5_docker_architecture_en.png)

* Docker: 1 large **light gray** box with dotted line
* Docker container: 5 **gray** boxes
* Services: **white**  rectangles
* Memory used in docker: **green**
* Ports: **yellow**
* Show optional ports to the network outside the server: **Spotted** (top)
* Optional web server for e.g. HTTPS or Single Sign-On: **light blue** it rectangle (top)

&nbsp;

### Further
For example, The tasks of the individual components, see: [Technical documentation](../technical).

&nbsp;
