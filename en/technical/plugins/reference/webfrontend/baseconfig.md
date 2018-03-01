# Base-Configuration

```coffeescript

getFieldDefFromParm: (baseConfig, pname, def, parent_def) ->
  if def.plugin_type != "wordpress-auth"
    return



BaseConfig.registerPlugin(new BaseConfigWordpress())
```
