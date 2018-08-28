```apache2
Listen 1.2.3.4:80
<VirtualHost *:80>
    RewriteEngine on
    RewriteRule ^/(.*) https://as.in.certificate.example.com/$1 [R]
</VirtualHost>
```