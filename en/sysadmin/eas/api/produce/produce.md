#  EAS-API: /produce

##  Example

~~~
 http://eas.example.com/eas/produce/123?instance=example&target_format=jpg&target_size=1024x1024
~~~


##  Parameter


|---|---|
|`Instance`| Instance name (required) |
|`Version`| Name of the target version (necessary) |
|`Custom`| additional data to be managed by EAS |
|`Priority`| Priority of the task, default: `0`, higher is more important (from 4.1.1) |
|`Rebuild`|`1`: rebuild the version if it already exists |
|`New_original`|`1`: the version becomes a new derived asset |
|`No_link_to_orig`|`1`: in conjunction with `new_original` the version becomes a new original without reference to the source (from 4.2.37) |
|`Thumbnailsize`| if set, a thumbnail version of this size is created (for example `128x128`) |
| -------------------- | ---------------------------------------------------- |
|`Target_format`| File format of the version |
|`Target_size`| Size (e.g. `128`, `640x480`, `x12` or `45x`) |
|`Target_page`| a page is to be extracted (counting starts at `0`) |
|`Target_extractdpi`| When converting Office documents to images, this DPI number should be used (default:`300`) |
|`Target_metadata`| JSON list of rows for Exiftool for writing metadata (see option `-` from Exiftool) |
|`Target_rotate`| Angle of rotation in degrees |
|`Target_mirror`| Mirroring at the specified axis ( `x` or `y`) |
|`Target_crop`| Cut out an image area ( `<w> x <h> + <x> + <y>`, for example `400x300 + 100 + 30` ) |
|`Target_size_force`|`1`: Force Size (Disallow Aspect Ratio) |
|`Target_size_limit`|`1`: Do not create version if the original size is smaller than the requested size |
|`Target_size_min`|`1`: Specified size is desired minimum and not maximum size (from *(version) version 4.2.47*) |
|`Target_no_enlarge`|`1`: Do not enlarge if the original size is smaller than the requested size (from *(version) version 4.2.34*) |
|`Target_dpi`| DPI setting for the output file (does not affect the size) |
|`Target_wm_image`| Watermark image to be included in the version (specified with absolute path, which is readable for www-data). |
|`Target_wm_dissolve`| Watermark transparency (from `0`- invisible - up to `100`- covering - the default is `50`) |
|`Target_wm_gravity`| Aligning the watermark (direction of the sky), an option from: `c` (default), `n`, `e`, `s`, `w`, `ne`, `nw`, `se`, `Sw` |
|`Target_wm_size`|`100x100` or `50% x50%` (default: `100% x100%`; |
|`Target_wm_tile`|`1`: Watermark is tiled. `Target_wm_gravity` is not taken into account in this case. (Ab *(version) version 4.2.36*) |
|`Target_colorspace`| Color space, tested with `rgb`, `cmyk` and `gray`|
|`Target_numcolors`| Number of colors, possible values: `2` .. `256` , `32k` , `64k` , `16m`. The color depth is correspondingly adjusted to 8, 15, 16 and 32 bits, respectively. (From 4.1.1) |
`Target_alpha`| Transparency settings, an option from `on` , `off` , `set` order `opaque` (default `off` ; see also "ImageMagick documentation": http: //www.imagemagick.org /script/command-line-options.php#alpha) |
|`Target_profile`| File name of a color profile file for `convert` . If only a file name is specified without a path, the profile file is searched (starting from 4.1.1) in the `eas/data` directory of the EAS |
|`Target_quality`| Quality of the output file from `0` to `100` (depending on the output format) |
|`Target_compress`| Compression method for output file (depending on format, for example `lzw` ) |
|`Target_strip`|`1`: remove all metadata |
|`Target_no_rgb`|`1`: no automatic conversion to RGB |
|`Target_no_autorot`|`1`: no automatic rotation/mirroring using EXIF ​​tags |
|`Target_zoomer`|`1`: Preparing the version for the zoomer ( `target_format` must be `jpg` ) |
|`Target_duration`| Number of seconds from beginning to be calculated for a video version. If not set, the complete video will be converted. (Ab *(version) Version 4.2.32*) |
|`Target_audio_bitrate`| Audio bit rate for video and audio files, e.g. `160k` (ab *(version) Version 4.2.49*) |
|`Target_audio_bitrate`| Video bit rate for video, e.g. `800k` (ab *(version) Version 4.2.49*) |
| -------------------- | ---------------------------------------------------- |
|`Target_commandfile`| Command file for automator requests |
|`Target_fail_on_error`|`1`: If the addition of individual assets fails, the processing of the command file is aborted (for `target_commandfile`, ab *(version) version 4.2.33*) |

##  Sequence

Transformations are performed in the following order:
* `target_crop`
* `target_size`
* `target_mirror`
* `target_rotate`
