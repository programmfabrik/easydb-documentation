---
title: "119 - Transitions"
menu:
  main:
    name: "Transitions"
    identifier: "technical/transitions"
    parent: "technical"
---
# Transitions

Transitions can be used to create a workflow when operating with user objects. They can control which operations are
possible and trigger actions when they are performed.

## Levels

Transitions can be defined at three levels: global, pool and objecttype. Global transitions are applied to all objects,
as long as the pool or objecttype they belong to does not specify otherwise.

Global transitions are defined using [/api/transition](/en/technical/api/transitions). If they are marked as sticky, they will be
shared by all objects.

Objecttype transitions are only relevant for non-pool objects. They are defined using [/api/objecttype](/en/technical/api/objecttype).
If an objecttype has **private_transitions**, it means that the global transitions that are not sticky will be cancelled.

Pool transitions are only relevant for pool objects. They are defined using [/api/pool](/en/technical/api/pool). Normally,
transitions are inherited from the parent pool and the root pool inherits the global transitions.
If a pool has **private_transitions**, all inherited transitions that are not sticky will be cancelled.

## Procedure

When an operation (INSERT, UPDATE or DELETE) is performed on an object using [/api/db](/en/technical/api/db), all transitions that are
applicable to that object are gathered. If they are no transitions, the operation continues normally.

If there are transitions, they are checked (see [transition](/en/technical/types/transition)):

1. The operation must match the transition `operation`
2. The session user/group must match any entry in the transition `who`
3. The `tagfilter:before` must match the current object's tags (not checked for INSERT)
4. The `tagfilter:after` must match the new object's tags (not checked for DELETE)

If no transition survived this check, an error will be returned (403 forbidden).

If any of the transitions that apply requires confirmation (`confirm` is not null), the server will return a status code of 428
with the list of all confirmation messages and a confirmation key. The next call from the client should include the confirmation
key as query string parameter (see [/api/db](/en/technical/api/db)). If the key is provided, the operation will continue.

If the transitions specify any actions, these will be processed.

