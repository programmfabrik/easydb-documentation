---
title: "128 - L10n"
menu:
  main:
    name: "L10n"
    identifier: "technical/types/l10n"
    parent: "technical/types"
---
# L10n

This type is a localized string field. For each culture supported by the server, there is an attribute containing
the localized string. If the attribute has to be given (not "optional"), at least one culture must be not null. If
the attribute is marked as "unique", it means that its values have to be unique for the same culture.

Example of an l10n field:


{{< include_json "./example.json" >}}


