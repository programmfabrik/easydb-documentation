```bash
docker run -d -ti \
    --name easydb-webfrontend \
    --net easy5net \
    --volume=$BASEDIR/config:/config \
    -p 127.0.0.1:80:80 \
    docker.easydb.de:5000/pf/webfrontend
```