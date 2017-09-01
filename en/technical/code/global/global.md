### Global functions

\$xml(element, ns\_short)

creates an xml schema element

##### Parameters

 `element: string`
:   element name. Namespace `es:` is mapped to
    `http://schema.programmfabrik.de/easydb-database-schema/0.1`

 `[ns_short]: string`
:   if the element contains no namespace string,

    -   `"easydb-mask"` maps to
        `http://schema.programmfabrik.de/easydb-mask-schema/0.1`

    -   `"database"` maps to
        `http://schema.programmfabrik.de/database-schema/0.1`

##### Returns

`$()` a jQuery object containing a namespaced element.

includeScript(src)

dynamically loads a Javascript file

##### Parameters

 `src: string`
:   file uri

isUndef(obj)

shortcut for typeof obj === "undefined"

##### Parameters

`obj: object`

##### Returns

`boolean`

isString(obj)

shortcut for typeof obj === "string"

##### Parameters

`obj: object`

##### Returns

`boolean`

isNull(obj)

shortcut for isUndef(obj) || obj === null

##### Parameters

`obj: object`

##### Returns

`boolean`

s(obj):

alter `null` to an empty string

##### Parameters

`obj: object`

##### Returns

`string | obj`

toXml(obj)

one-step XML serialization to a string

##### Parameters

`obj: object`

##### Returns

`string`

removeFromArray(value, arr)

save removal of a value from an array

##### Parameters

 `value: mixed`
:   to look up `arr: array` the array to alter

copyObject(obj, deep)

make a copy of an object

##### Parameters

 `obj: object`
:   the object to copy

 `deep: boolean`
:   whether to make a deep copy

isEmpty(obj)

shortcut for isNull(obj) || obj === ""

##### Parameters

`obj: object`

##### Returns

`boolean`

isTrue(obj)

evaluates not-null objects, `1`, `"1"`, `true` and `"true"` as `true`

##### Parameters

`obj: object`

##### Returns

`boolean`

isFalse(obj)

evaluates `null`, `undefined`, `0`, `false`, `"0"` and `"false"` as
`false`

##### Parameters

`obj: object`

##### Returns

`boolean`

nl2Br(s)

exchanges `\n` for HTML `<br/>`

##### Parameters

`s: string`

##### Returns

`string`

toHtml(data)

escapes HTML entities `<`, `>` and `&`

##### Parameters

`data: string`

##### Returns

`string`

formatXml(xml)

pretty-print XML strings

##### Parameters

`xml: string`

##### Returns

`string`
