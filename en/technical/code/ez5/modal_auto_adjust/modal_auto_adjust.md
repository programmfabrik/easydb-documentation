#### ez5.modal\_auto\_adjust

ez5.modal\_auto\_adjust(\$mod)

Enables automatic height resizing for a [ez5.modal](../modal/modal.md) manually.
The function is also called if `modal` is constructed with the
`auto_height` parameter set.

##### Parameters

 `$mod: ez5.modal`
:   The modal that should be resizable.

     `[mod.set_heights]: function()`
    :   A custom resizing function. If not set, a default function is
        used for resizing.

