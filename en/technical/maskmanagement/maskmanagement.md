# Mask management

Objects are displayed and changed through masks. Each objecttype can have multiple masks defined.

## Available masks

The `mask` right determines which masks are available to the user for a certain object. The `mask`
right has as parameter a list of masks and can be granted through pools and objecttypes. See
[rights management](/technical/rightsmanagement/rightsmanagement.html).

The list of available masks for an object depends on its objecttype and - if the objecttype has a
pool link - also from its pool. It is composed of all the masks of that objecttype that are linked
by `mask` rights granted through the objecttype's and pool's ACLs.

The special mask "\_all\_fields" can only be used by root.

[/api/db_info](/technical/api/db_info/db_info.html) can be used to get the list of available masks for an objecttype [and pool].

## Mask preference

For each objecttype, the maskset defines a preferred mask. This is the mask used for rendering linked objects.
The system generates a mask preference order based on the maskset, where the preferred mask is the first one
and the rest follow in not guaranteed order.

The user can specify a preference order at objecttype and/or pool level using the `_standard_masks` attributes
(see [objecttype](/technical/types/objecttype/objecttype.html) and [pool](/technical/types/pool/pool.html)). This will be used when rendering
the masks in [/api/db_info](/technical/api/db_info/db_info.html) and can be used in the frontend to sort the masks. The order is defined
by the first source that has a non-null attribute `_standard_masks`:

1. object's pool (if the objecttype has a pool link)
2. pool's ancestors up to the root pool (if the objecttype has a pool link)
3. objecttype

If none of these sources specify a mask order, the auto-generated one is used.

If the user is root, the special mask "_all_fields" will appear at the end of the list.

