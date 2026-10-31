---
name: DateTime
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "A data type that represents a moment in time."
---

# DateTime

A data type that represents a moment in time.

**Type:** datatype

## Description

The **DateTime** data type represents a moment in time using a Unix timestamp.
It can be used to easily format dates and times in specific locales. When
converted to a string, a string conversion of the stored timestamp integer is
returned. They don't store timezone values. Instead, timezones are considered
when constructing and using **DateTime** objects.

**DateTime** objects are equal if and only if their
[UnixTimestampMillis](/docs/reference/engine/datatypes/DateTime.md) properties are
equal.

#### Time Value Table

The [ToUniversalTime()](/docs/reference/engine/datatypes/DateTime.md) and
[ToLocalTime()](/docs/reference/engine/datatypes/DateTime.md) methods return a table of
time-related values, such as `Year`, `Month`, and `Day`. The format of the
table returned by these functions is described below, with each integer
element in descending size order.

| Name | Range | Notes |
| --- | --- | --- |
| `Year` | 1400–9999 | — |
| `Month` | 1–12 | — |
| `Day` | 1–31 | — |
| `Hour` | 0–23 | — |
| `Minute` | 0–59 | — |
| `Second` | 0–59 | — |
| `Millisecond` | 0–999 | — |

#### String Format

The [DateTime](/docs/reference/engine/datatypes/DateTime.md) object supports date/time conversion into a string
through the [FormatUniversalTime()](/docs/reference/engine/datatypes/DateTime.md)
and [FormatLocalTime()](/docs/reference/engine/datatypes/DateTime.md) methods. They both
work the same except for which timezone the [DateTime](/docs/reference/engine/datatypes/DateTime.md) should be
interpreted in.

The first argument passed to these methods must be a string representing one
of the tokens shown below. The tokens are then replaced with a specific value
depending on the provided locale.

```lua
local dt = DateTime.now()

-- The "dddd" token is replaced with the full day of the week
print("Today is " .. dt:FormatLocalTime("dddd", "en-us"))

-- For the "en-us" locale, the "LL" token equals "MMMM D, YYYY"
print("The date is " .. dt:FormatLocalTime("LL", "en-us"))
```

##### Composite Tokens

Depending on locale, these tokens replace to **specific combinations** of the
**elemental tokens** described in the next section. This produces a correct
date/time string depending on the locale. For example, in English, the date
has the "[month]&nbsp;[day]" as in "June&nbsp;11". In French, the date is in a
"[day]&nbsp;[month]" format as in "11&nbsp;juin". These special rules are
handled for you automatically through the following composite tokens, so use
these if you're displaying simple time and/or date information.

| Token(s) | Locale Examples (Format) |
| --- | --- |
| Time |
| `LT` | `en-us` : `8:30 PM` (`h:mm A`)`zh-cn` : `20:30` (`HH:mm`) |
| Time with Seconds |
| `LTS` | `en-us` : `8:30:25 PM` (`h:mm:ss A`)`zh-cn` : `20:30:25` (`HH:mm:ss`) |
| Month (Number), Day, Year |
| `L` | `en-us` : `09/04/1986` (`MM/DD/YYYY`)`zh-cn` : `1986/09/04` (`YYYY/MM/DD`) |
| `l` | `en-us` : `9/4/1986` (`M/D/YYYY`)`zh-cn` : `1986/9/4` (`YYYY/M/D`) |
| Month (Name), Day, Year |
| `LL` | `en-us` : `September 4, 1986` (`MMMM D, YYYY`)`zh-cn` : `1986年9月4日` (`YYYY年M月D日`) |
| `ll` | `en-us` : `Sep 4, 1986` (`MMM D, YYYY`)`zh-cn` : `1986年9月4日` (`YYYY年M月D日`) |
| Month (Name), Day, Year, Time |
| `LLL` | `en-us` : `September 4, 1986 8:30 PM` (`MMMM D, YYYY h:mm A`)`zh-cn` : `1986年9月4日晚上8点30分` (`YYYY年M月D日Ah点mm分`) |
| `lll` | `en-us` : `Sep 4, 1986 8:30 PM` (`MMM D, YYYY h:mm A`)`zh-cn` : `1986年9月4日 20:30` (`YYYY年M月D日 HH:mm`) |
| Day of Week, Month (Name), Day, Year, Time |
| `LLLL` | `en-us` : `Thursday, September 4, 1986 8:30 PM` (`dddd, MMMM D, YYYY h:mm A`)`zh-cn` : `1986年9月4日星期四晚上8点30分` (`YYYY年M月D日ddddAh点mm分`) |
| `llll` | `en-us` : `Thu, Sep 4, 1986 8:30 PM` (`ddd, MMM D, YYYY h:mm A`)`zh-cn` : `1986年9月4日星期四 20:30` (`YYYY年M月D日dddd HH:mm`) |

