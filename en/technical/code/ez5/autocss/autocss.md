#### ez5.autoCSS

ez5.autoCSS()

resize all elements in the current window that are marked as having
[ez5.autoCSSRules](../...md#autoCSSRules) by calling
[autoCSSInit()](#autoCSSInit), on a time-delayed thread.

\$().autoCSSInit(class\_name)

apply autoCss styling rules to an element. The width and height values
noted in the class style rule are subtracted from the respective values
of the next parent element with attribute `auto-css-parent` and
re-applied to the element

##### Parameters

 `class_name: string`
:   selector applied to identify elements. This should be a class name
    staring with `auto-css-`

