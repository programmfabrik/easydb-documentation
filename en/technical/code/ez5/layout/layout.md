#### ez5.layout

ez5.layout(opts)

Sets the JQuery.Layout for the current page. Options for north, south
and center layouts are set to fixed values. Resizing of the center pane
triggers the [ez5.layout\_resize](../layout_resize/layout_resize.md) function.

##### Parameters

`opts: object`
:   Layout widths for east and west panel. Giving -1 will hide the pane,
0 will close it.

+east: int
:    *Default:* 200
:

+west: int
:    *Default:* 250
:

