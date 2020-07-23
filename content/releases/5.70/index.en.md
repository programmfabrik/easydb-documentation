---
menu:
  main:
    name: "5.70 (July 2020)"
    identifier: "5.70"
    parent: "releases"
    weight: -570
---

> This release brings extensive **changes in the design** of the **search, detail and editor**. If you are using your **own CSS**, we recommend a test installation and the corresponding adaptation in advance.
>
> This release **does not** require a re-index.

# Version 5.70.2

*Published on 23.07.2020*

## Web frontend

*Fixed*

- Detail view failed to open when standard was not set.

# Version 5.70.1

*Published on 20.07.2020*

## Web frontend

*Fixed*

- Display of the **Object ID** in the **group editor** was superfluous, since it cannot be rewritten.
- **Typo3**: If no Typo3 mapping was stored in the base configuration, an error occurred during data transfer.

# Version 5.70.0

*Released on 15.07.2020*

## Web frontend

*New*

- **Display** of all **reverse linked** objects from the detail in the search via a menu item.

*Improved*

- Support for **Chromium** based browsers.
- New design for Finder. The Finder access has been split into the sections Folders and Searches for a better overview.
- **Accelerated display** of Finder for many shared folders.
- Improved **split mode** to display a folder and search simultaneously.
- General display of standard information (object type, pool, system object ID, standard info, tags) in **detail, editor and text view**.
- Accelerated loading of the frontend for returning users.
- Display of a **generic footer** in detail and editor with system information.

*Fixed*

- **Expert search**: Fixed the search for ranges of currency numbers with decimal places.
- Fixed display of multilingual fields for some cases.
- Fixed loading preferences for new anonymous users in some cases.
- Fixed input of data model checks for ranges of numbers.

## Server

*New*

- **/api/user**: `include_password` is a new URL parameter for outputting stored passwords.
- Support of object **updates via hotfolder**, using settings in the collection.

*Improved*

- **Improved performance** in the group editor when changing the pool.

*Fixed*

- Reindexing of bidirectional links improved.
- When deleting objects in folders, unique constraint errors could occur that prevented deletion.

# Checksums

Here are the checksums of our docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:62ac9147529a03491b3edc35898b076fad86be181c96be9b2b701962688623f5
docker.easydb.de/pf/eas                  sha256:ba2f1a42f281934a56f88cb8790f4d40e0787a2a5856ad9d495e6aad7fa46af6
docker.easydb.de/pf/elasticsearch        sha256:d6737a517f2cbc2c4441eb37173901ded1042250b17eef426e5758c709bf307f
docker.easydb.de/pf/fylr                 sha256:714c66d7570a96a015dce120ad1de4769dc4f8eb7bc74dbb9f41a6b55f2fb5c7
docker.easydb.de/pf/postgresql-11        sha256:a491f8fbb5e1df8e1acd804455a6cf3c459afdd2b63aad47595945ec2c55fe81
docker.easydb.de/pf/postgresql           sha256:6a3453a8b7066ded00a8255a4ab02b587b7a534c9effcbab8ee4d721533d8eae
docker.easydb.de/pf/server-base          sha256:2b2ae03b4e4c29417d1d672a1f4000a73c153bd0a372840eda79cda662df722b
docker.easydb.de/pf/webfrontend          sha256:2e6aab97a873c8e8f65b9452c210d5c32f63e3c27f09f4fe41048cae09008be4
```

*Translated with www.DeepL.com/Translator*
