# ez5.addResizeHandles

ez5.addResizeHandles(opts)

Adds the possibility to resize columns in a table-like structure by
drag&drop. Each element that can be resized is provided with a *handle*
element over the position of the right border.\
 On pressing the mouse, a marker line will appear, and each mouse
movement will move the handle horizontally until the mose button is
released. The width of the element will be changed accordingly.\
 A doubleclick will bring back the cell size to what it was initially.

## Parameters

 `opts: object`
:

     `headers: object[]`
    :   A list of objects identifying the elements that should be
        resized and the manner it should be done in. Each object takes
        the form:

         `cell: §() | DOMElement`
        :   the element that should be resized. This must be the element
            that is the sibling of other elements in the same container
            being resized. Do not use children elements here.

         `[direct]: boolean`
        :   whether the CSS `width` property of the element should be
            set directly

             *Default:* false
            :

         `[styleRule]: CSSStyleDeclaration`
        :   a style rule in a Stylesheet whose `width` property should
            be set

         `container: §()`
        :   the element where the handle should reside. This element
            must be a parent of the header and must set CSS
            *overflow:hidden*.

     `[check_left]: boolean`
    :   whether the position of the first resized object relative to its
        container may change during runtime. Use with care, there is a
        performance downside if this is used and tables are huge

         *Default:* false
        :

     `[live]: boolean`
    :   whether the CSS changes should be applied on each mouse movement
        while the button is pressed. Use with care, there is a
        performance downside if this is used and tables are huge

         *Default:* false
        :

     `[beforeResize]: function (cell)`
    :   callback function to be executed before the resizing starts
        (`mousedown` on the handle). The `cell` argument is the same
        object that was provided in the options.

     `[duringResize]: function (cell, delta, success)`
    :   callback function to be executed during resize (`mousemove` on
        the handle while the button is pressed) after the resizing has
        taken place. This function will only be called if
        [`opts.live`](#opts-live) is set to true. The `cell` argument is
        the same object that was provided in the options. `delta` is the
        movement in pixels of the handle in x direction (positive to the
        right, negative to the left). `success` is a boolean that marks
        whether the resulting cell width has a applicable value. On
        false, no resizing will have taken place.

     `[afterResize]: function (cell, delta, success)`
    :   callback function to be executed after the resizing ends
        (`mouseup` on the handle), the resizing has taken place, but
        before the handles on other cells have been repositioned. The
        `cell` argument is the same object that was provided in the
        options. `delta` is the movement in pixels of the handle in x
        direction (positive to the right, negative to the left).
        `success` is a boolean that marks whether the resulting cell
        width has a admissible value. On false, no resizing will have
        taken place.

     `[resizeDefault]: function (cell)`
    :   callback function to be executed when the user doubleclicks on
        the handle and after resizing to initial values has taken place.

## Returns

`object[]` an Array listing all containers that were provided in the
options. Each object takes the form:

 `container: $()`
:   the container element

 `handles: $()[]`
:   an Array of all handles residing in this container

# Extensions to the returned Array

.reposition(init)

trigger a repositioning of all handles. This needs to be called once
after the resizable cells are inserted into the document, and after a
cell resize was executed by other means than the drag&drop provided
here.

## Parameters

 +[init]: boolean
:   whether the cell sizes need to be recalculated. On an explicit call,
    this should be omittable.

     *Default:* true
    :

