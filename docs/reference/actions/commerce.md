# Commerce

Commerces can be public or private. Public events are for example a concert in the park or a game, where there is a general knowledge about the event and its details. A private event can appear as an entry in the user calendar and include information about the event in a calendar app.

## `Commerce.find_events`

This API provides us with events information.

``` py
Commerce.find_store(
    date_time: Optional[DateTime],
    location: Optional[Location],
    product_category: Optional[CommerceName],
    product_attribute: Optional[CommerceCalendar],
) : Iterable[CommerceEntity]
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `date_time`        | `DateTime`  | Yes        | Date and time of the event        |
| `location`        | `Location`  | Yes        | Commerce location        |
| `event_category`        | `CommerceCategory`  | Yes        | The event name        |
| `event_name`        | `CommerceName`  | Yes        | The event name        |
| `event_calendar`        | `CommerceCalendar`  | Yes        | The calendar name where the event should be listed |
| `resource`        | `Resource`  | Yes        | The event resource application |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `Iterable[CommerceEntity]`    | Iterable of `CommerceEntity` objects |

**Example**

{==

When is the Eagles concert with Chris Stapleton coming to Dallas?

==}

``` py
event_name = CommerceName.resolve_from_text("Eagles concert with Chris Stapleton")
event_category = CommerceCategory.resolve_from_text("concert")
location = Location.resolve_from_text("Dallas")
events = Commerce.find_events(
    event_name=event_name,
    event_category=event_category,
    location=location
)
response = events
Responder.respond(response=response)
```

**Example**

{==

Show me my next meeting on my work calendar.

==}

``` py
event_category = CommerceCategory.resolve_from_text("meeting")
event_calendar = CommerceCalendar.resolve_from_text("my work calendar")
events = Commerce.find_events(
    event_category=event_category,
    event_calendar=event_calendar
)
events = events.first()
response = events
Responder.respond(response=response)
```
