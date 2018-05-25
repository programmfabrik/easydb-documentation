# Custom data type

A custom data type can be used to extends easydb with your own data type. A custom data type can store any data in a JSON-Map. The Input, Output and Search-Mapping of that type can be managed by plugin code.

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

## Search-Mapping

The search mapping for the fields of the custom data type can be defined in the plugin configuration. Under the node `mapping`, the field names and their `type` can be defined:

Types that can be specified are:

- `text`
  - a text field
- `text_oneline`
  - a one line text field
- `text_l10n`
  - a multilanguage text field
- `text_l10n_oneline`
  - a multilanguage, one line text field

```yaml
custom_types:
  link:
    mapping:
      url:
        type: text_oneline
      text_plain:
        type: text
      tld:
        type: text
      text:
        type: text_l10n_oneline
```
