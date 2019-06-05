---
title: "81 - Python"
menu:
  main:
    name: "Python"
    identifier: "technical/api/tutorial/python_tutorial"
    parent: "technical/api/tutorial"
---

# Python Quickstart

Use python with requests

## Table of Contents

 - [Getting Started](#getting-started)
 - [Purpose](#purpose)
 - [HTTP status codes](#http-status-codes)
 - [Command line](#running-from-the-command-line)
 - [Results](#results)
 - [Methods](#methods)
    - [Start Session](#start-session)
    - [Retrieve Current Session](#retrieve-current-session)
    - [Authenticate Session](#authenticate-session)
    - [Deauthenticate Session](#deauthenticate-session)
    - [Search](#search)
    - [Server Information](#server-information)
 - [`tutorial.py`](#tutorial-py)
 - [`criteria_template.json`](#criteria-template-json)

## Getting Started

To get started, please complete the following steps

1. [python 2.7 downloaded](https://www.python.org/downloads/),
    - Set up environment -> [here's how](https://www.tutorialspoint.com/python/python_environment.htm)

2. [install Requests](http://docs.python-requests.org/en/master/user/install/)
    - User friendly library for making HTTP requests

3. Copy the [code](#tutorial-py) at the end of this page and save (as `tutorial.py`)

4. Copy and save the [JSON text](#criteria-template-json) (as `criteria_template.json`)

## Purpose

The `tutorial.py` script attempts a couple simple interactions with your easydb database.

- [Start new session](#start-session)
- [Retrieve current session with session token](#retrieve-current-session)
- [Session Authentication](#authenticate-session)
- [Session Deauthentication](#deauthenticate-session)
- [Search assets](#search)
- [View server information](#server-information)

Every interaction will print a HTTP status code to the console

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 500 | [Server error](/en/technical/errors): internal server error |

- _Reference_

    [HTTP Status Codes](https://docs.easydb.de/en/technical/api/session)

## Running from the command line

`tutorial.py` may be run from the command line.

- easydb server url in the `--server_url` argument
- either search for a string with `--search` or an explicit search criteria in json format for `--json`

A valid login/email and password are necessary for authentication

multiple search criteria may be given, separated by commas or spaces. `tutorial.py` will create a custom search criteria passable as a HTTP request postfield.
The custom search criteria is saved to search.json in the same directory as `tutorial.py`. View this for syntactical information regarding easydb searches.

A personally written search criteria may be passed through `--json`, please save the file indiscreetly so the script may quickly locate it.

    -$ python tutorial.py --server_url 5.easydb.pf-berlin.de --search holiday,travel

    -$ python tutorial.py --server_url 5.easydb.pf-berlin.de --json criteria_template.json

## Arguments

### `server_url`

Distinguish the url of your easydb database:

    --server_url 5.easydb.pf-berlin.de

### `search`

Distinguish your search, search values may by spaces or commas from one another:

    --search easydbrules

    --search one,2,three,four,0101,0x6

    --search red fox yellow canaries

### `json` (Optional)

Filepath to a json file with predefined searches.

Explicitly distinguish your search criteria:

    -$ ls
        tutorial.py  criteria_template.json  search.json

    -$ python tutorial.py --server_url 5.easydb.pf-berlin.de --json search.json

Please save the file indiscreetly so the script may quickly locate it.

## Results

After a succesfull run, the results of your search will be saved in your current working directory as `searchResults.json`; as well, an informative table will be printed on the console regarding your easydb instance (see [Server Information](#server-information))

## Methods

### Start Session

    def start_session(Session)

- _Parameters_

    `Object` Session

- _Return_

    void

- _Description_

    A `GET` HTTP request is made using the new_session URL without postfields

    Status Code is printed to console. A 400 status code indicates an invalid URL.

    Session token is extracted from the response header and saved as Session.token, header is saved as Session.header, and whole response is saved as Session.content

- _Exceptions_

    [requests.exceptions.ConnectionError](http://docs.python-requests.org/en/master/_modules/requests/exceptions/) due to Invalid URL.

- _Reference_

    [Start a session](https://docs.easydb.de/en/technical/api/session)

- _Example_

```python
def start_session(ezdb):
    try:
        r = requests.get(ezdb.new_session)
    except requests.exceptions.ConnectionError as e:
        error_message_url(ezdb.new_session, e)

    ezdb.session = r
    ezdb.header = r.headers
    ezdb.token = getVal(r.json(), "token")
    ezdb.content = r.json()

```

### Retrieve Current Session

    def retrieve_current_session(Session)

- _Parameters_

    `Object` Session

- _Return_

    void

- _Description_

    A `GET` HTTP request is made using the new_session URL with the previously stored session token as the postfields.

    Status Code is printed to console. A 400 status code indicates an invalid session token.

    The `instance` value from the response body is compared to the instance value from Session.content to verify that they are indeed the same session.

- _Exceptions_

    none

- _Reference_

    [Retrieve current session](https://docs.easydb.de/en/technical/api/session)

- _Example_

```python
def retrieve_current_session(ezdb):
    payload = {
        "token": ezdb.token
    }
    r = requests.get(ezdb.new_session, params=payload)
```

### Authenticate Session

    def authenticate_session(Session)

- _Parameters_

    `Object` Session

- _Return_

    void

- _Input_

    `String` account login/email

    `String` account password

- _Description_

    At runtime the user will be prompted to enter an account login/password in order for the session to be authenticated.

    A `POST` HTTP request is made using the auth_session URL with the session token, login, and password as postfields.

    Status Code is printed to console. A 400 status code indicates an invalid login/password.

- _Exceptions_

    none

- _Reference_

    [Authenticate a session](../../session)

- _Example_

```python
def authenticate_session(ezdb):
    ezdb.login = raw_input('login: ')
    ezdb.password = raw_input('password: ')
    payload = {
        "token": ezdb.token,
        "login": ezdb.login,
        "password": ezdb.password
    }
    r = requests.post(ezdb.auth_session, params=payload)
```

### Deauthenticate Session

    def deauthenticate_session(Session)

- _Parameters_

    `Object` Session

- _Return_

    void

- _Description_

    A `POST` HTTP request is made using the deauth_session URL with the session token as the postfields.

    Status Code is printed to console. A 400 status code indicates an invalid session token.

- _Exceptions_

    none

- _Reference_

    [Deauthenticate a session](http://docs.5.easydb.de/en/technical/api/session/session.html#deauthenticate-a-session)

- _Example_

```python
def deauthenticate_session(ezdb):
    # Initialize array, insert session token with key "token"
    payload = {
        "token": ezdb.token
    }
    # POST request, use array as postfields
    r = requests.post(ezdb.deauth_session, params=payload)
```

### Search

    def search(Session)

- _Parameters_

    `Object` Session

- _Return_

    void

- _Description_

    A `POST` HTTP request is made using the search URL with the session token and search criteria as postfields.

    Status Code is printed to console. A 400 status code indicates an invalid session token.

    The request response is written to the locally viewable file `searchResults.json`

- _Exceptions_

    none

- _Reference_

    [Search](https://docs.easydb.de/en/technical/api/search)

### Server Information

    def root_menu_about(Session)

- _Parameters_

    `Object` Session

- _Return_

    `array` aboutDetails

- _Description_

    A table is produced containing relevant information to the user's easydb instance.

- _Exceptions_

    none

- _Reference_

    [Retrieve the list of plugins](https://docs.easydb.de/en/technical/api/plugin)

- _Example_

| About | Information |
|---|---|
| api | 1 |
| server_version | 1 |
| user-schema | 320 |
| solution | easydb |
| name | easydb |
| db-name | easy5-easydb-user |
| Plugins | basemigration, css, custom-data-type-gnd, custom-data-type-link, easydb-export-transport-ftp, easydb-wordpress-plugin, eventmanager, hotfolder, ldap, oai, presentation-pptx, server |
| server | http://5.easydb.pf-berlin.de |
| Build | 2017-06-14T14:50:09Z  @galaxy |
| 5 git | 8d98f7502d950be6c8786eb043799414688a65be/(detachedfrom8d98f75) |
| CUi git | 8645fc4b75cd8bc8715d09c8e07f72b0c9bbaecb/(detachedfrom8645fc4) |

### Helper Methods

- `getVal(array haystack, String needle)`

    search `array` haystack for specific `String` needle, return `String` value

- `write_json(array content, String filename)`

    write json encoded `array` content to a file `String` filename.

- `pretty_printer(array table)`

    print `array` table to command line, with table headings as "About" and "Information".

<!-- ------------------------- -->

## `tutorial.py`

```python
import requests
import json
import os
import copy
import argparse

argparser = argparse.ArgumentParser(
    description="easydb session creation and search")

argparser.add_argument("-u", "--server_url", help="Url of the server")
argparser.add_argument("-s", "--search", default=[], nargs="*", help="Search item, can accept multiple elements, comma separated")
argparser.add_argument("-j", "--json", default="", help="Handwritten search criteria replaces search argument")

args = argparser.parse_args()


"""
	Session class handles all Session API applications
"""


class Session:
    _session, _token, _header, _content, _plugins, _password, _login = "", "", "", "", "", "", ""

    def __init__(self, server, searchable, searchjson=""):
        http = "http://"
        if server.startswith("http"):
            http = ""

        self.new_session = http + server + "/api/v1/session"
        self.auth_session = http + server + "/api/v1/session/authenticate"
        self.deauth_session = http + server + "/api/v1/session/deauthenticate"
        self.search = http + server + "/api/v1/search"
        self.plugin = http + server + "/api/v1/plugin"
        self.server = http + server + "/api/v1/plugin/base/server/status"
        self.searchable = searchable
        self.searchjson = searchjson

    def _setSession(self, session=None):
        self._session = session

    def _getSession(self):
        return self._session

    def _setHeader(self, header):
        self._header = header

    def _getHeader(self):
        return self._header

    def _setToken(self, token):
        self._token = token

    def _getToken(self):
        return self._token

    def _setContent(self, content):
        self._content = content

    def _getContent(self):
        return self._content

    def _setPassword(self, password):
        self._password = password

    def _getPassword(self):
        return self._password

    def _setLogin(self, login):
        self._login = login

    def _getLogin(self):
        return self._login

    def _setPlugins(self, plugins):
        self._plugins = plugins

    def _getPlugins(self):
        return self._plugins

    token = property(_getToken, _setToken)
    header = property(_getHeader, _setHeader)
    session = property(_getSession, _setSession)
    content = property(_getContent, _setContent)
    password = property(_getPassword, _setPassword)
    login = property(_getLogin, _setLogin)
    plugins = property(_getPlugins, _setPlugins)


"""
	Create new session using URL directed towards database
"""


def start_session(ezdb):
    try:
        print("start session")
        r = requests.get(ezdb.new_session)
        check_status_code(r, True)
    except requests.exceptions.ConnectionError as e:
        server_url_error_message(ezdb.new_session, e)

    ezdb.session = r
    ezdb.header = r.headers

    ezdb.token = getVal(r.json(), "token")
    ezdb.content = r.json()


"""
	Retrieve the same session using Token and plain url
	Compare instances to prove similarity
"""


def retrieve_current_session(ezdb):
    payload = {
        "token": ezdb.token
    }

    print("retrieve current session, payload: %s" % json.dumps(payload, indent=4))
    r = requests.get(ezdb.new_session, params=payload)
    check_status_code(r, True)

    # proof that the session is the same
    if getVal(r.json(), "instance") == getVal(ezdb.content, "instance"):
        print("retrieved correct session")


"""
	Authenticate Session using authenticate url
	login and password credentials required, or email instead of login
"""


def authenticate_session(ezdb):
    ezdb.login = raw_input("login: ")
    ezdb.password = raw_input("password: ")

    payload = {
        "token": ezdb.token,
        "login": ezdb.login,
        "password": ezdb.password
    }

    print("authenticate session, payload: %s" % json.dumps(payload, indent=4))
    r = requests.post(ezdb.auth_session, params=payload)
    check_status_code(r, True)


"""
	Deauthenticate session using deauthenticate url
"""


def deauthenticate_session(ezdb):
    payload = {
        "token": ezdb.token
    }

    print("deauthenticate session, payload: %s" % json.dumps(payload, indent=4))
    r = requests.post(ezdb.deauth_session, params=payload)
    check_status_code(r)


"""
	Search database using search url and search criteria from json file
"""


def search(ezdb):
    tokenpayload = {
        "token": ezdb.token
    }

    if ezdb.searchjson != "":
        filename = ezdb.searchjson
        do_write_criteria = False
    else:
        filename = "search.json"
        do_write_criteria = True

    if do_write_criteria:
        write_criteria(ezdb)

    _file = os.path.join(os.getcwd(), filename)

    if not os.path.isfile(_file):
        print(_file + " does not exist")
        exit(1)

    f = open(_file)
    data = json.load(f)

    print("search, payload: %s" % json.dumps(data, indent=4))
    r = requests.post(ezdb.search, params=tokenpayload, data=json.dumps(data))
    search_result = r.json()
    write_json(search_result, "searchResult.json")

    if "count" in search_result:
        print("search response: %s hit(s) found" % search_result["count"])

    print("search response was saved as searchResult.json\n")

    print(perform_curl_request(r.request))


def perform_curl_request(req):

    command = "curl -X {method} -H {headers} -d '{data}' '{uri}'"
    method = req.method
    uri = req.url
    data = req.body
    headers = ['"{0}: {1}"'.format(k, v) for k, v in req.headers.items()]
    headers = " -H ".join(headers)
    return command.format(method=method, headers=headers, data=data, uri=uri)


def write_criteria(ezdb):
    with open(os.path.join(os.getcwd(), "criteria_template.json"), "r") as jsonFile:
        data = json.load(jsonFile)

        tmp = data["search"][0]
        criteria = []
        for x in ezdb.searchable:
            tmp["string"] = x
            criteria.append(copy.copy(tmp))

        data["search"] = criteria

        with open(os.path.join(os.getcwd(), "search.json"), "w") as jsonFile:
            jsonFile.write(json.dumps(data))
            print("generated search criteria, saved in " + str(os.path.abspath(jsonFile.name)))


"""
	Print the Root Menu About
"""


def root_menu_about(ezdb):
    aboutDetails = {
        "api": "",
        "server_version": "",
        "user-schema": "",
        "solution": "",
        "instance": "",
        "db-name": "",
        "Plugins": "",
        "Optionen": "",
        "last-modified": "",
        "Fivegit": "",
        "CUIgit": "",
        "Style": "",
        "server": ""
    }

    print(ezdb.header)

    instance = getVal(ezdb.content, "instance")
    for key, value in instance.items():
        if key in aboutDetails:
            aboutDetails[key] = value

        # Instance code is labelled as 'name' in dict
        if key == "name":
            aboutDetails["instance"] = value

    for key, value in ezdb.header.items():
        if key in aboutDetails:
            aboutDetails[key] = value

    # Get Plugins
    print("get plugins")
    r = requests.get(ezdb.plugin)
    ezdb.plugins = r.json()["plugins"]

    plgns = []
    for plg in ezdb.plugins:
        plgns.append(plg["name"])

    aboutDetails["Plugins"] = plgns

    # Get Server Info
    payload = {
        "token": ezdb.token
    }
    print("get server info")
    r = requests.get(ezdb.server, params=payload)

    pretty_printer(aboutDetails)


"""
	Helper Methods
"""


def getVal(data, str):
    for key, value in data.items():
        if key == str:
            return value


def write_json(data, name):
    with open(name, "w") as outfile:
        json.dump(data, outfile, indent=4)


def write_file(self, r, filename):
    with open(filename, "wb") as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)


def pretty_printer(dict):

    print "{:<20} {:<20}".format("About", "Information")
    for k, v in dict.iteritems():
        if v == "":
            continue
        if isinstance(v, list):
            print "{:<20} {:<20}".format(k, ", ".join(v))
            continue

        print "{:<20} {:<20}".format(k, v)


def check_status_code(response, exit_on_failure=False):
    if response.status_code != 200:
        print("got status code %s: %s" %
              (response.status_code, json.dumps(response.json(), indent=4)))
        if exit_on_failure:
            print("exit after unexpected status code")
            exit(1)


"""
	error_message
"""


def server_url_error_message(str, err):
    print "URL is invalid"
    print "{0} raises {1}".format(str, err)
    sys.exit()


if __name__ == "__main__":

    ezdb = Session(args.server_url, args.search, args.json)

    print("\nCreate and authenticate session\n")

    start_session(ezdb)
    retrieve_current_session(ezdb)
    authenticate_session(ezdb)

    print("\nShow root menu\n")

    root_menu_about(ezdb)

    print("\nPerform search: %s\n" % ("from file %s" % args.json if args.json != "" else ("[%s]" % ", ".join(args.search))))

    search(ezdb)

    print("\nDeauthenticate session\n")

    deauthenticate_session(ezdb)
```

<!-- ------------------------- -->

----

## `criteria_template.json`

```json
{
    "search": [
        {
            "type": "match",
            "mode": "fulltext",
            "string": "2",
            "phrase": false,
            "bool": "must"
        }
    ]
}
```
