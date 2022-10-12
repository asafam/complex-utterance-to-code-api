# NavTravelMethod

## `NavTravelMethod.resolve_from_text`

This API allows us to resolve a navigation method for travelling.

``` py
NavTravelMethod.resolve_from_text(
    text: str
) : NavTravelMethod
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `text`        | `str`         | No        | Textual navigation travelling method description        |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `NavTravelMethod`    | `NavTravelMethod` object |

**Example**

{==

how long is the drive to SF on the PCH

==}

``` py
nav_travel_method = NavTravelMethod.resolve_from_text("drive")
```
