# Content

## `Content.resolve_from_text`

This API allows us to resolve the textual content from a given user input, for example, for a reminder or a text message.

``` py
Content.resolve_from_text(
    text: str
) : Content
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `text`        | `str`         | No        | Textual content         |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `Content`    | `Content` object |

**Example**

A `Content` can be a day, a specific time, or any publicly known place (for example, Times Square).

{==

Remind me tomorrow to postpone my dentist appointment

==}

``` py
content = Content.resolve_from_text("postpone my dentist appointment")
```

!!! tip
    When resolving Content from a text we will usually ignore reference words like "to", which are not part of the body of the content (like the message or the reminder).

## `Content.resolve_from_entity`

This API allows us to resolve a Content from a given entity.

**Arguments**

| Name          | Type          | Optional  | Description                                   |
| ------------- | ------------- | --------- | --------------------------------------------- |
| `entity`      | `Entity`      | No        | An `Entity` object to be transformed to a `Content` |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `Content`    | A Content object |

**Example**

A `Content` can be be inferred from different objects. For example, messaging navigation directions where the directions should be transformed to the message content.

{==

Send Joshua my arrival time to his house if I leave now

==}

``` py
location = Location.resolve_from_text("his house")
destination = location
date_time = DateTime.resolve_from_text("now")
departure_date_time = date_time
estimated_arrival_time = Navigation.get_estimated_arrival_timie(
    destination=destination,
    departure_date_time=departure_date_time
)
content = Content.resolve_from_entity(estimated_arrival_time)
...
```
