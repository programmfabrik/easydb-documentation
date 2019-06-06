import requests
import json
import os
import copy
import argparse

argparser = argparse.ArgumentParser(
    description="easydb session creation and search")

argparser.add_argument("-u", "--server_url", help="Url of the server")
argparser.add_argument("-s", "--search", default=[], nargs="*",
                       help="Search item, can accept multiple elements, comma separated")
argparser.add_argument("-j", "--json", default="",
                       help="Handwritten search criteria replaces search argument")

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

    print("retrieve current session, payload: %s" %
          json.dumps(payload, indent=4))
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

    print("authenticate session, payload: %s" %
          json.dumps(payload, indent=4))
    r = requests.post(ezdb.auth_session, params=payload)
    check_status_code(r, True)


"""
	Deauthenticate session using deauthenticate url
"""


def deauthenticate_session(ezdb):
    payload = {
        "token": ezdb.token
    }

    print("deauthenticate session, payload: %s" %
          json.dumps(payload, indent=4))
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
            print("generated search criteria, saved in " +
                  str(os.path.abspath(jsonFile.name)))


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

    print("\nPerform search: %s\n" % ("from file %s" %
                                      args.json if args.json != "" else ("[%s]" % ", ".join(args.search))))

    search(ezdb)

    print("\nDeauthenticate session\n")

    deauthenticate_session(ezdb)
