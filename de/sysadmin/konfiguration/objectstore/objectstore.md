# Datenmodell-Server

Der Datenmodell-Server kann verwendet werden, um für diesselbe easydb mit mehreren Servern (Test, Staging, Production),
das Datenmodell (Schema, Masken, Lokalisierung), zentral zu verwalten.

## Konfiguration in der easydb

Die Installation in easydb erfolgt in der server.yml.

	default_client:
		datamodel:
			uid: 6b6640c4-771a-4a66-9308-dbc372b0bcdf
			server: http://10.150.0.2:3000

Die *uid* muss auf allen easydb diesselbe sein, ebenso der angegebene Server.

# Installation

Die Installation des Datenmodell-Server erfolgt aus einem GIT-Checkout von [easydb-objectstore](https://github.com/programmfabrik/easydb-objectstore).
