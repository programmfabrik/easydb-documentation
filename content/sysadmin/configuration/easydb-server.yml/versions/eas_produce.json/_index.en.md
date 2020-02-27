---
title: "eas_produce"
menu:
  main:
    name: "eas_produce"
    identifier: "sysadmin/configuration/easydb-server.yml/versions/produce"
    weight: -949
    parent: "sysadmin/configuration/easydb-server.yml/versions"
easydb-server.yml:
  - eas.rights_management.image.versions[].<class>.size_print
  - eas.rights_management.image.versions[].<class>.size_limit
  - eas.rights_management.image.versions[].<class>.export
  - eas.rights_management.image.versions[].<class>.rightsmanagement
  - eas.rights_management.image.versions[].<class>.group
  - eas.rights_management.image.versions[].<class>.zoomable
  - eas.rights_management.video.versions[].<class>.version
  - eas.rights_management.video.versions[].<class>.size_print
  - eas.rights_management.video.versions[].<class>.size_limit
  - eas.rights_management.video.versions[].<class>.export
  - eas.rights_management.video.versions[].<class>.group
  - eas.rights_management.video.versions[].<class>.rightsmanagement
  - eas.rights_management.video.versions[].<class>.standard
  - eas-rights_management.audio.versions[].<class>.version
  - eas-rights_management.audio.versions[].<class>.size_print
  - eas-rights_management.audio.versions[].<class>.export
  - eas-rights_management.audio.versions[].<class>.rightsmanagement
  - eas-rights_management.audio.versions[].<class>.group
  - eas-rights_management.audio.versions[].<class>.standard
  - eas-rights_management.office.versions[].<class>.version
  - eas-rights_management.office.versions[].<class>.size_print
  - eas-rights_management.office.versions[].<class>.export
  - eas-rights_management.office.versions[].<class>.rightsmanagement
  - eas-rights_management.office.versions[].<class>.standard
  - eas-rights_management.archive.versions[].<class>.version
  - eas-rights_management.archive.versions[].<class>.size_print
  - eas-rights_management.archive.versions[].<class>.group
  - eas-rights_management.archive.versions[].<class>.rightsmanagement
  - eas-rights_management.archive.versions[].<class>.limit
  - eas-rights_management.archive.versions[].<class>.standard
  - eas-rights_management.unknown.versions[]
  - eas-rights_management.vector2d.versions[]
  - eas-rights_management.vector3d.versions[]
---
# eas_produce.json

## Variables

