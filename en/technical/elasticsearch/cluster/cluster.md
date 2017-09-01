<!-- md:body_class:api, md:debug -->
# Elasticsearch-Cluster

## Installation

Auf jedem Node wird folgendes installiert:

- Java 7: bessere Verwaltung vom Speicher (Garbage Collector)
- ES: neueste Version (gerade: 0.90.3)
- ES-Plugins:
  - ICU: Unterstützung für Unicode (`plugin -install elasticsearch/elasticsearch-analysis-icu/1.11.0`)
  - Monitoring Plugins (siehe unten)

Die Monitoring-Plugins kann man jederzeit installieren oder entfernen, aber ICU muss installiert
werden, bevor Easydb startet.

## Konfiguration

Alle Variablen werden in `/etc/elasticsearch/elasticsearch.yml` konfiguriert, wenn nicht anders gesagt.

### Nodes und Shards

Wenn die Nodes gestartet werden, bilden sie automatisch einen Cluster, wenn alle den gleichen `cluster.name`
haben. `node.name` ist der ID für den jeweiligen Node.

Man kann die Nodes spezialisieren. Die Konfiguration läuft über die Variablen in `node.master`
und `node.data`:

| Typ | node.master | node.data | Bedeutung |
|-----|-------------|-----------|-----------|
| Master node | true | false | Koordiniert die anderen Nodes, speichert keine Shards |
| Data node | false | true | Speichert Shards und macht die Suchoperationen |
| Load balancer | false | false | Verteilt die Anfragen zu den Data Nodes |
| Nicht spezialisiert | true | true | Macht alles |

ES wählt automatisch einen Master Node von allen, die es können. Anfänglich werden wir ausschließlich
nicht spezialisierte Nodes haben, weil das sich erst lohnt, wenn man einen großen Cluster hat.

Die Nodes verteilen die Dokumente eines Indexes in Shards. Leider lässt sich die Anzahl der Shards nicht
ändern, wenn ein Index angelegt wird. Das heißt, man muss im Voraus denken, wie groß der Cluster werden
kann. Die Konfigurationsvariable dazu ist `index.number_of_shards`. Man kann die auch beim Mapping für
einen Index bestimmen, aber für unseren Fall macht das wahrscheinlich keinen Sinn.

### Speicher

Lucene stützt sich stark auf Filesystem-Cache. Das heißt, man sollte Elasticsearch nicht so viel
Speicher zuweisen. Auf der Webseite steht, man sollte ungefähr die Hälfte vom verfügbaren Speicher
zuweisen. Danach kann man über die Monitoring-Tools schauen, ob wir diesen Wert ändern.

Elasticsearch kann so konfiguriert werden, dass der ihm zugewiesene Speicher gelockt wird, sodass
das Betriebsystem ihn nicht swapt.

Man sollte folgende Umgebungsvariablen konfigurieren:

- `ES_HEAP_SIZE=...`: z.B. "6g"
- `MAX_LOCKED_MEMORY=unlimited`

Und in der Konfigurationsdatei:

- `bootstrap.mlockall: true`

### Andere Konfigurationsvariablen

Man kann in `plugin.mandatory` eine Liste von Plugins konfigurieren. Elasticsearch wird nicht
startet, wenn ein Plugin aus der Liste fehlt. Bei Easydb ist "analysis-icu" notwendig.

Abhängig von der Netzwerk-Architektur des Clusters muss man auch Einstellungen für Network,
Gateway, Recovery und Discovery setzen. Für Amazon EC2 gibt es spezielle Plugins und Einstellungen.

## Monitoring and Control

Es gibt viele Monitoring-Plugins:

- http://mrburns:9200/_plugin/HQ/
- http://mrburns:9200/_plugin/kopf/
- http://mrburns:9200/_plugin/bigdesk/
- http://mrburns:9200/_plugin/head/
- http://mrburns:9200/_plugin/paramedic/
- http://mrburns:9200/_plugin/segmentspy/

Im laufenden Betrieb kann man bestimmte Routing-Eigenschaften eines Indexes ändern, wie z.B. wie viele
Shards maximal in einem Node gespeichert werden (`routing.allocation.total_shards_per_node`). Die Liste
der möglichen Variablen ist hier: http://www.elasticsearch.org/guide/reference/api/admin-indices-update-settings/

Auch die Anzahl von Replikas lässt sich im laufenden Betrieb ändern (`index.number_of_replicas`). Dabei muss
man darauf achten, dass Elasticsearch versucht, die Replica Shards immer in einem anderen Node als die Primary Shards
zu stellen. Der Cluster-Status wird dann Rot, wenn das nicht möglich ist.

Ansonsten kann man die Logs benutzen. Die lassen sich über `/etc/elasticsearch/logging.yml` konfigurieren.
Elasticsearch benutzt log4j (http://logging.apache.org/log4j/2.x/manual/configuration.html).

