# easydb API

The easydb server offers a RESTful API over HTTP. Almost all operations require a session token, which can be acquired and
authenticated with <a href="../../technical/api/session/session.html">/api/v1/session</a>. This token is passed in the query string as the parameter
`token`.

## HTTP Request

Unless otherwise stated, all API calls use the following structure:

- URL path that may contain path parameters. These are described in the section "Path parameters"
- URL query string that may contain other parameters. These are described in the section "Query string"
    - optionally, the query string parameters may be passed in the body using the Content-Type "application/x-www-form-urlencoded", provided the call does not expect a body
- Many API calls expect data in the HTTP Request body. This data is described in the section "Input". Unless stated otherwise,
the input format is JSON.

The HTTP Content-Type must be set according to the input given:

- JSON (the most common), as `application/json` (`charset=utf-8` is recommended)
- XML, as `text/xml` (`charset=utf-8` is recommended)
- Binary, as `multipart/form-data`

## HTTP Response

The server will sometimes provide output data in the HTTP Response.
Unless stated otherwise, the output format is JSON.
The server will set the HTTP Response Content-Type accordingly.

There are three types of responses:

| Reponse Type | HTTP status code | Description |
|--------------|------------------|-------------|
| Success      | 200              | The request was successful. The data format is described in the "Output" section of the API call |
| Partial      | 202              | The request was partially successful. More information and/or actions from the user are required. These kind of responses can be found in the section [Confirmation responses](../../technical/confirmation/confirmation.html) |
| Error        | 400 / 500        | The request was unsuccessful. The errors are described in the section [Errors](../../technical/errors/errors.html). A status code of 500 is an internal server error; 400 means an expected error occurred |

The section "HTTP status codes" of each API call contains a description of the possible responses.

The server always returns the following response headers:

- X-Easydb-Base-Schema-Version: the current base schema version
- X-Easydb-User-Schema-Version: the current user schema version
- X-Easydb-API-Version: the API version
