# EventCalendar

## `EventCalendar.resolve_from_text`

This API allows us to resolve a calendar name listing an event from a given user input.

``` py
EventCalendar.resolve_from_text(
    text: str
) : EventCalendar
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `text`        | `str`         | No        | Textual EventCalendar description        |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `EventCalendar`    | `EventCalendar` object |

**Example**

A `EventCalendar` is the name of the calendar journey to search or create meeting in.

{==

Do I have a townhall meeting this Friday on my work calendar?

==}

``` py
event_calendar = EventCalendar.resolve_from_text("my work calendar")
```
