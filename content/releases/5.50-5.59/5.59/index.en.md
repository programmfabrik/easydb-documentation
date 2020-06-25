---
menu:
  main:
    name: "5.59"
    identifier: "5.59"
    parent: "releases"
    weight: -559
---

# Version 5.59.0

*Published on 06.11.2019*

### Web frontend

*New*

- **Schedules** can now be saved with time zone. Older versions of easydb always use UTC here, so schedules that should start at midnight actually started at 02:00 in summer.
- Support of **deep hierarchical object export** for XML (maximum depth adjustable in base configuration).

*Improved*

- **Copying rights** is more stable when copying mask rights.

*Fixed*

- Fix for marking during **auto-completion**.
- Improved **cookie handling** when saving user settings for the detail view.

### Server

*New*

- **XML export** supports merge_max_depth for depthhierarchical rendering of objects.
- Time zone support for schedules.
- When **saving collections**, the permissions are now always checked even if the user has the `system.root` permission.

*Improved*

- The deletion of **linked objects** can be activated or skipped by the user.
- More EXIF tags available in **metadata mapping** (**ExifIFD**).
- **XML export** has been accelerated, especially for the **OAI/PMH** interface.
- **XML export** contains more system fields.
- More **email addresses** are accepted when saving.

*Fixed*

- **CSV export of events**: Correct export of truncated fields with multi-byte UTF-8 values.
- **CSV export of events**: Export now also works with archived users.
- **Sorting of multiple fields** has been fixed.

*Translated with www.DeepL.com/Translator*