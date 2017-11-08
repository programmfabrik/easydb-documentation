### jQuery object extensions

#### Utility extensions

\$().outerHTML()

?

##### Returns

`string` html contents

\$().value()

returns the element value

##### Returns

`mixed` true/false for checkboxes, val() otherwise from the first node

\$().value(set)

sets the element value

##### Parameters

 `set: mixed`
:   true/false for checkboxes, appropriate values otherwise

\$().attrs()

return all attributes from the first node

##### Returns

`object` all attributes as name-vaalue pairs

\$().arrayIntersect(a, b)

return the common elements of two arrays as a new array

##### Parameters

 `a: array`
:   first array to search through

 `b: array`
:   second array to search through

##### Returns

`array` an array containing all elements found in both arrays

#### Widget extensions

\$().ez5datetimepick(field, data)

constructs a input element for picking date and/or time and appends it
to a jQuery object.

##### Documentation

see [ez5.datetimepick](../ez5/datetimepick/datetimepick.html)

\$().ez5edittable(opts)

renders a table and appends it to a jQuery object.

##### Documentation

see [ez5.edittable](../ez5/edittable/edittable.html)

\$().ez5modal(opts)

constructs a modal, appends it to a jQuery object, and shows it.

##### Documentation

see [ez5.modal](../ez5/modal/modal.html)

\$().autoCSSInit(class\_name)

apply autoCss styling rules to an element.

##### Documentation

see [ez5.autoCSS](../ez5/autoCSS/autoCSS.html)
