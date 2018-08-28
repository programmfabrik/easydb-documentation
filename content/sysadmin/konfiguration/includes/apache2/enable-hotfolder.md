```apache2
<VirtualHost *:443>
	AliasMatch ^/upload(.*)$ /media/upload$1
	<Location /upload>
		ProxyPass "!"
		Require all granted
		DAV on
		Options -MultiViews
		ErrorDocument 404 "Not Found"
		ErrorDocument 500 "Internal Server Error"
		ErrorDocument 502 "Bad Gateway"
	</Location>

	ProxyPass / http://127.0.0.1:80/
	ProxyPassReverse / http://127.0.0.1:80/
	…
</VirtualHost>
```