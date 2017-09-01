# <a name="date"></a> Date

This type is a timestamp that can be provided in different precision levels (year, month, day, hour, minute, second).

The date is represented as an object with an attribute `value`, which can be set by the user and remains unaltered.
It is a string with a timestamp in ISO 8601 format (like [Timestamp](/technical/types/timestamp/timestamp.md).
Easydb generates an internal range that is used to index the date in Elasticsearch (fields `_from` and `_to`).

# <a name="daterange"></a> Date Range

This time is composed of two dates that define an inclusive time interval. The dates are provided as ISO 8601
timestamps in the fields `from` and `to`. Again, the fields `_from` and `_to` will be auto-generated. It is possible
to define open ranges to either side, but not to both sides.

~~~~json
@@include:example.json@@
~~~~

