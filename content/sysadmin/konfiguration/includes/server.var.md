### server
| Variable                                           | Typ           | Pflicht | Erklärung | Default-Wert |
|----------------------------------------------------|---------------|---------|-----------|--------------|
| `external_url`                             | String         | No       | URL for the Server connection from outside of Easydb | |
| `directory.imexporter`                       | Catalogue      | Yes      | Imexporter Directory | |
| `directory.pflib`                            | Catalogue      | Yes      | Directory where the pflib is located | |
| `directory.output`                           | Catalogue      | Yes      | output directory | |
| `directory.logfile`                          | File           | Yes      | Log-File | `/tmp/easydb-server.log` |
| `directory.umask`                            | Integer        | Yes      | umask | `022` |
| `directory.server_errors`                    | Catalogue      | No       | Catalog for Server Error Information | `<directory/logfile>.errors` |
| `directory.l10n_dir`                         | Catalogue      | Yes      | Catalogues for the L10n configuration | |
| `directory.tmp`                              | Catalogue      | Yes      | Catalogue for temporary files | |
| `exporter.num_workers`                      | Integer        | Yes      | Number of Workers | `0` |
| `exporter.batch_size`                       | Integer        | Yes      | Batch Size | `100` |
| `exporter.max_xml_size_for_xslt`            | Integer        | Yes      | Max. size for XML Files to allow XSLT post processing (in MB) | `10` |
| `janitor.eas_sync_commit`                  | Boolean        | No       | Enable asset status sync to EAS. Assets not linked in easydb are removed by EAS janitor | `true` |
| `janitor.enabled`                          | Boolean        | Yes      | Whether the janitor is running | `true` |
| `janitor.interval`                         | Integer        | Yes      | How often the Janitor runs (every X seconds) | `600` (10 minutes) |
| `janitor.max_age`                          | Integer        | Yes      | When a file expires (after X seconds) | `259200` (3 days) |
| `imexporter.socket`                           | File           | Yes      | Socket | `/tmp/easydb-server-imexporter.sock` |
| `imexporter.num_services`                     | Integer        | Yes      | Number of services | `2` |
| `frontend.socket`                           | File           | Yes      | Socket | `/tmp/easydb-server-frontend.sock` |
| `frontend.num_services`                     | Integer        | Yes      | Number of services | `0` |
| `upload-server.socket`                           | File           | Yes      | Socket | `/tmp/easydb-server-upload.sock` |
| `upload-server.num_services`                     | Integer        | Yes      | Number of services | `2` |
| `indexer.enabled`                          | Boolean        | Yes      | Whether the indexer is running | `true` |
| `indexer.num_processes`                    | Integer        | Yes      | Number of processes | `1` |
| `indexer.objects_per_batch`                | Integer        | Yes      | Number of objects in a batch | `1000` |
| `mailer.enabled`                          | Boolean        | Yes      | Whether the mailer is running | `true` |
| `mailer.interval`                         | Integer        | Yes      | How often the mailer runs (every X seconds) | `60` (1 Minute) |
| `mailer.max_attempts`                     | Integer        | Yes      | Number of attempts before an e-mail is classified as undeliverable | `3` |
| `mailer.sender_address`                   | String         | Yes      | Sender Address | `easydb-server@localhost` |
| `mailer.envelope_address`                 | String         | Yes      | Envelope Address | |
| `api.settings.purgeall`                 | Boolean        | No       | Allow requests on `POST /api/v1/schema/purgeall` | `false` |
| `api.settings.purgedata`                | Boolean        | No       | Allow requests on `POST /api/v1/schema/purgedata` | `false` |
| `api.settings.restart`                  | Boolean        | No       | Allow requests on `POST /api/v1/schema/restart` | `false` |