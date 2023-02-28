---
title: "Presentation-pptx"
menu:
  main:
    name: "Presentation-pptx"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/presentation-pptx"
    weight: -950
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
easydb-server.yml:
  - plugins.enable.base.presentation
---
# Presentation PPTX Plugin

## Description {#description}

## View {#view}

![ez5 pptx editor](ez5_pptx_editor.png)

## Enable easydb-presentation-pptx-plugin {#presentation-pptx}

```yaml
plugins:
  enabled+:
    - base.presentation-pptx
```