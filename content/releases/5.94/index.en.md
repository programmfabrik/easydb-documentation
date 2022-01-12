---
menu:
  main:
    name: "5.94 (January 2022)"
    identifier: "5.94"
    parent: "releases"
    weight: -594
---

> This version brings **accelerated loading time** of the application. In some tests **easydb** now loads up to **5x faster** than before. This acceleration could be achieved by massive parallelization during initial loading of required resources. 

# Version 5.94.0

*Released on 12.01.2022*

## Webfrontend

### New

- **Fullscreen**: Display of detail information is in new design and to the right of the fullscreen display.
- **Editor**: When copying, it is now possible to select whether reverse nested objects are also copied or not.

### Improved

- **Optimization** of application loading time.
- **Filtertree**: Output of duplicate labels for multiple fields has been suppressed.
- **Search**: display of hierarchical objects with long names has been improved 

### Fixed

- **Detail**: Info > Version sometimes had problems displaying more complex version hierarchies.
- **PDF printing**: It could happen that some images were not displayed in the PDF.
- **Accessibility attributes** for some inputs were corrected.

## Server

### New

- **Easdb asset server:** SVG support in `vector2d`.
- **Group Edit Mode**: Update the pool in reverse nested objects.
- **Transitions**: Email from pool contact can be used for **transition emails**.

### Improved

- **Performance** improvements for **session requests**. 
- **Performance** improvements for type `message` searches.
- Elastic mapping optimizations with many configured languages and custom data types.

### Fixed

- Fixed an **indexing issue** when importing hierarchical objects.

# Checksums

Here are the checksums of our Docker images (latest version): 

*Translated with www.DeepL.com/Translator*

