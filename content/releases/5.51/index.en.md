---
menu:
  main:
    name: "5.51"
    identifier: "5.51"
    parent: "releases"
    weight: -551
---

# Version 5.51.1

*Published on 23.05.2019*

### Web frontend

*New*

- Folder-deep links can be used with the URL addition `anonymous` for anonymous logins.

*Fixed*

- In pool searches, it is again possible to select higher-level structuring pools. 
- Solved problem in Objectstore Synchronization.

### Server

*Fixed*

- Determination of mask sequence corrected. May have led to missing results in the search.
- Corrected session-group assignment. Led to errors in SSO authentication.

# Version 5.51.0

*Published on 22.05.2019*

### Web frontend

*New*

- Metadata mapping: You can add your **own metadata fields** to profiles.
- Metadata Mapping: Two **new profiles without preconfigured metadata** for own filling.
- Editor: In all editors there is a new possibility to switch **back and forth** between the currently selected (or found) profiles.
- Data model: Two new mask options allow you to **hide the mask** in the editor and in detail.

*Improved*

- Display of the zoom level has been graphically improved.
- In the info menu of a publication there is now a button **Copy Link**.

*Fixed*

- **Detail**: In some cases the info button of the previous file remained visible.
- Empty restarted easydbs did not start the search.

### Server

*New*

- New endpoint **/api/xmlmapping/tags**: Lists available tags for reading and writing metadata.
- **/api/mask**: Two new options: `hide_in_editor`, `hide_in_detail`. 
- The **Gazetteer plugin** now uses the automatic update mechanism to regularly update existing entries.
- Expired sessions are deleted from the system by the Janitor.
- Full text search for numbers
- New endpoint: **/api/settings/updatecustomdata**.

*Improved*

- The **Webhook plugin** now uses the central Node.js infrastructure of the server. The webhook of the Example plugin has been extended.
- Performance improvements for **/api/session**.
- **MAIL_SENT** events are regularly disposed of by the Janitor.

*Fixed*

- **Scheduled exports** now also work when the associated session is logged off.
- Re-indexing of objects that link to children of the edited object has been fixed.
- In some cases no tags could be set on transaction abort.

*Translated with www.DeepL.com/Translator*