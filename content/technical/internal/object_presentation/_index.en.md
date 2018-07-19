---
title: "98 - object"
menu:
  main:
    name: "object"
    identifier: "technical/internal/object_presentation"
    parent: "technical/internal"
---
# Object Presentation


## Table of Usage

* for linked objects, *Style* is determined in the Mask
* for search results, *Style* is determined by the Result Mode

|Style     |Hierarchy|Assets|Editor (LO)|Detail (LO)|Search Result |Hierarchy Path |Autocompletion|Bulk Editor|
|----------|---------|------|-----------|-----------|--------------|---------------|--------------|-----------|
| standard |         |      |cs2+Tag    |cs3+Tag    |st+tag        |cs2**          |cs2+Tag+H     |cs2+Tag    |
| short    |         |      |cs1+Tag    |s1+list    |-             |-              |cs1+H         |-          |
| text     |         |      |t+TAG      |t+TAG      |t+TAG         |cs2**          |cs2+Tag+H     |-          |
| list     |         |      |-          |-          |cs3+Tag       |-              |-             |-          |
| standard |         |  x   |cs2+a+Tag  |cs3+a+Tag  |st+tag        |cs2+a**        |cs2+a+Tag+H   |cs2+a+Tag  |
| short    |         |  x   |cs1+a+Tag  |s1+a       |-             |-              |cs1+a+Tag+H   |-          |
| text     |         |  x   |t+a+TAG    |t+a+TAG    |t+a+TAG       |cs2+a**        |cs2+Tag+H     |-          |
| list     |         |  x   |-          |-          |cs3+a+Tag     |-              |-             |-          |
| standard |   x     |      |cs2+p+Tag  |cs3+p+Tag  |st+tag        |-              |cs2+p+Tag+H   |cs2+p+Tag  |
| short    |   x     |      |cs1+p+Tag  |s1+p       |-             |-              |cs1+p+Tag+H   |-          |
| text     |   x     |      |t+p+TAG    |t+p+TAG    |t+p+TAG       |-              |cs1+p+Tag+H   |-          |
| list     |   x     |      |-          |-          |cs3+Tag       |-              |-             |-          |
| standard |   x     |  x   |cs2+a+p+Tag|cs3+a+p+Tag|st+tag        |-              |cs2+a+p+Tag+H |cs2+p+a+Tag|
| short    |   x     |  x   |cs1+a+p+Tag|s1+a+p     |-             |-              |cs2+a+p+Tag+H |-          |
| text     |   x     |  x   |t+a+p+TAG  |t+a+p+TAG  |t+a+p+TAG     |-              |cs2+a+p+Tag+H |-          |
| list     |   x     |  x   |-          |-          |cs3+a+Tag     |-              |-             |-          |

**LO**: Linked Object
**-** Not Applicable
**(l)** show as inline list

**\*** path shown only in non ResultList views
**\*\*** hierarchy path is shown in separate markup, connecting full cs2-card markups


## Description of Presentation Modes


### s1

*no path, no asset, standard 1*

The short output is shown with no asset and no path. Only Standard 1 is shown.

### s1+a

*no path, asset, standard 1*

Like **s1** but with the asset show very small left to the standard 1 text.

### s1+p

*path, no asset, standard 1*

Like **s1**. The path is integrated in the output.

### s1+a+p

*path, asset, standard 1*

Like **s1+a** but with the asset show very small left to the standard 1 text, last element.

### cs1

*no path, no asset, standard 1+2*

The card is shown with no asset and no path. Only Standard 1 is shown.

### cs2

*no path, no asset, standard 1+2*

The card is shown with no asset and no path. Only Standard 1+2 are shown. The height of this card is determined by the maximum available Standard field.

### cs3

*no path, no asset, standard 1+2+3*

The card is shown with no asset and no path. Standard 1+2+3 are shown. Standard 3 can be long, so this card can be very high. The height of this card is determined by the maximum available Standard field.


### cs1|2|3+a

*no path, asset, standard 1[+2[+3]]*

Like **cs2|3** but with a small asset shown to the left of the standard texts.

### cs1|2|3+p

*path, no asset, standard 1[+2[+3]]*

Like **cs1|2|3** but with the path shown above, path is rendered like *cs1*.

### cs1|2|3+p+a

*path, asset, standard 1[+2[+3]]*

Like **cs1|2|3+a** but with the path shown above, path is rendered like *cs1+a*.

## st

*no path, asset, standard 1,2,3, objecttype, pool-path*

Standard Result includes all standard output, asset-browser, objecttype, and pool-path. asset-browser holds a placeholder if mask has no assets.


### t

*no path, no asset, all text fields*

This is the key/value table. Its huge an bulky, so use with care!

### t+p

*path, no asset, all text fields*

This is the key/value table. Its huge an bulky, so use with care! The path
is shown inside the table as key.

### t+p+a

*path, asset, all text fields*

This is the key/value table. Its huge an bulky, so use with care! The path
is shown inside the table as key. The asset is also shown.

### t+a

*no path, asset, all text fields*

This is the key/value table. Its huge an bulky, so use with care! The asset is shown.


## Modifier

### +H

Use the highlight version of the output, that version does not use any design formatting within a standard representation.

### +TAG

Full Tag representation (Icon+Text)

### +Tag

Tag representation (Text)

### +tag

Tag representation (Icon)

### +list

Show as inline list.
