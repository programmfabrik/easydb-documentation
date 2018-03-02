# Custom data type

A custom data type can be used to extends easydb with you own data type. A custom data type can store any data in a JSON-map. The Input, Output and Search of that type can be managed by plugin code.

An example for a custom data type is [Web link](https://github.com/programmfabrik/easydb-custom-data-type-link) or the [Remote Plugin](https://github.com/programmfabrik/easydb-remote-plugin) both provided by Programmfabrik and made open source on Github.




```yaml

_fulltext:
  string:
  text:
  l10ntext:
    de-DE:
    en-US:



custom_types:
  link:
    config:
      schema:
        - name: title
          parameters:
            type:
              type: select
              options: ["none", "text", "text-l10n"]
        - name: add_timestamp
          parameters:
            value:
              type: bool
      mask:
        - name: editor_style
          parameters:
            value:
              type: select
              options: ["inline",  "popover"]
```
