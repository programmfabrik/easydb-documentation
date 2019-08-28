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

![ez5 pptx editor](/sysadmin/installation/plugin/base/presentation-pptx/ez5_pptx_editor.png)

## Enable presentation-pptx plugin {#presentation-pptx}

easydb-server: 
```yaml
plugins:
  enable:
    - base.presentation-pptx
```
