# Leistung Optimieren

Falls die Konfiguration nichts anderes sagt, dann gelten folgende Einstellungen:

~~~~
easydb-server:
  server:
    frontend:
      num_services: 1
    upload-server:
      num_services: 1
    indexer:
      num_services: 1
    preindexer:
      num_services: 1
~~~~

Wenn Sie diese Werte in der Konfiguration überschreiben, dann bedenken Sie bitte dass die easydb für mehr Prozesse auch mehr Hardware benötigt.

Die Konfiguration findet wie immer in der zentralen Datei `easydb5-master.yml` statt, deren Speicherort bei der [Installation](/sysadmin/installation/installation.html#datenablage-bestimmen) festgelegt wurde.

# Szenarien

## Mehr Mitarbeiter sollen parallel Daten erfassen können

Erhöhen Sie schrittweise den folgenden Wert, z.B. als erstes auf 2.

~~~
easydb-server:
  server:
    frontend:
      num_services: 2
~~~


## Viele neue Daten sollen schneller in den Suchergebnissen erscheinen

Erhöhen Sie schrittweise den folgenden Wert, z.B. als erstes auf 2.

~~~
easydb-server:
  server:
    preindexer:
      num_services: 2
~~~

