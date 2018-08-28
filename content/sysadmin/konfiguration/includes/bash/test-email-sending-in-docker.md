```bash
docker exec -ti easydb-server bash

echo "Subject: testing sSMTP"|ssmtp -v -fnoreply@example.com -Fnoreply you@example.com
```