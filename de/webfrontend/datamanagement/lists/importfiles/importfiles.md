# Dateien importieren

Es gibt keinen 'Datei-Importer' im eigentlichen Sinne, allerdings sind der CSV-Importer und der JSON-Importer in der Lage, Dateien zu importieren. Beide haben eine gemeinsame Konfiguration.

### Configuration

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

![](/assets/webserver_chrome_de.png)
![](/assets/my_image_de.png)






