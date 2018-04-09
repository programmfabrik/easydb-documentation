# Supported datatypes {#supported-datatypes.top}

The EAS can take <b> all </b> file types, but it supports thumbnails/previews and metadata for the following formats:

## IMAGE

Pictures are well supported. Basic support is provided by [ImageMagick](http://imagemagick.org/), for comments to individual formats, the [List of supported Formats](http://imagemagick.org/script/formats.php). In the EAS, however, the format must also be known in order to display the image (IMAGE) to be recognized.

Support for raw formats (including **cr2**, **crw**, **nef**, **orf**, **raw** and partial **tiff**) is of [Dcraw](./http://www.cybercom.net/~dcoffin/dcraw/dcraw.html).

Vector formats are processed very rudimentarily in this class. To count **ai** and **eps**. More vector graphic formats are currently available unsupported.

If the support is not good (**+++**), then there is either single problem files (**++**) or here is still general for the format minor, known problems (**+**).

|Extension|Scope of support|
|--|--|
|ai|+|
|bmp|+++|
|crw|+|
|cr2|+|
|eps|+|
|gif|+++|
|jpeg, jpg|+++|
|jp2|++|
|nef|+|
|orf|+|
|png|+++|
|ppm|+|
|psd|++|
|raw|+|
|tif, tiff|++|
|wmf|+ |

## VIDEO

Videos are processed by[ffmpeg](http://ffmpeg.org/). there can preview (IMAGE) or re-video in other formats and sizes to be created.

For the representation in the browser is usually from the video a FLV version that is played in the built-in video player can.

The following list contains the supported container formats. These can return the user data in different audio and video codecs contain. Here, all the codecs of the installed ffmpeg version supported. A clue is provided by the ffmpeg documentation for [Audio](http://ffmpeg.org/general.html#Audio-Codecs) and [Video](http://ffmpeg.org/general.html#Video-Codecs) Codecs, below the tested audio and video codecs are listed.

## Supported container formats

|Extension|Description|
|--|--|
|avi|AVI|
|flv|Flash Video|
|mov|QuickTime Video|
|mpg, mpeg|MPEG 1/2 PS/TS|
|mp4|ISO MPEG4|
|ogg, ogv|Multimedia-Dateien|
|rm |Real Media|
|ts|MEPG-2 (.MPEG) video compression |
|wmv|Windows Media Video|



## Tested Video and Audio Codecs

|Video(V) / Audio(A)|Description|
|--|--|
|V|           FLV|
|V|           H.264|
|V|           MPEG 1|
|V|           MPEG 2|
|V|           MPEG 4|
|V|           Ogg Theora|
|V|           WMV1|
|V|           WMV3|
|A|           AAC|
|A|           AC3|
|A|           ADPCM|
|A|           MPEG Layer 2|
|A|          MPEG Layer 3|
|A|           Ogg Vorbis|
|A|           WMAv2|
|A|           WMA Voice|


## AUDIO

The handling of audio files is very similar to that of videos. Also an FLV version is usually generated for display in the browser. Due to a limitation in the format, however, it is currently not possible to use the integrated video player within these FLVs certain times to jump.

Currently, the following formats are supported:


|  Extension   |Description|
|  ----------- |------------|
|  flac        |Free Lossless Audio Codec|
|  mp3         |MPEG Layer 3|
|  ogg         |Ogg Vorbis|
|  wav         |RIFF WAVE|
|  wma         |Windows Media Audio|

Since these are usually container formats, individual case also come to that they are unsupported audio codecs contain.

## OFFICE

Most office formats are processed by [OpenOffice.org](http://openoffice.org/).

### Word processing formats

|Extension|Description|
|--|--|
|doc    |     MS Word|
|docx   |     MS Word 2003*|
|odt    |     OOo 2.x* Writer|
|ott    |     OOo 2.x+ Writer|
|rtf    |     Rich Text Format|
|sxw    |     OOo 1.x Writer|


### Spreadsheet formats

|  Extension   |Description|
|  ----------- |------------|
|  ods         |OOo 2.x+ Calc|
|  ots         |OOo 2.x+ Calc|
|  sxc         |OOo 1.x Calc|
|  xls         |MS Excel |
|  xlsx        | MS Excel 2003+|

### Presentation Formats

|  Extension   |Description|
|--|--|
|ods    |     OOo 2.x+ Calc|
|ots    |     OOo 2.x+ Calc|
|sxc    |     OOo 1.x Calc|
|xls    |     MS Excel|
|xlsx   |      MS Excel 2003+|

### Other Formats

|Extension|Description|
|--|--|
|odf    |     OOo 2.x+ Formula|
|otf      |   OOo 2.x+ Formula|

### Formats that are not processed by OpenOffice.org

 |Extension |Description|
|--|--|
|pdf   |    Portable Document Format|
|txt    |   Plain Text

## 3D FORMATE

|Extension|Description|
|--|--|
|kmz| Keyhole Markup Language |
|ply| Polygon File Format |
|stl|ASCII, binary Format |
|3ds|Autodesk 3ds Max |

> NOTE: currently no support for previews.

## ARCHIVE

|Extension|Description|
|--|--|
|zip|file compression |
|webdvd.zip|file compression for WebDVD |

> NOTE: no support for previews.

## OTHER

By activating the checkbox for "other" data formats, all other file types that are not listed in the selection above are also allowed for uploading to easydb.

> NOTE: no support for previews.

