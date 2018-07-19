---
title: "24 - /search"
menu:
  main:
    name: "/search"
    identifier: "sysadmin/eas/api/search"
    parent: "sysadmin/eas/api"
---
#  EAS-API: /search

##  Example

~~~
 http://eas.example.com/eas/search/keyword?instance=example&type.extension=jpg
http://eas.example.com/eas/search/keyword/ids?instance=example&type.width=RANGE(100,1000)
~~~


##  Parameter


|key|value|
|---|---|
|`instance`          |Name der Zielinstanz|
|`parent_id`         |Suche nach Kindern des mit dieser ID angegeben Assets|
|`*.*`               |Suchfeld und -wert für die Suche|

##  Advanced search functions

The search value supports various functions that influence the search. Only one function can be used per search value.

For efficiency reasons, the EAS sets the values for all keywords in three different tables to get a result often has to be searched in the correct table. Without a search function, equivalence is searched for in text fields.

|key|type|value|
|---|---|---|
| ` Int ` | Integers | all integer values |
| ` Text ` | Text | short strings that do not contain spaces |
| ` Text_full ` | fulltext | all remaining strings |

The following functions are available:

|key|value|
|---|---|
|`RANGE([<start>],[<end>])`|Range search on integer fields. This function must also be used before *(version) EAS 4.2.30* also for equivalence search on number fields. Examples:|
|type.colordepth=RANGE&#40;8,8)     |       # Color depth exactly 8 bits|
|type.height=RANGE&#40;,1000)       |       # Height up to 1000|
|type.width=RANGE&#40;200,)         |       # Width from 200|
|type.pages=RANGE&#40;4,8)          |       # Between 4 and 8 Sides|
|`INT(<value>)`|Equivalence search on number fields *(version)EAS 4.2.30*. Example:|
|type.height=INT&#40;1080)             |        # Height exactly 1080|
|`REGEXP(<regexp>)`|Search with regular expression in text fields. Example:|
|type.fileclass=REGEXP&#40;^&#40;audi&#124;vide)o$)| # Fileclass "audio" oder "video"|
|`INLIST(<item1>[;<item2> ...])`|Equivalence search in text fields according to different search terms. At least one term must be found (OR connection). Example:|
|type.extension=INLIST&#40;ppt;pptx;doc;docx) | # File one from the list|
|Note: the semicolon is a reserved character within the HTTP query string; It must be URL encoded (%3b).||
|`FULLTEXT(<word>)`|Search in fulltext field (momentan `LIKE '%<word>%'`). Example:|
|metadata.IPTC::ApplicationRecord.IPTC:Caption-Abstract=FULLTEXT&#40;Ente)|                                      # Search in the image description for Ente|
|`FULLTEXTEXT(<word>)`|Wie `FULLTEXT()`, But it is also searched in text fields|


 

