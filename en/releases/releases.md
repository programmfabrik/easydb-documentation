# Releases

Regularly easydb is updated with new functions, error solutions, and overall improvements

* A new version is prepared every 2 weeks and - if appropriate for customers - published and is then ready to be updated.
* Bug fixes can create additional versions (also called "patch").

### To update

Updating is the first step of the [install](/docs/sysadmin/installation). Unless otherwise agreed, this task is the customer's responsibility.

easydb instances on our own servers, including tests and presentations, are updated by us.

&Nbsp;

# Versions

## Version 5.13

*Published on 28.06.2017*

Changes to the search index require a re-indexing. Depending on the database size, this can result in a limitation of usability lasting several hours.

#### server

* Search index takes fulltext setting to nested tables
* Fix for download transport without packer
* Expand the information about download transport files in the export API
* Correction of the EAS links in the export
* Preparation for hotfolder import into linked tables
* Search corrected with accents
* Enhancement to `exclude_fields` in the search API
* Optimization when generating `ALL_FIELDS` links

### Webfrontend

* Download and export of remotely linked files, which are displayed in the detail viewer
* A robots.txt ensures that search engines do not index
* Expert search: Improved tokenizer for autocompletion in text fields
* CSVImporter: Bugfixes when importing linked objects
* Other minor bug fixes

## Version 5.12
 
*Published on 14.06.2017*

### Webfrontend

* Support for single-field legal management
* Support for serial images, versions(RAW, Jpeg) and remote objects during upload
* Improved drag & drop in folders
* Date selection possible without time
* CSVImporter: Support for multilingual link fields in search and creation
* Troubleshoot grouping in the filter tree
* Bug fixes and performance improvements

#### server

* All-Fields-Mask also links the mask with all fields for links
* Field filter I/O
* Update date for user changes
* Hotfolder extensions
* `OBJECT_DELETE` event for archived users
* Wildcard search corrected, case no matter now
* LDAP and SSO users now get workbooks. In order to benefit from this, the user "ldap" or "sso" stored in the easydb has to be deleted. This will be created again on the next login.
* Selection of the field to be exported for the CSV export corrected

## Version 5.11

*Published on 31.05.2017*

#### server

* Restrict fields after mask settings(full text search) for phrases search
* New API request `settings`
* Filter for `/api/user`
* `OBJECT_INDEX` events are always generated for assets, even at low priority
* Bug fixes

## Version 5.10

*Published on 17.05.2017*

#### Webfrontend

* Hierarchy browser in detail(for hierarchical object types).
* In table view, the column widths can be adjusted manually.
* Hierarchy checkbox is removed from the object type/pool selector.
* Hierarchy checkboxes in each view as option.
* Improved marking of required fields, especially in the group and new editor.
* CSV Importer: Support for decimal fields, import of MS Access data(YYYMMDD format).
* Bug fixes and performance improvements.

#### server

* Download of large files corrected.
* Caching policy is left to the plugins.
* Custom settings in schema/masks for more field types.
* Missing foreign key in the data model.
* Links corrected in XML export.
* Import of bidirectional data corrected with the group editor.
* Failed to create indexes with long names fixed.

## Version 5.9

*Published on 03.05.2017*

#### Webfrontend

* Schedule with presets for emails and export transport
* Support for optional separators in field identifiers.
* Printing now works in Internet Explorer.
* Mark all hits in the secondary search.
* CSVImporter: improvements and fixes.
* Plugin: Wordpress CMS Transport(Beta).
* Plugin: export transport FTP is now a plugin.
* Troubleshooting and speed optimization

#### server

* Login names and e-mail addresses must now be unique regardless of the case.
* Group assignment for LDAP and SSO authentication has only validity for the session and is no longer persistent.
* Index error during import with mask "\ _all \ _fields" fixed.
* Parallelism removed during export to increase reliability.
* Added minutes accuracy for scheduler.


## Version 5.8

*Published on 19/04/2017*

#### Webfrontend

* CSVImporter: Support for multilingual fields(hierarchy + updates)
* New system privileges to hide group and user managers, but still allow access via the API
* Improved self-registration dialog
* File download of linked objects containing the files displayed in the standard(single download only)
* "Discard Changes?" Dialog in Profile & Tag Manager
* Graphical improvements
* Troubleshooting: Language selection at restart was always "en-GB".
* Other bug fixes

