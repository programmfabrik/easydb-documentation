# ez5

Application namespace

## Constants

Name

Value

Input

Description

field\_needs\_data

128

false

Bitmask value for Input fields. It is set for all appropriate elements,
so no need to add it by hand.

NO\_LABEL

1 \<\< 0

false

Bitmask value for fields that should have no label.

TEXTAREA

1+128

true

multi-line text input element.

INPUT

2+128

true

single-line text input element.

CHECKBOX

3+128

true

checkbox element.

RADIO

4+128

true

radio button element.

SELECT

5+128

true

select (dropdown) element.

FORM

15+128

true

{@link ez5.modal} element.

IMAGE

16+128

true

?? element.

PASSWORD

17+128

true

?? element.

BUTTON\_SELECT

18+128

true

?? element.

DATETIME

19+128

true

?? element.

OUTPUT

6

false

Constant indicates an arbitrary element as indicated by the
`field.tagname` parameter of {@link ez5.\$render\_element}.

BUTTON

7

false

{@link ez5.button} element.

REMOVE\_ROW

8

false

clickable element for removing a table row.

SPLITTER

9

false

?? element.

LINKED\_TABLE

10

false

?? element.

TABLE

11

false

?? element.

SEARCH

12

false

text input element used for searching.

SPLITTER\_SUB

13

false

?? element.

TEXT

14

false

read-only text element.

## Attributes

ez5.datatypes: array

Array of pre-defined named datatype objects.

### Datatype object

Each element is organized as an array with two entries:

ez5.datatypes = [
[ string, object ],
...
]

The first being the datatype name, the second an object describing the
type:

`group: int`
:   0 = text, 1 = date/time, 2 = number, 3 = other,

`check: string[]`
:   at least one of `"required"`, `"range"` or `"regexp"`

### Defined datatypes

name

group

check

text\_1

0

required, regexp

text\_multi

0

required, regexp

email

0

required

text\_identifier

0

required, regexp

date

1

required, range

datetime

1

required, range

date\_range

1

required

datetime\_range

1

required

number

2

required, range

decimal.2

2

required, range

float

2

required, range

eas

3

required

boolean

3

required

position-2d

3

required

area-2d

3

required

ez5.validator: object

Associative array of validation rules, identified by name.

### Members

Each named validator has the format:

`check: string`
:   RegExp pattern

`tooltip: string`
:   tooltip text

### Defined validators

name

Description

dbname

validate database names

ez5.autoCSSRules: object

generated associative array of all stylesheet-based CSS class rules that
start with `auto-css-`. The string part after that is used as name.

### Styles

autoCSS-Rules only contain the attributes - `width` - `height` On
rendering, their value will be subtracted from the size of parent
elements marked with attribute `auto-css-parent` and the result applied
to matching elements.

ez5.server\_call\_count: int

ajax counter
