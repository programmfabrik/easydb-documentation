# Changelog Entry

An entry in the changelog of an object represents a certain action that was undertaken on it.

Every attribute is readable-only.

## Attributes

| Name                        | Description                                                                                               | Search        |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|---------------|
| `batch_id`                  | ID of the batch operation in which this object was changed (integer, unique)                              | Number        |
| `operation`                 | Name of the operation (string): **INSERT**, **UPDATE** or **DELETE**                                      | NotAnalyzed   |
| `schema_version`            | Schema version that was active when the change took place (integer)                                       | Number        |
| `time`                      | Timestamp of the change ([Timestamp](/technical/types/timestamp/timestamp.md))                                              | Timestamp     |
| `version`                   | Version of the object (integer): the `_version` attribute of the object                                   | Number        |
| `current_version`           | Whether this is the current version of the object (boolean)                                               | Boolean       |
| `user`                      | User that performed the operation ([user (short)](/technical/types/user/user.md#short))                                | Number(\*)    |
| `groups`                    | Groups the `user` belonged to at the time of the operation (array of integers): ref [group](/technical/types/group/group.md).\_id) | Number |
| `comment`                   | Comment (string, optional)                                                                                | Text          |

(\*) `user.user._id` is searchable as Number

## Searching objects using the changelog

The changelog is searchable both using direct queries and nested queries. Normally, you would want to use a nested query. Here's why:

Mr. White is looking for an object. He knows it is a "picture" and he changed it today (April 17). He therefore uses a query with the conditions:

(1) objecttype is "picture"
(2) changelog user is Mr. White
(3) changelog operation is UPDATE
(4) changelog time is April 17

Now, there are two pictures:

**Picture 1**

~~~~json
@@include:object1.json@@
~~~~

**Picture 2**

~~~~json
@@include:object2.json@@
~~~~

**Normal query**

If Mr. White uses a normal query like this...

~~~~json
@@include:normal_query.json@@
~~~~

... the result will be pictures 1 AND 2. The problem is that the query matches all conditions **across
all** changelog entries. In order to specify that all conditions should be matched in one particular entry,
Mr. White should use a nested query:

**Nested query**

~~~~json
@@include:nested_query.json@@
~~~~

This query returns only picture 1 because it has a changelog entry (the last one) that matches all conditions.

Usually you want to use a nested query for changelog entries, but sometimes a normal query works,
and it is faster. For example, if you need to search for objects that were changed today, or objects that have Mr. White
as last editor, you can use a normal query.

