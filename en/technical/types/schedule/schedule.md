# Schedule

A schedule defines when a certain action takes place. It is represented as a JSON object with the following attributes:

## Attributes

| Name            | Description |
|-----------------|-------------|
| `weekdays`      | Days of the week when the action takes place (array of strings): the valid values are the english names for the days of the week |
| `days_of_month` | Days of the month when the action takes place (array of integers): the valid range is 1-31 |
| `hours`         | Hours of the day when the action takes place (array of integers): the valid range is 0-23 |
| `minutes`       | Minutes when the action takes place (array of integers): the valid range is 0-59 |

- `weekdays` and `days_of_month` can be left out, meaning all weekdays and days of the month, respectively
- if `hours` is left out, a standard hour will be used (depends on functionality using the schedule)
- if `minutes` is left out, a standard minute will be used (depends on functionality using the schedule)

Example: *each first Sunday of a month at 10*

~~~~json
@@include:example.json@@
~~~~

Example: *every 5 minutes*

~~~~json
{
	"hours": [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ],
	"minutes": [ 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55 ]
}
~~~~

Example: *everyday at the standard hour*

~~~~json
{}
~~~~

