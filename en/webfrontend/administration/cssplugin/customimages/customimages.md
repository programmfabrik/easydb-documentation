# Include your own pictures or other media
To include your own media, these must be relative to the SCSS file URL specified in the basic configuration (see [Quick Start](../quickstart/quickstart.md)).
Using the EasyDB's own SCSS variable $urlBase, you can create a link to your own media file.

Example:
```
background-image: url($__urlBase+"/custom_image.png")
```  


