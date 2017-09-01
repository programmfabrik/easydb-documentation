#### ez5.server

ez5.server(opts)

wraped ajax call, so we have debug and some generic error handling. On
502 error (bad gateway), calls will be repeated every 2.5 seconds

##### Parameters

 `opts: object`
:   the associative array of settings sent to the `jQuery.ajax()`
    method. Additionally, these options can be set:

     `success: function(data)`
    :   callback function for successfull requests.\
         The data parameter contains the data returned from the server.
        The function is wrapped before being supplied to
        `jQuery.ajax()`.

     `error: function(xhr)`
    :   callback function in case an error occured. If no error handling
        function is supplied, [error\_handler()](../error_handler/error_handler.md) is
        called, so that the error message will be displayed on screen.\
         The xhr parameter is the jQuery xhr object. The function is
        wrapped before being supplied to `jQuery.ajax()`.

     `json_data: JSON`
    :   data to be sent to the server as a JSON object

     `complete: function(data)`
    :   This option is overwritten and cannot be set.

