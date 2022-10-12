# WeatherTemperatureUnit

## `WeatherTemperatureUnit.resolve_from_text`

This API allows us to resolve a requested temperature unit (like celsius or fahrenheit) .

``` py
WeatherTemperatureUnit.resolve_from_text(
    text: str
) : WeatherTemperatureUnit
```

!!! note
    Weather tempreature unit is represented by `WeatherTemperatureUnit` and is not a weather attribute.

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `text`        | `str`         | No        | Textual WeatherTemperatureUnit description        |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `WeatherTemperatureUnit`    | `WeatherTemperatureUnit` object |

**Example**

A `WeatherTemperatureUnit` denote the weather attribute "sunny" in a user command:

{==

Tell me the weather in fahrenheit.

==}

``` py
weather_temperature_unit = WeatherTemperatureUnit.resolve_from_text("fahrenheit")
```
