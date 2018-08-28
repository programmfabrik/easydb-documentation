| Config                                        | Format | Description                                                  |
| --------------------------------------------- | ------ | ------------------------------------------------------------ |
| `server.addr`                                 | String | Address of the server.                                       |
| `server.accounts`                             | Map    | Key-Value map of **login** and **password** for access of the admin pages on Fylr. |
| `objectstore.dir`                             | String | Top-Level-Directory where Fylr stores its data.              |
| `objectstore.uids[].uid`                      | String | UID of the storage, this is a unique id for each storage group. |
| `objectstore.uids[].allowed_instances[].id`   | String | Identifier of one of the clients for the storage.            |
| `objectstore.uids[].allowed_instances[].name` | String | Optional name for the client, as shown in the overview page on Fylr. |
| `zip.allowed_urls[]`                          | String | If set, the *Zip*  service is enabled and allows Zipfiles to be created with files originating the given URLs. Each entry is endpoint |