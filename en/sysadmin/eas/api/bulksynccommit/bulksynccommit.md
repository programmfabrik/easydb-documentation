#  EAS-API: /bulksynccommit

The `bulksynccommit` -Request can be used to match the assignment of EAS assets to the application. Because only one asset can have the committed flag within an asset tree, the asset ID list can not contain several equal or multiple assets (the uploaded asset including derived assets).

##  Example

~~~
 http://eas.example.com/eas/bulksynccommit?instance=example&final_time=1305803367&asset_ids=[23,42,17]
~~~


##  Parameter


|---|---|
|`instance`          |Name of the Instance|
|`final_time`        |New assets are ignored, Server-Timestamp can be requested with  "status-Request":../status |
|`asset_ids`         |List of the Asset-IDs|

 
