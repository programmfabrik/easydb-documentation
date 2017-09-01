# HTTPS

Der Datenverkehr mit der easydb kann jederzeit per HTTPS verschlüsselt werden.

Tatsächlich muss die easydb dazu nicht verändert werden, sondern wird nur durch einen zusätzlichen Webserver geschützt der außerhalb der docker-Container läuft.

HTTPS betrachten wir somit nicht als Teil der easydb; aber zur Erleichterung Ihrer Arbeit zeigen wir hier die beispielhafte Umsetzung per Apache Webserver.

> Ein vorhandenes passendes Zertifikat wird vorausgesetzt.

## Konfiguration des HTTPS-Webservers


Für diesen Zweck reicht eine reduzierte Konfiguration des Apache.

Falls Sie weiterhin auch unverschlüsselten Datenverkehr zulassen wollen, dann müssen Sie darauf achten, dass Apache nicht den Port 80 nutzt, wo bereits die easydb lauscht.

Hier die wichtigsten Zeilen der Konfiguration:

~~~~
Listen *:443
<VirtualHost *:443>
	ProxyPass / http://127.0.0.1:80/
	ProxyPassReverse / http://127.0.0.1:80/

	SSLEngine on
	SSLCertificateFile /etc/ssl/private/cert.pem
	SSLCertificateKeyFile /etc/ssl/private/key.pem
    # ggf. weitere SSL-Konfiguration je nach Ihren Anforderungen
</VirtualHost>
~~~~


Unter Debian 8 aktivieren Sie die notwendigen Module z.B. mit:

~~~~
a2enmod ssl
a2enmod proxy
a2enmod proxy_http
a2enmod rewrite
apache2ctl configtest
~~~~

## Verhindern von Zugriffen ohne HTTPS

Falls Sie unverschlüsselten Zugriff unterbinden wollen sind auch dazu nur wenige Änderungen notwendig.

### easydb-Start

Beim Start des Cotainers "easydb-webfrontend" kann dazu die lokale Netzwerk-Schnittstelle angegeben werden, die von außerhalb des Servers nicht direkt erreicht werden kann.

Im Vergleich zum Start im Kapitel [Installation](/sysadmin/installation/installation.md#start) ändert sich nur die vorletzte Zeile: Sie wird um `127.0.0.1:` ergänzt:

~~~~
docker run -d -ti \
    --name easydb-webfrontend \
    --net easy5net \
    --volume=$BASEDIR/config:/config \
    -p 127.0.0.1:80:80 \
    docker.easydb.de:5000/pf/webfrontend
~~~~


### easydb-Konfiguration

In der zentralen `easydb5-master.yml`, deren Speicherort Sie bei der [Installation](/sysadmin/installation/installation.md#datenablage_bestimmen) festgelegt haben, sollten Sie die URL von http zu https ändern:

~~~~
easydb-server:
  server:
    external_url: https://hostname.as.in.certificate.example.com
~~~~

Falls Sie sowohl http als auch https-Zugriffe erlauben dann geben Sie hier trotzdem nur ein Protokoll an.

## Umleiten von HTTP-Zugriffen

Damit Anfragen per HTTP nicht abgewiesen werden sondern in HTTPS-Anfragen umgewandelt werden sind z.B. folgende Angaben notwendig:

Apache:

~~~~
Listen 1.2.3.4:80
<VirtualHost *:80>
    RewriteEngine on
    RewriteRule ^/(.*) https://as.in.certificate.example.com/$1 [R]
</VirtualHost>
~~~~

Bei Verwendung des Port 80 durch sowohl easydb als auch Apache muss mit der `Listen`-Direktive sichergestellt werden, dass Apache andere IP-Adressen nutzt als die easydb. Die easydb nutzt in diesem Beispiel nur die Adresse der lokalen Schnittstelle, also 127.0.0.1.

Bitte ersetzen Sie "example.com" und "1.2.3.4" durch Hostname und IP-Adresse Ihres Servers. Der Hostname sollte mit der Angabe im Zertifikat übereinstimmen.

