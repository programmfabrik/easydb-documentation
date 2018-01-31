# Retrieve the list of plugins

    GET /api/v1/plugin

Returns a list of available plugins.

## Output

The output is an array of plugin descriptions. Each description contains the "plugin" part of the JSON file that
describes the plugin. The following fields are always part of the description:

| Name           | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `name`         | Plugin name (string)                                                        |
| `base_url`     | URL for the plugin content (string): relative path from the easydb base URL |

## Permissions

This call does not require any permission.

## HTTP status codes

|Code|Status|
|----|------|
| 200| Success |
| 500| [Server error](/technical/errors/errors.html#server_error): internal server error |
