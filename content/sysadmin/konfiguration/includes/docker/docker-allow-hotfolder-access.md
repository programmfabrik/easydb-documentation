```bash
docker run -d -ti \
	--name easydb-server \
	…
	--volume=/media/hotfolder:/hotfolder \
	docker.easydb.de:5000/pf/server-$SOLUTION
```