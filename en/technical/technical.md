# easydb Technical Overview

**easydb** is a full featured data and digital asset management system build on top of the Open Source Technologies:

* [Linux](http://www.linux.org)
* [Apache](http://www.apache.org/)
* [PostgreSQL](http://www.postgresql.org/)
* [Elasticsearch](https://www.elastic.co/)

The system **easydb** consists of three major parts

* the **easydb asset server** (EAS)
* the **easydb server**
* the ***easydb webfrontend***

## Overview

All services are connected using HTTP(S) and can be installed on different servers. The EAS data store can be local, SAS or NAS. EAS stores file as actual files, all metadata is store in an RDBMS (Postgresql), the Elasticsearch index is used only for searches and thus a copy of the SQL-data.

easydb is packaged as a [Docker](https://www.docker.com/) image and runs on many Linux distributions.

Elasticsearch can be installed on multiple machines for best performance result.

## Docker integration
This is covered in [System Administration: Docker integration](../sysadmin/sysadmin.html#docker-integration).

## Plugins

**easydb server** and **easydb webfrontend** has full plugin support. Plugins for the server are written in Python and for the Webfrontend in Javascript (or any other browser language). Many features of the **easydb server** can be intercepted, such as object get & store or search.

## easydb asset server (EAS)

**EAS** is a distributable storage system with a simple programming HTTP-API with JSON output. It does not have a graphical frontend. **EAS** stores all file formats and is able to produce derived versions for many of them.

### The EAS as the central management system for files (assets) supports:

* Storing files
* Generating thumbnail & previews
* Extensive page support (e.g. a *pdf* with 100 pages has previews and zoomsupport for each page!)
* Manipulating images (crop, mirror, etc.)
* Watermarking of files
* Real-time jpeg zooming with seamless tiles
* Converting office formats (e.g. docx to pdf, html to pdf)
* Transcoding video and audio (e.g. avi to flv)
* Managing embedded file metadata
* Files can be searched by metadata
* Programmers can store additional custom information for each files
* Video streaming

### The technical features of the EAS

* It is mostly written in Python.
* **EAS** features a database based job queue.
* **EAS** workers (programs that do conversion jobs) can be distributed across machines
* Partitioning support: Files can be stored on different file systems, locally and on the network.
* **EAS** reads and writes metadata (IPTC, XMP, EXIF, etc.) information for a plenty of file formats.
* **EAS** supports many file formats like JPEG, TIFF, PNG, PDF, PDFA, AVI, MOV, MP3, MP4, WAV, DOC[X], PPT[X], XLS[X], etc.
* **EAS** manages "OpenOffice":http://www.openoffice.org processes to support all the office file formats).
* **EAS** works with millions of files and concurrent users.
* Every file gets a unique ID under which it can be referred to when talking to the **EAS**.
* **EAS** can be given conversion jobs, jobs can be queried for their current status.
* **EAS** stores its meta-information in an SQL database (PostgreSQL), and its files on the filesystem.
* Files can be derivates from other files (tree support), that way you can crop and image, have thumbnails for the cropped image and can still keep the referenced original.


## easydb server

**easydb server** is C++-Server with Python-Plugin-Extensions with the following features:

### Features

The main features of **easydb server** are:

* hierarchical objecttype modelling: an objecttype may be stored in many relational tables
* objects can be hierarchical (tree), organized in pools, have tags attached, have access control lists
* objects and all data is copied on write, so we have full history and rollback support
* rightsmanagement based on pools, tags, and on the object level
* authentication / authorization
* datamodelling
* search & suggest
* facetting
* object store & retrieval
* object bulk updates
* right smanagement
* pool management
* tag management
* collection managements
* base configuration
* user / group / role management
* image rotation
* full export suite
* multi-language support for data storage

### HTTP-Restful-API

The API support all features of the server and is the only way to interact with the server.

### Backend

**easydb server** stores it's data in the following backend systems:

* Postgresql as main metadata store
* *easydb asset server* as asset store and retrieval
* Elasticsearch index for search


## easydb webfrontend

**easydb webfrontend** is a HTML5/Javascript Application written in Coffeescript/Javascript to utilize all features of the easydb server.

Browsers supported:

* Chrome (latest)
* Firefox (latest)
* Internet Explorer 11 & Edge

The webfrontend supports all features of the **easydb server**.

The frontend has some special features:

* image zoom viewer
* audio & video playback
* pdf / office document preview
* image rotation & cropping
