---
title: "Testsysteminstallation"
menu:
  main:
    name: "Testsysteminstallation"
    identifier: "tutorials/testsysteminstallation"
    parent: "tutorials"
---
# Testsysteminstallation (unter Debian Stretch bzw. Buster)

## Installation von Docker


Installation der Abhängigkeiten von Docker

```bash
apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common
```

Hinzufügen von Dockers GPG Key:
```bash
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
```

Dockers Fingerprint bestätigen bzw, hinzufügen:
```bash
apt-key fingerprint 0EBFCD88
```

Docker zu den APT Quellen hinzufügen:
```bash
add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"
```

Docker-CE installieren:
```bash
apt-get update
apt-get install docker-ce docker-ce-cli containerd.io
```

Das Docker Netzwerk für die easydb5 erstellen:
```bash
docker network create easy5net
```

***Mehr zu der Installation und Konfiguration von Docker, entnehmen Sie bitte der Dokumentation: https://docs.docker.com/install/linux/docker-ce/debian/***

---

## Startskripte der easydb5 anlegen

Startskript für den **postgres** Container anlegen (```/srv/easydb/run-pgsql.sh```) und mit folgendem Inhalt befüllen:
```bash
BASEDIR=/srv/easydb
docker run -d -ti \
    --name easydb-pgsql \
    --net easy5net \
    --security-opt seccomp=unconfined \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/pgsql/etc:/etc/postgresql \
    --volume=$BASEDIR/pgsql/log:/var/log/postgresql \
    --volume=$BASEDIR/pgsql/var:/var/lib/postgresql \
    --volume=$BASEDIR/pgsql/backup:/backup \
    docker.easydb.de/pf/postgresql
```

Startskript für den **elasticsearch** Container anlegen (```/srv/easydb/run-elasticsearch.sh```) und mit folgendem Inhalt befüllen:
```bash
sysctl -w vm.max_map_count=262144
# ... can be added persistently via /etc/sysctl.conf instead.
BASEDIR=/srv/easydb
docker run -d -ti \
    --name easydb-elasticsearch \
    --net easy5net \
    --security-opt seccomp=unconfined \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/elasticsearch/var:/var/lib/elasticsearch \
    docker.easydb.de/pf/elasticsearch
```

Startskript für den **eas** Container anlegen (```/srv/easydb/run-eas.sh```) und mit folgendem Inhalt befüllen:
```bash
BASEDIR=/srv/easydb
docker run -d -ti \
    --name easydb-eas \
    --net easy5net \
    --security-opt seccomp=unconfined \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/eas/lib:/var/opt/easydb/lib/eas \
    --volume=$BASEDIR/eas/log:/var/opt/easydb/log/eas \
    --volume=$BASEDIR/eas/tmp:/tmp \
    docker.easydb.de/pf/eas
```

Startskript für den **easydb** Container anlegen (```/srv/easydb/run-server.sh```) und mit folgendem Inhalt befüllen:
```bash
BASEDIR=/srv/easydb
SOLUTION=base
docker run -d -ti \
    --name easydb-server \
    --net easy5net \
    --security-opt seccomp=unconfined \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/easydb-server/var:/easydb-5/var \
    --volume=$BASEDIR/easydb-server/nginx-log:/var/log/nginx \
    docker.easydb.de/pf/server-$SOLUTION
```

Startskript für den **webfrontend** Container anlegen (```/srv/easydb/run-webfrontend.sh```) und mit folgendem Inhalt befüllen:
```bash
BASEDIR=/srv/easydb
docker run -d -ti \
    --name easydb-webfrontend \
    --net easy5net \
    --security-opt seccomp=unconfined \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    -p 80:80 \
    docker.easydb.de/pf/webfrontend
```

