# DateTime

## `DateTime.resolve_from_text`

This API allows us to resolve a date or time decription from a given text.

``` py
DateTime.resolve_from_text(
    text: str
) : DateTime
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `text`        | `str`         | No        | Textual decription of a time description         |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `DateTime`    | `DateTime` object |

**Example**

A `DateTime` can be a day, a specific time, or any publicly known place (for example, Times Square).

{==

If I leave now will I get to 37 Spring St by 12:30 pm?

==}

``` py
date_time = DateTime.resolve_from_text("now")
```

## `DateTime.resolve_from_entity`

This API allows us to resolve a DateTime from a given entity.

**Arguments**

| Name          | Type          | Optional  | Description                                   |
| ------------- | ------------- | --------- | --------------------------------------------- |
| `entity`      | `Entity`      | No        | An `Entity` object to be transformed to a `DateTime` |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `DateTime`    | A DateTime object |

**Example**

A `DateTime` can be be inferred from different objects. For example, an event time or the estimated time of arrival to a place.

{==

Will there be traffic downtown during the Rockets game?

==}

``` py
event_name = EventName.resolve_from_text("the Rockets game")
event = Event.find(event_name=event_name)
date_time = DateTime.resolve_from_entity(event)
...
```
