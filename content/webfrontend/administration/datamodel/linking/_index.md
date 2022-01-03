---
title: "Verlinkungen"
menu:
  main:
    name: "Verlinkungen"
    identifier: "webfrontend/administration/datamodel/linking"
    parent: "webfrontend/administration/datamodel"
---
# Verlinkungen

In easydb gibt es verschiedene Möglichkeiten andere Objekttypen zu verlinken um auf andere Listen, kontrollierte Vokabulare oder Thesauri zuzugreifen. Diese sind nachfolgend erläutert.



## Einfache Verlinkung

Möchte man bei einem Eingabefeld keine Freitexteingabe verwenden, sondern auf andere Listen, kontrollierte Vokabulare oder Thesauri zugreifen, so wählt man im Datenmodell bei diesem Feld einfach einen anderen Objekttyp aus, dessen Inhalte anschließend in diesem Feld zur Verfügung stehen sollen. 

**Beispiel:** man möchte bei einem Foto auf eine Liste von Fotografen zugreifen um nicht jedes Mal den Namen des Fotografen manuell eingeben zu müssen.

Hierbei handelt es sich um ein sog. "forward linking". Das bedeutet, dass zwar das Foto weiß, welcher Fotograf verlinkt ist, der verlinkte Fotograf aber keinerlei Information darüber hat mit welchen Fotos er verknüpft ist. Beim Export von Fotografen sind demnach keine Informationen zu den Fotos bei denen dieser hinterlegt ist, enthalten. 

Um bei den Fotografen in der Detailansicht alle Fotos anzuzeigen, bei denen dieser verknüpft ist, kann das Plugin https://github.com/programmfabrik/easydb-custom-mask-splitter-detail-linked-plugin verwendet werden.



## Editierbar in Verlinkung (Hierarchie)

Diese Option ist nur bei hierarchischen Objekttypen verfügbar und befindet sich auf dem Reiter "Allgemein" unter "Datenbankoptionen". 

**Beispiel:**

```
Deutschland
    Berlin
    	Prenzlauer Berg
    	Mitte
    Hamburg
    München
Spanien
    Barcelona
    Lissabon
```



Standardmäßig weiß der Eintrag "Deutschland" nicht, dass sich unter ihm noch die Einträge "Berlin", "Hamburg" und "München" befinden. Lediglich "Berlin", "Hamburg" und "München" wissen, dass sie unter "Deutschland" hängen. Dies bedeutet, dass man in der Detailansicht von "Deutschland" die untergeordneten Einträge nicht sieht, sondern nur bei den untergeordneten Einträgen den übergeordneten.

Möchte man nun bei "Deutschland" aber auch die direkt untergeordneten Einträge sehen und möglicherweise sogar bearbeiten können, so muss für den Objekttyp "Editierbar in Verlinkung" aktiviert werden. Anschließend steht in der Maske eine automatisch generierte Zeile zur Verfügung über die man steuern kann, welche Informationen der untergeordneten Einträge angezeigt bzw. editiert werden können sollen. In der Eingabemaske steht darüber hinaus auch ein Plus zur Verfügung um neue untergeordnete Einträge anlegen zu können. 

Die Informationen der untergeordneten Einträge werden in den Index des übergeordneten Eintrags integriert und stehen somit auch in der Suche und beim Export zur Verfügung.



## Editierbar in Verlinkung (einfach)

"Editierbar in Verlinkung" kommt zum Einsatz, wenn man zwei unterschiedliche Objekttypen miteinander verknüpfen und die Informationen eines dieser Objekttypen in den anderen integrieren möchte. Als Beispiel kann hier die Verknüpfung von Sammlungsobjekten und Fotos herangezogen werden. Nehmen wir an, dass ein Foto immer nur mit einem Sammlungsobjekt verknüpft werden soll und ein Sammlungsobjekt mehrere Fotos haben kann. Ohne "Editierbar in Verlinkung" würde man im Objekttyp "Sammlungsobjekte" ein Mehrfach-Feld mit Verlinkung auf den Objekttyp "Fotos" einbauen. Dies hätte allerdings zur Folge, dass bei den Fotos nicht ersichtlich wäre, mit welchem Sammlungsobjekt dieses verknüpft ist. Würde man die Verlinkung auf Seiten des Objekttyps "Fotos" einbauen, so würde man bei den Sammlungsobjekten die Fotos nicht sehen. 

Um dies zu ermöglichen, muss im Objekttyp "Fotos" ein einfaches Link-Feld auf den Objekttyp "Sammlungsobjekte" eingebaut und dort "Editierbar in Verlinkung" aktiviert werden. Dies bewirkt, dass die Informationen der Fotos in den Objekttyp "Sammlungsobjekte" integriert werden. In der Maske der Sammlungsobjekte wird automatisch eine Zeile für die Fotos erzeugt über die gesteuert werden kann, welche Felder vom Sammlungsobjekt heraus eingesehen bzw. direkt bearbeitet werden können. Es ist auch möglich vom Sammlungsobjekt heraus neue Fotos anzulegen und direkt mit dem Sammlungsobjekt zu verknüpfen. 

Die Informationen der eingebundenen Objekttypen werden mit indiziert und stehen in der Suche im beim Export zur Verfügung (in diesem Fall sind bei einem Export von Sammlungsobjekten auch Informationen zu den Fotos enthalten).