Startskript für den **fylr** Container anlegen (```/srv/easydb/run-fylr.sh```) und mit folgendem Inhalt befüllen:
```bash
BASEDIR=/srv/easydb
docker run -d -ti \
    --name easydb-fylr \
    --net easy5net \
    --security-opt seccomp=unconfined \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/fylr/objectstore:/objectstore \
    docker.easydb.de/pf/fylr
```

---

## Installation der easydb5

Login in die Docker-Registry der Programmfabrik
```bash
KONTONAME=meinUsernameVonDerProgrammfabrik
SOLUTION=base
docker login --username=$KONTONAME docker.easydb.de
```

Die Container von der Docker registry holen:
```bash
docker pull docker.easydb.de/pf/server-$SOLUTION
docker pull docker.easydb.de/pf/webfrontend
docker pull docker.easydb.de/pf/elasticsearch
docker pull docker.easydb.de/pf/eas
docker pull docker.easydb.de/pf/postgresql
docker pull docker.easydb.de/pf/fylr
```

Definition des Speicherortes für die easydb und die Assets (hier: ```/srv/easydb```):
```bash
BASEDIR=/srv/easydb
mkdir -p $BASEDIR/config/easydb-server.d
cd $BASEDIR
mkdir -p webfrontend eas/{lib,log,tmp} elasticsearch/var pgsql/{etc,var,log,backup} easydb-server/{nginx-log,var} fylr/objectstore
chmod a+rwx easydb-server/nginx-log elasticsearch/var eas/tmp; chmod o+t eas/tmp
touch config/eas.yml config/fylr.yml config/elasticsearch.yml
chown 1000:1000 fylr/objectstore
```

---

## Konfiguration der easydb5

Eine easydb-server Konfigurationsdatei anlegen (```/srv/easydb/config/easydb-server.yml```)
```yml
hostnames:
  server: easydb-server:80
  pgsql: easydb-pgsql:5432
  eas: easydb-eas:80
  elasticsearch: easydb-elasticsearch:9200
  fylr: easydb-fylr:4000

pgsql:
  host: easydb-pgsql
  port: 5432
  database: easydb

extension:
  external-user-schema: True

server:
  external_url: https://schulung.pf-berlin.de
  enable_post_settings: True
  api:
    settings:
      restart: True
      purgedata: False
      purgeall: False
  mailer:
    enabled: True

eas:
  url: http://easydb-eas:80/eas
  instance: easydb5

elasticsearch:
  url: http://easydb-elasticsearch:9200
  default_template: /config/elastic_index_template.json

docker-hostname: easydb-server

smtp:
  server: mail.programmfabrik.de
  hostname: schulung.pf-berlin.de
  from-address: noreply@schulung.pf-berlin.de
```

Mehr zu der Installation der easydb5 entnehmen Sie bitte folgender Quelle: [hier](/en/sysadmin/installation)

------

## easydb mit LDAP Authentifizierung

In der ```/srv/easydb/conf/easydb-server.d/ldap.yml```
```yml
plugins:
  enabled+:
    - base.ldap

ldap:
  - user:
      protocol: ldap
      server: potsdam.pf-berlin.de
      basedn: dc=potsdam,dc=pf-berlin,dc=de
      filter: '(&(objectClass=posixAccount)(uid=%(Login)s))'
    group:
      protocol: ldap
      server: potsdam.pf-berlin.de
      basedn: dc=potsdam,dc=pf-berlin,dc=de
      filter: '(&(memberUid=%(user.uid)s)(objectClass=posixGroup))'
    environment:
      mapping:
        u_login:
          attr: user.uid
          regex_match: '$'
          regex_replace: '@LDAP'
        g_ldap_prefixed:
          attr: group.cn
          regex_match: '^'
          regex_replace: 'ldap.'
      user:
        login: '%(u_login)s'
        displayname: '%(user.givenName)s %(user.sn)s'
        email: '%(user.mail)s'
      groups:
        - attr: g_ldap_prefixed
```

------

## Shibboleth Installation und Konfiguration

### Shibboleth Installation
```
apt-get install libapache2-mod-shib2
```

