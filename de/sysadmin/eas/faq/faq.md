#  Problemlösungen

##  Fehler beim EAS-Start beheben

Im Ausnahmefall kommt es dazu, dass der EAS nicht korrekt startet. Versuchen Sie zuerst, den EAS über das Init-Skript neu zu starten:

~~~
# /etc/init.d/easydb-asset-server restart
~~~


Kommt es dabei zu einem Fehler, konsultieren Sie bitte zuerst die Log-Dateien des EAS. Eventuelle Fehler finden sich in `eas-worker.log` (in wenigen Fällen auch in `eas-exception.log`) im EAS-Log-Verzeichnis (normalerweise `/var/opt/easydb/log/eas`, kann aber mit "EAS_LOG_DIR":../conf/#EAS_LOG_DIR geändert werden).

h3. belegte OpenOffice-Ports (ab EAS 4.2.38)

Ab Version 4.2.38 überprüft der EAS beim Start, ob alle Netzwerkports verfügbar sind, die für die Benutzung von OpenOffice vorgesehen sind (siehe auch "EAS_SOFFICE_BASEPORT":../conf/#EAS_SOFFICE_BASEPORT). Unter gewissen Umständen kann es passieren, dass beim Beenden des EAS Teile von OpenOffice weiterlaufen und die Ports blockieren. Dieser Umstand wird nun beim Start des EAS erkannt und ist im Log durch eine Fehlermeldung folgender Art zu erkennen:

~~~
eas_general(32598):2013-11-18 11:12:45,777:ERROR: designated port already in use:
TCPv4        127.0.0.1:2002  -         0.0.0.0:0      (LISTEN)

Vor Version 4.2.38 wurde dieser Fehler nicht automatisch erkannt und führte zu schleichenden Problemen, z.B. OpenOffice-Prozessen, die dauerhaft unter Volllast liefen.

Zum Beheben des Problem beenden Sie bitte zuerst den noch laufenden OpenOffice-Prozess. Sie können diesen Prozess z.B. mit folgendem Aufruf von `ps` finden:

~~~
# ps -edalf
|---|---|
| grep 'soffice.bin.*port=2002'

Nachdem der Prozess beendet ist, sollte der EAS wieder starten.

##  Neue Farbprofile hinzufügen

Farbprofile werden in `/opt/easydb/eas/eas/data/profiles` nach Farbraum getrennt in den Verzeichnissen `rgb` und `cmyk`. Neue Farbprofile können in die Verzeichnisse kopiert werden, sie stehen dann zur Verfügung.

##  Alle fehlgeschlagenen Jobs neu starten

Auf der PostgreSQL-Datenbank des EAS kann dazu folgendes ausgeführt werden:

~~~
. BEGIN;

UPDATE eas.job SET job_status = 'pending' WHERE job_id IN (
SELECT DISTINCT ON(derived_asset_id) job_id
FROM eas.job
JOIN eas.derived_asset USING(derived_asset_id)
WHERE derived_asset.derived_asset_status = 'failed'
ORDER BY derived_asset_id, job_time_created DESC
);

UPDATE eas.derived_asset
SET derived_asset_status = 'pending'
WHERE derived_asset_status = 'failed'
AND derived_asset_id IN (
SELECT derived_asset_id
FROM eas.job
WHERE job_status IN ('failed', 'pending')
);

COMMIT;

