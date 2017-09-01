# Plugins

Plugins erlauben die Funktionalität der easydb zu erweitern. Plugins werden über die YAML-Konfiguration des Servers definiert und lassen sich einfach ein- und ausschalten.

Plugins allow for an extension of easydb functionality. They are easily integratged into the Server through it's YAML and defined by YAML files themselves.

Folgende Möglichkeiten stehen zur Verfügung:

* Frontend-Apps erstellen
* Systemrechte definieren
* Übersetzungskeys definieren oder ersetzen
* Server-Callbacks definieren

Plugin functionality includes:

* creating frontend apps
* defining system rights
* define or replace localization keys
* define server callbacks

## Client:

Frontend-Apps laufen direkt im Javascript des Browsers und können entweder als Top-Level-App im Menü erscheinen oder aus dem User-Tray ein Popover öffnen.

Frontend apps are Javascript applications that run client-side and can be integrated into the easydb Interface as top level apps in the sidebar or as popovers opened from within the user tray.

## Server-Callbacks:

Die Server-Callbacks sind Python-Skripte, die in bestimmten Situationen ausgeführt werden. Das Verfahren ist immer gleich: das Plugin registriert eine Funktion mit einem bestimmten Typ und der Server ruft diese Funktion bei bestimmten Ereignissen auf. Der Server liefert Information zur Funktion und erwartet eine Antwort, die dann verwendet wird. Zum Beispiel, ein "api_db_pre_update"-Callback erhält das vom User angegebene Objekt bei POST /api/db und kann es beliebig modifizieren und als Antwort an den Server zurückliefern. Der Server bearbeitet den Request weiter.

Server-Callbacks are Python scripts, that are run in specific situations in a standardized procedure. The plugin registers a function at the server. From then on everytime a certain event happens, the server calls this function.
The server calls the function with information to be processed and expects a response with altered content for further use.
An "api_db_pre_update" callback for example receives the data entered by a user when a POST api/db call is made, alters the data if necessary, and passes it to the server. From here on the altered data is processed as it would have been without the plugin.

Server-Callbacks können auch easydb-Fehler werfen, wie "der User verfügt nicht über das Recht X". Sie können auch eigene Fehlertypen definieren, die im Frontend korrekt (und übersetzt) angezeigt werden.

Server callbacks are enabled to throw easydb errors like "The user has insufficient rights for ..." It is also possible to define custom error types, which will be displayed in the frontend properly and localized.

Das ist eine Übersicht der Server-Callbacks:

* Allgemeine Callbacks: z.B. Server-Start und -Stopp
* API-Callbacks: vom Plugin definierte API-Erweiterungen
* Extension points: bei bestimmten Operationen kann das Plugin das Ergebnis einer Operation modifizieren, z.B. nach einem POST /api/db
* Transition-Extensions: Plugin-definierte Transition-Actions werden durch diese Callbacks realisiert
* Export-Extensions: Plugin-definierte Transporttypen und Export-Erweiterungen

This is an overview of server callbacks:

* General callbacks: e.g. server start and stop
* API callbacks: API extensions defined in a plugin
* Extension points: On occurence of certain events the plugin can alter the outcome of an action, e.g after a POST /api/db call
* Transition extensions: Transition actions defined by a plugin are realised using this callback
* Export extensions: Allows plugins to define transport types and export extensions

Die Server-Callbacks haben Zugriff zu vielen internen easydb-Informationen und -Tools.
Sie können z.B. in der offenen DB-Transaktion eines Frotend-Requests arbeiten, die Basis-Konfiguration lesen, die offene Session anfragen (z.B. welcher User? welche Rechte?).

Server callbacks have access to many of easydb's internal information and tools.
They may for example alter an open database transaction of a frontend request, read the base configuration, or request open sessions (which user, what rights?)


## Callback Typen/Callback Types

* register_callback "process"

* register_callback "api"

* register_callback "export_transport"

* register_callback "export_produce"

* register_callback "db_pre_update_one"

* register_callback "db_pre_update"

* register_callback "db_post_update"

* register_callback "db_pre_delete"

* register_callback "db_post_delete"

* register_callback "user_post_update"

* register_callback "transition_action"

* register_callback "sso_get_user"

##Beispiel (Server Callback) Example

### Plugin Code
#### Python

Plugins werden in Form eines Python-Skripts geschrieben.
Plugins are realised in fomr of a python script
```python
def easydb_server_start(easydb_context):
easydb_context.register_callback('db_pre_update', {'callback': 'pre_update_function'})


def pre_update_function(easydb_context, easydb_info):
logger = easydb_context.get_logger('helmsmuseum')
logger.debug('pre_update_function')
data = easydb_context['data']
data['name']="TEST-PLUGIN"
return data
```
Die Methode "easydb_server_start" wird beim Server-Start einmal ausgeführt. Hier müssen Callbacks beim Server registriert werden. Je nach Typ werden diese dann bei unterschiedlichen Ereignissen ausgeführt.
Beim Code-Beispiel wird die Funktion "pre_update_function" für das Ereignis "db_pre_update" registriert. Jedes mal, wenn ein Objetk erzeugt oder geändert wird, wird dessen Feld "name" auf den Wert "TEST-PLUGIN" gesetzt.

The Function "easydb_server_start" is called once at startup. In this function
callbacks are registered at the server. Depending of their type the registered callbacks are then called at occurance of certain events.
In the sample code the function "pre_update_function" is registered to be called at ever "db_pre_update" event. Each time an object is created or changed, this function will be called and change the objects "name" field, setting it's value to "TEST-PLUGIN"

#### YAML

Um das Skript vom Server ausführbar zu machen wird eine YAML benötigt, die das Plugin definiert.

In order for the Script to be executable by the server a YAML defining the plugin is necessary.

```
plugin:
name: example_plugin
version: 1.0
server:
api-version:
require: 1
python-2:
file: example_plugin.py
```

Hier wurde angenommen, dass das Plugin "example_plugin" heißen soll. Das Python-Skript heißt "example_plugin.py" und befindet sich im selben Ordner wie die YAML. Die hier gezeigte Konfiguration enthält die  minimal mögliche Anzahl an Variablen.

In this case was assumed that the plugin is called "example_plugin" and it's python script lies within the same directory as the YAML. The YAML configuration shown here contains the bare minimum of entries.

Des Weiteren muss die Solution-YAMEL angepasst werden. Hier muss folgendes ergänzt werden:

Besides defining the plugin YAML it is necessary to alter the server YAML.
It must be extended in the following way:

```
solution:
name: beispiel-instanz
plugins:
- name: example_plugin
file: plugins/example_plugin/example_plugin.yml

plugins:
enabled+:
- solution.beispiel-instanz.example_plugin
```
Die Punkte "solution" und "solution.name" sind für gewöhnlich bereits gesetzt. Innerhalb des Solution Verzeichnisses sind die Dateien in diesem Beispiel folgendermaßen geordnet.

The entries "solution" as well as "solution.name" are by default already set.

The solution directory which contains the plugin files is structured like this in the example described:
```
Solution-Folder
│   solution.yml
│
└───plugins
│
└───example_plugin
│   example_plugin.yml
│   example_plugin.py


```

