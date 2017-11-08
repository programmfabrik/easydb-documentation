# Tag management

Tags are defined using [/api/tag](/technical/api/tags/tags.html). They can be assigned to objects using [/api/db](/technical/api/db/db.html).
However, there are rules that determine which tags can be applied to which objects.

First of all, a tag can only be assigned to an object if its [schema type definition](/technical/types/schema/schema.html#table)
has the `has_tags` fag set. This flag can only be changed by a schema update using [/api/schema](/technical/api/schema/schema.html).

## Global tags

At global level tags have three flags (see [tag definition](/technical/types/tag/tag.html#tag)): `enabled`, `sticky` and `is_default`.

This is how `enabled` and `sticky` work:

| # | enabled | sticky | Meaning |
|---|---------|--------|---------|
| 1 | true    | true   | This tag is enabled for all objects, regardless of objecttype and pool |
| 2 | true    | false  | This tag is enabled by default, but can be disabled through configuration (see below) |
| 3 | false   | true   | This tag is disabled for all objects, regardless of objecttype and pool |
| 4 | false   | false  | This tag is disabled by default, but can be enabled through configuration (see below) |

The flag `is_default` specifies which tags are set by default. For tag groups of the type "choice", only one tag may be default
at the same time.

## Objecttype

Objects that belong to an objecttype **without pool link** (see [table definition](/technical/types/schema/schema.html#table))
are affected by the tag configuration of their objecttype (see [objecttype](/technical/types/objecttype/objecttype.html)):

- if the flag `_private_tags` is not set, the objecttype assumes the default configuration
- if the flag is set, the attribute `_tags` will be used to specify which tags other than the sticky ones are enabled (defaults are cancelled)
- the attribute `_tags` can only contain tags that are not sticky (#2 and #4)

Objecttypes can override the "default" setting of tags. Notice that if a tag was specified as default at the global level
and another tag of the same "choice" group is specified at objecttype level, the latter will be the new default, even if
the tag at global level is sticky.

## Pool

Objects that belong to an objecttype **with pool link** (see [table definition](/technical/types/schema/schema.html#table))
are affected by the tag configuration of their pool (see [pool](/technical/types/pool/pool.html)). The configuration works
recursively across the pool hierarchy:

- if the flag `_private_tags` is not set, the pool inherits the default configuration from its ancestors; the root
  pool assumes the default global configuration
- if the flag is set, the attribute `_tags` will be used to specify which tags other than the sticky ones are enabled
  (defaults to not enabled, not sticky and not default)
- the attribute `_tags` can only contain tags that are not sticky
- the pool provides a read-only attribute, `_compiled_tags`, that specifies the resulting tag configuration:

| enabled | sticky | Meaning |
|---------|--------|---------|
| true    | true   | Enabled through sticky global configuration (#1) or a sticky setting within the pool hierarchy |
| true    | false  | Enabled either through default configuration (global, #2, or ancestor pool) or through `_tags` |
| false   | true   | Disabled through sticky global configuration (#3) or a sticky setting within the pool hierarchy |
| false   | false  | Disabled either through default configuration (global, #4, or ancestor pool) or through `_tags` |

Pools can override the "default" setting of tags in the same way as described above for the objecttypes.

## Object

[/api/db_info](/technical/api/db_info/db_info.html) can be used to know which tags can be applied to a certain objecttype. The information
returned includes the `is_default` flag.

