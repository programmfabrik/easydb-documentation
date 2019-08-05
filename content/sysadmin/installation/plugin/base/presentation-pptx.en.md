---
title: "Presentation pptx Plugin"
layout: config
menu:
  main:
    name: "Presentation PPTX"
    identifier: "sysadmin/installation/plugin/base/presentation-pptx"
    parent: "sysadmin/installation/plugin/base"
    weight: 12
easydb-server.yml:
  - plugins.enable.base.presentation
---
# Presentation PPTX Plugin

## Description {#description}

## View {#view}

![ez5_pptx_editor](/content/sysadmin/installation/plugin/base/ez5_pptx_editor.jpg)

## Enable presentation-pptx plugin {#presentation-pptx}

easydb-server: 
```yaml
plugins:
  enable:
    - base.presentation-pptx
```