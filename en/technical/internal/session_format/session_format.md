# Markdown source example for the api/session page

		# Start a session
		---
		###### GET /api/session[?token=token][&signout=1]

		With no `token` given, this call starts a new session It returns a
		session object which contains a `token` and is unauthorized. The `token`
		is required for all other api calls.

		With a `token` given, the call returns the current session object.

		If the system is not yet configured (has no users), the session gets all
		available system rights and is immediately authenticated.

		If the optional `signout` parameter is given, the session is
		de-authenticated and the user need to login again.


		## Authentication

		This call requires no authentication.

		## Parameters


		|  |                    |
		|-----|--------------------|
		| `token` |   The session token 			 |
		|`signout`|        |


		## Returns
		### Example output:



		```
		{
			token: "c473472d-c085-4043-9bf0-ee80bff73d40",
			authenticated: "false/true",
			system_rights: "[right1, right2, right3]",
			max_message_id: "1234" // current MAX(ez_message_log:id)
		}
		```


		| Http Status Codes |                    |
		|-------------------|--------------------|
		| *200* 			|   OK 			 |
		| *400*             |   Bad Request. Something is malformed. |
		| *404*             | Not Found. If a `token` was given and the session was not found. |
		| *500*  			|  Internal Server Error. |

		---

		# Authenticate a session
		---

		###### POST /api/session/authenticate


		Use this call to authenticate a session using the provided user
		credentials.


		## Authentication

		This call requires no authentication.


		## Parameters
		|  |                    |
		|---|---|
		| `token` |   The session token |


		## Input

		|  |                    |
		|-----|--------------------|
		| `login` |   &lt;login&gt; |
		| `password` |   &lt;password&gt;|
		| `token` |   &lt;token&gt; |
		| `success` |   &lt;url-to-redirect-to-if-success&gt; |
		| `error` |   &lt;url-to-redirect-to-if-error&gt;  |



		## Returns

		This call redirects to the given urls depending on the success or
		failure of the login attempt.



		| HTTP Status Codes|                    |
		|-------------------|--------------------|
		| *302* 			|   Redirect to success or error page.		 |
		| *400*             |   Bad Request. Something is malformed. |
		| *403*            |   Forbidden. The token is invalid. |
		| *500*  			|   Internal Server Error. |



