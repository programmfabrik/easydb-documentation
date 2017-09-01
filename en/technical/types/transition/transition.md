# Transition

Transitions define actions that are applied when manipulating user objects. This is the way transitions are evaluated:

**Gather transitions**

Transitions can be defined at global, objecttype and pool level. Depending on whether the object has a pool or not, objecttype or
pool level transitions are gathered. This defines a hierarchy where every level may set a "_private_transitions" flag to indicate that
transitions from higher levels should be ignored. A "sticky" flag can be set to indicate that a transition will be always gathered,
regardless of the "_private_transitions" flag.

Transitions are processed in order: first the global transitions and then the other ones. In each level, the position is used for
ordering purposes.

**Check which transitions apply**

From the list of transitions only those are taken into account which match the conditions they define:
- the operation is one of the given `operations`
- the objecttype meets the requirements of `objecttype_ids`
- `who` contains the session user or a group it belongs to
- `tagfilter:before` evaluates to true for the object before the operation
- `tagfilter:after` evaluates to true for the object after the operation

**Check the transition type**

1. if any transition is "reject", the operation is rejected
2. else, if any transition has a "resolve" action, the operation continues
3. else, if any transition has an "exit" action, take the last one defined and:
    3a. if it is an "exit_reject" action, the operation is rejected
    3b. if it is an "exit_resolve" action, the operation continues
4. else (type "process"), the operation continues normally (notice that this is case also happens when no matching transitions are found)

If the transaction is rejected, the transition which caused the rejection (case 1 or case 3a) is used for the following:

- the rejection text is the confirm message of the transition, or a standard one if not set
- if the transition contains "email" actions, they are executed

**Check the confirmation messages**

All `confirm` messages from the transitions without process actions and with "resolve" process actions are gathered. If the process
step (3b) has been reached and this transition also has a `confirm` message, it will be gathered too.

The first time, the server generates a code based on the operation and sends a 202 to the client. If the user confirms the messages,
the client will retry the operation with the confirmation code. This second time, the operation continues.

**Perform the operation**

If any transition has the action "set_tags", the object's tags are changed accordingly.
Then, all plugin defined actions are executed, which can result in changing the objects.
At last, the operation runs.

**Send e-mails**

If the operation was succesful and there are any actions of type "email", execute them.

See [/api/db](/technical/api/db/db.md) for more information.

## Attributes

| Name               | Description                                                                                               |
|--------------------|-----------------------------------------------------------------------------------------------------------|
| `_id`              | Transition ID (integer, unique, r) |
| `type`             | Transition type (string): one of **process**, **reject**, **resolve**, **exit_reject** and **exit_resolve** |
| `who`              | List of user and/or group this transition applies to (array of [groups (short)](/technical/types/group/group.md#short) and/or [users (short)](/technical/types/user/user.md#short)) |
| `operations`       | Operations this transition applies to (non-empty array of strings): valid operations are **INSERT**, **UDPATE** and **DELETE** |
| `objecttype_ids`   | Objecttypes this transition applies to (array of objecttype-IDs, optional): an empty array or **null** means that it applies to all objecttypes |
| `tagfilter:before` | Tag filter that should match to the object before the operation ([tag filter](/technical/types/tag_filter/tag_filter.md), optional) |
| `tagfilter:after`  | Tag filter that should match to the object after the operation ([tag filter](/technical/types/tag_filter/tag_filter.md), optional) |
| `sticky`           | Specifies that this transition should be sticky in hierarchies (boolean, optional): defaults to **false** |
| `confirm`          | Confirmation text ([l10n](/technical/types/l10n/l10n.md), optional): if not given, no confirmation is required |
| `actions`          | Actions to perform (array of [actions](#action), optional, rw) |

# <a name="action"></a> Transition action

All actions have the common structure:

| Name               | Description                                                                                               |
|--------------------|-----------------------------------------------------------------------------------------------------------|
| `type`             | Action type (string) |
| `info`             | Action description (JSON object): parameters of the action (see below) |

There are two pre-defined action types: "set_tags" and "email". These are defined below. Plugins can define more actions.

## Action "set_tags"

The action "set_tags" defines a list of tags to be set / unset. If a tag is marked to be set and it already is, nothing happens.
Similarly, if a tag is marked to be unset and it is not found on the object, nothing happens.

| Name               | Description                                                                                               |
|--------------------|-----------------------------------------------------------------------------------------------------------|
| `tags`             | Array of: |
| &#8614; `_id`      | Tag ID (integer) |
| &#8614; `set`      | Value (boolean): whether the tag must be set or unset |

## Action "email"

The action "email" is used to send an e-mail to one or more users:

| Name                | Description                                                                                               |
|---------------------|-----------------------------------------------------------------------------------------------------------|
| `recipients`        | Array of [groups (short)](/technical/types/group/group.md#short) and/or [users (short)](/technical/types/user/user.md#short), at least one must be provided |
| `subject`           | E-mail subject ([l10n](/technical/types/l10n/l10n.md), optional): defaults to a standard subject defined in the L10n configuration |
| `message`           | E-mail message ([l10n](/technical/types/l10n/l10n.md), optional): defaults to a standard message defined in the L10n configuration |
| `batchable`         | Whether the e-mail is batchable or not (boolean): defaults to **true** |

The e-mail will be sent to the user(s) according to their configuration. If `batchable` is set, all e-mails that were generated by
this transition will be merged. If not, a separate e-mail will be sent for each action.

