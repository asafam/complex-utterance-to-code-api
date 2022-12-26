# Testing

We collected user commands for a virtual assistance (like Siri or Alexa). The virtual assistant offers help in navigation, weather forecasts, messaging, reminders, shopping and more. The goal of this project is to match user commands in English to a valid Python code.

This section will walk you through the process of testing the generated code.

## Evaluating text to code models

Text to code models are machine learning models that are trained to generate code from natural language descriptions. One way to evaluate a text to code model is by comparing the generated code to a gold standard or reference implementation, also known as denotation, to ensure that the generated code is equivalent in functionality and performance.

Evaluating generated code is an important step in the process of using code generation tools. Generated code should be thoroughly tested and reviewed to ensure that it meets the desired specifications and functions correctly, without errors or bugs. This can be tested through manual testing or by using automated testing tools.

We evluate the quality of the text to code model by testing the generated code using unit tests and integration tests. The tests are used to test the generated code in isolation. We test each generated code snippet in isolation to ensure that it functions correctly in the context of the frameworks API.

## API tests

We release a set of API libraries that simulate the functionality of the APIs that are used in the generated code. These libraries are used to test the generated code in isolation. The API libraries and their spec are listed in the [API](/reference/) reference page.

The API tests are located in the `tests` directory.

## Getting started with API tests

Throughout this tutorial we will walk you through the creation of a basic Python code for given virtual agent user commands.

!!! note
Without the generated code we are nto able to run the tests. Yet, we can still write tham in isolation of the generated code. The tests are dependant from the actual generated code.

### Prerequisites

- Basic knowledge of Python.
- Get yourself farmiliar with the API [Getting started](/get_started) and [API](/reference/) reference pages.

That's it. We are ready to start writing tests.

### Writing tests

Let's learn by example.

#### Simple command

Simple commands express a single action that the virtual assistant is expected to perform.

{==

Text Karen that I will be late.

==}

