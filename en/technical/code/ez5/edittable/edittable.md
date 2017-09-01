#### ez5.edittable

ez5.edittable(opts)

renders a table and returns a jQuery object

\$().ez5edittable(opts)

renders a table and appends it to a jQuery object

#### Parameters

`opts: object`
:

`id: string`
:   The grid element will be given the string identifier `id`

`[class]: string`
:   class attributes given to the `<table>` elements

`[header]: boolean`
:   if `false` is given, no table header will be shown. Otherwise,
the headings defined in [`opts.fields`](#opts-fields) will be
used for a table header row.

*Default:* true
:

`[extra_header]: object[]`
:   One additional header row can be shown above the main headers by
defining an object array containing cell definitions like this:

`[th_class]: string`
:   class attributes added to the column header

`[th_label]: string`
:   language-independent column label to be rendered in the
header. If none is given, the cell will remain empty

`[th_colspan]: int`
:   number of columns the header field should span

*Default:* 1
:

`fields: object[]`
:   defines the columns of the table.\
The object will also be the opts object used for the
construction of the rendering element identified by `type`.
Therefore all options specific to the control element can be
added.\
Each object in the array takes the form:

`name: string`
:   field name used to identify the data contained in a column

`type: int`
:   one of the ez5 constants identifying control elements for
rendering the data in a column

`[th_class]: string`
:   class attributes added to the column header. A special
meaning is given to class `ez-rotate90`: if it is included,
the header label will be shown rotated by 90°

`[th_label]: string`
:   language-independent column label to be rendered in the
header. If none is given, the cell will remain empty

*Default:* ""
:

`[th_label_localized]: string`
:   language-specific column label to be rendered in the header.
No localization routine will be applied. If this is given,
it superseeds `th_label`

*Default:* ""
:

`[render_in_idx]: int`
:   if given, this field will be rendered not in its own column,
but appended to the column that was described in the fields
array entry with that number

`[colspan]: int`
:   number of columns the content row cell should span

*Default:* 1
:

`[td_class]: string`
:   class attributes added to the content row cells

`[sort_column]: boolean`
:   if true, rows can be sorted by the values in that column.
The header will be appended with controls for defining sort
order and sort priority,

*Default:* false
:

`[sort_order]: string`
:   If the data contained in the field are of the Javascript
type Boolean, Number or Date, the sort order of that column
will always be numerical. If they are strings, comparisons
will be based on this option: "locale" sorts by using the
Javascript String.localeCompare() function (which means it
will use the Browser-defined locale, not the application
localization!), "numerical" will implicitely convert values
to numbers. Other datatypes are not ordered.

*Default:* "locale"
:

`[$footer]: $()`
:   One or more jQuery objects that will be added in a line below
the table.

`[row_content_height]: int[]`
:   A number of heights in pixels that should be used as the height
of a row. Each number stands for the height of one subsidiary
level, starting with top level rows.\

*Default:* If no height is given for a level, a row will be rendered with a fitting height. This might lead to a massive performance degradation for rendering a table with more than a few rows
:

`[prev_content_height]: int`
:   A number of heights in pixels that should be used as the height
of a [interspersed header](#virtual_prev_row) shown above a
row.\

*Default:* If no height is given, the header will be rendered with a fitting height. This might lead to a massive performance degradation for rendering a table with more than a few rows
:

`[next_content_height]: int`
:   A number of heights in pixels that should be used as the height
of a [interspersed footer](#virtual_prev_row) shown below a
row.\

*Default:* If no height is given, the footer will be rendered with a fitting height. This might lead to a massive performance degradation for rendering a table with more than a few rows
:

`[rows]: object[]`
:   The data the table will initially contain. For the format of
each object, see [Row data object](#Data).

`[virtual_load]: object`
:   If this object exists, rows will be loaded dynamically after the
initialization of the table (Virtual Grid). If the option is
given, the functions `total_row_number` and `load_chunk` need to
be present:

`row_data_provider: function (row, number, start, sort, callback)`
:   return some rows from the data source. The parameters are:

`row: object[]`
:   Either `undefined` for top-level rows or a [Row data
object](#Data) that the rows to be loaded are subsidiary
to.

`number: int`
:   the number of rows to load

`start: int`
:   zero-based number of the first row to load, relative to
all rows

`sort: object[] | null`
:   the currently applied column sort object. If no sorting
should be applied, this parameter may be null. See
[`opts.default_row_sort`](#opts-default_sort) for a
description of the format.

`callback: function (chunk)`
:   When row data are ready to be delivered, they must be
passed back by calling this function. The parameter
`chunk` must must be an array of [Row data
objects](#Data). If for a row there exist some
subsidiary rows, the row parameter `rows` must set to
`true`. They will then be loaded as needed in a
subsequent call.

`total_row_number: function (row, callback)`
:   return the total number of rows in the data source.

`row: object[]`
:   Either `undefined` for top-level rows or a [Row data
object](#Data) that the rows to be inspected are
subsidiary to.

`callback: function (length)`
:   When the total number of rows is ready to be delivered,
it must be passed back by calling this function. The
parameter `length` must must be an integer greater than
or equal 0.

`[padding]: int`
:   If there are regions of the table outside its visible part,
they can be reached by scrolling. At each time, only a
limited number of rows will be loaded in these regions. This
number defines the height in pixels that will contain such
rows, both above the visible top or below the visible
bottom, provided the end of the table is not reached first.
Further removed rows will not be added to the markup or will
be removed.

*Default:* 2000
:

`[delay]: int`
:   Scrolling the table will trigger a check wether new rows
need to be loaded by calling `load_chunk`, or if loaded rows
can be removed. This number defines a minimum time in
milliseconds that will pass between two such subsequent
checks.

*Default:* 50
:

`[plain]: boolean`
:   If `true` is given and rows are loaded directly, all rows
present in the loaded object will be shown, even if they are
subsidiary. In the case of a virtual grid, only the top level
rows will be rendered. On `false`, superior rows will be
rendered with a tree handle that can be used to expand or hide
the subsidiaries.\
`true` will also have the same effect as setting
[`frozen`](#opts-frozen) to 0, namely no horizontal scrolling
mechanism is provided, and the last column will expand to a size
so that the table will allways fill out the grid width.\
Setting this option to `true` excludes the use of the features
set with the options [`resizable_columns`](#opts-resizable),
[`selectable`](#opts-selectable) and
[`rows_sortable`](#opts-sortable).\

*Default:* false
:

`[frozen]: int`
:   the number of columns at the left side of the table that are
excluded from the horizontal scrolling mechanism. Setting
[`plain`](#opts-plain) to `true` or this option to `0` are
equivalent: no horizontal scrolling mechanism is provided, and
the last column will expand to a size so that the table will
allways fill out the grid width. `plain=true` supercedes setting
`frozen`.\
In case the table has only one column and `frozen` is set to 1,
no horizontal scrolling mechanism is provided, and the column
will allways fill out the grid width.

*Default:* 1
:

`[resizable_columns]: boolean`
:   If `true` is given, all column widths will be resizable by
dragging their right border in the header region with the mouse.
A double click on the border will reset the column width to its
default.\
The default width is the larger content width of the header and
the first currently loaded row. If either the column header or a
content cell has a class that defines a width, rules for the
layout of HTML table columns apply to this default.\
The default width as defined above is only applied on initial
load or for a column after a double click. At any other time,
the column width is held constant and changed only as a result
of user action.\
If `false` is given, columns remain at their default size, even
if the content cannot fit into this width. If
[`plain`](#opts-plain) is set to `true` or the table has only
one column, this option will have no effect.

*Default:* true
:

`[selectable]: boolean`
:   if `true` is given, one row can be marked by clicking on it. The
selected row will have a `data.selected` value of `true`.\
If [`plain`](#opts-plain) is set to `true`, this option will
have no effect.

*Default:* false
:

`[rows_sortable]: boolean`
:   if `true` is given, the position of a row can be changed by
dragging it vertically to another position. If the table
contains hierarchically ordered rows, dragging is restricted to
positions where hierachies will not be impacted.\
If [`plain`](#opts-plain) is set to `true`, this option will
have no effect.

*Default:* false
:

`[columns_sortable]: boolean` *(Not yet implemented)*
:   if `true` is given, the position of a column can be changed by
dragging it horizontally to another position.
[Frozen](#opts-frozen) columns are excluded and can never be
dragged.

*Default:* false
:

`[default_row_sort]: object[]`
:   Initial sort order for the rows. Rows will be ordered first by
the first given field, then by next item, and so on. Each sort
description object takes the form:

`field: string`
:   must match a field name

`order: string`
:   sort direction, `"ASC"` for ascending, `"DESC"` for
descending order

`[click]: function (event)`
:   global callback function to be executed when the table body is
clicked. The `event` argument is the jQuery event object.

`[start_add_row]: function ($tr)`
:   callback function to be executed before a row is rendered. This
function will be executed also if a previously hidden subsidiary
row is shown and on each reordering of the rows. The
[`$tr`](#Tr) argument is a jQuery object containing the rendered
row.

`[end_add_row]: function ($tr)`
:   callback function to be executed after a row is rendered. This
function will be executed also if a previously hidden subsidiary
row is shown and on each reordering of the rows. The
[`$tr`](#Tr) argument is a jQuery object containing the rendered
row.

`[selected]: function ($tr)`
:   callback function to be executed when a row is selected. The
[`$tr`](#Tr) argument is a jQuery object containing the selected
row.

`[deselected]: function ($tr)`
:   callback function to be executed when a row selection ends,
either because another row is selected, or the row is clicked a
second time. The [`$tr`](#Tr) argument is a jQuery object
containing the previously selected row.

#### Extensions to the returned jQuery Object

\$edittable.sort\_rows(sort)

Sorts the table (chainable).

##### Parameters

`sort: object[]`
:   If not given, the current column sort will be re-applied. If an
argument is given, it supplants the current sort with a new one.
Thus, giving an empty array will remove any sort.\
Rows will be ordered first by the first given field, then by next
item, and so on. Each sort description object takes the form:

`field: string`
:   must match a field name

`order: string`
:   sort direction, `"ASC"` for ascending, `"DESC"` for descending
order

##### Returns

`$()` a jQuery object containing the table.

\$edittable.get\_selected\_\$tr()

Returns the selected row as a [jQuery object](#Tr).

##### Returns

`$()` a jQuery object containing the row element. Extensions to this
object are described separately [below](#Tr).

\$edittable.load\_data(rows\_tmp)

Loads all rows in one chunk (chainable). All previously loaded rows will
be discarded.

##### Parameters

`rows_tmp: object[]`
:   The data the table will contain. For the format of each object, see
[Row data objects](#Data). Giving an empty array will empty the
table.

##### Returns

`$()` a jQuery object containing the table.

\$edittable.get\_rows()

Returns the row data currently contained in the table, in their current
sort order. Hidden subsidiary rows will also be returned.

##### Returns

`object[]` Data for each row. For the format of each object, see [Row
data objects](#Data).

\$edittable.add\_row(row)

Add a single row to the table (chainable).

##### Parameters

`row: object`
:   A [row data object](#Data) as described below, containing those
options that may be used for defining a row

##### Returns

`$()` a jQuery object containing the table.

\$edittable.render()

Initialize the table layout (chainable). This function must be called
once after the element is both

-   inserted into the document DOM

-   and actually rendered, i. e. not hidden by setting `display=none` or
other mechanisms preventing the CSS engine from returning
meaningfull values for positions and sizes of its constituent HTML
elements.

##### Returns

`$()` a jQuery object containing the table.

\$edittable.data()

Returns no data

#### Row data objects

Row data can be acccessed through the [`get_rows()`](#get_rows) method
or through the table row object by calling `$tr.data("row")`. From the
following members the first may be used in a [`add_row()`](#add_row) or
[`load_data()`](#load_data) method call. The second group will be
returned after initialisation (rendering).

##### Members

**For the use in defining a row:** \
`[data]: object`
:   a named list of values to be rendered in that row. Keys must match a
field name.

`[fields]: object[]`
:   defines the columns of the row. Each field object has the same
format as described above for [`opts.fields`](#opts-fields)\
Columns are identified by the `name` option. If `opts.fields`
contains an object with the same `name`, all its members will be
mixed into the row-specific object with `$.extend()`. (which means
specific options take priority.) If a column `name` is missing, a
copy of `opts.fields[name]` is used instead.

`[rows]: object[]`
:   an array of subsidiary rows attached to this row. The syntax for
each object is the same as for the parent row.

`[has_children]: boolean`
:   If [`opts.virtual`](#opts-virtual) is given, subsidiary rows will
only be fetched when their branch of the tree is rendered. In this
case, a value of `true` will indicate that there are potentially
loadable rows.

`[virtual_prev_row]: $()`
:   One or more jQuery objects that will be added in a line above the
row. If the row is sortable by dragging, it will be moved together
with that header.

`[virtual_next_row]: $()`
:   One or more jQuery objects that will be added in a line below the
row and potential subsidiaries. If the row is sortable by dragging,
it will be moved together with that footer.

`[selected]: boolean`
:   if true and if also opts.selectable is true, the row will initially
be shown as selected.

*Default:* false
:

`[opened]: boolean`
:   if `false`, subsidiaries of this row will initially be hidden.

*Default:* false
:

**Returned from the initialized (rendered) object:** \
`data.$tr: $()`
:   the [jQuery object](#Tr) representing the rendered row

`path: int[]`
:   an array describing the position of the row in the hierachy of rows.
A top-level row will have only one entry giving the index of the row
considering only the top-level. For subsidiary rows, the last entry
gives the index considering only the immediate siblings, while
preceding entries describe the indices of the parent rows

`[father_row]: object`
:   the data object describing the immediate parent row. `undefined` for
top level rows.

`is_selected: function()`
:   returns a boolean exposing whether the row is selected

`select: function()`
:   selects the row

`deselect: function()`
:   cancel the selection of the row

`update: function()`
:   render all fields in this row anew. Connected header/footer-rows are
not affected

`[open]: function()`
:   shows the immediate subsidiaries of the row. Only exists if the row
object contains a `rows` array.

`[close]: function()`
:   hides all subsidiaries of the row Only exists if the row object
contains a `rows` array.

`[add_row]: function(row)`
:   adds a single subsidiary row to this row and renders it. Only exists
if the row object contains a `rows` array.

#### Row elements

Row elements in the form of jQuery objects can be accessed through calls
to [`get_selected_$tr()`](#get_selected_tr) or from row data objects as
`row.data.$tr`.\
The elements containing the cell content, as defined by
[`opts.fields.type`](#opts-fields), are rendered as direct children of
their `<td>` element if [`opts.resizable_columns`](#opts-resizable) is
set to `false`, otherwise they are rendered as children of a
`<div class="ez-edittable-forced">` element.

##### Extensions to the returned jQuery Object

\$tr.remove\_row()

removes the row from the table

\$tr.select()

selects the row

\$tr.deselect()

cancel the selection of the row

\$tr.data()

**Returns**

`object`
:    `row: object`
:   the row data object

`[$_prev_tr]: $()`
:   a header row associated to the row. The actual content is placed
inside a `<div class="ez-edittable-wrapper">`.

`[$_next_tr]: $()`
:   a footer row associated to the row The actual content is placed
inside a `<div class="ez-edittable-wrapper">`.

`[connected]: $()`
:   if [`opts.plain`](#opts-plain) is set to false, the frozen
columns are moved to an extra table. This object contains the
connected row element in the frozen table. Note that `$tr` will
still contain the same number of empty cells as placeholders as
there are frozen columns, while the actual contents are moved to
the connected row, and placed inside a
`<div class="ez-edittable-wrapper">`.\
The connection is actually two-sided, calling
`$tr.data("connected").data("connected")` would therefore lead
back to the original row element.

