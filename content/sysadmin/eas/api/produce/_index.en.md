---
title: "20 - /produce"
menu:
  main:
    name: "/produce"
    identifier: "sysadmin/eas/api/produce"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /produce

##  Example

```url
http://eas.example.com/eas/produce/123?instance=example&target_format=jpg&target_size=1024x1024
```


##  Parameter


|key|value|
|---|---|
|`instance`| Instance name (required) |
|`version`| Name of the target version (necessary) |
|`custom`| additional data to be managed by EAS |
|`priority`| Priority of the task, default: `0`, higher is more important (version 4.1.1) |
|`rebuild`|`1`: rebuild the version if it already exists |
|`new_original`|`1`: the version becomes a new derived asset |
|`no_link_to_orig`|`1`: in conjunction with `new_original` the version becomes a new original without reference to the source (version 4.2.37) |
|`thumbnailsize`| if set, a thumbnail version of this size is created (for example `128x128`) |
| -------------------- | ---------------------------------------------------- |
|`target_format`| File format of the version |
|`target_size`| Size (e.g. `128`, `640x480`, `x12` or `45x`) |
|`target_extent`| Target size independent of input data. The image is centered inside the given extent. If the image should be resized and cropped to this extent, combine `target_extent` with `target_size` and `target_size_min`. (version 4.2.94) |
|`target_page`| a page is to be extracted (counting starts at `0`) |
|`target_extractdpi`| When converting Office documents to images, this DPI number should be used (default:`300`) |
|`target_metadata`| JSON list of rows for Exiftool for writing metadata (see option `-` from Exiftool) |
|`target_rotate`| Angle of rotation in degrees |
|`target_mirror`| Mirroring at the specified axis (`x` or `y`) |
|`target_crop`| Cut out an image area ( `<w>x<h>+<x>+<y>`, for example `400x300+100+30` ) |
|`target_size_force`|`1`: Force size (ignore aspect ratio) |
|`target_size_limit`|`1`: Do not create version if the original size is smaller than the requested size |
|`target_size_min`|`1`: Specified size is desired minimum and not maximum size (version 4.2.47) |
|`target_no_enlarge`|`1`: Do not enlarge if the original size is smaller than the requested size (version 4.2.34) |
|`target_no_fallback`|`1`: for `audio` source class, disable the placeholder icon if no cover image is found in metadata; for `unknown` source class disable the rendering of filename into image. For other source classes this option has no effect. Only applies if target class is `image`. The requested version fails, if no fallback image is rendered. |
|`target_dpi`| DPI setting for the output file (does not affect the size) |
|`target_wm_image`| Watermark image to be included in the version (specified with absolute path, which is readable for www-data). |
|`target_wm_dissolve`| Watermark transparency (from `0`- invisible - up to `100`- covering - the default is `50`) |
|`target_wm_gravity`| Aligning the watermark (direction of the sky), an option from: `c` (default), `n`, `e`, `s`, `w`, `ne`, `nw`, `se`, `sw` |
|`target_wm_size`|`100x100` or `50%x50%` (default: `100%x100%`) |
|`target_wm_tile`|`1`: Watermark is tiled. `target_wm_gravity` is not taken into account in this case. (version 4.2.36) |
|`target_colorspace`| Color space, tested with `rgb`, `cmyk` and `gray`|
|`target_numcolors`| Number of colors, possible values: `2` .. `256` , `32k` , `64k` , `16m`. The color depth is correspondingly adjusted to 8, 15, 16 and 32 bits, respectively. (version 4.1.1) |
|`target_alpha`| Transparency settings, an option from `on`, `off`, `set` or `opaque` (default `off`; see also [ImageMagick documentation](http://www.imagemagick.org/script/command-line-options.php#alpha)) |
|`target_profile`| File name of a color profile file for `convert` . If only a file name is specified without a path, the profile file is searched (starting from version 4.1.1) in the `eas/data` directory of the EAS |
|`target_quality`| Quality of the output file from `0` to `100` (depending on the output format) |
|`target_compress`| Compression method for output file (depending on format, for example `lzw`) |
|`target_strip`|`1`: remove all metadata |
|`target_no_rgb`|`1`: no automatic conversion to RGB |
|`target_no_autorot`|`1`: no automatic rotation/mirroring using EXIF tags |
|`target_zoomer`|`1`: Preparing the version for the zoomer ( `target_format` must be `jpg` ) |
|`target_duration`| Number of seconds from beginning to be calculated for a video version. If not set, the complete video will be converted. (version 4.2.32) |
|`target_audio_bitrate`| Audio bit rate for video and audio files, e.g. `160k` (version 4.2.49) |
|`target_audio_bitrate`| Video bit rate for video, e.g. `800k` (version 4.2.49) |
| -------------------- | ---------------------------------------------------- |
|`target_commandfile`| Command file for automator requests |
|`target_fail_on_error`|`1`: If the addition of individual assets fails, the processing of the command file is aborted (for `target_commandfile`, version 4.2.33) |

##  Sequence

Transformations are performed in the following order:



* `target_crop`
* `target_size`
* `target_mirror`
* `target_rotate`
