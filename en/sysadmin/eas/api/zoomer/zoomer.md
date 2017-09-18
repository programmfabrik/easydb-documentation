#  EAS-API: /zoomer

Returns a tile or thumbnail for the zoomer

##  Example

~~~
 http://eas.example.com/eas/zoomer/123/d8e8fca2dc0f896fd7cb4cb0031ba249/zoom1920/part2x1.jpg?instance=example
http://eas.example.com/eas/zoomer/123/d8e8fca2dc0f896fd7cb4cb0031ba249/thumbnail.jpg?instance=example
~~~


From *(version) version 4.2.37*, the EAS for `/zoomer` also supports the following syntax:

~~~
 http://eas.example.com/eas/zoomer/123/d8e8fca2dc0f896fd7cb4cb0031ba249/zoom1920[/size256][/avoid_interpolation]/part2x1.jpg?instance=example
~~~

##  Structure

The path parts to `zoomer` are structured as follows:

* Asset ID
* Asset version (MD5)
* `zoom <destdim>` where `destdim` is the target dimension (pixels, see below)
* `size <size>`, where size is the tile size (pixels) (from *(version) 4.2.37*)
* `Avoid_interpolation`: Do not use interpolation if the zoom factor is a natural number (ab *(version) 4.2.37*)
* `part <tile_x> x <tile_y> .jpg`, where `(tile_x, tile_y)` are the tile coordinates. `(0,0)` is top left

The zoom factor is specified by the target dimension. That is, the image is zoomed so that the width of the resulting image is as large as this parameter.
The zoom factor is: destdim/image_width

In the example, if the original image is (3840x1200), the zoom factor is 1920/3840 = 0.5. The zoomed image is (1920x600).

If `avoid_interpolation` is set, the zoom factor must be less than 1 or a natural number. This means: 0.5 is allowed, but 1.5 is not allowed.

##  Parameter


|key|value|
|---|---|
|`Instance`| Name of the target entity|

 

