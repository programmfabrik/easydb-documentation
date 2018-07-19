---
title: "57 - config"
menu:
  main:
    name: "config"
    identifier: "technical/api/config"
    parent: "technical/api"
---
# Get config

    GET /api/v1/config?token=<token>

Outputs the current config as visible to the current session.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Authentication

This call requires the system right `system.config`.

## Output
```json
{
	"system": { // config context
		"name": {
			"value": "<name of easydb>"
		},
		"displayname": {
			"value": {
				"de-DE": "horst db",
				"en-US": "horst db"
			}
		},
		"languages": {
			"frontend": [ "de-DE","en-US" ],
			"database": [ "de-DE" ]
		},
		"upload.limit": {
			"value": 0
		},
		"upload.image": {
			"extensions": [ "jpeg","tiff" ]
			"limit": 0
		},
		"login.internet": true,
	    "login.intranet": true,
		"logo": {
			"logo": {
				"image": {
					"id": 1000120998
				}
			}
		}
	}
}

```


|   |   |
|---|---|
| 200 | Success |
| 403 | Unauthorized session |





# Save config

    POST /api/v1/config?token=<token>

Use this call to update and insert config information.

Currently all keys need to be send at once per class. All not-sent keys
in the same class will be removed.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Authentication

This call requires the system right `system.config`.

## Input
```json
{
	"system": {
		"name": {
			"value": "<new name of easydb>"
		},
		"displayname": {
			"value": {
				"de-DE": "horst db",
				"en-US": "horst db"
			}
		},
		"languages": {
			"frontend": [ "de-DE","en-US" ],
			"database": [ "de-DE" ]
		},
		"upload.limit": {
			"value": 0
		},
		"upload.image": {
			"extensions": [ "jpeg","tiff" ]
			"limit": 0
		},
		"login.internet": true,
		"logo": {
			"logo": {
				"image": {
					"id": 1000120998
				}
			}
		}
	}
}

```


## Output

This call redirects to the given urls depending on the succes or failure
of the login attempt.

|   |   |
|---|---|
| 200 | Success |
| 400 | Bad Request. Something is malformed |
| 403 | Unauthorized session |





# Get configuration options

    GET /api/v1/config/list?token=<token>

Outputs the available config options.

|  |                    |
|-----|--------------------|
| `token` |   The session token.		 |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Output



```json
{
    "system": [ // config context
        {
            "name": "name",
            "group": "general",
            "parameters": [
                {
                    "type": "string",
                    "value": "<name of easydb>"
                }
            ]
        },
        {
            "name": "displayname",
            "parameters": {
                "value": {
                    "type": "l10n_string"
                }
            }
        },
        {
            "name": "languages",
            "parameters": {
                "frontend": {
                    "type": "list_multi",  // this results in an array
                    "choices": [ "de-DE","en-US" ]
                },
                "database": {
                    "type": "list_multi",  // this results in an array
                    "choices": [ "de-DE","en-US" ]
                }
            }
        },
        {
            "name": "upload.limit",
            "parameters": {
                "value": {
                    "type": "integer",
                    "range_from": 0,
                    "range_to": 73872397129
                }
            }
        },
        {
            "name": "upload.image",
            "parameters": {
                "extensions": {
                    "type": "list_multi",  // this results in an array
                    "required": true|false,
                    "choices": [ "jpeg","tiff" ]
                },
                "limit": {
                    "range_from": 0,
                    "required": true|false
                }
            }
        },
        {
            "name": "upload.video",
            "parameters": {
                "extensions": {
                    "type": "list_multi", // this results in an array
                    "choices": [ "avi","mp4","mkv" ]
                },
                "video_codecs": {
                    "type": "list_multi", // this results in an array
                    "choices": [ "mp4","xvid" ]
                },
                "audio_codecs": {
                    "type": "list_multi", // this results in an array
                    "choices": [ "mp3","aac" ]
                },
                "limit": {
                    "range_from": 0
                }
            }
        },
        {
            "name": "upload.audio",
            "parameters": {
                "extensions": {
                    "type": "list_multi", // this results in an array
                    "choices": [ "mp3", "m4a", "aac", "flac" ]
                }
            }
        },
        {
            "name": "upload.office",
            "parameters": {
                "extensions": {
                    "type": "list_multi", // this results in an array
                    "choices": [ "doc", "docx", "xls",... ]
                }
            }
        },
        {
            "name": "upload.other",
            "parameters": {
                "limit": {
                    "range_from": 0
                }
            }
        },
        {
            "name": "logo",
            "parameters": {
                "logo": {
                    "type": "image",
                    "eas_id": "<id>"
                }
            }
        },
        {
            "name": "administrator.emails",
            "parameters": {
                "value": {
                    "type": "string"
                }
            }
        },
        {
            "type": "intranet.nets",
            "name": "logo",
            "parameters": {
                "value": {
                    "type": "string"
                }
            }
        },
        {
            "name": "login.internet"
        },
        {
            "name": "login.intranet"
        }
    ]
}
```


# Config Variables

|Name					|Format/Parameters		| Description					|
|-----------------------|-----------------------|-------------------------------|
|`system.name`			| string `^[a-zA-Z][a-zA-Z0-9_-.]{5,31}$` | Name of the easydb. This name is used as a reference in filenames, emails, domain names.|
|`system.displayname`	| l10n-string			| Name of the easydb to display. |
|`system.logo`			| eas-id				| Base logo of this easydb. Use /api/v1/eas to get an EAS-ID.  |
|`system.administrator.emails`| multi-line string | Email-Addresses of system administrators. easydb uses this to send system related emails. There can be one email on each line.|
|`system.intranet.nets`		   | multi-line string, one network per line | Newline separated list of networks which will be considered *intranet*.|
|`system.languages`   		   | list of languages for frontend and database. | Ordered list of user available frontend languages and languages for db-l10n-fields. |
|`system.upload`   	   		   | list of fileclasses, extensions, upload limits. | This list is the global limit.  |


|Name					|Format/Parameters		| Description					|
|-----------------------|-----------------------|-------------------------------|
|`system.login.internet`	   | boolean	| Clients considered on the internet (on an IP basis) are required to login. Default is true. |
|`system.login.intranet`	   | boolean	| Clients considered on the internet (on an IP basis) are required to login. Default: true. |
|`system.login.user.send_email`	 | boolean	| If set, send emails to the user with login information. Default to set in the user record when a user is created. Default: true. |
|`system.login.user.confirm_email`	| boolean	| If set, the user needs to confirm the email. Default to set in the user record when a user is created. Default: true. |
|`system.login.password_policy` | regexp | The default password policy. Defaults to `ini:system.login.user.password_policy`. |
|`system.login.password_policy.hint` | String-L10n | Text to explain the password policy to the user. Defaults to `csv:system.login.user.password_policy.hint`. |
|`system.login.forgotten_password_process` | Boolean | The system is allowed to support a forgotten password process. |
