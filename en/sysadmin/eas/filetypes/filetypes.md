Supported datatypes {# supported-datatypes .top}
=======================

The EAS can take <b> all </b> file types, but it supports
Thumbnails/Previews and metadata for the following formats:

IMAGE
=====

Pictures are well supported. Basic support is provided by
[ImageMagick](http://imagemagick.org/), for comments
To individual formats, the[List of supported
Formats](http://imagemagick.org/script/formats.php).
In the EAS, however, the format must also be known in order to display the image (IMAGE)
To be recognized.

Support for raw formats (including **cr2**, **crw**,
**nef** , **orf**, **raw** and partial **tiff**) is of
[Dcraw](http://www.cybercom.net/~dcoffin/dcraw/).

Vector formats are processed very rudimentarily in this class. To
Count **ai** and **eps**. More vector graphic formats are currently available
unsupported.

If the support is not good (**+++**), then there is either
Single problem files (**++**) or there is still general for the format
Minor, known problems (**+**).

  Extension   Scope of support
  ----------- ------------------------
  ai          +
  bmp         +++
  cr2         +
  eps         +
  gif         +++
  jp2         ++
  jpeg, jpg   +++
  nef         +
  orf         +
  png         +++
  psd         ++
  raw         +
  tif, tiff   ++

VIDEO
=====

Videos are processed by[ffmpeg](http://ffmpeg.org/). there
Can preview (IMAGE) or re-video in other formats and sizes
to be created.

For the representation in the browser is usually from the video a
FLV version that is played in the built-in video player
can.

The following list contains the supported container formats. These
Can return the user data in different audio and video codecs
contain. Here, all the codecs of the installed ffmpeg version
supported. A clue is provided by the ffmpeg documentation for
[Audio](http://ffmpeg.org/general.html\#Audio-Codecs)
And [Video](http://ffmpeg.org/general.html#Video-Codecs) Codecs, below
The tested audio and video codecs are listed.

Supported container formats
------------------------------

  Extension               Description
  ----------------------- ------------
  avi                     AVI
  flv                     Flash Video
  mp4                     ISO MPEG4
  mov                     QuickTime Video
  mpg, mpeg, mpv, ts, vdr MPEG 1/2 PS/TS
  ogg, ogv                Ogg
  rm, rv                  Real Media

Tested Video and Audio Codecs
---------------------------------

  Audio/Video   Description
  ----------- ------------
  V           FLV
  V           H.264
  V           MPEG 1
  V           MPEG 2
  V           MPEG 4
  V           Ogg Theora
  V           WMV1
  V           WMV3
  A           AAC
  A           AC3
  A           ADPCM
  A           MPEG Layer 2
  A           MPEG Layer 3
  A           Ogg Vorbis
  A           WMAv2
  A           WMA Voice

AUDIO
=====

The handling of audio files is very similar to that of videos. Also
An FLV version is usually generated for display in the browser.
Due to a limitation in the format, however, it is currently not possible to use the
Integrated video player within these FLVs certain times
to jump.

Currently, the following formats are supported:


  Extension   Description
  ----------- ------------
  flac        Free Lossless Audio Codec
  mp3         MPEG Layer 3
  ogg         Ogg Vorbis
  wav         RIFF WAVE
  wma         Windows Media Audio

Since these are usually container formats,
Individual case also come to that they are unsupported audio codecs
contain.

OFFICE
======

Most office formats are processed by
[OpenOffice.org](http://openoffice.org/). Minimum requirement
Version 3.0, newer versions can be improved in individual cases
Results during processing.

Word processing formats
------------------------

  Extension   Description
  ----------- ------------
  doc         MS Word
  docx        MS Word 2003*
  odt         OOo 2.x* Writer
  ott         OOo 2.x+ Writer
  rtf         Rich Text Format
  sxw         OOo 1.x Writer

Spreadsheet formats
---------------------------

  Extension   Description
  ----------- ------------
  ods         OOo 2.x+ Calc
  ots         OOo 2.x+ Calc
  sxc         OOo 1.x Calc
  xls         MS Excel
  xlsx         MS Excel 2003+

Presentation Formats
--------------------

  Extension   Description
  ----------- ------------
  odp         OOo 2.x+ Impress
  otp         OOo 2.x+ Impress
  ppt         MS PowerPoint
  pptx         MS PowerPoint 2003+
  sxi         OOo 1.x Impress

Other Formats
----------------

  Extension   Description
  ----------- ------------
  odf         OOo 2.x+ Formula
  otf         OOo 2.x+ Formula

Formats that are not processed by OpenOffice.org
----------------------------------------------------------

 Extension Description
 --------- ------------
 pdf       Portable Document Format
 txt       Plain Text

VECTOR2D
========

Support for Vector2D is still at the very beginning and beyond
Easydb first time in **(version) version 4.0.xx\* accessible.


  Extension   Description
  ----------- ----------------------------------------------------------------------
  dwg       [AutoCAD-Zeichnung](https://de.wikipedia.org/wiki/AutoCAD#DWG)
  dxf       [AutoCAD-Austauschformat](https://de.wikipedia.org/wiki/AutoCAD#DXF)

VECTOR3D
========

Support for Vector3D is still at the beginning and beyond
Easydb first time in **version 4.0.259** accessible.

  Extension   Description
  ----------- -------------------------------------------------------------------------
  stl       [StereoLithography](http://en.wikipedia.org/wiki/STL_%28file_format%29)


