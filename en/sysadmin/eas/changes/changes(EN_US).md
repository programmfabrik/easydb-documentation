Release History {# release-history.top}
================

Changes to the easydb asset server in the overview.

4.2.46 (2 March 2014)
---------------------

- Error handling of `/ eas / delete / <asset-id> / (asset | children)`
    corrected
- Support for Opus audio files
- XMP packet can be extracted from images using
    `/ Produce? Target_format = xmp`
- Partitions in `/ status` are filtered by instance
- File extension of special files in the ZIP container
    output
- PLYs with \\ r as line separators are supported

4.2.45 (3 November 2014)
-------------------------

- PLYs are detected in ZIP files, allowing external texture images
- Recognition of PLYs corrected

4.2.44 (10 September 2014)
---------------------------

- Workaround for some TIFFs with broken metadata

4.2.43 (22 July 2014)
----------------------

- minor errors in Exiftool are skipped

4.2.42 (May 23, 2014)
---------------------

- Video thumbnail extraction corrected, the last frame should not
    be used
- File name encoding of files delivered by Apache
    corrected

4.2.41 (8 April 2014)
----------------------

- Implementation `/ search / failedversions` and
    `/ Search / keyword? Foo = FAILED_VERSIONS ()` to search for
    Failed versions
- Implementation of `target_size` for images improved
- Conversion of audio files to FLV for ffmpeg \> 0.8.x corrected

4.2.40 (13 March 2014)
----------------------

- Thumbnail version can be rebuilt with `/ produce`
- more thumbnail options can be specified with `/ put`
- new Apache macro `EasydbAssetServerExt` to create a unique
    Identifiers independent of the directory
- Non-ASCII characters can be used in the name of e-mail attachments
    become
- Cover pictures in FLAC and Ogg Vorbis can be read out
- Fix for alignment in the metadata
- Fix for conversion of grayscale images without color profile
    sRGB
- Color mode is obtained if `target_no_rgb = 1`
    becomes
- Detection of grayscale TIFFs improved
- Scaling of EPS corrected when the resolution of 72 dpi
    differs

4.2.39 (17 January 2014)
------------------------

- Umlauts in zip filenames are rewritten
- Fix for Janitor and Maintenance restart
- `target_clip = auto`, clip path from image is used as long as
    available
- sRGB treatment when using watermarks
- WAV output format for audio

4.2.38 (21 November 2013)
--------------------------

- Check the Office process ports at startup
- Zoomer creates temporary directory, if it does not exist
- Evaluation of the zoomer configuration corrected

4.2.37 (25 September 2013)
---------------------------

- more stable hashes for versions
- Support for `target_size` for converting PDF to image
- implementation `/ produce? New_original = 1 & no_link_to_orig = 1`
- implementation `/ delete / <id> / versions? Except = [" foo "," bar "]`
    Delete all versions with exceptions
- Support of other tile sizes in the zoomer
- Fixed errors when extracting some binary metadata
- Fix `target_crop` if` target_size` is not specified

4.2.36 (6 August 2013)
-----------------------

- new zoomer implementation
- improved support for POST uploads
- Request / query / capabilities
- IPTC metadata is obtained
- Fixes for color space and color depth
- improved support for grayscale images
- Fixes for conversion from CMYK to RGB
- Increased speed of / query / distinct / extension
- Raw thumbnail is used more often if large enough
- automatic rotation for raw images corrected
- Fix `target_fail_on_error`
- The same picture is used for all previews of a video

4.2.35 (29 January 2013)
------------------------

- EAS asset as a source of watermark image possible
- E-mail: Zip file name can be specified
- Fixes for color space and gamma correction
- Fallback to thumbnail when raw processing failed
- Fix for background update PV9
- Size for video calculation can be forced

4.2.34 (26 October 2012)
-------------------------

- Check the number of configured Office processes at startup
- Option `target_no_enlarge` for images, so as not to enlarge them
    become
- Fixes for background updates PV6 and PV8
- Current and maximum version of background updates in / config
- Workaround for errors of ffmpegthumbnailer 2.0.0

4.2.33 (26 September 2012)
---------------------------

- Support of 3D models, calculation of preview images for
    STL files
- EPS and PDF as target formats when converting images
- When calculating the preview images of files with invalid
    In case of errors, color profiles will also be converted without
    Consideration of the profiles.
- Support for Ubuntu 12.04 and thus LibreOffice instead
    OpenOffice.org
- Improved generation of preview images for videos
- Corrected height and width information for automatically rotated
    pictures
- Prevention of hanging processes at Janitor and internal
    Full text update

4.2.32 (July 31, 2012)
----------------------

- New installations of the EAS have errors when creating an asset
    Because a keyword has not been created
- Video to video conversions now support the
    Option `target_duration`, which is the maximum length of the target version
    Can be limited

4.2.31 (15 June 2012)
----------------------

- Janitor re-enabled, potential problem resolved and general
    improved
- / bulkversions request for quick but incomplete request
    Multiple assets
- Priority of the thumbnail version can be influenced externally
- Partitions are checked before starting a job
- Barcode renderer integrated
- some metadata fields are additionally fulltextindicated

4.2.30 (March 23, 2012)
----------------------

- AND- instead of OR link in / search / keyword, if multiple queries
    At the same time
- Janitor is activated by default (disabled by 4.2.30.4,
    Since images used in certain circumstances are deleted
    could)
- Runtime of videos in the format HH: MM: SS in the summary
- / bulksynccommit warns about queried but unavailable assets
- Temporary files when writing metadata are restored
    deleted
- Creation date of an asset is extracted from the metadatem
- Fulltext search optimized
- Support for Exiftool 8.76
- / query / distinct to determine existing metadata content
- Integration of easydb's version-creation logic into the EAS (yet
    Not for productive use)
