# CSS-Plugin

Das CSS-Plugin hilft beim erweitern des Standard-CSS um eigene CSS-Regeln. Das easydb CSS ist in der Sprache [SCSS](http://sass-lang.com/) geschrieben.

Die Oberfläche von easydb basiert auf unserer Bibliothek [coffeescript ui](https://github.com/programmfabrik/coffeescript-ui), kurz CUI. Zusätzlich zu dem SCSS von CUI wird easydb spezifisches SCSS geladen.

Der SCSS Code ist jeweils in mehrere Dateien strukturiert um das einkoppeln an den verschiedenen Stellen zu erlauben.

|Datei|Verwendung|
|---|---|
|header.scss|Hier liegen die Variablen wie z.b. die Menü Farben. Es wird auch die [header.scss](https://github.com/programmfabrik/coffeescript-ui/blob/master/src/scss/themes/ng/header.scss) von CUI eingebunden.|
|body.scss|Hier liegt der Hauptteil des SCSS: spezifisches Layouting und Styling für die verschiedenen Bereiche der Applikation. Analog wird hier die [body.scss](https://github.com/programmfabrik/coffeescript-ui/blob/master/src/scss/themes/ng/body.scss) von CUI eingebunden.|
|footer.scss|Leer für zukünftige Zwecke bereitgehalten|

Das Plugin ist standardmäßig aktiviert und erscheint in der [Basis-Konfiguration](../base-config/base-config.html#design) in einem eigene Reiter **CSS**.

Das CSS-Plugin stellt für Benutzer mit dem System-Recht **root** eine Developer-Console bereit die die folgenden Funktionen umfasst.

## CSS-Developer-Console

![CSS-Developer-Console](cssdeveloper.png)

In der Hauptübersicht werden die Ressourcen angezeigt die geladen werden, um das SCSS zu erzeugen aus dem dann das eine CSS erzeugt wird, welches in die easydb geladen wird.

Über die Buttons **View** und **Download** können die einzelnen Ressourcen angeschaut bzw. geladen werden.

Ressourcen die mit **string://** beginnen, werden direkt aus der Basis-Konfiguration in das SCSS geschrieben. Diese Ressourcen können nicht angeschaut oder geladen werden.

Im unteren Bereich kann man im Pulldown den Lademodus des Plugins einstellen:

|Modus|Beschreibung|
|---|---|
|CSS-Plugin (dynamic)|Hier wird das CSS komplett gebaut und mit Plugins geladen. Plugins haben die Möglichkeit eigene **header**, **body** und **footer** zu definieren.|
|Remove CSS Plugin (dynamic)|In einem Cross-Server-Setup wird das CSS hier vom entfernten Server geladen. Nur verfügbar, wenn das Webfrontend auf einen anderen easydb Server zugreift.|
|Solution (static)|Für easydb-Solutions kann es ein eigenes CSS Setup geben, falls vorhanden, kann man mit dieser Einstellung dieses CSS laden (ohne Plugins).|
|Standard (static)|Das Standard-CSS der easydb wird geladen. Dabei werden weiteren keine Ressourcen geladen sondern das minimale CSS für easydb geladen.|

Mit dem Button **View CSS** kann das aktuelle erzeugte CSS im Browser angezeigt werden. Im Kommentar des CSS werden alle verwendeten Ressourcen aufgelistet. Im Falle eines Fehlers sind hier die SCSS Fehler einsehbar.

Mit dem Button **Reload CSS** kann das CSS neu erzeugt und geladen werden.

Das Pulldown oben rechts dient der Auswahl des **Themes**. Derzeit liefern wird nur ein Theme aus, weshalb das Pulldown aktuell keine Funktion hat.
