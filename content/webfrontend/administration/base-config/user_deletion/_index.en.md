---
title: "Deleting & Pseudonymization"
menu:
  main:
    name: "Deleting & Pseudonymization"
    identifier: "webfrontend/administration/base-config/user_deletion"
    parent: "webfrontend/administration/base-config"
---
# Deletion & Pseudonymization

easydb supports archiving and final deletion of users, as well as pseudonymization of archived users.



## Method for deleting users

Select the deletion method to be applied when a user is deleted in the user administration via the minus.

| Option  | Comment                                                      |
| ------- | ------------------------------------------------------------ |
| Ask     | If an administrator clicks on the minus to delete a user from the system, this option asks whether the user should be archived or permanently deleted. |
| Archive | If an administrator clicks on the minus sign to delete a user from the system, this user is only archived with this option. However, the user can no longer be found in the user administration and can no longer log in. If a [pseudonymization](../../../rightsmanagement/groups/) is configured on a group of the user, it will be performed during archiving. |
| Delete  | If an administrator clicks on the minus sign to delete a user from the system, this user will be permanently deleted if this option is selected. The folders that this user has created will also be permanently deleted. Data records in which he is stored as "responsible" are attributed to the system user "deleted_user". The same applies to the events of the deleted user. |



## Automatic deleting & archiving of users

easydb supports automatic archiving of inactive users and automatic deletion of archived or anonymous users. By default, users are neither automatically archived nor deleted.

| Option                              | Comment                                                      |
| ----------------------------------- | ------------------------------------------------------------ |
| Archive after n days of inactivity  | Users who have not logged into easydb after n days will be archived and will not be able to log into the system afterwards. |
| Delete archived users after n days  | Archived users will be permanently deleted after n days.     |
| Delete anonymous users after n days | Anonymous users (i.e. users accessing easydb without login) are permanently deleted after n days. |

