```bash
docker exec -ti easydb-server bash

apt-get install telnet
telnet 172.18.0.1 25

mail from:<noreply@example.com>
rcpt to:<you@example.com>
data
Subject: test via SMTP
.

quit
```