Apache2 requirements aktivieren:
```
a2enmod shib2
a2enmod socache_shmcb
a2enmod headers
a2enmod ssl
a2enmod rewrite
a2enmod proxy_http
a2enmod proxy
```

### Shibboleth Konfiguration

In der ```/srv/easydb/conf/easydb-server.d/shib.yml```
```yml
plugins:
  enabled+:
    - base.sso

sso:
  environment:
    mapping:
      m_login:
        attr: REMOTE_USER
        regex_match: '@.*$'
        regex_replace: ''
    user:
      login: "%(m_login)s"
      displayname: "%(cn)s"
      email: "%(mail)s"
    groups:
      - attr: affiliation
        divider: ';'

  auth_method:
    client:
      login:
        visible: true
        window_open: ""
        show_errors: true
      logout:
        url: https://schulung.pf-berlin.de/Shibboleth.sso/Logout
        window_open: ""
```

In der ```/etc/apache2/sites-enabled/easydb.conf```
```
<VirtualHost *:80>
    ServerAdmin administratoren@programmfabrik.de

    RewriteEngine on
    RewriteRule ^/(.*) https://schulung.pf-berlin.de/$1 [R]
</VirtualHost>

<VirtualHost *:443>
    ServerAdmin administratoren@programmfabrik.de

    SSLEngine on
    SSLCertificateFile  /etc/ssl/cert.pem
    SSLCertificateKeyFile /etc/ssl/private/server-key.pem

    # shibboleth
    RewriteEngine on
    RewriteRule .* - [E=X_REMOTE_USER:%{LA-F:REMOTE_USER}]
    RequestHeader set X-Remote-User "%{X_REMOTE_USER}e"
    ProxyPass /Shibboleth.sso !
    ProxyPass /shibboleth !
    ProxyPass /shibboleth-sp !
    Alias /shibboleth-sp /usr/share/shibboleth
    <Location /api/v1/session/sso/authenticate>
        AuthType shibboleth
        ShibRequireSession on
        ShibRequestSetting requireSession 1
        ShibUseHeaders on
        Require valid-user
    </Location>
    ErrorDocument 401 /web/sso_authentication_required.html

    ProxyPass / http://127.0.0.1:81/
    ProxyPassReverse / http://127.0.0.1:81/
</VirtualHost>
```

Sollte die Authentifizierung nicht funktioniert, schauen Sie sich bitte die Antwort Ihres Shibboleth-IDP's an. Dies können Sie dem easydb-server log entnehmen, welches Sie wie folgt sehen: ```docker logs --tail 1000 -f easydb-server```

------

# Wasserzeichen in der easydb5

In der ```/srv/easydb/conf/easydb-server.d/watermark.yml```:
```yml
include_before:
  - /config/eas_rights_management.yml

eas:
  produce_settings: /config/eas_produce.json

default_client:
  watermark_configured: true
```

Um an die Standard-Konfigurationsdateien der easydb5 zu gelanden, können Sie diese aus den Docker-Containern kopieren:
```bash
docker cp easydb-server:/easydb-5/base/eas/rights_management.yml /srv/easydb/config/eas_rights_management.yml
docker cp easydb-server:/easydb-5/base/eas/eas-produce.json      /srv/easydb/config/eas_produce.json
```

Nun können Sie die angelegten Dateien abändern und Ihre Versionen hinzufügen bzw. bestehende abändern und ein Wasserzeichen hinzufügen. Um Wasserzeichen für eine Version zu aktivieren, fügen Sie folgenden Key zu einem Eintrag hinzu:
```yml
watermark: true
```

Als Beispielkonfiguration schauen Sie sich in der nachfolgenden Konfiguration, die Version: ```preview_watermark``` an. 