#### server

* More fields in XML export
* New parameter "hide_frontend_app" for system rights "system.user" & "system.group"
* Search & Suggest in more fields
* Fixed issue collection issues
* Fixed bug when evaluating plugin configuration
* Fixed DB error in export scheduler

## Version 5.7

*Published on 05.04.2017*

#### Webfrontend

* Display of linked objects from the detail in the search.
* CSV Exporter for users
* Supports multilingualism, date and ID columns in the CSV importer
* Single-Sign-On supports authentication in a separate browser window.
* Bug fixes

#### server

* User-blocking in case of multiple attempts at client blocking
* Support for custom types in the search
* Max. Length for ngram search is increased from 30 to 50
* Suggestion for file properties corrected
* Archived users are not output via the API
* XML namespace corrected in export metadata mapping
* No persistent DB connection in the Janitor more
* Thread leak in the Exporter fixed
* Fixed errors when saving e-mail addresses

## Version 5.6

*Published on 20.03.2017*

#### Webfrontend

* Connection of [cloudsight.com](http://cloudsight.com).
* Improved language selection at the first start of easydb.
* Bug fixes & performance enhancements

#### server

* Output of old record versions accelerated
* Object URLs in XML export
* Indexing of bidirectional links improved
* Handling of tags in the group editor corrected without other changes
* Output of standard EAS block unified for records without assets

## Version 5.5

*Published on 08.03.2017*

#### Webfrontend

* CSV importer for users and lists
* Performance improvements & bug fixes
* Support for custom colors in basic configuration.
* A Markdown link opens in a separate browser window.
* Fix for keeping the visible order when reordering in collections.

#### server

* New event `USER_CREATED`
* LDAP support
* Additional columns for bidirectional links are copied
* Removes tag filters from object types
* Fixed bug in collections operations
* Fixed metadata with NULL bytes
* Improved speed for collection requests

## Version 5.4

*Published on 22.02.2017*

#### Webfrontend

* Change to new design
* Performance improvements & bug fixes

#### server

New:

* ZIP64 support for exports.
* Timeout of users(for example, if there are too many attempts to log on when logging in).
* System name visible without login.
* Root right no longer visible to non-root users.
* Event for base config update.
* UNIQUE Contraints for date ranges.
* Plugins can create their own events.

Added:

* Deeplink extensions.
* "AOContentDescription" for export profile.
* Better error messages and translations("L10N").

Repaired:

* Export the complete search.
* Remove all ACLs.
* The password-forgotten link.
* Setting "inactive" to ACLs.
* More details and little things. For more information please ask specific questions at support@programmfabrik.de.
* Speed ​​of ACL treatment improved.


## Version 5.3

*Published on 31.01.2017*

#### server

* Custom Datatypes: more comprehensive support for search and aggregations. Caution: this change requires an adjustment of the configuration of the Custom Datatype plug-ins.
* Search:/api/search works only with "aggregations", "facets" are no longer supported.

## Version 5.2

*Published on 02.12.2016*

#### Webfrontend

* Conversion of folders, search and finder.
* Redefined selection paradigms.
* Directly accessible flyout buttons as addition to the Context menu.

#### server

* OAI/PMH interface.
* Deep link interface.
* Extension for Custom Data Types.

## Version 5.1.1

*Published on 10.11.2016*

Bugfix # 39365: - dbapi_import: fix UPDATE: insert dirty job for deleted reverse nested objects

## Version 5.1

*Published on 06.11.2016*


### Support

We will remedy faults in the following timeframe depending on the fault class (if booked by the customer and not otherwise agreed):

Deficiency class        Reaction time       Recovery time
----------------        -------------       -------------
Preventive shortage     2 hours             24 hours = 3 working days
Operational obstruction 2 hours             40 hours = 5 working days = 1 week
Light shortage          2 hours             80 hours = 10 working days = 2 weeks

For this listing only hours are within our service times: from 9 am to 5 pm on weekdays.

Depending on the situation, deficiencies can also be solved in a local workaround instead of in a new version or up to a new version.