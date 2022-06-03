---
title: "67 - Export, Deep-Links und XSLT"
menu:
  main:
    name: "Export, Deep-Links und XSLT"
    identifier: "webfrontend/administration/base-config/export"
    parent: "webfrontend/administration/base-config"
---
## Export, Deep-Links und XSLT

easydb stellt verschiedene Arten des unauthentifizierten Zugriffs auf die Dateien und Daten bereit. Für die Zugriffe stehen zum einen Deep-Links und zum anderen OAI/PMH zur Verfügung.

Nutzen Sie Deep-Links, wenn es darum geht, eine Ressource aus der easydb direkt im Zugriff zu haben, OAI/PMH kann genutzt werden, um mehrere Ressourcen und auch Veränderungen an Ressourcen zu überwachen und zu laden.

### Deep-Link-Freigabe

Die Deep-Link-Freigaben sind technisch über die API-Schnittstelle [/api/objects](https://docs.easydb.de/en/technical/api/objects) gelöst. Dort finden sich explizite Informationen über den Aufbau der URL. Im Frontend finden Sie an verschiedenen Stellen diese Deep-Links [Detail(Teilen)]() und im [EAS-Column(Teilen/) und im [EAS-Column(Teilen.html)](). Deep-Links werden immer über den Benutzer *DeepLink* authentifiziert. Geben Sie diesem Benutzer die nötigen Rechte an den Daten, damit der Zugriff von außen erfolgen kann.

|Einstellung | Erläuterung |
|----|---|
|erlauben| An- und Ausschalten der Deep-Link-Schnittstelle. |
|inklusive sichtbarer Referenz auf ID| Erlaubt einen direkt Zugriff per Objekt-ID. Da diese Objekt-IDs fortlaufend vergeben werden, kann es ein Sicherheitsrisiko sein, diese Option freizuschalten. Ein Benutzer, dem ein Deep-Link bekannt gemacht wird, kann durch Probieren weitere Deep-Links erraten. Für alle Deep-Links gilt aber immer, dass der *DeepLink*-Benutzer auf die Objekte Zugriff haben muss, damit sie funktionieren. |
|inklusive sichtbarer Referenz auf ein eindeutiges Feld| Wie die Referenz auf ID legen sie hiermit fest, ob über eineindeutige Datenfelder ein Deep-Link-Zugriff erfolgen darf oder nicht.|
|EAS-URLs anzeigen|Mit dieser Option werden direkte Datei-Links in der z. B. XML Ausgabe der Deep-Links geschrieben. Diese Links zielen direkt auf eine Datei und sind nicht mehr rechte-gemanagt. Diese URLs verlieren nie ihre Gültigkeit. Ohne diese Option stehen im XML noch anderen URLs für den Zugriff auf Dateien zur Verfügung. |
| Verlinkte Datensätze einbetten | Verlinkte Objekte sind, wie beim XML-Export, standardmäßig nicht im XML-Dokument enthalten.<br>Wird die Option "Alle" ausgewählt, werden alle verlinkten Datensätze nachgeladen.<br>Wird "Nicht in der Hauptsuche enthaltene Datensätze" gewählt, werden während des Exports alle verlinkten Objekte, die nicht in der Hauptsuche enthalten sind, nachgeladen und im XML eingebettet.<br>ird "Nicht in der Hauptsuche enthaltene Datensätze + reverse-editierbare Datensätze" gewählt, werden während des Exports alle verlinkten Objekte, die nicht in der Hauptsuche enthalten oder über "Editierbar in Verlinkung" verknüpft sind, nachgeladen und im XML eingebettet.<br>Wird "Keine" ausgewählt, werden keine verlinkten Datensätze nachgeladen, sondern nur der Standard wird exportiert. <br>**Hinweis:** diese Option hat nur Auswirkungen, wenn das [Format `xml_easydb`](https://docs.easydb.de/en/technical/api/objects/#path-part-format) für den Deep-Link verwendet wird. |
| Verschachtelungstiefe | Wenn verlinkte Objekte nachgeladen werden, gibt die Tiefe an, wie viele Ebenen von Verlinkungen nachgeladen werden (`1` - `9`). |

### XSLT-Formate

Verschiedene [XSLT](https://www.w3.org/TR/xslt/) Stylesheets können hochgeladen werden, um ausgegebene easydb-Daten im XML Format in beliebige andere Formate zu transformieren. Dies beinhaltet [Exporte im XML format](/de/webfrontend/datamanagement/features/export/#daten), [Deep-Links im XML format](/en/technical/api/objects/#path-part-format) und die OAI/PMH Schnittstelle.

Die OAI/PMH-Schnittstelle kann neben dem Standard-easydb-Format und [Dublin-Core](http://dublincore.org/) (das ist Pflicht bei OAI-PMH), eigens definierte Formate bereitstellen (z.B. LIDO). Um Dublin Core zu nutzen, muss im Bereich [Metadaten-Mapping](../../profiles) ein Dublin-Core-Mapping eingerichtet werden.

Darüber hinaus muss dieses im Anschluss beim entsprechenden [Objekttyp](../../datamodel/objecttype) verknüpft werden. Für diese Formate muss ein XSLT erstellt werden, welches das Standard-easydb-Format umwandelt.

Die OAI/PMH-Schnittstelle stellt je hochgeladenem XSLT ein Metadaten-Format bereit. Um ein XSLT für OAI/PMH zu nutzen, muss dafür ein spezifischer, technischer Name vergeben werden (dieser wird als Prefix verwendet), sowie die Checkbox "Für OAI/PMH verwenden" aktiviert werden. Danach wird dieses XSLT-Format als zusätzliches [Metadaten-Format](/en/technical/protocols/oai-pmh/#metadata-formats) zur Verfügung gestellt.

|Einstellung | Erläuterung |
| ------ |  -------- |
| Name | Technischer Name. In der OAI / PMH Schnittstelle wird dies als Metadatenformat (`metadataFormat=<name>`) genutzt. In der Deep-Link-Schnittstell kann dieses XSLT mit `format/xslt/<name>` ausgewählt werden. |
| Für OAI/PMH verwenden | Dieses XSLT für die OAI/PMH Schnittstelle nutzen. **Hinweise:** da der OAI/PMH Standard XML voraussetzt, stellen Sie sicher, dass dieses XSLT valides XML produziert. Andernfalls können im OAI/PMH plugin interne Fehler beim Parsen auftreten. |
| Für Deep-Links verwenden | Dieses XSLT für die Deep-LinkSchnittstelle nutzen. |
| Schema | XML Schema (optional). |
| Namespace | XML Namespace (optional). |
| Anzeigename | Anzeigenname des Formates (optional). |
| Beschreibung | Beschreibung des Formates (optional). |
| XSLT | XSLT-Datei zur Tranformation der Daten. |

## Veröffentlichen

Objekte können über die [`publish` API](/en/technical/api/publish/#publish-an-object) auf externen Repositories veröffentlicht werden.

Es können mehrere Collectoren konfiguriert werden:

|Einstellung | Erläuterung |
|---|---|
| Anzeigename | Anzeigename für diesen Collector (optional) |
| Interner Name| Name des Collectors, der die Veröffentlichung ausgelöst hat. Dieser interne Name wird in der API genutzt, um den Collector eindeutig zu identifizieren |
| URL | URL des Repositories (optional, muss valide URL sein falls gesetzt) |
| Typ | Freitext zur Identifizierung und Gruppierung der Collectoren (optional) |
| Präfix | Wenn Objekte an einer relativen URI veröffentlicht werden, wird zusammen mit dem Präfix die URI des Objekts gebildet (optional, muss valide URL sein falls gesetzt) |
| Logo | Laden Sie hier ein kleines Logo für Collectoren hoch (optional). |
| Display | Wählen Sie hier, welche Informationen in der Detailansicht zu den Collectoren angezeigt werden sollen: "Name, Typ und DOI/URN", "Name und Typ" oder nur "Name" oder "Typ". |

### OAI/PMH

Die OAI/PMH-Schnittstelle ist eine Harvesting-Schnittstelle. Mehr Informationen dazu finden Sie in der [Protokoll-Beschreibung](https://docs.easydb.de/en/technical/protocols/oai-pmh) und auf [Openarchives](http://www.openarchives.org/).

Die Suchen, die die Schnittstelle durchführt, werden mit dem System-Benutzer *OAI/PMH* durchgeführt. Geben Sie diesem Benutzer die Rechte, Daten zu sehen.

|Einstellung | Erläuterung |
|----|---|
|Freigeben| An- und Ausschalten der OAI/PMH-Schnittstelle. |
|Repository-Name| Name des OAI/PMH-Repository. |
|Administrator-E-Mail| Email, die in den OAI-Antworten angegeben ist. |
|Namespace| Frei definierbarer OAI-Identifier-Namespace. Objekte können beispielsweise über `oai:<namespace>:<uuid>` in der URL angefordert werden. |
|Tag-Sets|Definieren Sie hier Tagfilter, um neue OAI/PMH-Sets zu erzeugen. Sie können damit z.B. alle Objekte zusammenfassen, die den Tag *Internet* haben. |
|EAS-URLs anzeigen|Wie bei den Deep-Links wird damit festgelegt, ob die direkten Datei-Links im XML ausgeben werden oder nicht. Siehe Deep-Link.|
| Verlinkte Datensätze einbetten | Verlinkte Objekte sind, wie beim XML-Export, standardmäßig nicht im XML-Dokument enthalten.<br>Wird die Option "Alle" ausgewählt, werden alle verlinkten Datensätze nachgeladen.<br>Wird "Nicht in der Hauptsuche enthaltene Datensätze" gewählt, werden während des Exports alle verlinkten Objekte, die nicht in der Hauptsuche enthalten sind, nachgeladen und im XML eingebettet.<br>Wird "Keine" ausgewählt, werden keine verlinkten Datensätze nachgeladen, sondern nur der Standard wird exportiert. |
| Verschachtelungstiefe | Wenn verlinkte Objekte nachgeladen werden, gibt die Tiefe an, wie viele Ebenen von Verlinkungen nachgeladen werden (`1` - `9`). |