In der ```/srv/easydb/conf/eas_rights_management.yml```:
```yml
eas:
  rights_management:
    image:
      versions:
        - version: small
          size_print: 250px
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: preview_watermark
          size_print: 1000px (watermark)
          size_limit: 1000
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: huge
          size_print: 2000px
          size_limit: 2000
          export: true
          rightsmanagement: true
          group: huge
          zoomable: true
        - version: full
          size_print: Original (formatiert)
          export: true
          rightsmanagement: true
          group: huge
          zoomable: true
    video:
      versions:
        - version: small
          size_print: 250px
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 720px
          size_limit: 720
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: preview_watermark
          size_print: 720px (watermark)
          size_limit: 720
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: huge
          size_print: 1920px
          size_limit: 1920
          export: true
          group: huge
          rightsmanagement: true
          zoomable: true
        - version: 360p
          size_print: 360p
          size_limit: 360
          export: true
          group: preview
          rightsmanagement: true
        - version: 720p
          size_print: 720p
          size_limit: 720
          export: true
          group: preview
          rightsmanagement: true
        - version: 1920p
          size_print: 1920p
          size_limit: 1920
          export: true
          rightsmanagement: true
          group: huge
    audio:
      versions:
        - version: small
          size_print: 250px (small)
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: preview_watermark
          size_print: 1000px (watermark)
          size_limit: 1000
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: aac
          size_print: aac
          export: true
          rightsmanagement: true
    office:
      versions:
        - version: small
          size_print: 250px (small)
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: preview_watermark
          size_print: 1000px (watermark)
          size_limit: 1000
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: pages
          size_print: pages
          rightsmanagement: true
          use_for_pages: true
    archive:
      versions:
        - version: small
          size_print: 250px (small)
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
        - version: directory
          size_print: directory
          group: huge
          rightsmanagement: true
    unknown:
      versions: []
    vector2d:
      versions:
        - version: small
          size_print: 250px
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
    vector3d:
      versions: []

```

