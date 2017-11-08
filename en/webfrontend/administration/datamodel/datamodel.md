# Data model

In the data model, the current data model <code class="tab">Current</code> can be displayed, and with proper access rights the development version <code class="tab">Development</code> can be displayed. <code class="button">Activate Changes</code> to accept changes made in the development version. This will overwrite the current version.

> NOTE: Be aware that this process is causing a lot of activity on the server side, A complete re-indexing of all records. Until full indexing, users may find records in the old format. In some cases, it may also happen that records affected by changes are not displayed to users until the re-indexing is complete.

Data types and Masks are defined in the Data Model. Object types describe the structure of the data in the database. Masks describe the input and output views of the object types and therefore the data records. If, for example, 20 fields are defined for an object type, different field combinations can be output via masks. User 1 could have the right to mask 1 e.g. 5 of these fields. User 2 could be provided with mask 2 e.g. 5 other fields are received and with mask 3 again see 15 fields.

* [Object Types](./objecttype/objecttype.html)

* [Masks](./mask/mask.html)