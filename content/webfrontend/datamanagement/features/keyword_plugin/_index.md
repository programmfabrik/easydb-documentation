---
title: "88 - Auto Keyworder Plugin"
menu:
  main:
    name: "Auto Keyworder Plugin"
    identifier: "webfrontend/datamanagement/features/keyword_plugin"
    parent: "webfrontend/datamanagement/features"
---
# Auto Keyworder Plugin

##Plugin API

Dieses Plugin stellt der easydb-API einen neuen Endpunkt zur Verfügung: `api/plugin/base/auto-keyworder/start_now`.

Die API kann mit einer GET/POST -Anfrage mit einem leeren Body aufgerufen werden. Wenn die Anfrage authentifiziert ist, wird die `start_now`-Flag zu `true` gesetzt. Sobald die Basis-Konfiguration das nächste Mal geladen wird, sorgt die Flag dafür, dass die Prozessschleifen sofort starten. Dieses Verahlten ist das gleiche, wie wenn man die **Update-Prozess nach dem Speichern**-Chechbox aktiviert, die im Frontend in der Basiskonfiguration zu finden ist.

###Authentifizierung

Die API benötigt eine Authentifizierung mit einer HMAC-Signatur. Der Body der Anfrage muss mit einem HMAC-Secret verschlüsselt sein, welches SHA1 benutzt und die Signatur muss hexadezimal vorliegen. Die Signatur muss in der Kopfzeile X-Hub-Signatur entahlten sein.

```
    -H 'X-Hub-Signature: sha1=69a026d1baf79cc241ca82ffc4d47a6ee7d01337'
```

Das HMAC-Secret muss dasselbe sein, das in der Serverkonfiguration system.auto_keyworder.webhook_hmac konfiguriert ist. Wenn dieser Wert in der Serverkonfiguration nicht gesetzt ist, kann die API nicht verwendet werden.

###Verwendung der API mit einer easydb-Transition (Workflow)

Um diese API automatisch aufzurufen und einen Aktualisierungsprozess im Hintergrund zu starten, nachdem Objekte mit Tags eingefügt/aktualisiert wurden, können Sie einen Webhook konfigurieren, der als Aktion eines Workflows registriert wird.


1. Fügen Sie in der Basiskonfiguration unter "Tag & Workflow" eine Webhook-Konfiguration mit den folgenden Einstellungen hinzu:
    * **URL**: `<easydb url>/api/plugin/base/auto-keyworder/start_now`
    * **HMAC secret**: Value of `system.auto_keyworder.webhook_hmac` from the [server configuration](/en/sysadmin/configuration/easydb-server.yml/plugins/auto-keyworder/)
    
2. Siehe [easydb documentation: Workflows](/en/webfrontend/rightsmanagement/tags/#a-nameworkflows-a-workflows), wie man einen Workflow einrichtet. Für jeden der Dienst-Konfigurationsblöcke sollte ein Workflow die folgenden Einstellungen haben:
    * **Operation**: Einfügen and Update
    * **Typ**: NORMAL
    * **Objekt Typ**: Wählen Sie die Objekttypen aus, die in der Servicekonfiguration konfiguriert sind.
    * **Benutzer/Gruppen**: Wählen Sie Gruppen oder Benutzer aus, die in der Lage sein sollen, diesen Workflow auszulösen.
        * Wählen Sie **nicht** den Benutzer aus, der in der Basiskonfiguration für die API-Verwendung des Plugins konfiguriert ist! Dies kann eine Endlosschleife von Aktualisierungen von Objekten erzeugen!
    * **Tags Nach dem Speichern**: der Tagfilter sollte der gleiche sein wie der Tagfilter in der Dienst-Konfiguration
    * **Aktionen**: eine der Aktionen sollte die Webhook-Aktion mit dem Webhook sein, der so konfiguriert ist, dass er den Plugin-API-Endpunkt `/start_now` aufruft 
    
> HINWEIS: Dieses Plugin wird als separates Modul lizensiert. Bitte überprüfen Sie im Zweifel Ihren Lizenzvertrag.