## Editierbar in Verlinkung (doppelt)

Möchte man zwei unterschiedliche Objekttypen so miteinander verbinden, dass eine Mehrfach-Verlinkung auf beiden Seiten eingesehen bzw. bearbeitet werden kann, muss man einen sog. Verbindungsobjekttypen anlegen, der zwei Felder enthält. Dies kann z.B. beim Leihverkehr notwendig werden. Nehmen wir an, wir haben einen Objekttyp "Sammlungsobjekte" und einen Objekttyp "Leihgaben", so möchte man bei den Leihgaben einsehen und bearbeiten können, welche Sammlungsobjekte verliehen wurden und bei den Sammlungsobjekten sehen und bearbeiten, bei welchen Leihvorgängen diese verknüpft sind.

**Beispiel Objekttyp "Sammlungsobjekt-Leihgaben":**

| Feldname        | Datentyp                              | Editierbar in Verlinkung |
| --------------- | ------------------------------------- | ------------------------ |
| Sammlungsobjekt | Link auf Objekttyp "Sammlungsobjekte" | Ja                       |
| Leihgaben       | Link auf Objekttyp "Leihgaben"        | Ja                       |



Durch Aktivierung von "Editierbar in Verlinkung" bei beiden Feldern, wird in den Masken der dort verwendeten Objekttypen jeweils eine Zeile generiert, über die u.a. gesteuert werden kann, ob die Verknüpfung nur eingesehen oder auch bearbeitet werden kann. 

Bearbeitet man nun eine Leihgabe und fügt dieser ein Sammlungsobjekt hinzu, so wird das Sammlungsobjekt automatisch auch mit der Leihgabe verknüpft. Die Informationen werden in den Index beider Objekttypen integriert und stehen somit auch in der Suche und beim Export zur Verfügung.



## Bidirektionale Verlinkung

Die bidirektionale Verknüpfung steht im Objekttyp nur zur Verfügung, wenn in einem Mehrfachfeld auf den gleichen Objekttyp verlinkt wird.

Beispiel: man möchte von einem Sammlungsobjekt auf anderes Sammlungsobjekt verlinken um Beziehungen / Verweise zwischen verschiedenen Sammlungsobjekten festzuhalten.

Standardmäßig wird bei einer Verlinkung von Objekt A auf Objekt B nur ein Link von A zu B abgespeichert. Dies bedeutet, dass Objek B nicht weiß, dass Objekt A auf ihn verweist. Man müsste demnach auch Objekt B bearbeiten und manuell einen Link auf Objekt A hinterlegen. Da dies besonders bei großen Datenmengen nicht handhabbar und auch fehleranfällig ist, kann dies automatisiert werden, indem man bei dem betroffenen Feld "bidirektional" aktiviert. Dies bewirkt, dass beim Verknüpfen von Objekt A mit Objekt B, bei Objekt B automatisch ein sog. Rücklink auf Objekt A abgespeichert wird. Somit kann die Verknüpfung auf beiden Seiten eingesehen und bearbeitet werden und wird ständig synchron gehalten. Befinden sich mehrere Felder in dem Mehrfachfeld, wie z.B. eine Bemerkung, so werden diese ebenfalls auf beiden Seiten gespeichert.



## Bidirektional Reverse

"Bidirektional Reverse" macht nur Sinn im Kontext einer bidirektionalen Verknüpfung. Nehmen wir noch einmal das Beispiel aus der bidirektionalen Verlinkung (s.o.), so kann es sein, dass dieser Verknüpfung von Objekt A und Objekt B noch ein Attribut mitgegeben werden soll. Beispielsweise um welche Art der Beziehung es sich handelt. Nehmen wir also an, dass Objekt B Teil von Objekt A ist, so bedeutet dies im Umkehrschluss, dass Objekt A aus dem Teil Objekt B besteht. Würde jetzt also diese Verknüpfung zwischen Objekt A und B über die bidirektionale Verlinkung automatisch erstellt werden, so würde das Attribut "ist Teil von" auf beiden Seiten stehen. Dies wäre natürlich falsch. Hier kommt dann "bidirektional reverse" ins Spiel. 

Im Objekttyp der für das Attribut (in unserem Beispiel "Verweistyp") verwendet wird, muss also festgehalten werden, welche Attributspaare zusammengehören. In unserem Fall wären dies die Einträge "ist Teil von" und "hat Teile". 

**Beispiel Objekttyp "Verweistyp":**

| Feldname                 | Datentyp                        | Bidirektional Reverse | Bemerkung                                                    |
| ------------------------ | ------------------------------- | --------------------- | ------------------------------------------------------------ |
| Verweistyp               | Freitext                        |                       | Bezeichnung des Verweistyps, z.B. "ist Teil von"             |
| Dazugehöriger Verweistyp | Link auf Objekttyp "Verweistyp" | Ja                    | der Verweistyp, der beim sog. Rücklink verwendet werden soll, z.B. "hat Teile" |



**Einträge "Verweistyp":**

| Verweistyp   | Dazugehöriger Verweistyp |
| ------------ | ------------------------ |
| ist Teil von | hat Teile                |
| hat Teile    | ist Teil von             |



Wird also in einer bidirektionalen Verknüpfung nun der Verweistyp "ist Teil von" ausgewählt, so wird beim Speichern des sog. Rücklinks automatisch der Verweistyp "hat Teile" gesetzt.
