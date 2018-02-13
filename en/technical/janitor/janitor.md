# Janitor

The Janitor is a process running inside the easydb-server. Its purpose is to clean up temporary data in filesystem or database.

For a list of configuration options see the [YAML configuration reference](/sysadmin/konfiguration/yaml/yaml.html).

The following tasks are performed by the Janitor process:

* All files prepared by exports are removed. The default retention period is 3 days.
* All events of the types `OBJECT_INDEX` and `API_PROGRESS` older than 1 week are removed from the database.
* The clients blocked because of too many wrong login attempts are checked and released if the blocking period is over.
