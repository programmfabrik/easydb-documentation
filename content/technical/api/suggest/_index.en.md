---
title: "77 - suggest"
menu:
  main:
    name: "suggest"
    identifier: "technical/api/suggest"
    parent: "technical/api"
---
# Suggestion / Autocompletion

    POST /api/v1/suggest?token=\<token\>

Autocomplete a user query.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Input

The input is provided as a JSON object with the following attributes:

| Name                  | Description                                                                     |
|-----------------------|---------------------------------------------------------------------------------|
| `objecttypes`         | Object types that are taken into accout for the autocompletion (array of strings) |
| `query`               | The user query to be autocompleted (string, optional): defaults to `""` |
| `tokens`              | Whether this call returns token suggestions (boolean, optional): defaults to **`true`** |
| `fields`              | Fields to be taken into account for the autocompletion (array of strings, optional\*) |
| `languages`           | Languages to be taken into account for l10n fields (array of strings, optional): defaults to all search languages of the user |
| `linked_objecttypes`  | Suggest also linked objects from this objecttypes (array of strings, optional\*) |
| `analyze_wildcards`   | Whether wildcards (`"*"` and `"?"`) are allowed in the `query` (boolean, optional): defaults to **`false`** |
| `tokens_mode`         | How the query token will be matched against the suggest index: For `"ngram"` the token matches against the `ngram` subfield; for `"edgengram"` the token matches against the `left_ngram` subfield (for a prefix search); for `"exact"` the token matches against the `folded` subfield (exact search for the whole token). (string, optional, defaults to `"ngram"`) |
| `timeout`             | If set, the request will return after the timeout with the results gathered so far (integer, optional): time in ms |
| `limit`               | Number of items to return in each response type (`"tokens"`, `"fields"`, `"linked_objects"`) (integer, optional, defaults to **10**) |

Remarks:

- `linked_objecttypes` and `fields` cannot be set simultaneously
- `languages` are only taken into account if `fields` are given
- `timeout` is only used for the Elasticsearch request to retrieve tokens. It does not affect the requests for fields and linked
objecttypes. The whole API call may take longer than the given value.

Example:


{{< include_json "./example.json" >}}


## Procedure

- The `query` can contain any number of tokens. Suggest will search objects containing all tokens
 and autocomplete the last one.
Suggest is permissive and will match case-insensitive and ICU folded. If `query` is empty, the best suggestions
(for the given tokens or overall) are returned.

- The `query` can include wildcards if the flag `analyze_wildcards` is set (if not, they will be treated like normal characters).
Currently supported wildcards are "*" for "any number of characters, including 0" and "?" for "none or one character".

- The query is furthermore restricted by the given `objecttypes`, `fields` and `languages`.

- If there are `linked_objecttypes`, suggest will search in the related linked objects based on the results in the main objects.


## Output

The output is given as a JSON object. The input attributes are provided as a copy in the output.
The rest is the real output of the autocompletion:

| Name                  | Description                                                                     |
|-----------------------|---------------------------------------------------------------------------------|
| `es_time`                    | Time this request took in the Elasticsearch query/queries in milliseconds (integer) |
| `timed_out`                  | Whether the request timed out (boolean): only present if the input parameter `timeout` was set |
| `suggestions`                | Object that MAY contain the following lists:                                |
| `suggestions.tokens`         | - List of results of the "token" type (see below)                           |
| `suggestions.fields`         | - List of results of the "field" type (see below)                           |
| `suggestions.linked_objects` | - List of results of the "linked object" type (see below)                   |

### Type "tokens"

If the request parameter `tokens` is **false**, no tokens are returned.

The autocompleted tokens are ordered by descending reference count.
If a suggestion is considered an "exact match" of the last query token,
it is marked so. Exact match means that a complete token matching the request (that is, ICU folded) was found. Exact
matches are given priority and pushed to the beginning of the list. Each token suggestion has the following
properties:

| Name                  | Description                                                                     |
|-----------------------|---------------------------------------------------------------------------------|
| `suggest`             | The suggestion, with `<b></b>` markers for the given part (string)              |
| `tokens`              | The tokens that build up the suggestion (array of strings)                      |
| `count`               | The number of occurrences of the autocompleted token (integer\*)                |
| `exact_match`         | Whether the autocompleted token was found exactly as given (boolean)            |

Remarks:

- `count` refers to the number of objects the token was found in, regardless of how many times it occurs in one document

### Type "field"

These suggestions are only given if `fields` is set and the field is not of type "string". They show the whole field
and not just the autocompleted tokens.

| Name                  | Description                                                                     |
|-----------------------|---------------------------------------------------------------------------------|
| `field`               | The complete field text that matches (string)                                   |
| `suggest`             | The suggested field, with `<b></b>` markers for the given part (string)         |
| `count`               | The number of occurrences of the autocompleted field (integer)                  |

### Type "linked_object"

These are objects that are linked to the main objects and match the autocompletion.

| Name                  | Description                                                                     |
|-----------------------|---------------------------------------------------------------------------------|
| `object`              | The linked object ([object](/en/technical/types/object))                                |

The linked object is annotated with highlights, in the same way as in the results of [/api/v1/search](/en/technical/api/search).

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | Error parsing request: attribute expected, incorrect type or value |
| 403 | Unauthorized session |
| 404 | Objecttype or field not found |