- Upload support for / put via PUT or POST
- Force the storage tables for individual keywords
- ZIP64 support for large amounts of data
- numerous optimizations and minor bugs fixed

4.2.29 (28 November 2011)
--------------------------

- preliminary filing for unfinished derived assets
- automatic start and restart of the EAS during installation and update
- Set up the EAS start at system start
- Fixed bug with link matching when the EAS is empty (/ bulksynccommit)
- Fixed deletion of assets

4.2.28 (4 November 2011)
-------------------------

- logrotate configuration is installed
- Enhancements for / bulkfetch

4.2.27 (21 October 2011)
-------------------------

- new request type: / bulkfetch
- Parameter query extended for images (/ query / param / image)
- Janitor can delete assets, function not yet activated

4.2.26 (3 August 2011)
-----------------------

- pdftoppm is used instead of ghostscript to convert PDFs to images
    used
- potential DB jam fixed
- DEFLATE for assets disabled, if enabled before
- Worker stores start and end times for jobs
- possibly missing, temporary directory is generated

4.2.25 (6 July 2011)
---------------------

- Error in option "link" for / produce corrected
- minor improvements

4.2.24 (1 July 2011)
---------------------

- internal conversion of the job treatment
- new request type: / query / profiles
- Database upgrade v18
- new request types: / bulksynccommit & / uncommit
- Asset tree is checked for commit flag before deletion of assets
- Janitor process
- EAS :: Common is set for generated versions
- Reduced metadata is copied for derived versions
- Conversions video = \> image can all image conversion options
    use
- Package version is output in / config

4.2.23.1 (17 June 2011)
------------------------

- URL import corrected
- target \ _no \ _ * options
- slightly improved error handling

4.2.23 (4 April 2011)
----------------------

- sorted output of "named-versions" \
- Improved Locking \
- Status for recalculated assets remains "done" until calculation \
- Easily improved error handling for batch request
    
4.2.22 (21 March 2011)
----------------------

- Improvements in job and cache handling
- initial DB checks implemented correctly
- the detection of raw images has been improved

4.2.21 (March 11, 2011)
----------------------

- Changed job logic
- Watermark calculation converted
- "reap asset" functionality for / put installed
- new request type: / updatecustom
- Functions REGEXP () & INLIST () for / search
- Link option for / produce again activated
- some minor fixes

4.2.20 (18 February 2011)
-------------------------

- Images in the zip as an e-mail attachment possible
- Metadata writing without generating new versions
- Video watermark for FFmpeg 0.6+ (above -vf)
- Video properties with ffprobe instead of mplayer determined
- cleans up various places

4.2.19.1 (11 February 2011)
---------------------------

- more robust error messages
4.2.19 (24 January 2011)
------------------------

- Improved error handling in batch handler
- OpenOffice processes are restarted from time to time
- Job restarts corrected
- Improved logging

4.2.18 (6 January 2011)
-----------------------

- LSB header corrected in init script
- new request type: / query
- Changes to / status: all partitions, deactivation parameters
    appropriate
- Improved watermark support for videos
- Times are exported via the metadata
- Whitelist for file names in ZIPs
- Fixed bug & improved logging
- Fault injection framework

4.2.17 (1 December 2010)
-------------------------

- Attempt to fix OOo Tempfile leak
- maximum size for versions specified in the / versions request
- some fields in the version record are skipped (saves
    Storage)
- further bugs fixed

4.2.16 (3 November 2010)
-------------------------

- Fixed access control / stream error
- Fixed migration errors

4.2.15 (1 November 2010)
-------------------------

- collected keywords
- better handling of broken input data

4.2.14 (October 27, 2010)
-------------------------

- Fixed partitions on CIFS shares

4.2.13 (26 October 2010)
-------------------------

- Parallel upgrades
- many optimizations

4.2.12 (1 October 2010)
------------------------

- DB Upgrade v11: System Versions
- DB upgrade v12: Index update
- DB upgrade v13: Status of jobs and versions disconnected
- further bugs fixed

4.2.11 (17 September 2010)
---------------------------

Improvements in the determination of the page number of
    Office documents

4.2.10 (17 September 2010)
---------------------------

- Troubleshooting the OOo control
- Use of the FCGI interface (flup) corrected

4.2.9 (16 September 2010)
--------------------------

- Access to incorrect partition corrected

4.2.8 (16 September 2010)
--------------------------

- implicit conversion of images to sRGB
- Better handling of temporary files
- Improvement of OOo interface
- other minor bugs fixed

4.2.7 (31 August 2010)
-----------------------

- Improvements in caching

4.2.6 (13 August 2010)
-----------------------

- DB upgrade v10: faster access to the next job
- cmdlist jobs are retried after error

4.2.5 (10 August 2010)
-----------------------

- DB upgrade v9: new index
- Job maintenance implemented

4.2.4 (9 August 2010)
----------------------

- DB upgrade v8: DB unification

4.2.3 (5 August 2010)
----------------------

- Support for raw images
- more caching
- Fault has been corrected

4.2.2 (23 July 2010)
---------------------

- Locking error in queue fixed
- Fixed UTF-8 problems in Exiftool wrapper
- Init script corrected
- Fixed libmagic bug
- DB upgrade v6: Optimization of the status
- Basic port configurable for OOo
- User / group can be changed by configuration

4.2.1 (5 July 2010)
--------------------

- Added character recognition

4.2.0 (June 21, 2010)
---------------------

- Conversion to common server for service, job calculation & OOo start

4.1.0 (April 20, 2010)
----------------------

- first DB-based release