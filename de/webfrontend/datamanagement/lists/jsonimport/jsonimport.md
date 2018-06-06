# JSON Importer

Der JSON-Importer kann zum Massenimport von Daten im [JSON format](../../../technical/datamanagement/jsonimport.md) verwendet werden.

Den Importer finden Sie unter "Listen &gt; JSON Import".

Der Importer kann über eine ".json"-Datei konfiguriert werden. Die Datei enthält bereits Konfigurationen für die Verwendung im Importer.

## Frontend Formular

Felder:

* URL manifest.json: \(Optional\) Indem Sie auf die Schaltfläche 'Laden' neben der Eingabe klicken, erhalten Sie eine URL, um die manifest.json zu laden. 
* Source: \(Optional\) Name der Quellinstanz
* Payloads base URI: \(Optional\) Basis-URI für alle Payloads in der Liste. It will be prepended to each payload.
* Upload Typ für Dateien: Siehe [Import von Dateien ](../importfiles/importfiles.html)
* EAS-URL Ersetzung für Dateien: \(Optional\) The location for each file URL will be replaced by the value configured here.
* Payload list
  * Enabled: Checkbox to enable or skip the payload
  * Status: Current status of the payload. Pending/Success/Error
  * URL: The url of the payload
  * Actions
    * Open the payload in a new tab.

Buttons:

* Start: It starts the import of all the enabled payloads.
* Rollback: - Rollback: It makes a rollback of the imported data. The rollback data will be lost if the JSON Importer modal is closed.
* Logs



