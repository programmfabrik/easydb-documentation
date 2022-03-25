---
menu:
  main:
    name: "5.97 (March 2022)"
    identifier: "5.97"
    parent: "releases"
    weight: -597
---

> This version **does not require a new index build**

> After deleting files in easydb, they are finally deleted from the storage medium of the easydb server with a time offset. This final deletion has now been improved. Deleted are all files that are deleted in easydb and thus are not linked in a current nor in a published version of an easydb object.
>
> After applying the update this improvement is disabled as default setting. It must be manually enabled by the maintenance administrator. This technical variable `server/janitor/enable_asset_cleanup` is described in easydb-5 documentation: https://docs.easydb.de/en/sysadmin/configuration/easydb-server.yml/available-variables/.
>
> In easydb frontend in main menu > administration > server status in tab "data overview" in block "files" you can find how many files will be deleted after activation and how much disk space these originals occupy.
>
> Please make sure to have created a complete and restorable BACKUP BEFORE!
>
> For customers with a maintenance contract, we create this backup and then activate the enhanced deletion.

# Version 5.97.2

*Released on 25.03.2022*

# Version 5.97.1

*Released on 21.03.2022*

## Server

### Fixed
* fixed security issue

# Version 5.97.0

*Released on 16.03.2022*

## Webfrontend

### New
* **Export/download/upload**: new rights for metadata mapping

### Improved
* **Table view**: selection for different image sizes
* **Connector**: instance name is shown next to pool name in filter
* **Accessibility**: general improvements

### Fixed
* **Detail mask splitter plugin**: fix for non-searchable fields
* **Expert search**: fix objecttype filter
* **CSV importer**: JS error fix
* **CSV importer**: show only searchable fields in mapping tab
* **Rights**: remove invalid heading
* **Export list**: update navigation when exports are removed
* **Search**: "Modified today" can be allowed independently of "Saved searches"
* **Create objects**: pool for new linked objects from metadata mapping can be selected
* **Editor**: fix error after applying template
* **Startup**: load l10n earlier to avoid missing translations

## Server

### Improved
* **Rights**: allow to revoke own rights
* **Rights**: given text parameters imply "lower" values
* **Rights**: new values for `metadata_export`, new parameter `metadata_upload`
* **CORS**: wild cards possible for allowed origins
* **asset cleanup**: finalized, but disabled by default
* **/api/v1/objecttype**: minor performance improvements

### Fixed
* **ZIP export**: no padding to avoid warnings
* **EAS**: blacklist problematic `docx` files
* **EAS**: fix internal error in office process restart
* **EAS**: fix autorotation of `heic` files

# Checksums

Here are the checksums of our Docker images (latest version): 

```ini
docker.easydb.de/pf/chrome               sha256:a1bacefda757e7d44a00bd89b30c041fffc9973b553014152ee3ef69a50e33d1
docker.easydb.de/pf/eas                  sha256:c25d07a55d0f81795b195afe4e2d7ebe21d6dbe23fc6cb41128d9d6f5ce75c5e
docker.easydb.de/pf/elasticsearch        sha256:2b1942a329ebbd104cb5427307d150f67b60ebde84918dfe5a6b03f2a0f997af
docker.easydb.de/pf/fylr                 sha256:22b0b504e4f66b6d0542efeb89bea9512c94cd479d4ef7287a398038c148084c
docker.easydb.de/pf/postgresql-11        sha256:85d4ceba8eef8c125ee4b276cb3f97bd03cb7d9e714fac3cde7b2f66199ccacd
docker.easydb.de/pf/server-base          sha256:7120d05d937d52c4614334c31871501f3edc3c677f9fe2ddb8c14f1cd9b1b500
docker.easydb.de/pf/server-base-py3      sha256:640860f211c42d6a65d7f3f57e3abdcfd52f42b116b95e925c7caa8656697394
docker.easydb.de/pf/webfrontend          sha256:e56d5be05e5ad29a91ee8d130e2d5bf0419fe566a96f5b1e01088ae702997a55
```
