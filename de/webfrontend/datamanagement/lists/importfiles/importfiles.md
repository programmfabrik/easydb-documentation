# Dateien importieren

Web-Browser unterstützen keinen direkten Zugriff auf Dateien auf Ihrem Computer, weshalb für den [CSV Importer](../csvimport/csvimport.html) und den [JSON Importer](../jsonimport/jsonimport.html) Dateien grundsätzlich über einen Web-Server bereitgestellt werden müssen.

Eine Möglichkeit diese Einschränkung zu umgehen, bietet eine Extension für den Google Chrome Browser. Hierdurch es ermöglicht mit wenigen Klicks einen Web-Server auf Ihrem Computer einzurichten und darüber Ihre Dateien zu erreichen.

Der CSV- und JSON-Importer bekommen über den Web-Server Zugriff auf Ihre Netzlaufwerke und lokalen Festplatten.

### Konfiguration

* Upload Typ für Dateien: Methode zum Hochladen der Dateien
  * Direkt: Die Datei wird heruntergeladen und dann mit /eas/put hochgeladen.
  * URL \(remote PUT\): Die Datei wird nicht heruntergeladen und /eas/put wird direkt über die Datei-URL aufgerufen. Die Datei wird vom Server heruntergeladen und hochgeladen. \(Diese Option ist die schnellste.\)
  * FYLR. Proxy: Diese Option funktioniert ähnlich wie 'Direkt'. Der Unterschied besteht darin, dass die URL den FYLR. Proxy verwendet, der in der Basiskonfiguration konfiguriert wird. Diese Option ist deaktiviert, wenn keine FYLR-Konfiguration in der Basiskonfiguration vorhanden ist.
  * Dateien ignorieren: Alle Dateien werden ignoriert.

### Lokale Dateien importieren

#### Mit Chrome

Um Dateien zu importieren, die sich im lokalen Dateisystem befinden, ist es notwendig, sie auf einem lokalen Server bereitzustellen. Der einfachste und schnellste Weg ist, eine bekannte Google Chrome-Erweiterung namens ['Web Server for Chrome'](https://legacy.gitbook.com/book/programmfabrik/easydb/edit#) zu verwenden. In diesem Fall muss der Typ 'Direkt' gewählt werden.

1. Installieren Sie die Erweiterung und öffnen Sie sie.  ['Jetzt downloaden.'](https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb)
2. Klicken Sie auf "Choose folder" und wählen Sie den Ordner, in dem sich die gewünschten lokalen Dateien für den Import befinden.
3. Öffnen Sie die erweiterten Einstellungen und aktivieren Sie die Option 'Set CORS headers'.
4. Starten Sie den Browser neu und öffnen Sie die Erweiterung erneut.
5. Geben Sie "[http://127.0.0.1:8887](http://127.0.0.1:8887)" ein. Dort befinden sich alle Bilder. \(Voreingestellt ist der Port 8887. Dieser kann geändert werden.\)

![](webserver_chrome_de.png)
![](my_image_de.png)






