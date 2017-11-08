# Pluginkonfiguration

Die easydb5 bringt bereits mehrere Plugins mit, diese werden in der Konfiguration mit "base" gekennzeichnet.

Diese Plugins müssen nur noch aktiviert werden, in der zentralen Konfigurationsdatei `easydb5-master.yml`, deren Speicherort bei der [Installation](/sysadmin/installation/installation.html#anpassungen) festgelegt wurde.

In diesem Beispiel wird das Plugin "custom-data-type-link" als aktiv konfiguriert:

~~~~
  plugins:
    enabled+:
      - base.custom-data-type-link

~~~~

Nach einem Neustart findet sich das Plugin in der Liste "Plugins" auf der Seite "Versionsinformation".

Der Klickweg dorthin ist: `i`-Knopf (ganz links in der Leiste) -> `Über`.

# Extension Plugins

Extensions-Plugins müssen installiert werden und aktiviert werden.

Dies ist beschrieben unter [Plugin-Installation](/sysadmin/plugin/plugin.html).
