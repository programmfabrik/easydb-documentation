---
title: "Developement"
menu:
  main:
    name: "Developement"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/developement"
    weight: -1000
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
---
# Plugin developement enviroment setup

## Enviroment setup

Before we can start developing a plugin, we have to adapt our development environment accordingly.

### Server installation

To install and configure an easydb5 instance, refer to the [Installation](/en/sysadmin/installation) and [Configuration Guide](/en/sysadmin/configuration/easydb-server.yml).

Since we now want to make more plugins known to the server, we first have to map another volume where the server can find the plugins. In this example we use `/home/<name>/easydb5/custom-plugins` as the place where we will develop our plugins. 

As I mentioned before, we need to provide the server with a new volume. To do this now, we need to modify the `run-server.sh` file that was created during [installation](/en/sysadmin/installation). The highlighted lines in the following snippet have been added.

```bash {hl_lines=["11"]}
BASEDIR=/srv/easydb
SOLUTION=base
docker run -d -ti \
    --name easydb-server \
    --net easydb5 \
    --security-opt seccomp=unconfined \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/easydb-server/var:/easydb-5/var \
    --volume=$BASEDIR/easydb-server/nginx-log:/var/log/nginx \
    --volume=/home/<name>/custom-plugins:/custom-plugins \
    docker.easydb.de/pf/server-$SOLUTION
```

### Installing the dependencies

Since the webfrontend of easydb5 is mainly written in coffeescript, we have to install the coffeescript compiler.

```bash
sudo npm install -g coffeescript@1.12.7
```

To be able to use `sass` as well, we will install `sass` next. We recommend the NPM version, otherwise errors may occur.

```bash
sudo npm install -g sass
```

### Development of a new plugin

Since this guide does not cover the actual development of a plugin, we will now consider the [easydb-plugin-example](https://github.com/programmfabrik/easydb-plugin-examples) as our already developed plugin. 

Since we chose `/home/<name>/easydb5/custom-plugins` as our location for our plugins above, we will clone the plugin into that folder:

```bash
cd /home/<name>/easydb5/custom-plugins
git clone git@github.com:programmfabrik/easydb-plugin-examples.git
```

Since our example plugin has a submodule, we also have to initialize it:
```bash
cd easydb-plugin-examples
git submodule update --init --recursive
```

Now we can finally "build" our plugin:
```bash
make
```

If your plugin has now been successfully built, we still have to make the plugin known to the server. For this we create another `.yml` file in the folder `/home/<name>/easydb5/custom-plugins`. In this example we will name this file `custom-plugins.yml`. 

This file now has the following content:

```yaml {hl_lines=[2]}
base:
  plugins+:
    - name: example-plugin
      file: /home/<name>/easydb5/custom-plugins/easydb-plugin-examples/example-plugin.config.yml

plugins:
  enabled+:
    - base.example-plugin
```

**WARNING** if you remove the `+` at ***plugins*** in line 2 (is marked), your easydb will no longer start because you overwrite the list of plugins.

Now that we have a file that takes care of our own creations, we have to make it known to the server. To actually realize this, there are two possibilities:

Solution 1:

You enter the following lines in the `easydb-server.yml`

```yaml
include_before:
  - /custom-plugins/custom-plugins.yml
```

Solution 2:

You copy the `custom-plugins.yml` to the `easydb-server.d` directory, which is on the same level as the `easydb-server.yml` whose path was defined during [Installation](/en/sysadmin/installation).