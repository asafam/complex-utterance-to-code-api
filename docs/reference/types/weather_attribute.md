# WeatherAttribute

## `WeatherAttribute.resolve_from_text`

This API allows us to resolve a weather attribute or condition from a user input. For example, "stormy", "rain" or "cold" are all weather attributes.

Weather temperature are also a weather attribute. For example, "80 degrees" or "below 60s", should be resolved using this component.

``` py
WeatherAttribute.resolve_from_text(
    text: str
) : WeatherAttribute
```

!!! note
    Weather tempreature unit is represented by `WeatherTemperatureUnit` and is not a weather attribute.

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `text`        | `str`         | No        | Textual WeatherAttribute description        |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `WeatherAttribute`    | `WeatherAttribute` object |

**Example**

A `WeatherAttribute` denote the weather attribute "sunny" in a user command:

{==

Will it be sunny with clear skies this weekend?

==}

``` py
weather_attribute = WeatherAttribute.resolve_from_text("sunny with clear skies")
```