In der ```/srv/easydb/conf/eas_produce.json```:
```json
{
	"__all": {
		"__all": {
			"small": {
				"target_size": "250x250",
				"target_size_min": "1",
				"target_format": "jpg",
				"target_quality": "80",
				"target_no_enlarge": "1",
				"target_no_fallback": "1",
				"priority": "12"
			}
		}
	},

	"image": {
		"__all": {
			"small": {
				"target_size": "250x250",
				"target_size_min": "1",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1",
				"priority": "12"
			},
			"preview": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			},
			"preview_watermark": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			},
			"huge": {
				"target_size": "2000x2000",
				"target_size_minimum": "1001x1001",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			},
			"full": {
				"target_format": "png",
				"target_size_minimum": "2001x2001",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			}
		},

		"jpg": {
			"small": {
				"target_size": "250x250",
				"target_format": "jpg",
				"target_quality": "80",
				"target_interlace": "1",
				"target_size_min": "1",
				"target_no_enlarge": "1",
				"priority": "12"
			},
			"preview": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_interlace": "1",
				"target_quality": "80",
				"target_no_enlarge": "1"
			},
			"preview_watermark": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_interlace": "1",
				"target_quality": "80",
				"target_no_enlarge": "1"
			},
			"huge": {
				"target_size": "2000x2000",
				"target_size_minimum": "1001x1001",
				"target_format": "jpg",
				"target_quality": "80",
				"target_interlace": "1",
				"target_no_enlarge": "1"
			},
			"full": {
				"target_format": "jpg",
				"target_size_minimum": "2001x2001",
				"target_interlace": "1",
				"target_quality": "80"
			}
		}
	},

	"video": {
		"__all": {
			"preview": {
				"target_size": "720x720",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_interlace": "1",
				"target_quality": "80",
				"target_no_enlarge": "1"
			},
			"preview_watermark": {
				"target_size": "720x720",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_interlace": "1",
				"target_quality": "80",
				"target_no_enlarge": "1"
			},
			"huge": {
				"target_size": "1920x1920",
				"target_size_minimum": "721x721",
				"target_format": "jpg",
				"target_quality": "80",
				"target_interlace": "1",
				"target_no_enlarge": "1"
			},
			"360p": {
				"target_height": "360",
				"target_format": "mp4",
				"target_no_enlarge": "1",
				"target_audio_bitrate": "160k",
				"target_video_bitrate": "840k"
			},
			"720p": {
				"target_height": "720",
				"target_size_minimum": "10000x361",
				"target_format": "mp4",
				"target_no_enlarge": "1",
				"target_audio_bitrate": "160k",
				"target_strip": "1",
				"target_video_bitrate": "840k"
			},
			"1920p": {
				"target_height": "1920",
				"target_size_minimum": "10000x721",
				"target_format": "mp4",
				"target_no_enlarge": "1",
				"target_audio_bitrate": "160k",
				"target_strip": "1",
				"target_video_bitrate": "840k"
			}
		}
	},

	"audio": {
		"__all": {
			"preview": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_quality": "80",
				"target_no_fallback": "1",
				"target_interlace": "1"
			},
			"preview_watermark": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "jpg",
				"target_interlace": "1",
				"target_no_fallback": "1",
				"target_quality": "80",
				"target_no_enlarge": "1"
			},
			"aac": {
				"target_format": "aac",
				"target_no_fallback": "1",
				"target_audio_bitrate": "160k"
			}
		}
	},

	"office": {
		"__all": {
			"__pages": {
				"__source": {
					"target_format": "png",
					"target_size": "1000x1000"
				},
				"small": {
					"target_size": "200x200",
					"target_format": "png"
				}
			},
			"preview": {
				"target_size": "1000x1000",
				"target_format": "png"
			},
			"preview_watermark": {
				"target_size": "1000x1000",
				"target_format": "png"
			}
		}
	},

	"archive": {
		"__all": {
			"thumb": false
		},
		"webdvd.zip": {
			"directory": {
				"target_format": "directory"
			},
			"small": {
				"target_size": "250x250",
				"target_extractsize": "1024x768",
				"target_format": "jpg",
				"target_quality": "80",
				"source_version": "directory",
				"priority": "12"
			},
            "preview": {
                "target_size": "1000x1000",
                "target_extractsize": "1024x768",
                "target_format": "jpg",
				"target_quality": "80",
                "source_version": "directory"
            }
		}
	},

	"unknown": {
        "__all": {
            "small": false
        }
	},
    "vector2d": {
		"__all": {
			"small": {
				"target_size": "250x250",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			},
			"preview": {
				"target_size": "1000x1000",
				"target_size_minimum": "251x251",
				"target_format": "png",
				"target_alpha": "on",
				"target_no_enlarge": "1"
			}
		}
    },
    "vector3d": {
        "__all": {
            "small": false
        }
    }
}
```

- Versionen Dokumentation: [hier](/en/sysadmin/configuration/easydb-server.yml/versions/)

# Befehle zur Administration der Docker-Container:

***Starten der Container***
```bash
/srv/easydb/run-pgsql.sh
/srv/easydb/run-elasticsearch.sh
/srv/easydb/run-eas.sh
/srv/easydb/run-server.sh
/srv/easydb/run-webfrontend.sh
/srv/easydb/run-fylr.sh
```

***Aktuell laufende Container anzeigen:***
```bash
docker ps
```

***Container stoppen:***
```bash
docker stop <containername>
```

Hier beachten Sie bitte, das der Container nach dem Stop nicht mit dem Startscript gestartet werden kann. 

Um den Container wieder mithilfe des Run-Skriptes starten zu können, muss der Container entfernt werden. Dies machen Sie bitte wie folgt:
```bash
docker rm <containername>
```

***Logs eines Containers anzeigen:***
```bash
docker logs --tail 1000 -f <containername>
```

```--tail 1000``` gibt an, das Sie die letzten 1000 Zeilen sehen möchten.

```-f``` gibt an, das Sie dem Log folgen möchten, wenn neuer Inhalt entsteht. 