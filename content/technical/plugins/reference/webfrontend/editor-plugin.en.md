---
title: "Editor Plugin"
menu:
  main:
    name: "Editor plugin"
    identifier: "technical/plugins/reference/webfrontend/editor-plugin"
    parent: "technical/plugins/reference/webfrontend"
---

# Editor plugin

The editor plugin is a general callback plugin for the editor. 

The example Plugin contains an [example for this Plugin](https://github.com/programmfabrik/easydb-plugin-examples/blob/master/src/webfrontend/ExampleEditorPlugin.coffee).

Currently there is one Callback implemented.

## checkForm(opts)

The method is called with every form update. The method can return an Array of instances of **CheckDataProblems**.

Most important info in **opts**:

| key          | description                                                  |
| ------------ | ------------------------------------------------------------ |
| resultObject | Instance of ResultObject. This has all information about the current object. Use **.getData()** to get the current map of data. |
| editor       | Instance of the Editor. Use that (**editor_info**) to check which editor you are in. |

A **CheckDataProblem** takes:

| option        | description                                                  |
| ------------- | ------------------------------------------------------------ |
| text          | The text describing the problem, this needs to be localized. Use **$$("<loca.string.key>")** to localize a CSV loaded key |
| field         | The instance of the field where the problem exists.          |
| renderedField | The instance of the rendered field where the problem exists. It is used to set the red triangle marker in the Frontend. The rendered field can be obtained from the data map. Inside the data map each field has a corresponding entry with a key called **\<name of the field\>:rendered**. This can be used to set the rendered Field option. |

```coffeescript
class ez5.ExampleEditorPlugin extends ez5.EditorPlugin
	checkForm: (opts) ->
		data = opts.resultObject.getData()
		problems = []

        // this is a bogus check if any of the provided data reads "Example"
		ok = false
		for k, v of data[data._objecttype]
			if v == "Example"
				ok = true
				break;

		if !ok
			problems.push(new CheckDataProblem(text: "ExampleEditorPlugin: One field needs to be filled with **Example**."))

		return problems

ez5.session_ready ->
	Editor.plugins.registerPlugin(ez5.ExampleEditorPlugin)
```

