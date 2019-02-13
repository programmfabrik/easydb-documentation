---
title: "91 - Dateien importieren"
menu:
  main:
    name: "Dateien importieren"
    identifier: "webfrontend/datamanagement/lists/importfiles"
    parent: "webfrontend/datamanagement/lists"
---
# Dateien importieren

Web-Browser unterstützen keinen direkten Zugriff auf Dateien auf Ihrem Computer, weshalb für den [CSV Importer](../csvimport) und den [JSON Importer](../jsonimport) Dateien grundsätzlich über einen Web-Server bereitgestellt werden müssen.

Eine Möglichkeit diese Einschränkung zu umgehen, bietet eine Extension für den Google Chrome Browser. Hierdurch wird es ermöglicht, mit wenigen Klicks einen Web-Server auf Ihrem Computer einzurichten und darüber Ihre Dateien zu erreichen.

Der CSV- und der JSON-Importer bekommen über den Web-Server Zugriff auf Ihre Netzlaufwerke und lokalen Festplatten.

### Konfiguration

* Upload Typ für Dateien: Methode zum Hochladen der Dateien
  * Direkt: Die Datei wird heruntergeladen und dann mit /eas/put hochgeladen.
  * URL \(remote PUT\): Die Datei wird nicht heruntergeladen und /eas/put wird direkt über die Datei-URL aufgerufen. Die Datei wird vom Server heruntergeladen und hochgeladen. \(Diese Option ist die schnellste.\)
  * Dateien ignorieren: Alle Dateien werden ignoriert.

### Lokale Dateien importieren

#### Mit Chrome

Um Dateien zu importieren, die sich im lokalen Dateisystem befinden, ist es notwendig, sie auf einem lokalen Server bereitzustellen. Der einfachste und schnellste Weg ist, eine bekannte Google Chrome-Erweiterung namens ['Web Server for Chrome'](https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb) zu verwenden. In diesem Fall muss der Typ 'Direkt' gewählt werden.

1. Installieren Sie die Erweiterung und öffnen Sie sie.  ['Jetzt downloaden.'](https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb)
2. Klicken Sie auf "Choose folder" und wählen Sie den Ordner, in dem sich die gewünschten lokalen Dateien für den Import befinden.
3. Öffnen Sie die erweiterten Einstellungen und aktivieren Sie die Option 'Set CORS headers'.
4. Starten Sie den Browser neu und öffnen Sie die Erweiterung erneut.
5. Geben Sie **http://127.0.0.1:8887** ein. Dort befinden sich alle Bilder. \(Voreingestellt ist der Port 8887. Dieser kann geändert werden.\)

![](webserver_chrome_de.png)
![](my_image_de.png)






