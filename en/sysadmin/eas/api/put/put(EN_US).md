#  EAS-API: /put

The `put`-Request is used to import an asset into the EAS.

##  Example

~~~
 http://eas.example.com/eas/put?instance=example&filename=/tmp/some.jpg&custom={"producer": "admin"}
~~~


##  Parameter


|---|---|
| `Instance`| Name of the target entity |
| `Filename`| Path to the file to be taken |
| `Original_filename`| Original file name of file |
| `Symlink`| value `1` to link file symbolically instead of copy |
| `Hardlink`| value `1` to link file (hard-link) instead of copy |
| `Thumbnailsize`| if set, a *thumbnail* version is created with this size (for example `128x128`) |
| `Thumbnailpriority`| Priority of the *thumbnail* version (from EAS 4.2.31) |
| `thumbnail_target _ *`| Options for implicit *thumbnail* version (alternative to `thumbnailsize`, from EAS 4.2.40) |
| `Custom`| JSON object with name value options (stored and shipped but not evaluated or modified) |
| `Parent_id`| Asset ID of the parent asset (should not be used normally but is for migrations) |
| `No_fulltext_index`| Do not include the asset in the full text index (from EAS 4.2.12) |
| `Expires`| expiration interval, e.g. 7d for 7 days |
| `reap`| Asset ID and hash of a version of another asset that is to be imported as an original, for example `2364/f1d2d2f924e986ac86fdf7b36c94bcdf32beec15`. This option is not recommended |
| `Dispose_source_asset`| The asset of the version taken with `reap` will be deleted after extraction |
| `Dispose_source_version`| The version taken with `reap` will be deleted after extraction |
| `Url`| the processing is carried out by "/rput":../rput, all options are passed to this handler |
| `Zipasdirectory`| value `1`, if a uploaded ZIP is to be unpacked on the server (from EAS 4.2.49) |
| `Webdvdasdirectory`| as `zipasdirectory` , but only for ending `.webdvd.zip` (from EAS 4.2.49) |

##  *thumbnail*-version

As an alternative to `thumbnailsize`, all other parameters of the implicitly created *thumbnail* version can be determined as of EAS 4.2.40. Here are all `target_*` options from "/produce":../produce, but the options must be `fix_`. The reason for this is the specification of `thumbnail_target_format` , very useful is the setting of `thumbnail_target_size`. `Thumbnailpriority` is also valid when using `thumbnail_target_*`.