##### Elemental Tokens

Each of these tokens replace to a **single value** and can be used as elements
of a larger time string. Avoid using these if you only need simple date and
time information, as the **composite tokens** are more appropriate for those
purposes.

| Token(s) | Examples |
| --- | --- |
| Year |
| `YY` | `70`, `71`, …, `29`, `30` |
| `YYYY` | `1970`, `1971`, …, `2029`, `2030` |
| Month |
| `M` | `1`, `2`, …, `11`, `12` |
| `MM` | `01`, `02`, …, `11`, `12` |
| `MMM` | `Jan`, `Feb`, …, `Nov`, `Dec` |
| `MMMM` | `January`, `February`, …, `November`, `December` |
| Day of Month |
| `D` | `1`, `2`, …, `30`, `31` |
| `DD` | `01`, `02`, …, `30`, `31` |
| Day of Year |
| `DDD` | `1`, `2`, …, `364`, `365` |
| `DDDD` | `001`, `002`, …, `364`, `365` |
| Day of Week |
| `d` | `0`, `1`, …, `5`, `6` |
| `dd` | `Su`, `Mo`, …, `Fr`, `Sa` |
| `ddd` | `Sun`, `Mon`, …, `Fri`, `Sat` |
| `dddd` | `Sunday`, `Monday`, …, `Friday`, `Saturday` |
| Hour |
| `H` | `0`, `1`, …, `22`, `23` |
| `HH` | `00`, `01`, …, `22`, `23` |
| `h` | `1`, `2`, …, `11`, `12` |
| `hh` | `01`, `02`, …, `11`, `12` |
| Minute |
| `m` | `0`, `1`, …, `58`, `59` |
| `mm` | `00`, `01`, …, `58`, `59` |
| Second |
| `s` | `0`, `1`, …, `58`, `59` |
| `ss` | `00`, `01`, …, `58`, `59` |
| Fractional Second |
| `S` | `0`, `1`, …, `8`, `9` |
| `SS` | `00`, `01`, …, `98`, `99` |
| `SSS` | `000`, `001`, …, `998`, `999` |
| AM/PM |
| `A` | `en-us` : `AM`, `PM``zh-cn` : `凌晨\|早上\|上午\|中午\|下午\|晚上` |
| `a` | `en-us` : `am`, `pm``zh-cn` : `凌晨\|早上\|上午\|中午\|下午\|晚上` |

## Constructors

### DateTime.now

**Signature:** `DateTime.now()`

Returns a new [DateTime](/docs/reference/engine/datatypes/DateTime.md) representing the current moment in time,
using the device's local clock. Most operating systems automatically sync
their local time against online time servers, so this should be within a
few hundred milliseconds. However, users can easily disable sync behavior
and set the system time to anything they want; for synchronized time
between client and server, use [Workspace:GetServerTimeNow()](/docs/reference/engine/classes/Workspace.md)
instead.

When you need to precisely measure the time elapsed between two points in
time, like when testing performance, use [os.clock()](/docs/reference/engine/globals/os.md) instead.

### DateTime.fromUnixTimestamp

**Signature:** `DateTime.fromUnixTimestamp(unixTimestamp: number)`

Returns a new [DateTime](/docs/reference/engine/datatypes/DateTime.md) object from the given Unix timestamp, or
the number of **seconds** since January 1st, 1970 at 00:00 (UTC).

This function only has granularity to 1 second. To represent sub-second
timestamps, use [DateTime.fromUnixTimestampMillis()](/docs/reference/engine/datatypes/DateTime.md) instead.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `unixTimestamp` | `number` |  | The number of seconds since January 1st, 1970 at 00:00 UTC (the Unix epoch). Must be between -17,987,443,200 and 253,402,300,799 (approximately years 1400 to 9999). |

