---
title: "130 - Message"
menu:
  main:
    name: "Message"
    identifier: "technical/types/message"
    parent: "technical/types"
---
# Message

Messages are sent to the frontends for user confirmation. Before all pending messages are confirmed by the user,
the user can not be fully authenticated. More details in [/api/session](/en/technical/api/session).

## Attributes

| Name                        | Description                                                                                               | Search        |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|---------------|
| `_basetype`                 | Name of the base type (string, r): **message**                                                            |               |
| `_owner`                    | Owner of this message ([group (short)](/en/technical/types/group) or [user (short)](/en/technical/types/user), rw): see below | Number\* |
| `_groups`                   | Groups this message needs to be presented to (array of [groups (short)](/en/technical/types/group), r)      | Number\*      |
| `message`                   | Message attributes:                                                                                       |               |
| &#8614; `_id`               | Message ID (integer, unique, r\*)                                                                         | Number        |
| &#8614; `_version`          | Message version (integer, rw)                                                                             |               |
| &#8614; `title`             | Title ([l10n](/en/technical/types/l10n), rw)                                                                      | L10n (all)    |
| &#8614; `message`           | Message to show ([l10n](/en/technical/types/l10n), rw)                                                            | L10n (all)    |
| &#8614; `confirmation`      | Message confirmation text ([l10n](/en/technical/types/l10n), optional, rw): if set, user confirmation is required |               |
| &#8614; `confirm_every_version` | if set to `true`, every version of a message has to be confirmed (see `confirmation`) (defaults to **false**) |       |
| &#8614; `webfrontend_type`  | if set, the message does not generate a pending task but remains for the frontend to show (text, optional) | NotAnalyzed   |
| &#8614; `start_time`        | Start time (date, optional, rw)                                                                           | Date          |
| &#8614; `end_time`          | End time (date, optional, rw)                                                                             | Date          |
| &#8614; `webfrontend_props` | Webfrontend properties (json, optional) |    |
| &#8614; `reference`         | Message reference (string, unique, optional, rw) |
Remarks:

- `_id` has to be set for POST operations
- `_groups.group._id` is searchable as Number
- `_owner.group._id` and `_owner.user._id` are searchable as Number

## Owner

The message always has an owner. On creation, it is set automatically by the server to the message's creator, but the API won't complain if it is explicitly
set. It will return an error if it is set to something different. The owner cannot be set to **null** but can always be left out, meaning that it should not be changed.

## Related operations

- [/message](/en/technical/api/message): CRUD operations on messages
- [/search](/en/technical/api/search): Search type "message" (*TODO*)
- [/session](/en/technical/api/session): Confirm message


