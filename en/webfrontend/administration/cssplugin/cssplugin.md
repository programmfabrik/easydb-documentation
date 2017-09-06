# CSS plugin

The CSS plugin helps to extend the standard CSS by its own CSS rules. The easydb CSS is written in [SCSS](http://sass-lang.com/).

The easydb interface is based on our library [coffeescript ui](https://github.com/programfabrik/coffeescript-ui), or CUI for short. In addition to the SCSS of CUI, easydb specific SCSS is loaded.

The SCSS code is structured in several files to allow coupling in the various locations.

| File | Use |
| - | - |
| header.scss | Here are the variables like eg. The menu colors. The [header.scss](https://github.com/programfabrik/coffeescript-ui/blob/master/src/scss/themes/ng/header.scss) is also included by CUI
| body.scss | Here is the main part of the SCSS: specific layout and styling for the different areas of the application. Similarly, the [body.scss](https://github.com/programfabrik/coffeescript-ui/blob/master/src/scss/themes/ng/body.scss) is integrated by CUI
| footer.scss | Empty for future use

The plug-in is activated by default and appears in the [Basic configuration](./base-config/base-config.md#design) tab in a separate tab **CSS**.

The CSS plugin provides users with the system right **root** with a developer console that includes the following features.

## CSS Developer Console

![CSS Developer Console](cssdeveloper.png)

In the skin overview, the resources are displayed which are loaded to create the SCSS from which the CSS is created, which is loaded into the easydb.

Using the buttons **View** and **Download**, the individual resources can be viewed or loaded.

Resources starting with **string://** are written directly from the basic configuration into the SCSS. These resources can not be viewed or loaded.

In the lower area, you can set the plug-in mode of the plug-in in the pull-down menu:

| Mode | Description |
| - | - |
| CSS-Plugin (dynamic) | This is the CSS completely built and loaded with plugins. Plugins have the possibility to define their own **header**, **body**, and **footer**
| Remove CSS Plugin (dynamic) | In a cross-server setup, the CSS is loaded here from the remote server. Only available when the Web front end accesses another easydb server
| Solution (static) | For easydb-Solutions there may be a custom CSS setup, if available, you can load this CSS with this setting (without plugins)
| Default (static) | The default CSS of easydb is loaded. No more resources are loaded, but the minimal CSS is loaded for easydb

With the button **View CSS** the current generated CSS can be displayed in the browser. The CSS comment lists all the resources used. In the event of a fault, the SCSS errors can be seen here.

With the button **Reload CSS** the CSS can be created and loaded again.

The pulldown in the top right is used to select the **Themes**. At the moment, only one theme is provided, which is why the pulldown currently has no function.