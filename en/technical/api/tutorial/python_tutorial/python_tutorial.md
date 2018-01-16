# Python Quickstart 

    Use python with requests

## Table of Contents

---

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
 - [tutorial.py](#tutorial.py)
 - [criteria_template.json](#criteria_template.json)


## Getting Started

---

To get started, please complete the following steps

1. [python 2.7 downloaded](https://www.python.org/downloads/), 

    Set up environment -> [here's how](https://www.tutorialspoint.com/python/python_environment.htm)
 
2. [install Requests](http://docs.python-requests.org/en/master/user/install/)

    User friendly library for making HTTP requests
    
3. Copy the [code](#tutorial.py) at the end of this page and save (as tutorial.py)

4. (Optional) Copy and save the [JSON text](#criteria_template.json) (as criteria_template.json)
    
 
## Purpose

---

The tutorial.py script attempts a couple simple interactions with your easydb database.

- [Start new session](#start-session)
- [Retrieve current session with session token](#retrieve-current-session)
- [Session Authentication](#authenticate-session)
- [Session Deauthentication](#deauthenticate-session)
- [Search assets](#search)
- [View server information](#server-information)


Every interaction will print a HTTP status code to the console


## HTTP status codes

---

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.html#api_error): something is malformed |
| 500 | [Server error](/technical/errors/errors.html#server_errors): internal server error |

- _Reference_

    [HTTP Status Codes](https://docs.easydb.de/en/technical/api/session/session.html#http-status-codes)


## Running from the command line

---

tutorial.py may be run from the command line. 

- easydb server url in the `-server=<>` argument
- either search for a string with `-search=<>` or an explicit search criteria in json format for `-json=<>`
   
A valid login/email and password are necessary for authentication

multiple search criteria may be given, separated by commas or spaces. tutorial.py will create a custom search criteria passable as a HTTP request postfield.
The custom search criteria is saved to search.json in the same directory as tutorial.py. View this for syntactical information regarding easydb searches.

A personally written search criteria may be passed through `-json=<>`, please save the file indiscreetly so the script may quickly locate it.

    -$ python tutorial.py -server=5.easydb.pf-berlin.de -search=holiday,travel
    
    -$ python tutorial.py -server=5.easydb.pf-berlin.de -json=criteria_template.json


## Arguments

---

1. `-server=<>`

Distinguish the url of your easydb database:

    -server=5.easydb.pf-berlin.de
   
2. `search=<>` 

Distinguish your search, search values may by spaces or commas from one another:
 
    -search=easydbrules
    
    -search=one,2,three,four,0101,0x6
    
    -search=red fox yellow canaries
    
3. `-json=<>` (Optional)
    
Explicitly distinguish your search criteria:

    -$ dir
    tutorial.py  criteria_template.json
    
    -$ python tutorial.py -server=5.easydb.pf-berlin.de -json=criteria_template.json
    
    
please save the file indiscreetly so the script may quickly locate it.
    
    
4. `-type=<>` (Optional)
    
Distinguish which datatype to search for, or create a regular expression in your search query

    -type=Fulltext 
    
    -type=worter
    


## Results

---

After a succesfull run, the results of your search will be saved in your current working directory as `searchResults.txt`; as well, an informative table will be printed on the console regarding your easydb instance ( see [Server Information](#server-information))



## Methods

---

### Start Session
    
---

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

    [Start a session](https://docs.easydb.de/en/technical/api/session/session.html#start-a-session)

- _Example_

~~~~python
def start_session(ezdb):
    try:
        r = requests.get(ezdb.new_session)                      #GET request
        print(r.status_code)                                    #Status Code
    except requests.exceptions.ConnectionError as e:        
        error_message_url(ezdb.new_session, e)                  #Invalid URL

    ezdb.session = r                                            #Store response as session String
    ezdb.header = r.headers                                     #Store header as header String
    ezdb.token = getVal(r.json(), "token")                      #parse json encoded response for session token
    ezdb.content = r.json()                                     #Store json encoded response as content

~~~~
    


### Retrieve Current Session

---

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
    
    [Retrieve current session](http://docs.5.easydb.de/en/technical/api/session/session.html#retrieve-current-session)

- _Example_

~~~~python
def retrieve_current_session(ezdb):                             
    payload = {"token": ezdb.token}                                 #Initialize array, insert session token with key "token"
    r = requests.get(ezdb.new_session, params=payload)              #GET request, use array as postfields
    print(r.status_code)                                            #Status Code
    # proof that the session is the same
    if getVal(r.json(), "instance") == getVal(ezdb.content, "instance"):
        print("retrieved correct session")


~~~~


    
    
    
### Authenticate Session

---

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

    [Authenticate a session](http://docs.5.easydb.de/en/technical/api/session/session.html#authenticate-a-session)

- _Example_

~~~~python
def authenticate_session(ezdb):
    ezdb.login = raw_input('login:')                                                    #Prompt user for login
    ezdb.password = raw_input('password:')                                              #Prompt user for password
    payload = {"token": ezdb.token, "login": ezdb.login, "password": ezdb.password }    #Initialize array, insert session token with key "token", password, and login
    r = requests.post(ezdb.auth_session, params=payload)                                #POST request, array as postfields
    print(r.status_code)                                                                #Status Code
~~~~
    

### Deauthenticate Session

---

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

~~~~python
def deauthenticate_session(ezdb):
    payload = {"token": ezdb.token}                                  #Initialize array, insert session token with key "token"
    r = requests.post(ezdb.deauth_session, params=payload)           #POST request, use array as postfields
    print(r.status_code)                                             #Status Code
~~~~

    
### Search

---

    def search(Session)
    
- _Parameters_

    `Object` Session

- _Return_

    void
    
- _Description_
    
    A `POST` HTTP request is made using the search URL with the session token and search criteria as postfields. 
    
    Status Code is printed to console. A 400 status code indicates an invalid session token.
    
    The request response is written to the locally viewable file `searchResults.txt`
  
  
- _Exceptions_

    none
    
- _Reference_

    [Search](http://docs.5.easydb.de/en/technical/api/search/search.html#search)




### Server Information

---

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

    [Retrieve the list of plugins](http://docs.5.easydb.de/en/technical/api/plugin/plugin.html)

- _Example_

<table><thead><tr><th>About</th><th>Information</th></tr></thead><tbody><tr><td>api</td><td>1</td></tr><tr><td>server_version</td><td>1</td></tr><tr><td>user-schema</td><td>320</td></tr><tr><td>solution</td><td>easydb</td></tr><tr><td>name</td><td>easydb</td></tr><tr><td>db-name</td><td>easy5-easydb-user</td></tr><tr><td>Plugins</td><td>basemigration, css, custom-data-type-gnd, custom-data-type-link, easydb-export-transport-ftp, easydb-wordpress-plugin, eventmanager, hotfolder, ldap, oai, presentation-pptx, server</td></tr><tr><td>server</td><td>http://5.easydb.pf-berlin.de</td></tr><tr><td>Build</td><td>2017-06-14T14:50:09Z  @galaxy</td></tr><tr><td>5 git</td><td>8d98f7502d950be6c8786eb043799414688a65be/(detachedfrom8d98f75)</td></tr><tr><td>CUi git</td><td>8645fc4b75cd8bc8715d09c8e07f72b0c9bbaecb/(detachedfrom8645fc4)</td></tr></tbody></table>


### Helper Methods

---

- *getVal(array haystack, String needle)*
    
    search `array` haystack for specific `String` needle, return `String` value

- *write_json(array content, String filename)*
    
    write json encoded `array` content to a file `String` filename.

- *view_HTTP_request(request r)*

    prints Requests `Object` r onto command line, viewable as a cURL command.

- *find(String filename)*

    recursively search through file directory for file with `String` filename

- *pretty_printer(array table)*

    print `array` table to command line, with table headings as "About" and "Information".






## tutorial.py

---

~~~~python

import requests
import distutils
import json
import os
import sys
import copy


cookieAuth = 1
frontend_language = "en-US"


def main():
    ezdb = argument_handler(sys.argv)

    start_session(ezdb)
    retrieve_current_session(ezdb)
    
    
    authenticate_session(ezdb)

    search(ezdb)
    root_menu_about(ezdb)
    
    deauthenticate_session(ezdb)


"""
	Session class handles all Session API applications
"""


class Session:
    _session, _token, _header, _content,_plugins,_password,_login  = "","","","","","",""

    def _init_(self, server, searchable, searchtype, searchjson):  #
        http = "http://"
        if (server.startswith('http')):
            http = ""

        self.new_session = http + server + "/api/v1/session"
        self.auth_session = http + server + "/api/v1/session/authenticate"
        self.deauth_session = http + server + "/api/v1/session/deauthenticate"
        self.search = http + server + "/api/v1/search"
        self.plugin = http + server + "/api/v1/plugin"
        self.server = http + server + "/api/v1/plugin/base/server/status"
        self.searchable = searchable
        self.searchtype = searchtype
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
        self._content = token

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
        self._plugins = token

    def _getPlugins(self):
        return self._plugins


    token = property(_getToken, _setToken)
    header = property(_getHeader, _setHeader)
    session = property(_getSession, _setSession)
    content = property(_getContent, _setContent)
    password = property(_getPassword, _setPassword)
    login = property(_getLogin, _setLogin)
    plugins= property(_getPlugins, _setPlugins)



"""
	Create new session using URL directed towards database
"""


def start_session(ezdb):
    try:
        r = requests.get(ezdb.new_session)
        print(r.status_code)
    except requests.exceptions.ConnectionError as e:
        error_message_url(ezdb.new_session, e)

    ezdb.session = r
    ezdb.header = r.headers
    
    
    ezdb.token = getVal(r.json(), "token")
    ezdb.content = r.json()
    

"""
	Retrieve the same session using Token and plain url
	Compare instances to prove similarity
"""


def retrieve_current_session(ezdb):
    payload = {"token": ezdb.token}
    r = requests.get(ezdb.new_session, params=payload)
    print(r.status_code)
    # proof that the session is the same
    if getVal(r.json(), "instance") == getVal(ezdb.content, "instance"):
        print("retrieved correct session")


"""
	Authenticate Session using authenticate url
	login and password credentials required, or email instead of login
"""


def authenticate_session(ezdb):
    ezdb.login = raw_input('login:')
    ezdb.password = raw_input('password:')
    payload = {"token": ezdb.token, "login": ezdb.login, "password": ezdb.password }
    r = requests.post(ezdb.auth_session, params=payload)
    print(r.headers)
    print(r.status_code)


"""
	Search database using search url and search criteria from search.json
"""


def search(ezdb):
    tokenpayload = {"token": ezdb.token}
    if (ezdb.searchjson != ""):
        file = find(ezdb.searchjson)
    else:
        write_criteria(ezdb)
        file = os.path.join(os.getcwd(), "search.json")

    f = open(file)
    data = json.load(f)
    r = requests.post(ezdb.search, params=tokenpayload, data=json.dumps(data))
    write_json(r.json(), "searchResult.txt")

    print(deleteLater(r.request))
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    

def deleteLater(req):


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
        tmp['string'] = x
        criteria.append(copy.copy(tmp))

    # tmp = data["location"]
    data["search"] = criteria

    with open(os.path.join(os.getcwd(), "search.json"), "w") as jsonFile:
        jsonFile.write(json.dumps(data))


"""
	Deauthenticate session using deauthenticate url
"""


def deauthenticate_session(ezdb):
    payload = {"token": ezdb.token}
    r = requests.post(ezdb.deauth_session, params=payload)
    print(r.status_code)

    
"""
	Print the Root Menu About
"""


def root_menu_about(ezdb):
    aboutDetails = {"api" : "", "server_version" :"", "user-schema" : "", "solution" :"", "instance":"", "db-name":"", "Plugins":"", "Optionen":"", "last-modified":"","Fivegit":"", "CUIgit":"", "Style":"", "server":""}
    
    print(ezdb.header)
    
    instance = getVal(ezdb.content, "instance");    
    for key, value in instance.items():
        if key in aboutDetails:
            aboutDetails[key]=value;
        
        ## Instance code is labelled as 'name' in dict
        if key == "name":
            aboutDetails["instance"] = value;
            
    for key, value in ezdb.header.items():
        if key in aboutDetails:
            aboutDetails[key]=value;
    

    ## Get Plugins
    r = requests.get(ezdb.plugin)
    print(r.status_code)    
    ezdb.plugins = r.json()["plugins"]
    
    plgns = []
    for plg in ezdb.plugins:
        #if key == "name":
        plgns.append(plg["name"])
            
    aboutDetails["Plugins"] = plgns  
    
     ## Get Server Info
    payload = {"token": ezdb.token}
    r = requests.get(ezdb.server, params=payload)
              
    pretty_printer(aboutDetails)
    
    


"""
	argument_handler
"""


def argument_handler(sysargs):
    root, search_type, search_str, file_type = "", "", "", ""
    search_criteria = False

    for x in sysargs:

        if x.startswith('-server'):
            root = x[8:]  # Server URL address
            search_criteria = False
            continue

        if x.startswith('-search'):
            # search_str = [y.strip() for y in x[8:].split(',')] # File types, must be separated by commas
            search_str = [y.strip() for y in x[8:].split(',')]
            search_str = filter(None, search_str)
            search_criteria = True
            continue

        if x.startswith('-type'):
            search_type = [y.strip() for y in x[6:].split(',')]  # Strings to be searched, must be separated by commas
            search_criteria = False
            continue

        if x.startswith('-json'):
            file_type = x[6:].strip()  # json file to use as search criteria
            search_criteria = False
            continue

        if x.startswith('-h') or x.startswith('--help'):
            print_help()
            continue

        if search_criteria == True and x != "":
            search_str.append(x)  # this allows search criteria to be added even if CSV format is deprecated

    if root == "" or (search_str == "" and file_type == ""):
        command_line_error_message()

    new_session = Session(root, search_str, search_type, file_type)
    return new_session


"""
	Helper Methods
"""


def getVal(data, str):
    for key, value in data.items():
        if key == str:
            return value




def write_json(data, name):
    with open(name, 'w') as outfile:
        json.dump(data, outfile, indent=2)


def write_file(self, r, filename):
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)


    
"""
	searches given path for file, walks backwards when unsuccessful
"""


def find(name):
    looking = True
    while (looking):
        for root, dirs, files in os.walk(os.getcwd()):
            if name in files:
                looking = False
                return os.path.join(root, name)
        os.chdir('..')


"""
	print_help
"""


def print_help():
    print (

        "\n" + "easydb session creation and search"
        + "\n" + ""
        + "\n" + "usage: python session.py [arg] ..."
        + "\n" + "arguments (and corresponding environment variables):"
        + "\n" + ""
        + "\n" + "   -h                         : print this help message and exit (also --help)"
        + "\n" + ""
        + "\n" + "   -server=<server>           : url of the server"
        + "\n" + "                                  (Required)"
        + "\n" + "   -search=<search value>     : search item, can accept multiple elements, comma separate "
        + "\n" + "                                  (Required) "
        + "\n" + "   -type=<result type>        : datatype to search for"
        + "\n" + "                                  (Optional) Default is Fulltext"
        + "\n" + "                                  search types are:"
        + "\n" + "                                  Fulltext, worter, ODER, NICHTS, UND"
        + "\n" + "                                  (not implemented) "
        + "\n" + "   -json=<criteria.json>      : handwritten search criteria replaces search argument"
        + "\n" + "                                  (Optional) Default is criteria_template.json"
    )
    sys.exit()

    
"""
	error_message
"""


def server_url_error_message(str, err):
    print "URL is invalid"
    print "{0} raises {1}".format(str, err)
    sys.exit()


def command_line_error_message():
    print "Value must be entered in for -server and -search or -searchjson"
    print "Please run again"
    sys.exit()


def search_criteria_error_message():
    print "input search criteria does not exist"
    print "please check for spelling errors or move file closer to session.py directory"
    sys.exit()


def pretty_printer(dict):

    print "{:<20} {:<20}".format('About','Information')
    for k, v in dict.iteritems():
        if v == "":
            continue
        if isinstance(v, list):
            print "{:<20} {:<20}".format(k, ', '.join(v))
            continue
            
        print "{:<20} {:<20}".format(k, v)
    
    
    
if _name_ == "_main_":  #
    main()

~~~~

---

## criteria_template.json

~~~~json
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
      
~~~~
