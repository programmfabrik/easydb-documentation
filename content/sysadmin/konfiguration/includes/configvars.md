# Config vars

## YAML
- base.plugins

- solution.name
- solution.plugins

- server.external_url
- server.directory.imexporter
- server.directory.pflib
- server.directory.output
- server.directory.logfile
- server.directory.umask
- server.directory.server_error
- server.directory.l10n_dir
- server.exporter.num_workers
- server.exporter.batch_size
- server.exporter.max_xml_size_for_xslt
- server.janitor.eas_sync_commit
- server.janitor.enabled
- server.janitor.interval
- server.janitor.max_age
- server.imexporter.socket
- server.imexporter.num_services
- server.frontend.socket
- server.frontend.num_services
- server.upload-server.socket
- server.upload-server.num_services
- server.indexer.enabled
- server.indexer.num_processes
- server.indexer.objects_per_batch
- server.mailer.enabled
- server.mailer.interval
- server.mailer.max_attempts
- server.mailer.sender_address
- server.mailer.envelope_address
- server.api.settings.purgeall
- server.api.settings.purgedata
- server.api.settings.restart

- schema.base_dir
- schema.user_dir
- schema.dsn

- eas.url
- eas.instance
- eas.thumbnail_size
- eas.supervisor_enabled
- eas.vhost
- eas.external_url
- eas.procedure_settings
- eas.rights_management.<class>
- eas.rights_management.<class>.versions.version
- eas.rights_management.<class>.versions.size_print
- eas.rights_management.<class>.versions.size_limit
- eas.rights_management.<class>.versions.export
- eas.rights_management.<class>.versions.rightsmanagement
- eas.rights_management.<class>.versions.group
- eas.rights_management.<class>.versions.zoomable
- eas.rights_management.<class>.versions.watermark
- eas.rights_management.<class>.versions.standard

- config.config_settings

- default_pics.background
- default_pics.user_avatar
- default_pics.logo

- plugins.url_prefix_internal
- plugins.url_prefix_external
- plugins.url_prefix

- elasticsearch.url
- elasticsearch.connect_timeout_ms
- elasticsearch.transfer_timeout_ms
- elasticsearch.fielddata_memory
- elasticsearch.settings
- elasticsearch.begin_with_wildcards_allowed

- email.welcome_new_user
- email.forgot_password
- email.require_password_change
- email.confirm_email
- email.updated_self_service
- email.updated_record
- email.login_disabled
- email.share_collection
- email.transition_resolve
- email.transition_reject
- email.transport
- email.export

- ldap.user.protocol
- ldap.user.server
- ldap.user.port
- ldap.user.basedn
- ldap.user.scope
- ldap.user.filter
- ldap.user.user
- ldap.user.password
- ldap.group.protocol
- ldap.group.server
- ldap.group.port
- ldap.group.basedn
- ldap.group.scope
- ldap.group.filter
- ldap.group.user
- ldap.group.password
- ldap.enviroment.mapping.<var>.attr
- ldap.enviroment.mapping.<var>.regex_match
- ldap.enviroment.mapping.<var>.regex_replace
- ldap.enviroment.user.login
- ldap.enviroment.user.displayname
- ldap.enviroment.user.email
- ldap.enviroment.groups.attr
- ldap.enviroment.groups.divider

- sso.auth_method -> client
- sso.enviroment
- sso.ldap

- default_client.debug
- default_client.tag_icons
- default_client.tag_colors
- default_client.asset_browser_max_preview_filesize
- default_client.video_player_use_original
- default_client.audio_player_use_original
- default_client.webdvd_player_open_window_parameter
- default_client.print_limit
- default_client.collection_refresh_rate_seconds
- default_client.suggest_disable
- default_client.database.level
- default_client.watermark_configured

- hotfolder.enabled
- hotfolder.directory
- hotfolder.number_of_workers
- hotfolder.upload_batch_size
- hotfolder.upload_batches
- hotfolder.delay

- imexporter-database.dsn
- imexporter-database.schema

- server.directory.plans

- debug.exporter_sleep
- debug.exporter_fail
- debug.exporter_warnings
- debug.search_sleep

## Data model server
- default_client.datamodel.uid
- default_client.datamodel.server

## Email
- server.mailer.enabled
- email.login_disabled

## HTTPS
- server.external_url

## LDAP
- ldap.user.protocol
- ldap.user.server
- ldap.user.basedn
- ldap.user.filter
- ldap.group.protocol
- ldap.group.server
- ldap.group.basedn
- ldap.group.filter
- ldap.enviroment.mapping.u_login.attr
- ldap.enviroment.mapping.u_login.regex_match
- ldap.enviroment.mapping.u_login.regex_replace
- ldap.enviroment.mapping.g_ldap_prefixed.attr
- ldap.enviroment.mapping.g_ldap_prefixed.regex_match
- ldap.enviroment.mapping.g_ldap_prefixed.regex_replace
- ldap.enviroment.user.login
- ldap.enviroment.user.displayname
- ldap.enviroment.user.email
- ldap.enviroment.groups.attr
- ldap.enviroment.groups.attr

## Plugin configuration
- plugins.enabled.base.custom-data-type-link

## SSO
- plugins.enabled.base.sso
- sso.enviroment.mapping.m_login.attr
- sso.enviroment.mapping.m_login.regex_match
- sso.enviroment.mapping.m_login.regex_replace
- sso.enviroment.user.login
- sso.enviroment.user.displayname
- sso.enviroment.user.email
- sso.enviroment.groups.attr
- sso.enviroment.groups.divider

## Variants of filesize
- include_before
- eas.produce_settings
- eas.rights_management.image.versions[].<class>.size_print
- eas.rights_management.image.versions[].<class>.size_limit
- eas.rights_management.image.versions[].<class>.export
- eas.rights_management.image.versions[].<class>.rightsmanagement
- eas.rights_management.image.versions[].<class>.group
- eas.rights_management.image.versions[].<class>.zoomable
- eas.rights_management.video.versions[].<class>.version
- eas.rights_management.video.versions[].<class>.size_print
- eas.rights_management.video.versions[].<class>.size_limit
- eas.rights_management.video.versions[].<class>.export
- eas.rights_management.video.versions[].<class>.group
- eas.rights_management.video.versions[].<class>.rightsmanagement
- eas.rights_management.video.versions[].<class>.standard
- eas-rights_management.audio.versions[].<class>.version
- eas-rights_management.audio.versions[].<class>.size_print
- eas-rights_management.audio.versions[].<class>.export
- eas-rights_management.audio.versions[].<class>.rightsmanagement
- eas-rights_management.audio.versions[].<class>.group
- eas-rights_management.audio.versions[].<class>.standard
- eas-rights_management.office.versions[].<class>.version
- eas-rights_management.office.versions[].<class>.size_print
- eas-rights_management.office.versions[].<class>.export
- eas-rights_management.office.versions[].<class>.rightsmanagement
- eas-rights_management.office.versions[].<class>.standard
- eas-rights_management.archive.versions[].<class>.version
- eas-rights_management.archive.versions[].<class>.size_print
- eas-rights_management.archive.versions[].<class>.group
- eas-rights_management.archive.versions[].<class>.rightsmanagement
- eas-rights_management.archive.versions[].<class>.limit
- eas-rights_management.archive.versions[].<class>.standard
- eas-rights_management.unknown.versions[]
- eas-rights_management.vector2d.versions[]
- eas-rights_management.vector3d.versions[]