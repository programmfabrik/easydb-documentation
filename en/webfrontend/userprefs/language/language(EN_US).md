# Language settings

easydb provides the ability to enable multiple languages ​​for the application (system), data, and search; provided the easydb administrator has installed the multilingual feature.

![Language Settings](language.png)

| Setting | Note |
|--|--|
| Application | If the multilingual feature is installed, you can choose the language of the system. All application functions then appear in this language
| Data | Select the language (s) for the input and display of the data. The selection of several languages ​​is possible. The order of the languages ​​can be changed. The sequence can be changed by dragging the entries with the left mouse button to the desired position
| Spelling check | By activating the spelling check, the data entries are checked when they are entered. The spelling check of the browser is used for this. First, check your spelling checker to see if the spelling checker is enabled
| Search | Enable this setting to perform the search in one or more languages. |
| Sort | If several languages ​​are selected, drag and drop can be used to change the position of the language. The above language is shown in the data model above. |

## Sorting of languages

If multilingualism is used for the search, but the translations of the entries are not completely contained in all languages, the order in which the languages ​​for the entry is to be displayed can be specified by the search language.

If a particular value is to appear in a standard view, but the language does not exist, as in the example below, the missing value can be displayed by another filled database language.

Example:

    Record 1: Wasser / Water
    Record 2: Feuer / (nothing)
    Record 3: (nothing) / Air

Only one value appears in the default view. Depending on whether the order of the database languages ​​here is e.g. English-German, or German-English, the results are displayed as follows:

English-Deutsch: Water, Feuer, Air

Deutsch-English: Wasser, Feuer, Air