This command should return an object of [text message](/reference/actions/message/#messagesend_message). The generated code for this example can be found in the [Getting started](/get_started) page.

Every test should start by seeding the data. In this case we need to seed the data with the `recipient` and `content` attributes. We expect the generated code to create a `MessageEntity` object with the `recipient` and `message` attributes.

```py
from entities.generic import Contact, Content

data_model = DataModel(reset=True)
data_recipient = Contact(text="Karen")
data_model.append(data_recipient)
data_content = Content(text="I will be late")
data_model.append(data_content)
```

We start with creating a `DataModel` object and setting the `reset` attribute to `True`. This will reset the data model and remove all the data that was seeded before.

We then create a `Contact` object and set the `text` attribute to the contact name. We repeat the same process for the `Content` object with the expected message content.

We can now write the test.

```py
data_messages = data_model.get_data(MessageEntity)
assert len(data_messages) == 1
data_message = data_messages[0]
assert data_message[0].data.get("recipient") == data_recipient
assert data_message[0].data.get("message") == data_content
```

We start by getting the data from the data model. We use the `get_data` method to get the data with the `MessageEntity` type. We then assert that the data list has only one element. We expect our generated code to create only one `MessageEntity` object.

We then get the first element from the data list and assert that the `recipient` attribute is set to the `Contact` object that we seeded before. We also assert that the `message` attribute is set to the `Content` object that we seeded before.

That's it. We have written our first test.

#### Another simple command

Let's look at another simple command.

{==

Get directions from Disneyland to my house.

==}

This command should return a list of [navigation directions](/reference/actions/navigation/#navigationfind_directions). The generated code for this example can be found in the [Getting started](/get_started) page.

We remind you that every test should start by seeding the data. In this case we need to seed the data with the `origin` and `destination` locations. We can do this by creating a `Location` object and setting the `text` attribute to the location name.

```py
from entities.generic import Location
from entities.navigation import NavigationDirectionEntity

data_model = DataModel(reset=True)
data_origin = Location(text="Disneyland")
data_model.append(data_origin)
data_destination = Location(text="my house")
data_model.append(data_destination)
data_model.append(
    NavigationDirectionEntity(origin=data_origin, destination=data_destination)
)
data_model.append(
    NavigationDirectionEntity(origin=data_origin, destination=data_destination)
)
```

We start with creating a `DataModel` object and setting the `reset` attribute to `True`.

We then create two `Location` objects and set the `text` attribute to the location name. We then append the objects to the data model.
In this case we see the data with the origin `Location` object that will be set to `Disneyland`, and the data with the destination `Location` is set to `my house`.

Next we append two `NavigationDirectionEntity` object to the data model. We choose 2 as an arbitrary number, like there can be 2 possible directions to get from the origin to the destination. These objects will be used to test the generated code.

We can now write the test.

```py
data_navigation_directions_list = data_model.get_data(NavigationDirectionEntity)
assert len(data_navigation_directions_list) == 1
data_navigation_directions = data_navigation_directions_list[0]
assert len(data_navigation_directions) == 2
assert data_navigation_directions[0].data.get("origin") == data_origin
assert data_navigation_directions[0].data.get("destination") == data_destination
assert data_navigation_directions[1].data.get("origin") == data_origin
assert data_navigation_directions[1].data.get("destination") == data_destination
```

We start by getting the data from the data model. We get the data with the `NavigationDirectionEntity` object. We then assert that the length of the data is equal to 1. This means that we have one list of `NavigationDirectionEntity` objects in the data model, and that our generated code is matching the text description and created only a single `NavigationDirectionEntity` list of objects.

We then get the first `NavigationDirectionEntity` element from the data model. In the case of navigation direction, this is expected to be a list of `NavigationDirectionEntity` objects. We assert that this list length is equal to 2. This means that we have two `NavigationDirectionEntity` objects in the list.

We then assert that the `origin` attribute of each of the `NavigationDirectionEntity` objects is equal to the `data_origin` object. We also assert that the `destination` attribute of each of the `NavigationDirectionEntity` object is equal to the `data_destination` object.

!!! note
The `NavigationDirectionEntity` object is an object that we created to seed the test data for the generated code. It is **not** what is returned in `data_model.get_data(NavigationDirectionEntity)`. The objects that are returned are expected to be created in the generated code.

Voila! We have written our second test.

#### Sequence complex command

Complex commands allow you to combine multiple simple commands into a single request for your virtual assistant. These commands can be performed in a specific sequence, include conditional statements, or be executed multiple times.

Now let's look at a complex command  where commands are executed in a sequence.

{==

Get directions from Disneyland to my house and text Karen that I will be late.

==}

This command should return a list of [navigation directions](/reference/actions/navigation/#navigationfind_directions) **and** a [text message](/reference/actions/message/#messagesend_message). The generated code for this example can be found in the [Getting started](/get_started) page.

We remind you that every test should start by seeding the data. In this case we need to seed the data with the `origin` and `destination` locations. We also need to seed the data with the `Contact` and `Content` objects.

```py
from entities.generic import Contact, Content, Location
from entities.navigation import NavigationDirectionEntity

data_model = DataModel(reset=True)
# seed data for the 1st command
data_origin = Location(text="Disneyland")
data_model.append(data_origin)
data_destination = Location(text="my house")
data_model.append(data_destination)
data_model.append(
    NavigationDirectionEntity(origin=data_origin, destination=data_destination)
)
data_model.append(
    NavigationDirectionEntity(origin=data_origin, destination=data_destination)
)
# seed data for the 2nd command
data_recipient = Contact(text="Karen")
data_model.append(data_recipient)
data_content = Content(text="I will be late")
data_model.append(data_content)
```

Like before, we start with creating a `DataModel` object and setting the `reset` attribute to `True`.

We start by seeding the data for the first command. We create a `Location` origin object and set the `text` attribute to the location name. We then append the object to the data model. We do the same for the destination location. We also append two `NavigationDirectionEntity` object to the data model. We choose 2 as an arbitrary number, like there can be 2 possible directions to get from the origin to the destination. These objects will be used to test the generated code.

We then seed the data for the second command. We can do this by creating a `Contact` object and setting the `text` attribute to the contact name. We repeat the same process for the `Content` object with the expected message content. We then append the objects to the data model.

We can now write our complex command test.

```py
data_navigation_directions_list = data_model.get_data(NavigationDirectionEntity)
assert len(data_navigation_directions_list) == 1
data_navigation_directions = data_navigation_directions_list[0]
assert len(data_navigation_directions) == 2
assert data_navigation_directions[0].data.get("origin") == data_origin
assert data_navigation_directions[0].data.get("destination") == data_destination
assert data_navigation_directions[1].data.get("origin") == data_origin
assert data_navigation_directions[1].data.get("destination") == data_destination

data_messages = data_model.get_data(MessageEntity)
assert len(data_messages) == 1
data_message = data_messages[0]
assert data_message.data.get("recipient") == data_recipient
assert data_message.data.get("content") == data_content
```

We test the expected generated objects for the first command. We then test the expected generated objects for the second command. Nothing new here.

Congratulations! You have now written your first test for a complex command.

#### Conditional complex command

Conditional complex commands allow you to condition the execution of one command by checking the result of another command. This is useful when you want to execute a command only if a previous command was successful (or not).

Now let's look at a conditional complex command.

{==

Remind me to bring an umbrella if it rains tomorrow.

==}

Conditional complex commands are a bit more complex to test. We need to test two scenarios: the condition is met and the condition is not met. We will start by testing the scenario where the condition is met.

This command should return a [reminder](/reference/actions/reminder/#remindercreate_reminder) **only if** the [weather](/reference/actions/weather/#weatherget_weather) is rainy. The generated code for this example can be found in the [Getting started](/get_started) page.

Like before, we start by seeding the data. In this case we need to seed the data with the `Content` of the reminder, the `Contact` or the person being reminded, the `WeatherAttribute` and the `DateTime` objects for the weather forecasts.

```py
from entities.generic import Contact, Content, DateTime
from entities.weather import WeatherAttribute

data_model = DataModel(reset=True)
# seed data for the 1st command
data_person_reminded = Contact(text="me")
data_model.append(data_person_reminded)
data_content = Content(text="bring an umbrella")
data_model.append(data_content)
# seed data for the condition command
data_weather_attribute = WeatherAttribute(text="rains")
data_model.append(data_weather_attribute)
data_date_time_tomorrow = DateTime(text="tomorrow")
data_model.append(data_date_time_tomorrow)
data_model.append(
    WeatherEntity(
        attribute=data_weather_attribute,
        date_time=data_date_time_tomorrow
    )
)
```

We start by creating a `DataModel` object and setting the `reset` attribute to `True`.

We then seed the data for the first command. We create a `Contact` object and set the `text` attribute to the contact name. We then append the object to the data model. We do the same for the reminder content. We then seed the data for the condition command. We create a `WeatherAttribute` object and set the `text` attribute to the weather attribute. We then append the object to the data model. We do the same for the `DateTime` object with the date and time. We then append a `WeatherEntity` object to the data model. This object will be used to test the generated code.

!!! note
    The `WeatherEntity` object is a special case. It is not an entity that should be created like `MessageEntity` or `ReminderEndity`. It is something the generated code expects to fetch so we create it for that.

We can now write our conditional complex command test.

```py
data_messages = data_model.get_data(ReminderEntity)
assert len(data_messages) == 1
data_message = data_messages[0]
assert data_message.data.get("person_reminded") == data_person_reminded
assert data_message.data.get("content") == data_content
```

With conditional complex commands, we only test the expected generated object. This is because the generated code will not generate any objects when the condition is not met. We don't test the expected generated objects for the condition.

We now need to test the scenario where the condition is not met. We will do this by changing the weather attribute to something that is not rainy (any text value other than `rains` will do).

```py
from entities.generic import Contact, Content, DateTime
from entities.weather import WeatherAttribute

data_model = DataModel(reset=True)
# seed data for the 1st command
data_person_reminded = Contact(text="me")
data_model.append(data_person_reminded)
data_content = Content(text="bring an umbrella")
data_model.append(data_content)
# seed data for the condition command
data_weather_attribute = WeatherAttribute(text="sunny") # here we change the weather attribute to sunny instead of rains
data_model.append(data_weather_attribute)
data_date_time_tomorrow = DateTime(text="tomorrow")
data_model.append(data_date_time_tomorrow)
data_model.append(
    WeatherEntity(
        attribute=data_weather_attribute,
        date_time=data_date_time_tomorrow
    )
)
```

Now that the weather attribute is not rainy, we should not get a reminder. We can test this by checking that no `ReminderEntity` objects were generated.

```py
data_messages = data_model.get_data(ReminderEntity)
assert len(data_messages) == 0
```

We test that no `ReminderEntity` objects were generated. This is because the generated code will not generate any objects when the condition is not met.

Congratulations! You have now written the test for a conditional complex command.

#### Complex command with a loop

Complex commands with a loop allow you to execute a command multiple times. This is useful when you want to execute a command multiple times with different data. The text description of the commands expresses the multiple executions of the command.

Now let's look at a complex command with a loop.

{==
