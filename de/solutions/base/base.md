# Solution base

Für dies Solution "base" muss folgende Anpassung vorgenommen werden, damit der Dienst easydb-server starten kann.

Ergänzen Sie in der zentralen Konfigurationsdatei `easydb5-master.yml`, deren Ordner während der [Installation](/sysadmin/installation/installation.md#datenablage-bestimmen) festgelegt wurde:

~~~~~
easydb-server:
  [...]
  extension:
    external-user-schema: true

~~~~~

Die letzte Zeile ist zu ergänzen; die anderen wurden angegeben, um die korrekte Einrückung zu demonstrieren.

Außerdem zeigt das Beispiel den korrekten Eltern-Eintrag `extension`. Falls dieser in Ihrer Datei fehlt, muss er ebenfalls jetzt ergänzt werden.
