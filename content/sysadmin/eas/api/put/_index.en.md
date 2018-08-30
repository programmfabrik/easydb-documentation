---
title: "21 - /put"
menu:
  main:
    name: "/put"
    identifier: "sysadmin/eas/api/put"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /put

The `put`-request is used to import an asset into the EAS.

##  Example

```url
http://eas.example.com/eas/put?instance=example&filename=/tmp/some.jpg&custom={"producer": "admin"}
```


##  Parameter


|key|value|
|---|---|
| `instance`| Name of the target entity |
| `filename`| Path to the file to be taken |
| `original_filename`| Original file name of file |
| `symlink`| value `1` to link file symbolically instead of copy |
| `hardlink`| value `1` to link file (hard-link) instead of copy |
| `thumbnailsize`| if set, a *thumbnail* version is created with this size (for example `128x128`) |
| `thumbnailpriority`| Priority of the *thumbnail* version (from EAS 4.2.31) |
| `thumbnail_target_*`| Options for implicit *thumbnail* version (alternative to `thumbnailsize`, from EAS 4.2.40) |
| `custom`| JSON object with name value options (stored and shipped but not evaluated or modified) |
| `parent_id`| Asset ID of the parent asset (should not be used normally but is for migrations) |
| `no_fulltext_index`| Do not include the asset in the full text index (from EAS 4.2.12) |
| `expires`| expiration interval, e.g. 7d for 7 days |
| `reap`| Asset ID and hash of a version of another asset that is to be imported as an original, for example `2364/f1d2d2f924e986ac86fdf7b36c94bcdf32beec15`. This option is not recommended |
| `dispose_source_asset`| The asset of the version taken with `reap` will be deleted after extraction |
| `dispose_source_version`| The version taken with `reap` will be deleted after extraction |
| `url`| the processing is carried out by "/rput":../rput, all options are passed to this handler |
| `zipasdirectory`| value `1`, if a uploaded ZIP is to be unpacked on the server (from EAS 4.2.49) |
| `webdvdasdirectory`| as `zipasdirectory` , but only for ending `.webdvd.zip` (from EAS 4.2.49) |

##  *thumbnail*-version

As an alternative to `thumbnailsize`, all other parameters of the implicitly created *thumbnail* version can be determined as of EAS 4.2.40. All `target_*` options from [/produce](/en/sysadmin/eas/api/produce) are possible, but the options must include the prefix `thumbnail_`. The specification of `thumbnail_target_format` is decisive. Also useful is the setting of `thumbnail_target_size`. `thumbnailpriority` is also valid when using `thumbnail_target_*`.

## Upload the file

Alternatively to specifying the file path via `filename`, the file can also be uploaded directly. This can be done either directly or in a form.

### Direct Upload

Usually through HTTP PUT, for instance, with `curl`:

```bash
curl -XPUT http://eas.example.com/eas/put -H 'Content-Type: image/png' -T test.png
```

### Upload in the Form

With this approach only one file can be uploaded at a time. The name of the form field (in the example `file`) does not matter, for instance, with `curl`:

```bash
curl -XPOST http://eas.example.com/eas/put -F file=@test.png
```

