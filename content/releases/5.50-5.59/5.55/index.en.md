---
menu:
  main:
    name: "5.55"
    identifier: "5.55"
    parent: "releases"
    weight: -555
---

> This release requires a complete re-index. Schedule a downtime for the update because the system cannot be used completely during the re-indexing period.

> The CSV format of exported events has been changed.

# Version 5.55.0

*Published on 14.08.2019*

### Web frontend

*New*

- A **secondary list** (linked Objecttype) can be displayed as a **simple pulldown** via the mask setting. This is useful for value lists that only contain a small and completed set of objects.
- In the **search result**, you can now use the context menu to remove an **object from a folder** in which it is located.
- The user manager now shows LDAP and SSO users the **groups automatically assigned** at the last login of the user.
- **Experimental markdown support** in the detail view. Rendering with markdown can be activated in the mask editor when the debug mode is active.
- The **Webhook plugin** now supports automatic checking of HMAC secrets from the basic configuration.
- In the **Event Viewer** some options can be selected during **CSV download**.

*Improved*

- The **Hijri-Gregorian plugin** can now also be used in multiple fields and date range fields.
- **Graphical detail improvements** in CSS.
- **User management**: Users of type collection are no longer displayed.

*Fixed*

- **Metadata mapping**: The export of linked objects with only standard info and of fields with fixed text was fixed. Existing mappings have to be saved again.
- The *undefined* display in the **table view** was repaired.
- Fixed **date search** in **multiple fields**.
- Fixed **wildcard search query with quotation marks**.
- The **note for fields in detail** is now also displayed if the field can only be read.
- **Fixed full-screen display** from detail for cases where detail was opened from table view.
- **Filters with Connector enabled** were repaired, so that now not too many hits are displayed.

### Server

*New*

- The database language `nl-NL` is now supported.

*Improved*

- **Metadata mapping** now prefers dc-DateCreated, the capture of duplicate values is now also avoided.
- The **CSV expor**t uses compact JSON.
- When **exporting**, only the configured languages from the basic configuration or those of the user are used, not all languages. 
- For new systems now only the languages de-DE and en-US are activated by default. 
- The format `standard` in **/api/search** (type: object) now also contains `_collections`.

*Fixed*

- **Groups of users that are automatically assigned via LDAP and SSO** now remain permanently with the user. These groups will be updated at the next login. This ensures that folder releases made by LDAP / SSO users work.
- The **CSV export** of events (**/api/event**) has been corrected and improved. The generated columns of `event.info` are named `csv_explode` with a preceding `info.`. The column `event.info` is now exported correctly if `csv_explode=false`.

- Metadata mapping now exports **DateTime and Date** correctly.
- Deleting folders now also deletes their **subordinate folders** from the index.

*Translated with www.DeepL.com/Translator*