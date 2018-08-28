```apache2
Listen *:443
<VirtualHost *:443>
    ProxyPass / http://127.0.0.1:80/
    ProxyPassReverse / http://127.0.0.1:80/

    SSLEngine on
    SSLCertificateFile /etc/ssl/private/cert.pem
    SSLCertificateKeyFile /etc/ssl/private/key.pem
    # ggf. weitere SSL-Konfiguration je nach Ihren Anforderungen
</VirtualHost>
```