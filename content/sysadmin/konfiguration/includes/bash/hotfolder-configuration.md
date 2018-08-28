```yaml
easydb-server:
  hotfolder:
    enabled: true
    urls:
      - type: windows_webdav
        url: \\easydb.example.com@SSL\upload\collection
        separator: \
      - type: webdav_http
        urls: https://easydb.example.com/upload/collection
        separator: /
	
	plugins:
    enabled+:
      - base.hotfolder
```