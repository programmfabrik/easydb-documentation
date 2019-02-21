---
title: "161 - Upload"
menu:
  main:
    name: "Upload"
    identifier: "webfrontend/administration/base-config/upload"
    parent: "webfrontend/administration/base-config"
---
# Upload

This tab defines global limits for file uploads.

| Settings | | Explanation |
| ------ |---| -------- |
| Upload limit | | The global upload limit in bytes. If a file is larger, it is rejected in any case, even if other values ​​are set by means of the management. |
| _File class_ | Limit | A separate limit can be defined per file class. If it is larger than the global upload limit, it is ignored. |
| | Type | Only the formats for an upload are accepted, which are activated here. For the file class _Sonstige_, all formats that are not listed in one of the other file classes are always allowed. |

> NOTE: You can find further information on [File types](../../../../sysadmin/eas/filetypes) in the section System administration.



