---
title: "Barcode"
menu:
  main:
    name: "Barcode"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/barcode"
    weight: -940
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
---

# Barcode Plugin

This [plugin](https://github.com/programmfabrik/easydb-barcode-display) is a [custom mask splitter](/en/technical/plugins/reference/webfrontend/#masksplitter-plugins-registerplugin). 

It can be used to render different types of barcodes. 
The library used to generate the barcode is [JsBarcode](https://lindell.me/JsBarcode/), therefore all supported barcodes will depend on which ones the library supports.

The barcode represents a value of an available field in the mask. The type of the field needs to be **text** (not multilingual)

## Instalation
The easydb barcode plugin is a webfrontend plugin. To enable it:

In e.g. `/srv/easydb/config/easydb-server.yml`: (assuming `/srv/easydb` is your [base directory](../../../installation/#mount))

```yaml
plugins:
  enabled+:
    - base.barcode-display
    - base.barcode-display-pdf
    - base.pdf-creator
```

The easydb-server has to be restarted to make the change effective.

## Usage

Since it's a custom mask splitter, it's necessary to add it as a splitter in a mask, and then open its mask splitter options to configure which field will be used. It's also possible to change two other options: **Type** and **Barcode type**.

The default option for **Type** is **Barcode**, and when that option is selected, it's possible to change the **Barcode Type** to CODE128, CODE39, or [other](https://github.com/lindell/JsBarcode/wiki#barcodes). 

The other **Type** is **QR**, which basically generates a QR code instead of a Barcode.

## Pdf creator extension

It has an extension so it can be used in the pdf-creator

- https://github.com/programmfabrik/easydb-barcode-display-pdf
