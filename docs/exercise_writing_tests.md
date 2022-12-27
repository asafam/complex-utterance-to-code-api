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

## Exercise 4

Write a test for the following user command:

{==

Send Tyler a text saying hi and send one to Susan too.

==}

??? question "Solution"

    ```py
    from providers.data_model import DataModel
    from entities.generic import Contact, Content
    from entities.message import MessageEntity

    # test data
    data_model = DataModel(reset=True)
    data_contact1 = Contact(text="Tyler")
    data_model.append(data_contact1)
    data_contact2 = Contact(text="Susan")
    data_model.append(data_contact2)
    data_content = Content(text="hi")
    data_model.append(data_content)

    # test assertions
    data_messages_lists = data_model.get_response([MessageEntity])
    assert len(data_messages_lists) == 2
    data_message1 = data_messages_lists[0]
    assert data_message1.data.get("recipient") == data_contact1
    assert data_message1.data.get("content") == data_content
    data_message2 = data_messages_lists[1]
    assert data_message2.data.get("recipient") == data_contact2
    assert data_message2.data.get("content") == data_content
    ```

## Exercise 5

Write a test for the following user command:

{==

If I don't have anything scheduled on the 20th of this month on my calendar, message Alice and ask if she wants to go dinner.

==}

??? question "Solution"

    ```py
    from providers.data_model import DataModel
    from entities.event import EventCalendar, EventEntity, EventName
    from entities.generic import Contact, Content, DateTime
    from entities.message import MessageEntity

    # test data
    data_model = DataModel(reset=True)
    data_date_time_20 = DateTime(
        text="20th of this month", value=datetime.now().replace(day=20)
    )
    data_model.append(data_date_time_20)
    data_date_time_19 = DateTime(
        text="19th of this month", value=datetime.now().replace(day=19)
    )
    data_model.append(data_date_time_19)
    data_calendar = EventCalendar(text="my calendar")
    data_model.append(data_calendar)
    data_event_name = EventName(text="dinner")
    data_model.append(
        EventEntity(
            date_time=data_date_time_20,
            calendar=data_calendar,
            event_name=data_event_name,
        )
    )
    data_recipient = Contact(text="Alice")
    data_model.append(data_recipient)
    data_content = Content(
        text="she wants to go dinner"
    )
    data_model.append(data_content)

    # assertions
    data_messages = data_model.get_data(MessageEntity)
    assert len(data_messages) == 1
    data_message = data_messages[0]
    assert data_message.data.get("recipient") == data_recipient
    assert data_message.data.get("content") == data_content
    ```

    We write another test for the case the condition is not met:

    ```py
    from providers.data_model import DataModel
    from entities.event import EventCalendar, EventEntity, EventName
    from entities.generic import Contact, Content, DateTime
    from entities.message import MessageEntity

    # test data
    data_model = DataModel(reset=True)
    data_date_time_20 = DateTime(
        text="20th of this month", value=datetime.now().replace(day=20)
    )
    data_model.append(data_date_time_20)
    data_date_time_19 = DateTime(
        text="19th of this month", value=datetime.now().replace(day=19)
    )
    data_model.append(data_date_time_19)
    data_calendar = EventCalendar(text="my calendar")
    data_model.append(data_calendar)
    data_event_name = EventName(text="dinner")
    data_model.append(
        EventEntity(
            date_time=data_date_time_20,
            calendar=data_calendar,
            event_name=data_event_name,
        )
    )
    data_recipient = Contact(text="Alice")
    data_model.append(data_recipient)
    data_content = Content(
        text="she wants to go dinner"
    )
    data_model.append(data_content)

    # assertions
    data_messages = data_model.get_data(MessageEntity)
    assert len(data_messages) == 0
    ```
