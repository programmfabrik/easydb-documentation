# System Administration

In this section, we document administrative interventions outside the Web interface.


* [Prerequisites](./requirements/requirements.html)
* [Install](./installation/installation.html)
* [Configuration](./configuration/configuration.html)
* [Operation](./plant/plant.html)
* [Migration](./migration/migration.html)
* [Instantiation](./instances/instances.html) (multiple easydbs on the same server)

&nbsp;

### Explanation of Terms

In case of doubt, "Systemadministration" refers to this capital and ["Administration"](../webfrontend/administration/administration.html) refers to interventions using the web interface.

&nbsp;

# Docker Integration
![Docker Integration](../sysadmin/easydb5_docker_architecture.png)

* Docker: 1 large **light gray** box with dotted line
* Docker container: 5 **gray** boxes
* Services: **white**  rectangles
* Memory used in docker: **green**
* Ports: **yellow**
* Show optional ports to the network outside the server: **Spotted** (top)
* Optional web server for e.g. HTTPS or Single Sign-On: **light blue** it rectangle (top)

&nbsp;

### Further
For example, The tasks of the individual components, see: [Technical documentation](../technical/technical.html).

&nbsp;