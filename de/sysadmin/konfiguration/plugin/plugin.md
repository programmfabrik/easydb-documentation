# Pluginkonfiguration

Die easydb 5 bringt bereits mehrere Plugins mit, diese werden in der Konfiguration mit "base" gekennzeichnet.

Viele dieser Plugins sind standardmäßig aktiviert.

Änderungen können in der zentralen Konfigurationsdatei `easydb5-master.yml` vorgenommen werden, deren Speicherort bei der [Installation](/sysadmin/installation/installation.html#anpassungen) festgelegt wurde.

In diesem Beispiel wird das Plugin "custom-data-type-link" als aktiv konfiguriert:

~~~~
easydb-server:
  plugins:
    enabled+:
      - base.custom-data-type-link
~~~~

Ebenso ist es möglich, ein standardmäßig aktiviertes Plugin wieder zu deaktivieren:

~~~~
easydb-server:
  plugins:
    enabled-:
      - base.custom-data-type-link
~~~~

Nach einem Neustart findet sich das Plugin in der Liste "Plugins" auf der Seite "Versionsinformation".

Der Klickweg dorthin ist: `i`-Knopf (ganz links in der Leiste) -> `Über`.

# Extension Plugins

Extensions-Plugins müssen installiert werden und aktiviert werden.

Dies ist beschrieben unter [Plugin-Installation](/sysadmin/plugin/plugin.html).