### DateTime.fromUnixTimestampMillis

**Signature:** `DateTime.fromUnixTimestampMillis(unixTimestampMillis: number)`

Returns a new [DateTime](/docs/reference/engine/datatypes/DateTime.md) object from the given Unix timestamp, or
the number of **milliseconds** since January 1st, 1970 at 00:00 (UTC).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `unixTimestampMillis` | `number` |  | The number of milliseconds since January 1st, 1970 at 00:00 UTC (the Unix epoch). Must be between -17,987,443,200,000 and 253,402,300,799,999 (approximately years 1400 to 9999). |

### DateTime.fromUniversalTime

**Signature:** `DateTime.fromUniversalTime(year?: number, month?: number, day?: number, hour?: number, minute?: number, second?: number, millisecond?: number)`

Returns a new [DateTime](/docs/reference/engine/datatypes/DateTime.md) using the given units from a UTC time.
The values accepted are similar to those found in the time value table
returned by [ToUniversalTime()](/docs/reference/engine/datatypes/DateTime.md).

- Date units (year, month, day) that produce an invalid date will raise an
  error. For example, January 32nd or February 29th on a non-leap year.
- Time units (hour, minute, second, millisecond) that are outside their
  normal range are valid. For example, 90 minutes will cause the hour to
  roll over by 1; -10 seconds will cause the minute value to roll back
  by 1.
- Non-integer values are rounded down. For example, providing 2.5 hours
  will be equivalent to providing 2 hours, not 2 hours 30 minutes.
- Omitted values are assumed to be their lowest value in their normal
  range, except for year which defaults to 1970.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `year` | `number` | `1970` | The year value, between 1400 and 9999. |
| `month` | `number` | `1` | The month value, between 1 and 12. |
| `day` | `number` | `1` | The day of the month, between 1 and 31. |
| `hour` | `number` | `0` | The hour value, between 0 and 23. |
| `minute` | `number` | `0` | The minute value, between 0 and 59. |
| `second` | `number` | `0` | The second value, between 0 and 60. |
| `millisecond` | `number` | `0` | The millisecond value, between 0 and 999. |

### DateTime.fromLocalTime

**Signature:** `DateTime.fromLocalTime(year?: number, month?: number, day?: number, hour?: number, minute?: number, second?: number, millisecond?: number)`

Returns a new [DateTime](/docs/reference/engine/datatypes/DateTime.md) using the given units from a local time.
The values accepted are similar to those found in the time value table
returned by [ToLocalTime()](/docs/reference/engine/datatypes/DateTime.md).

- Date units (year, month, day) that produce an invalid date will raise an
  error. For example, January 32nd or February 29th on a non-leap year.
- Time units (hour, minute, second, millisecond) that are outside their
  normal range are valid. For example, 90 minutes will cause the hour to
  roll over by 1; -10 seconds will cause the minute value to roll back
  by 1.
- Non-integer values are rounded down. For example, providing 2.5 hours
  will be equivalent to providing 2 hours, not 2 hours 30 minutes.
- Omitted values are assumed to be their lowest value in their normal
  range, except for year which defaults to 1970.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `year` | `number` | `1970` | The year value, between 1400 and 9999. |
| `month` | `number` | `1` | The month value, between 1 and 12. |
| `day` | `number` | `1` | The day of the month, between 1 and 31. |
| `hour` | `number` | `0` | The hour value, between 0 and 23. |
| `minute` | `number` | `0` | The minute value, between 0 and 59. |
| `second` | `number` | `0` | The second value, between 0 and 60. |
| `millisecond` | `number` | `0` | The millisecond value, between 0 and 999. |

### DateTime.fromIsoDate

**Signature:** `DateTime.fromIsoDate(isoDate: string)`

Returns a [DateTime](/docs/reference/engine/datatypes/DateTime.md) from an ISO 8601 date-time string in UTC
time, such as those returned by
[ToIsoDate()](/docs/reference/engine/datatypes/DateTime.md). If the string parsing fails,
the function returns `nil`.

An example ISO 8601 date-time string would be `2020-01-02T10:30:45Z`,
which represents January 2nd 2020 at 10:30 AM, 45 seconds.

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `isoDate` | `string` |  | An ISO 8601 date-time string in UTC, such as `"2020-01-02T10:30:45Z"`. |

## Properties

### DateTime.UnixTimestamp

