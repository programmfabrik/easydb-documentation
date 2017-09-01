# Right Preset

A right preset contains a list of rights and optionally a tagfilter. It is used to configure ACL entries with these values
as presets. If a right preset changes the ACL entry linking it will also have a new effect. A right preset exists in a specific
right context (see [/api/right](/technical/api/right/right.md)).

A right preset consists of:

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `_basetype`                 | Name of the base type (string, r): **right_preset**                                                       |
| `right_preset`              | Right preset attributes:                                                                                  |
| &#8614; `_id`               | Right preset ID (integer, not null, unique, r)                                                            |
| &#8614; `_version`          | Right preset version (integer, rw)                                                                        |
| &#8614; `_position`         | Right preset position (integer, not null, unique for a given context, rw)                                 |
| &#8614; `displayname`       | Name used to display the right preset ([l10n](/technical/types/l10n/l10n.md), optional)                                |
| &#8614; `description`       | Description ([l10n](/technical/types/l10n/l10n.md), optional)                                                          |
| &#8614; `preset`            | Preset attributes (partial [ACL entry](/technical/types/acl_entry/acl_entry.md), rw)                                        |

The partial ACL entry in `preset` only contains the attributes `rights` and `tagfilter`.

