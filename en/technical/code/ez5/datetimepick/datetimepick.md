### ez5.\$datetimepick

ez5.\$datetimepick(field, data)

Contructs an input element for picking date and/or time through popup
picking elements, based on [Wijmo
Calendar](http://wijmo.com/wiki/index.php/Calendar) and [jQuery UI
Timepicker Addon](http://trentrichardson.com/examples/timepicker/). It
consists of a `<div>` contining one or two input fields that are coupled
with a button for calling up a popup date- or timepicker respectively.
If neither `field.datepicker` nor `field.timepicker` is given, a
datepicker is shown as default.

The Appearance of the element changes depending on the language for the
page, as defined by [field.culture](#culture).

\$().ez5datetimepick(field, data)

constructs a input element for picking date and/or time and appends it
to a jQuery object.

#### Parameters

 `[field]: object`
:

     `name: string`
    :

     `culture: string`
    :

     `[datepicker]: object`
    :   shows an input field for dates with a datepicker popup.\
         Most Parameters for the Calendar are set, some may be given:

         `[monthCols]: int`
        :   Gets or sets the number of calendar months in horizontal
            direction.

             *Default:* 1
            :

         `[calendarWeekRule]: string`
        :   Defines different rules for determining the first week of
            the year. Possible values are: "firstDay", "firstFullWeek"
            or "firstFourDayWeek".

             *Default:* "firstDay"
            :

         `[minDate]: Date`
        :   Determines the minimum date to display. It is impossible to
            disable the application of a minimum.

             *Default:* new Date(1900/01/1)
            :

         `[maxDate]: Date`
        :   Determines the maximum date to display. It is impossible to
            disable the application of a maximum.

             *Default:* new Date(2099/12/31)
            :

     `[timepicker]: object`
    :   shows an input field for times with a timepicker popup.\
         While the timepicker is based on an Addon for the jQuery UI
        Datepicker, and thus the multitude of options available for that
        widget can be set, it is strongly discouraged to set any but the
        following:

         `[stepHour]: float`
        :   Hour stepping: 0.05 is smooth, 1 would jump to each hour

             *Default:* 0.05
            :

         `[stepHour]: float`
        :   Minute stepping: 0.05 is smooth, 1 would jump to each
            minute, `n > 1` would resolve only every nth minute

             *Default:* 0.05
            :

         `[hourMin]: int`
        :   Determines the minimum hour to display. Use 24-hours
            notation even if the localization will result in an 12-hour
            formatting.

             *Default:* 0
            :

         `[hourMax]: int`
        :   Determines the maximum hour to display. Use 24-hours
            notation even if the localization will result in an 12-hour
            formatting.

             *Default:* 23
            :

         `[minuteMin]: int`
        :   Determines the minimum minute to display.

             *Default:* 0
            :

         `[minuteMax]: int`
        :   Determines the maximum minute to display.

             *Default:* 59
            :

 `[data]: object`
:   content data for each field element.

     `data[field.name]: String`
    :   The date to show formatted as

        -   either `yyyy-MM-dd HH:mm:sszz` if `timepicker` is set, where
            `zz` is an optional timezone offset consisting of a
            plus/minus sign and two digits,

        -   or `yyyy-MM-dd` if `timepicker` is ommitted or set to false
            This format does not really conform with ISO 8601, but
            instead follows the current db output.

#### Extensions to the returned jQuery Object

\$modal.value()

The selected date/time

##### Returns

 `String`
:   formatted as `yyyy-MM-ddTHH:mm:ss`. If `timepicker` is ommitted or
    set to false, time information will still be present but set to
    `00:00:00`. No timezone information is included.