**Type:** `number`

The number of **seconds** since January 1st, 1970 at 00:00 UTC (the Unix
epoch). Range is -17,987,443,200 to 253,402,300,799, approximately years
1400&ndash;9999.

### DateTime.UnixTimestampMillis

**Type:** `number`

The number of **milliseconds** since January 1st, 1970 at 00:00 UTC (the
Unix epoch). Range is -17,987,443,200,000 to 253,402,300,799,999,
approximately years 1400&ndash;9999.

## Methods

### DateTime:ToUniversalTime

**Signature:** `DateTime:ToUniversalTime(): Dictionary`

Converts the value of this [DateTime](/docs/reference/engine/datatypes/DateTime.md) object to Universal
Coordinated Time (UTC). The returned table contains the following keys:
`Year`, `Month`, `Day`, `Hour`, `Minute`, `Second`, `Millisecond`. For
more details, see the time value table in this data type's description.
The values within this table could be passed to
[fromUniversalTime()](/docs/reference/engine/datatypes/DateTime.md) to produce the
original [DateTime](/docs/reference/engine/datatypes/DateTime.md) object.

**Returns:** `Dictionary`

### DateTime:ToLocalTime

**Signature:** `DateTime:ToLocalTime(): Dictionary`

Converts the value of this [DateTime](/docs/reference/engine/datatypes/DateTime.md) object to local time. The
returned table contains the following keys: `Year`, `Month`, `Day`,
`Hour`, `Minute`, `Second`, `Millisecond`. For more details, see the time
value table in this data type's description. The values within this table
could be passed to [fromLocalTime()](/docs/reference/engine/datatypes/DateTime.md) to
produce the original [DateTime](/docs/reference/engine/datatypes/DateTime.md) object.

**Returns:** `Dictionary`

### DateTime:ToIsoDate

**Signature:** `DateTime:ToIsoDate(): string`

Formats a date as a ISO 8601 date-time string. The value returned by this
function could be passed to
[fromIsoDate()](/docs/reference/engine/datatypes/DateTime.md) to produce the original
[DateTime](/docs/reference/engine/datatypes/DateTime.md) object.

An example ISO 8601 date-time string would be `2020-01-02T10:30:45Z`,
which represents January 2nd 2020 at 10:30 AM, 45 seconds.

**Returns:** `string`

### DateTime:FormatUniversalTime

**Signature:** `DateTime:FormatUniversalTime(format: string, locale: string): string`

Generates a string from the [DateTime](/docs/reference/engine/datatypes/DateTime.md) value interpreted as
Universal Coordinated Time (UTC) and a format string. The format string
should contain tokens, which will replace to certain date/time values
described by the [DateTime](/docs/reference/engine/datatypes/DateTime.md) object. For more details, see the
**String Format** section in this data type's description.

```lua
local dt = DateTime.now()
-- For en-us, the "LL" token equals "MMM D, YYYY", which gives "June 11, 2020"
print("The date is " .. dt:FormatUniversalTime("LL", "en-us"))
--> "The date is June 11, 2020"
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `format` | `string` |  | A format string containing tokens that are replaced with date and time values, such as `"LL"` or `"YYYY-MM-DD"`. |
| `locale` | `string` |  | A BCP 47 locale identifier (such as `"en-us"`) that determines language and formatting conventions. |

**Returns:** `string`

### DateTime:FormatLocalTime

**Signature:** `DateTime:FormatLocalTime(format: string, locale: string): string`

Generates a string from the [DateTime](/docs/reference/engine/datatypes/DateTime.md) value interpreted as
**local time** and a format string. The format string should contain
tokens, which will replace to certain date/time values described by the
[DateTime](/docs/reference/engine/datatypes/DateTime.md) object. For more details, see the **String Format**
section in this data type's description.

```lua
local dt = DateTime.now()
-- For en-us, the "LL" token equals "MMM D, YYYY", which gives "June 11, 2020"
print("The date is " .. dt:FormatLocalTime("LL", "en-us"))
--> "The date is June 11, 2020"
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `format` | `string` |  | A format string containing tokens that are replaced with date and time values, such as `"LL"` or `"YYYY-MM-DD"`. |
| `locale` | `string` |  | A BCP 47 locale identifier (such as `"en-us"`) that determines language and formatting conventions. |

**Returns:** `string`