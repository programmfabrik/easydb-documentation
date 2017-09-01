### ez5.modal

ez5.modal(opts)

Constructs a Bootstrap-based
[modal](http://twitter.github.com/bootstrap/javascript.html#modals) and
shows it. It is composed of a header with a caption and a cancel/close
button, a content body and a footer containing one or more buttons.

\$().ez5modal(opts)

constructs a modal, appends it to a jQuery object, and shows it.

#### Parameters

`opts: object`
:   Only one of the options `text`, `error_text`, `$body` and
`form_opts` may be used.

`title: $.text()`
:   Title text of the modal.

`title_tag: string`
:   The HTML tag to use for the title.

*Default:* `<h3>`
:

`text: $.text()`
:   Content text of the modal.

`error_text: object`
:   Content text that displays an error to the user.

`$body: $()`
:   A more complex content structure for the modal. It will be
embedded into the outer content `<div>`.

`form_opts: object`
:   Options for the construction of a [ez5.form](../form/form.md) element.

`attr: string[string]`
:   A map of attribute-value pairs to set for the element. Set class
attributes will be dismissed.

`auto_height: boolean`
:   Enables automatic height resizing.

`buttons: button`
:   One or more custom buttons that are shown in the footer.

`cancel: function()`
:   Custom function to perform when the user clicks on a button.

`error_verbose: $.text()`
:   Additional content diplayed below the other content.

#### Extensions to the returned jQuery Object

ez5.modal.dismiss()

hides the modal.

\$modal.data()

Returns no data
