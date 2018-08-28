---
title: "Presentation pptx Plugin"
layout: config
menu:
  main:
    name: "Presentation PPTX Plugin"
    identifier: "sysadmin/konfiguration/easydb-server.yml/plugin/presentation-pptx"
    parent: "sysadmin/konfiguration/easydb-server.yml/plugin"
easydb-server.yml:
  - plugins.enable.base.presentation
---
# Presentation PPTX Plugin

## Description {#description}

## View {#view}

![ez5-pptx-editor](https://github.com/programmfabrik/easydb-documentation/content/sysadmin/konfiguration/easydb-server.yml/plugin/ez5-pptx-editor.png)

## Enable presentation-pptx plugin {#presentation-pptx}

easydb-server:
```yaml
plugins:
  enable:
    - base.presentation-pptx
```