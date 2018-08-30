```yaml
eas:
  rights_management:
    image:
      versions:
        - version: small
          size_print: 250px jpg
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px jpg
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: preview_watermark
          size_print: 1000px jpg (watermark)
          size_limit: 1000
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: huge
          size_print: 2000px jpg
          size_limit: 2000
          export: true
          rightsmanagement: true
          group: huge
          zoomable: true
        - version: full
          size_print: Original jpg
          export: true
          rightsmanagement: true
          group: huge
          zoomable: true
    video:
      versions:
        - version: small
          size_print: 250px jpg
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 720px jpg
          size_limit: 720
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: preview_watermark
          size_print: 720px jpg (watermark)
          size_limit: 720
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: huge
          size_print: 1920px jpg
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
          size_print: 250px png
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px png
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
    vector3d:
      versions: []
```