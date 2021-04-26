---
title: "General hints"
menu:
  main:
    name: "General hints"
    identifier: "tools/csvimport/general"
    parent: "tools/csvimport"
---
# General hints

- the CSV file must be UTF-8 or UTF-16 encoded (otherwise umlauts and special characters will not be imported correctly)
- comma, semicolon or tabulator can be used as column separator (detection is done automatically by easydb)
- texts containing commas, semicolons, tabs or breaks must be enclosed by double or single quotes (detection is done by easydb automatically)
- the column headers in the CSV file can be freely chosen (mapping of source and target fields must then be done manually, see [options](../options))
- if you use the internal easydb field names as column headers in the CSV file, the mapping is done automatically (to get the internal easydb field names it is best to download a dataset as CSV file first and apply the column headers)
- if possible always use a unique idendifier, because only this idendifier can be used to update existing datasets later on
- when importing quotes, please note the following:

| Text to import | Notation in CSV file |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| "Simple text enclosed in quotes to be imported". | """Simple text enclosed in quotes to be imported.""" |
| "Simple text enclosed in quotation marks".             | "Plain text that contains ""quotation marks""."         |
| "Simple text in quotes, but which also contains ""quotes""." | """Plain text in quotes, but which also contains ""quotation marks""."" |
| "This is a quote." said person Z.                        | """This is a quote."" said Person Z."                    |
| Person Z said "This quote."                               | "Person Z said ""This quote."""                           |


