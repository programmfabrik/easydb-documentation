---
menu:
  main:
    name: "5.67"
    identifier: "5.67"
    parent: "releases"
    weight: -567
---

# Version 5.67.0

*Published on 14.05.2020*

### Web frontend

*New*

- **Search**: A search filter for **vector3d** was added.

*Improved*

- **JSON importer**: Improved error output for defective payloads.
- **Detail**: The current version of the object is displayed in the footer.

- **Mask management**: Graphically improved display of sample data.

*Fixed*

- **Login**: In cases where a lot of text is displayed next to the login, the size of the dialog is now adjusted correctly.
- **Export**: Display of the XSLT file name as fallback if no separate name has been assigned.

### Server

*New*

- **File formats**: **3GPP** audio/video support.

*Improved*

- Less sensitive data such as FTP passwords are stored in **events**.

*Fixed*

- **Commit**: Errors in connection with sending email were corrected.
- **Rights management**: ACLs with tag filter applied to object types without tags caused a database error.
