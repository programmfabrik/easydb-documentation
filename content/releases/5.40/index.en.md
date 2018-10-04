---
menu:
  main:
    name: "5.40"
    identifier: "5.40"
    parent: "releases"
    weight: -540
---

# Version 5.40.2

*Published on Sep 27th 2018*

### Server

*Fixed*

- The file name in the **download_url** was not set correctly, which could lead to isolated problems with ZIP file creation via the connector or customer-specific applications

### Fylr

*Fixed*

- Firefox support for ZIP downloads with ZIP file names containing a space character

# Version 5.40.1

*Published on Sep 26th 2018*

### Asset-Server

*Improved*

- Support of UTF8 in Javascript files
- MP4 with YUV402p pixel format, for better support in Mozilla Firefox

# Version 5.40.0

*Published on Sep 19th 2018*

> This version does not require a new index to be built, so the update should go smoothly and quick.

### Server

*New*

- Original Filepath was included in mapping

*Fixed*

- Search for without was fixed for some fields
- Original Filebase is now saved without path.

### Webfrontend

*New*

- Metadata Mapping: New input mask with search filter and output of mapping tags
- JSON-Importer: Support of updates by _id:lookup and _version:autoincrement notation
- JSON Importer: setting to automatically ignore upload errors during import
- JSON-Importer: Output of the log as CSV file with structured information

*Improved*

- Configuration: New design for the display
- Editor: When copying objects, "UNIQUE" entries are no longer copied.
- Linked objects are no longer displayed in Detail and Editor.
- Only the first selected object of a selection is automatically displayed in the detail view.
- Output of "Original Filepath" in detail info for uploaded files
- Output of the actual file types in the download dialog

*Fixed*

- User-CSV-Importer: _groups#find functionality was repaired
- Event Manager: display of hierarchical information of events was repaired
- Expert search: In rare cases, the input was not removed from the form after it was transferred.
- Filter: The display of More... in lower hierarchy levels has been fixed.


