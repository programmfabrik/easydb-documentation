---
title: "120 - ACL Entry"
menu:
  main:
    name: "ACL Entry"
    identifier: "technical/types/acl_entry"
    parent: "technical/types"
---
# ACL Entry

An entry in an Access Control List.

An ACL entry is only valid if `active` is set to **true** and the validity specified by `when` is met.

## Attributes

| Name                      | Description                                                                                               |
|---------------------------|-----------------------------------------------------------------------------------------------------------|
| `_id`                     | ACL entry ID (integer, rw): if set, keep the ACL entry                                                    |
| `who`                     | User or group this entry applies to ([group (short)](/en/technical/types/group), [user (short)](/en/technical/types/user) or `"_owner": true`; optional) |
| `when`                    | Validity of this ACL entry (object, optional): if not set, the ACL entry has no time restrictions |
| &#8614; `from`            | - if set, the ACL entry will not be valid until this time has been reached (timestamp, optional) |
| &#8614; `to`              | - if set, the ACL entry will no longer be valid after this time has passed (timestamp, optional) |
| `date_created`            | Creation date of the ACL entry (timestamp, r) |
| `active`                  | Whether this ACL entry is active of not (boolean): defaults to **true** |
| `rights`                  | Rights that are granted ([rights specification](/en/technical/types/right)) |
| `sticky`                  | Specifies that this entry should be sticky in hierarchies (boolean, optional): defaults to **false** |
| `tagfilter`               | Tag filter to be applied to this ACL entry ([tag filter](/en/technical/types/tag_filter), optional) |
| `send_email_notification` | Send an e-mail notification when updating this ACL entry (see below, w, optional): only in the context of a collection |

## Remarks

Although the attributes `sticky` and `tagfilter` exist for all ACL, they will be only taken into account under certain circumstances:

- `sticky` only makes sense in hierarchical realms (collection, pool and hiararchical object)
- the `tagfilter` is only applied to object-related rights

`"_owner": true` as option for `who` object is currently not implemented in server rights management but only saved and loaded. It should only be used in contexts where `who` is evaluated by the client, e.g. in `_columnfilters` in [objecttype](../objecttype).

Please refer to the [rights management](/en/technical/rightsmanagement) documentation for more details.

## Send e-mail notification

The attribute `send_email_notification` can only be set for collection ACL entries.
It triggers the delivery of an e-mail containing information about the
collection that has been shared, including a direct link to it.
Optionally, a user-defined text. The e-mail goes to the following recipients:

- if `who` is a user and it has a valid e-mail, the e-mail of the user
- if `who` is a group, the valid e-mails of the users

If no e-mails are found, the e-mail will not be sent.

The attribute is a JSON object with the following attributes:

| Name   | Description                                             |
|--------|---------------------------------------------------------|
| `text` | Personalized text to be incorporated in the e-mail body |

