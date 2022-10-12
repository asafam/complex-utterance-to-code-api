# Location

## `Location.resolve_from_text`

This API allows us to resolve a location from a given text.

``` py
Location.resolve_from_text(
    text: str
) : Location
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `text`        | `str`         | No        | Textual decription of a location         |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `Location`    | `Location` object |

**Example**

A `Location` can be an address, a city or a country name, or any publicly known place (for example, Times Square).

{==

If I leave now will I get to 37 Spring St by 12:30 pm?

==}

``` py
location = Location.resolve_from_text("37 Spring St")
```

A `Location` can be also be private to the user. It is in the API responsibility to infer a user specific location.

{==

Is it currently raining at home?

==}

``` py
location = Location.resolve_from_text("at home")
```

## `Location.resolve_from_entity`

This API allows us to resolve a location from a given entity.

**Arguments**

| Name          | Type          | Optional  | Description                                   |
| ------------- | ------------- | --------- | --------------------------------------------- |
| `entity`      | `Entity`      | No        | An `Entity` object to be transformed to a `Location` |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `Location`    | A location object |

**Example**

A `Location` can be be inferred from different objects. One example may be a meeting location or an event venue.

{==

Directions to the Rockets game

==}

``` py
event_name = EventName.resolve_from_text("the Rockets game")
event = Event.find(event_name=event_name)
location = Location.resolve_from_entity(event)
...
```
