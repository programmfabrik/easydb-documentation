---
title: "85 - Confirmation responses"
menu:
  main:
    name: "Confirmation responses"
    identifier: "technical/confirmation"
    parent: "technical"
---
# Confirmation responses

A confirmation response indicates that the action requested can be completed, but it requires some feedback from
the user. The response provides information about the confirmation page that has to be presented to the user, as
well as the actions that the client must do according to the choices made by the user.

## Format

Its general format is an object containing a single attribute `tasks`, which is an array of objects with the  following structure:

| Name    | Description   |
|---------|---------------|
| `title`   | Title of the task: (string) translated to the session language, or (map) with a frontend code and parameters (\*) |
| `message` | Message to be displayed: (string) translated to the session language, or (map) with a frontend code and parameters (\*) |
| `form`    | Form elements (array of form elements, optional): see below "Form Elements" |
| `buttons` | Buttons (array of buttons, optional): see below "Buttons" |

### Form elements

Some tasks present form elements. A form element contains:

| Name    | Description   |
|---------|---------------|
| `label`   | Label of the form element: (string) translated to the session language, or (map) with a frontend code and parameters (\*) |
| `name`    | Name of the element (string): see below "Actions" |
| `type`    | Form type (string): there is currently one type: **options** |
| `options` | Array of: |
| &#8614; `text`  | Text to show to the user: (string) translated to the session language, or (map) with a frontend code and parameters (\*) |
| &#8614; `value` | Value for the element (string): see below "Actions" |

### Buttons

The confirmation page requires one or more buttons, which mark the end of the confirmation
procedure. The client must always show a "Cancel" button.

Other buttons are specified as follows:

| Name    | Description   |
|---------|---------------|
| `text`  | Text to show to the user: (string) translated to the session language, or (map) with a frontend code and parameters (\*) |
| `name`  | Name of the element (string, optional): see below "Actions" |
| `value` | Value for the element (string, optional): see below "Actions" |

### (\*) Frontend Codes with Parameters

To let the frontend translate the message (see [User Errors](/en/technical/errors)), instead of a translated string a map with a frontend code and a list of parameters is sent for a key.

Example:

```javascript
{
    "tasks": [
        {
            "message": {
                "code": "server.confirm.delete_object_with_children.message",
                "parameters": {
                    "objecttype": "hierarchic_objecttype",
                    "children_count": 4
                }
            }
        },
        ...
    ]
}
```

The frontend will select the translation of the text with the key `code` in the current user frontend language, and replace parameter placeholders like `%(objecttype)s` with the corresponding parameter values.

## Actions

**For each task, a confirmation page is showed:**

When a button is pressed, the client proceeds. If it is the "Cancel" button, the confirmation
page is closed and nothing more is done.

If it is an "Ok" button, the frontend will make sure that for every form only one option is selected
and will gather all actions:

1. If the button has a `name` and `value`, this is an action
2. For evey form element, pick the `name` and the selected option's `value`

**If all tasks are confirmed:**

The frontend then repeats the request providing all actions in the query string.

**Example:**

Request and confirmation response:


{{< include_json "./example1.json" >}}


A page is shown where the user has the options to confirm or abort the procedure. If the user
proceeds, by pressing the "Sure!" button, the form remembers the button action
("confirmation_code=g723hd67").

Then, a new page is shown where the user has to select between two options. If the user presses
the "Ok" button, the form remembers the action (for example, "project_action=delay"). If the user
presses the "Ok and notify" button, an addtional action is remembered ("project_notify=yes").

After this procedure, the frontend sends the request with the new parameters:


{{< include_json "./example2.json" >}}


The next sections describe the confirmation responses the server currently uses.

# List of confirmation responses

## <a name="transitions"></a> Confirm transitions

This response is provided by [/api/db](/en/technical/api/db) when an operation triggers one or more transitions
that require a confirmation code.

For each transition, a task is provided. The title of the task contains the transition number. The message
comes from the [transition definition](/en/technical/types/transition). There is one button ("Ok") for each task.
However, only the last button has an action associated. The name for that action is "confirm" and the value
is the confirmation code.

## <a name="corr"></a> Confirm action for collection owner rights revoked

This response is provided by [/api/db](/en/technical/api/db), [/api/objecttype](/en/technical/api/objecttype),
[/api/pool](/en/technical/api/pool) and [/api/tag](/en/technical/api/tags) when the operation revokes a right for a
collection object for the collection owner, which is granted by him via the collection ACL.

Two actions are possible (besides from cancelling the operation):

- remove the objects that are no longer in a valid state for the collection
- remove the ACL entries of the collection that grant the right which has been revoked
