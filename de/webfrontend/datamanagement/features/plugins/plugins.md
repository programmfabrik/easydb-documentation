# Plugins

## <a name="wordpress"></a>Wordpress

Datensätze können von easydb nach Wordpress exportiert werden. In Wordpress erscheinen sie in der Mediengalerie und können von dort wie gewohnt verwendet werden. Eine Anleitung zur Installation und Verwendung des Wordpress-Plugins ist auf [GitHub](https://github.com/programmfabrik/easydb-wordpress-plugin) zu finden.

Nach der Installation kann über den [Exporter](../../features/export/export.md) ein [Wordpress-Transport](../../features/export/export.md#transport) angelegt werden. Gesendet werden nur Bilddateien. Für Änderungen am Datensatz in easydb gilt folglich für Wordpress:

|Änderung in easydb|Beispiel|Veränderung in Wordpress|
|--|--|--|
|Löschen eines Datensatzes||Bilddatei bleibt in Wordpress erhalten.|
|Datei verändern|durch Zuschneiden|Bilddatei wird beim Transport in Wordpress neu angelegt. |
|Metadaten am Datensatz ändern| Titel ändern und durch Ersetzung als neuen Dateinamen für Export verwenden. | Beim Transport bleibt die existierende Datei in Wordpress erhalten. Der Name der Datei wird aktualisiert.|
|Änderung am Benutzer|durch Änderung des Namen|Bilddatei bleibt in Wordpress davon unberührt.|


## <a name="TYPO3"></a>TYPO3

Über ein easydb-Plugin für TYPO3 können Datensätze aus easydb zu TYPO3 gesendet werden. Sie erscheinen dort in der Filelist und können dann wie gewohnt verwendet werden.

Das Plugin ist zweiteilig und wird in easydb und in TYPO3 installiert. Das ausgelieferte Plugin für easydb muss von einem Systemadministrator in einer [YAML-Datei](../../../../sysadmin/konfiguration/yaml/yaml.md) installiert und aktiviert werden. Einstellungen zur Verwendung in der Benutzeroberfläche können anschließend in der [Basis-Konfiguration](../../../administration/base-config/base-config.md) vorgenommen werden.

Das Plugin für die Einrichtung in TYPO3 steht mit einer Installationsanleitung über [GitHub](https://github.com/programmfabrik/typo3-easydb-plugin) bereit.

![TYPO3 Plugin für easydb](typo3_easydb_plugin.png)

Nach der Installation erscheint oberhalb der Filelist ein Button, mit dem easydb in einem neuen Fenster öffnet. Hier werden die Datensätze gewählt, die zu TYPO3 gesendet werden sollen. Über die Toolbar und das Kontextmenü steht die Option "Übernehmen nach TYPO3" zur Verfügung.

Geänderte oder gelöschte Datensätze in easydb werden nicht mit TYPO3 synchronisiert. Änderungen am Datensatz müssen in TYPO3 manuell überführt werden.

## <a name="falconio"></a>Falcon.io

Datensätze können von easydb nach Falcon.io exportiert werden. In Falcon.io erscheinen sie im Content Pool und können von dort wie gewohnt verwendet werden. Eine Anleitung zur Installation und Verwendung des Falcon.io-Plugins ist auf [GitHub](https://github.com/programmfabrik/easydb-wordpress-plugin) zu finden.

Nach der Installation kann über den [Exporter](../../features/export/export.md) ein [Falcon.io-Transport](../../features/export/export.md#transport) angelegt werden. Gesendet werden nur Bilddateien. Änderungen am Datensatz in easydb gelten folglich auch für Falcon.io.
