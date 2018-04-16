# Extended functions {#design}

| Settings | | Explanation |
| ------ | - | -------- |
| Logo & Header |||
|| Logo | The logo can be uploaded. It is displayed in the original resolution and in the original format at the upper right. Use mouse wheel + move to adjust the logo. A path to a default image can be defined using the .ini variable `[default-pics] logo`. |
|| background color | Select background color for the logo. |
| CSS-Deteine ​​|| Create your own design for easydb. |
|Documentation|Link-Button|Activates the link button for the easydb documentation in the frontend. The button appears at the top right next to the user settings.|
||URL|If this field remains empty, the link leads to the general easydb documentation by default. You can create your own link to an individual documentation.|
|Map settings|Show [map in detail](/webfrontend/datamanagement/search/detail/detail.html)|Displays the thumbnail of a file in a map, if the file contains geocoordinates.|

When the CSS plugin (default) is loaded, input fields for modifying the loaded CSS appear here. The CSS plugin detects when the specified URLs change and provides a new CSS for the application. Also use the [CSS-Developer] tool to get more overview of the loaded SCSS files.

The easydb's CSS is created in [SCSS](http://sass-lang.com/).

### CSS files

| Settings |  Explanation |
| ------ |  -------- |
| Header | Here you can specify URLs for SCSS files that are loaded before the header SCSS of the easydb. |
| Body | Here, URLs can be specified for SCSS files that are loaded after the body SCSS of the easydb. |
| Footer | Here, URLs can be specified for SCSS files that are loaded after the footer SCSS of the easydb. |


