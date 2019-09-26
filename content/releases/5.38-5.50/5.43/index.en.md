---
menu:
  main:
    name: "5.43"
    identifier: "5.43"
    parent: "releases550"
    weight: -543
---

> - The CSS-Developer-Plugin has been removed and therefore server-side creation of the CSS is no longer necessary. CSS variables are now used for color changes, which only work in the current browsers. The possibility to load external CSS still exists with the remote plugin, which is activated by default in easydb. Color settings must be reset and saved.
> - CustomMaskSplitter: This new plugin API allows the creation of plugins that subdivide forms in the data model manager. Examples for existing splitters are: Tabs, Panels, Horizontal Dividers and Blocks
> - Beta: The new /api/publish will be released in this release.
> - Beta: Workflow webhooks that can be set in the basic configuration.
>

# Version 5.43.4

*Published on 05.12.2018*

### Server

*Fixed*

- `_id:lookup`for linked objects in group mode was repaired.

# Version 5.43.3

*Published on 28.11.2018*

### Webfrontend

*Fixed*

- The login with login names or passwords with special characters (e.g. ä, ö, Ü) was repaired.

# Version 5.43.2

*Published on 28.11.2018*

### Webfrontend

*Fixed*

- Loading all plugins is now done in the UTF-8 character set again. Special characters should be displayed correctly again.
- Fixed JavaScript error in export menu when selecting alternative masks.
- Display for a user with system.root now also shows the search in any case, even if Show folders only is configured in the system in general.

# Version 5.43.1

*Published on 21.11.2018*

### Webfrontend

*Fixed*

- Data model: New mask separators could not be added.
- Connector: Fixed download of local and remote files.
- Custom Data Type link: The URL verification was repaired.

# Version 5.43.0

*Published on 21.11.2018*

### Webfrontend

*New*

- Group editor: The user has the possibility to define a batch size, thus server timeouts can be avoided for complex updates.
- Favicon: A favicon can be uploaded in the basic configuration.
- Search: The table display allows you to browse pages of multiple fields per object.
- User management: An email confirmation request that prevents a login because the user has not confirmed the email can be withdrawn by the administrator.
- Autocompletion: The word suggestions now consider the currently activated pools of the user.

*Improved*

- CSV-Importer: Warning when importing error port JSON for Custom-Data-Types
- CSV-Importer: Improved display of file field settings
- JSON-Importer: Improvements in the protocol file
- Editor: Improvements in the preview of uploaded files that have not been calculated yet
- User/Group search: The grouping by type has been removed, it is now sorted by group and user only.
- Connector: Improved grouping of search results by pool.
- CSS Developer plugin removed, plugins must load their own CSS now.
- If you have to wait longer than 15 seconds when starting the application, the user will be informed that the server is too busy to answer requests (e.g. because an update with subsequent re-indexing is running).
- Expert search: The formatting and the alphabetical lists have been made clearer and no longer combine any fields.
- Detail: Graphical marking of file fields for which several versions are stored.
- The mask separator **Horizontal divider** is now always output, even if no fields are filled until the next divider. Use **Block** instead.

*Fixed*

- Download: If the connector was activated, no download was possible.
- Expert search: The search for unknown files without extension was repaired.
- Data Model: In models with multiple Reverse Nest object types a common localized name was used in the display.
- Folders: Corrected a loading error that could lead to incorrect widths of the preview display.
- Export: Fixed the mask selection when exporting single objects.

### Server & Plugins

*New*

- publish-API (Beta)
- Webhook Action in Workflows (Beta)

*Improved*

- array support for _lookup:id
- Improved error messages
- path.standard searchable
- Pool filter for suggest-API
- Base object lists limited to a maximum of 1000 results
- Event filter options extended
- Server plugin extended, more diagnostic information and configuration added

*Fixed*

- Search: place corrected
- Suggest index creation when using the special object type name "user" corrected
- Rights management for nested pools corrected
- Conversion of L10n and text fields corrected (both directions)
- Fixed removal of entries with group editor for certain contents
- Transaction is terminated if server responds with HTTP 202.
- possible error when saving the masks is recognized and rejected
- Embedding of linked objects in XML export with the format "flat" deactivated, because not implemented
- Fixed a bug when changing the primary e-mail
- Missing re-indexing linked when changing