| Variable <div style="width:300px"></div>              | Typ <div style="width:100px"></div>  | Required | Description |
|-------------------------------------------------------|---------------|---------|-----------
| `{`                                                   |               | yes     |           |
| &#8193;`"<class>": {`                                 | Hierarchy     | yes     | Configuration for EAS class (__all, image, video, audio, office, archive, unknown, vector2d, vector3d) |
| &#8193;&#8193;`"__all": {`                            | [ ] Hierarchy | yes     | Contains class version definitions |
| &#8193;&#8193;&#8193;`"<versionname>": {`             | Hierarchy     | no      | Contains the specific version definition |
| &#8193;&#8193;&#8193;&#8193;`"target_size":`          | String        | no      | Size (e.g. `128`, `640x480`, `x12` or `45x`) |
| &#8193;&#8193;&#8193;&#8193;`"target_size_min":`      | String        | no      | `1`: Specified size is desired minimum and not maximum size (from *(version) version 4.2.47*) |
| &#8193;&#8193;&#8193;&#8193;`"target_format":`        | String        | no      | File format of the version |
| &#8193;&#8193;&#8193;&#8193;`"target_alpha":`         | String        | no      | Transparency settings, an option from `on` , `off` , `set` order `opaque` (default `off` ; see also "ImageMagick documentation": http: //www.imagemagick.org /script/command-line-options.php#alpha) |
| &#8193;&#8193;&#8193;&#8193;`"target_quality":`       | Integer       | no      | Quality of the output file from `0` to `100` (depending on the output format) |
| &#8193;&#8193;&#8193;&#8193;`"target_no_enlarge":`    | Integer       | no      | `1`: Do not enlarge if the original size is smaller than the requested size (from *(version) version 4.2.34*) |
| &#8193;&#8193;&#8193;&#8193;`"target_no_fallback":`   | Integer       | no      | |
| &#8193;&#8193;&#8193;&#8193;`"priority":`             | Integer       | no      | |
| &#8193;&#8193;&#8193;&#8193;`"target_page":`          | Integer       | no      | a page is to be extracted (counting starts at `0`) |
| &#8193;&#8193;&#8193;&#8193;`"target_extractdpi":`    | Integer       | no      | When converting Office documents to images, this DPI number should be used (default:`300`) |
| &#8193;&#8193;&#8193;&#8193;`"target_metadata":`      | Integer       | no      | JSON list of rows for Exiftool for writing metadata (see option `-` from Exiftool) |
| &#8193;&#8193;&#8193;&#8193;`"target_rotate":`        | Integer       | no      | Angle of rotation in degrees |
| &#8193;&#8193;&#8193;&#8193;`"target_mirror":`        | Integer       | no      | Mirroring at the specified axis ( `x` or `y`) |
| &#8193;&#8193;&#8193;&#8193;`"target_crop":`          | Integer       | no      | Cut out an image area ( `<w> x <h> + <x> + <y>`, for example `400x300 + 100 + 30` ) |
| &#8193;&#8193;&#8193;&#8193;`"target_size_force":`    | Integer       | no      | `1`: Force Size (Disallow Aspect Ratio) |
| &#8193;&#8193;&#8193;&#8193;`"target_size_limit":`    | Integer       | no      | `1`: Do not create version if the original size is smaller than the requested size |
| &#8193;&#8193;&#8193;&#8193;`"target_dpi":`           | Integer       | no      | DPI setting for the output file (does not affect the size) |
| &#8193;&#8193;&#8193;&#8193;`"target_wm_image":`      | Integer       | no      | Watermark image to be included in the version (specified with absolute path, which is readable for www-data). |
| &#8193;&#8193;&#8193;&#8193;`"target_wm_dissolve":`   | Integer       | no      | Watermark transparency (from `0`- invisible - up to `100`- covering - the default is `50`) |
| &#8193;&#8193;&#8193;&#8193;`"target_wm_gravity":`    | Integer       | no      | Aligning the watermark (direction of the sky), an option from: `c` (default), `n`, `e`, `s`, `w`, `ne`, `nw`, `se`, `Sw` |
| &#8193;&#8193;&#8193;&#8193;`"target_wm_size":`       | Integer       | no      | `100x100` or `50% x50%` (default: `100% x100%`; |
| &#8193;&#8193;&#8193;&#8193;`"target_wm_tile":`       | Integer       | no      | `1`: Watermark is tiled. `Target_wm_gravity` is not taken into account in this case. (Ab *(version) version 4.2.36*) |
| &#8193;&#8193;&#8193;&#8193;`"target_colorspace":`    | Integer       | no      | Color space, tested with `rgb`, `cmyk` and `gray` |
| &#8193;&#8193;&#8193;&#8193;`"target_numcolors":`     | Integer       | no      | Number of colors, possible values: `2` .. `256` , `32k` , `64k` , `16m`. The color depth is correspondingly adjusted to 8, 15, 16 and 32 bits, respectively. (From 4.1.1) |
| &#8193;&#8193;&#8193;&#8193;`"target_profile":`       | Integer       | no      | File name of a color profile file for `convert` . If only a file name is specified without a path, the profile file is searched (starting from 4.1.1) in the `eas/data` directory of the EAS |
| &#8193;&#8193;&#8193;&#8193;`"target_compress":`      | Integer       | no      | Compression method for output file (depending on format, for example `lzw` ) |
| &#8193;&#8193;&#8193;&#8193;`"target_strip":`         | Integer       | no      | `1`: remove all metadata |
| &#8193;&#8193;&#8193;&#8193;`"target_no_rgb":`        | Integer       | no      | `1`: no automatic conversion to RGB |
| &#8193;&#8193;&#8193;&#8193;`"target_no_autorot":`    | Integer       | no      | `1`: no automatic rotation/mirroring using EXIF ​​tags |
| &#8193;&#8193;&#8193;&#8193;`"target_zoomer":`        | Integer       | no      | `1`: Preparing the version for the zoomer ( `target_format` must be `jpg` ) |
| &#8193;&#8193;&#8193;&#8193;`"target_duration":`      | Integer       | no      | Number of seconds from beginning to be calculated for a video version. If not set, the complete video will be converted. (Ab *(version) Version 4.2.32*) |
| &#8193;&#8193;&#8193;&#8193;`"target_audio_bitrate":` | Integer       | no      | Audio bit rate for video and audio files, e.g. `160k` (ab *(version) Version 4.2.49*) |
| &#8193;&#8193;&#8193;&#8193;`"target_video_bitrate":` | Integer       | no      | Video bit rate for video, e.g. `800k` (ab *(version) Version 4.2.49*) |
| &#8193;&#8193;&#8193;`}`                              | |         |           |
| &#8193;&#8193;`}`                                     | |         |           |
| &#8193;`}`                                            | |         |           |
| `}`                                                   | |         |           |

# Custom version configuration

Edit `eas_produce.json` and add the variants you desire.

Example: Adding a variant with maximum size of 500 pixels:

```json
"image": {
  "__all": {
	  "500px": {
			"target_size": "500x500",
			"target_size_min": "1",
			"target_format": "png",
			"target_alpha": "on",
			"target_no_enlarge": "1",
			"priority": "12"
		},
```

* Maximum size of 500 is implemented by `"target_size": "500x500",`.
* `500px` is the name of the variant. Names that only contain numbers are NOT VALID. Make sure to also include letters.
* There may be multiple variants with the same target_size. Just make sure to give them unique names.
* `__all` is an existing paragraph. You may put your new variant into it, as in this example. Then your new variant is produced for assets no matter whether the format of the original file is png, jpg, tiff, etc.. If you put a new variant under `jpg:` instead of `__all` then the new variant will only be created for assets which are of type jpg in their original ( = imported) file.
* Putting your new variant into the `image` clause, as in this example, defines that this variant is only to be produced for assets which are images in their original file. You could instead use the clauses `video`, `office`, etc. or the clause `__all` with the same indentation as `image`, to produce for all classes.
* `"target_size_minimum": "251x251",` defines that this preview is NOT to be generated for assets which are smaller than 251 pixels in both dimensions.
* The preview is generated as a jpg file. E.g. `png` and `tiff` are also possible.
* `target_interlace` and `target_quality` are for jpg only. For `png` and `tif` consider e.g. `"target_alpha": "on"` for transparency or `"target_dpi": "300"` for printing.
* Make sure to include all needed commas and to avoid any superflous commas. A superflous commma would be e.g. one at the end of a list. Note for example that there is no comma after `"target_no_enlarge": "1"` in the example above. Consider using a syntax checker and linter tool for json.

# Examples

For complete examples about versioning in easydb5, please refer to [this](../example).