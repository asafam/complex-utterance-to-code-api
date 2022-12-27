# Exercise writing tests

Let's test your knowledge of the [Tests](/tests) tutorial. We will provide you with a user command and you will write the test to match it.

## Exercise 1

Write a test for the following user command:

{==

Check the weather for the 4th of July and send a text to Grandpa that he should come over

==}

??? question "Solution"

    ```py
    from providers.data_model import DataModel
    from entities.generic import Contact, Content, DateTime
    from entities.weather import WeatherForecastEntity
    from entities.message import MessageEntity

    data_model = DataModel(reset=True)
    # seed data for the 1st command
    data_date_time = DateTime(text="4th of July", value=datettime.now() + timedelta(days=1))
    data_model.append(data_date_time)
    data_model.append(
        WeatherForecastEntity(date_time=data_date_time)
    )
    # seed the data for the 2nd command
    data_recipient = Contact(text="Grandpa")
    data_model.append(data_recipient)
    data_content = Content(text="he should come over")
    data_model.append(data_content)

    # test assertions for the 1st command
    data_weather_forecasts_list = data_model.get_data(WeatherForecast)
    assert len(data_weather_forecasts_list) == 1
    data_weather_forecasts = data_weather_forecasts_list[0]
    assert data_weather_forecasts[0].data.get("date_time") == data_date_time\
    # test assertions for the 2nd command
    data_messages = data_model.get_data(MessageEntity)
    assert len(data_messages) == 1
    data_message = data_messages[0]
    assert data_message.data.get("recipient") == data_recipient
    assert data_message.data.get("content") == data_content
    ```

## Exercise 2

Write a test for the following user command:

{==

If it rains tomorrow message dad that I will be running late.

==}

??? question "Solution"

    ```py
    from providers.data_model import DataModel
    from entities.generic import Contact, Content, DateTime
    from entities.weather import WeatherAttribute, WeatherForecastEntity

    data_model = DataModel(reset=True)
    # seed data for the condition query
    data_date_time_tomorrow = DateTime(text="tomorrow", value=datettime.now() + timedelta(days=1))
    data_model.append(data_date_time_tomorrow)
    data_weather_attribute = WeatherAttribute(text="rains")
    data_model.append(data_weather_attribute)
    data_model.append(
        WeatherForecastEntity(
            date_time=data_date_time_tomorrow,
            weather_attribute=data_weather_attribute
        )
    )
    # seed the data for the executed command
    data_recipient = Contact(text="dad")
    data_model.append(data_recipient)
    data_content = Content(text="I will be running late")
    data_model.append(data_content)

    # test assertions
    data_messages = data_model.get_data(MessageEntity)
    assert len(data_messages) == 1
    data_message = data_messages[0]
    assert data_message.data.get("recipient") == data_recipient
    assert data_message.data.get("content") == data_content
    ```

    Additional test for the case the condition is not met:

    ```py
    from providers.data_model import DataModel
    from entities.generic import Contact, Content, DateTime
    from entities.weather import WeatherAttribute, WeatherForecastEntity

    data_model = DataModel(reset=True)
    # seed data for the condition query
    data_date_time_tomorrow = DateTime(text="tomorrow", value=datettime.now() + timedelta(days=1))
    data_model.append(data_date_time_tomorrow)
    data_weather_attribute = WeatherAttribute(text="not rain")
    data_model.append(data_weather_attribute)
    data_model.append(
        WeatherForecast(
            date_time=data_date_time_tomorrow,
            weather_attribute=data_weather_attribute
        )
    )
    # seed the data for the executed command
    data_recipient = Contact(text="dad")
    data_model.append(data_recipient)
    data_content = Content(text="I will be running late")
    data_model.append(data_content)

    # test assertions
    data_messages = data_model.get_data(MessageEntity)
    assert len(data_messages) == 0
    ```

## Exercise 3

Write a test for the following user command:

{==

Set a timer for one hour and text Stacy that dinner will be ready in one hour.

==}

??? question "Solution"

    ```py
    from providers.data_model import DataModel
    from entities.generic import Contact, Content, DateTime
    from entities.message import MessageEntity
    from entities.timer import TimerEntity

    # test data
    data_model = DataModel(reset=True)
    data_duration = DateTime(text="one hour")
    data_model.append(data_duration)
    data_contact = Contact(text="Stacy")
    data_model.append(data_contact)
    data_content = Content(
        text="dinner will be ready in one hour",
        value="dinner will be ready in one hour",
    )
    data_model.append(data_content)

    # assertions
    data_timers = data_model.get_data(TimerEntity)
    assert len(data_timers) == 1
    data_timer = data_timers[0]
    assert data_timer.data.get("duration") == data_duration

    data_messages = data_model.get_data(MessageEntity)
    assert len(data_messages) == 1
    data_message = data_messages[0]
    assert data_message.data.get("recipient") == data_contact
    assert data_message.data.get("content") == data_content
    ```
