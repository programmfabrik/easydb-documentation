### elasticsearch
| Variable                                           | Typ           | Pflicht | Erklärung | Default-Wert |
|----------------------------------------------------|---------------|---------|-----------|--------------|
| `url`                                      | String         | Yes      | URL | |
| `connect_timeout_ms`                       | Integer        | Yes      | connection timeout (ms) | `30000` (30 seconds) |
| `transfer_timeout_ms`                      | Integer        | Yes      | transmission timeout (ms) | `300000` (5 minutes) |
| `fielddata_memory`                         | String-List    | No       | Index fields that use `"memory"` as Fielddata type | |
| `settings`                                 | File           | Yes      | Index-Settings (JSON) | |
| `begin_with_wildcards_allowed`             | Boolean        | No       | Whether Suggest wildcards are allowed at the beginning | `false` |