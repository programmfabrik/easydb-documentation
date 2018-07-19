---
title: "146 - Watermark"
menu:
  main:
    name: "Watermark"
    identifier: "technical/types/watermark"
    parent: "technical/types"
---
# Watermark

A watermark can be attached to a pool. It is defined by an image and some properties.

## Attributes

|   |   |
|---|---|
| `image`              | Watermark image ([Asset](/en/technical/types/asset), rw) |
| `dissolve`           | Dissolve factor (integer in the range [0-100], rw) |
| `gravity`            | Watermark position (string, rw): one of **n, e, s, w, ne, nw, se, sw, c** |
| `size`               | Watermark size (string, rw): see below |
| `tile`               | Tile (boolean, rw) |

The `size` parameter is given as `<widtdh>x<height>`. The width and the height can be either pixels (integer)
or a scale factor (integer+ "%").

## Related operations

- [/pool](/en/technical/api/pool): read / set the watermark associated with a pool

