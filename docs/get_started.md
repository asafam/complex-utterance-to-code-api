# Getting started

Let's learn by example.

Throughout this tutorial, we’ll walk you through the creation of a basic Python code for given virtual agent user commands.

We collected user commands for a virtual assistance (like Siri or Alexa). The virtual assistant offers help in navigation, weather forecasts, messaging, reminders and more. The goal of this project is to match user commands in English to a valid Python code.

We’ll assume you have a basic acquitance of Python already.

## Simple commands

Simple commands express a single action that the virtual assistant is expected to perform.

### Simple command example

Let's start by writing a code for a simple user command:

{==

Get directions from Disneyland to my house.

==}

To match this user command we need to map it with the `Navigation.find_directions(origin: Optional[Location], destination: Location)` in the [Navigation] API.

[Navigation]: /reference/actions/navigation/

``` py
origin = Location.resolve_from_text("Disneyland")
destination = Location.resolve_from_text("my house")
navigation_directions = Navigation.find_directions(
    origin=origin, 
    destination=destination
)
Responder.respond(response=navigation_directions)
```

`Navigation.find_directions` is taking a origin `Location` and destination `Location` as its parameters.

We first create the origin `Location` object. We name it according to the argument name `origin`. A text is usually mapped to a variable using the `resolve_from_text()` function.

Likewise, we first create the destination `Location` object. Likewise, We name it with the argument name `destination`.

Next, we plug the `origin` and `destination` parameters into the `Navigation.find_directions` function call. This function will return directions entity.

Last we report back the direction to the user using the `Responder.respond(response: Entity|Iterable[Entity])` API. As the `response` we set the `navigation_directions` entity recieved in the previous step.

### Another simple command example

Another simple user command:

{==

Text Karen that I will be late.

==}

To match this user command we need to map it with the `Messages.send_message(recipient: Contact, content: Content)` API.

``` py
recipient = Contact.resolve_from_text("Karen")
content = Content.resolve_from_text("I will be late")
Messages.send_message(
    recipient=recipient, 
    content=content
)
```

We first create the `Contact` object and name it according to the argument name `recipient`.

Similarly, we create the `Content` object and name it `content`.

Next we plug the `recipient` and `content` parameters into the `Messages.send_message` function call to call the function with its arguments.

## Complex commands

Complex commands can express multiple simple commands together like in sequences or conditions. Alterntaively, complex can call a single simple commands multiple times like in loops.

Let's see the code for complex commands.

### Complex command example

Complex user command:

{==

Get directions from Disneyland to my house and text them to Robert.

==}

We already went over the first part of the command ("Get directions from Disneyland to my house").

``` py
origin = Location.resolve_from_text("Disneyland")
detination = Location.resolve_from_text("my house")
directions = Navigation.find_directions(
    origin=origin, 
    destination=destination
)
```

Let's see the other part and put the code together. To match "text them to Robert" user command we need to map it with the `Messages.send_message` API.

``` py
recipient = Location.resolve_from_text("Robert")
content = Content.resolve_from_entity(directions)
Messages.send_message(
    recipient=recipient, 
    content=content
)
```

We already discussed how we create the `Contact` object and name it `recipient`.

Notice that in this example, the content of the message in this example is the the directions we got on the previous step. Therefore, we use the utility function `Content.resolve_from_entity()` to cast the `direction` entity to a `Content` entity.

Last, we call the `Messages.send_message` function with its arguments.

The final code should look like this:

``` py
origin = Location.resolve_from_text("Disneyland")
detination = Location.resolve_from_text("my house")
directions = Navigation.find_directions(
    origin=origin, 
    destination=destination
)

recipient = Location.resolve_from_text("Robert")
content = Content.resolve_from_entity(directions)
Messages.send_message(
    recipient=recipient, 
    content=content
)
```

### Another complex command example

Let's see another complex user command:

{==

Remind me to bring an umbrella if it rains tomorrow.

==}

The first part of the command: "Remind me to bring an umbrella" is conditioned by the second part of the sentence "if it rains tomorrow".

Conditions are another building blocks of complex commands.

We first get the weather forecasts by using the `Weather.find_weather_forecasts(date_time: Optional[DateTime], weather_attribute: Optional[WeatherAttribute])` API.

```py
date_time = DateTime.resolve_from_text("tomorrow")
weather_attribute = WeatherAttribute.resolve_from_text("rains")
weather_forecasts = Weather.find_weather_forecasts(
    date_time=date_time, 
    weather_attribute=weather_attribute
)
```

This API takes additional optional arguments, like a location, which we did not include in this example. In that case, the API assumes defaults values for the unspecified arguments (like the current location). Don't bother yourself with it and use only what is specified in the example.

Then, we check for the truthness of the condition expression. It will be valid if the `Weather.find_weather_forecasts` returned any result. This function return an iterable object of weather forecases that matches the `DateTime` and `WeatherAttribute`.

```py
expr = len(list(weather_forecasts)) > 0
if expr:
```

The condition body should include the "Remind me to bring an umbrella" command.

```py
person_reminded = Contact.resolve_from_text("me")
content = Content.resolve_from_text("Bring an umbrella").
Reminder.create_reminder(
    person_reminded=person_reminded, 
    content=content
)
```

We follow the `Reminder.create_reminder(person_reminded: Optional[Contact], content: Content)` API spec.

!!! note
    Notice that in the `content` object we omit the word "to" and keep the content that should appear in the reminder ("bring an umbrella").

Putting everything together:

```py
date_time = DateTime.resolve_from_text("tomorrow")
weather_attribute = WeatherAttribute.resolve_from_text("rains")
weather_forecasts = Weather.find_weather_forecasts(
    date_time=date_time, 
    weather_attribute=weather_attribute
)
expr = len(weather_forecasts) > 0
if expr:
    person_reminded = Contact.resolve_from_text("me")
    content = Content.resolve_from_text("Bring an umbrella")
    Reminder.create_reminder(
        person_reminded=person_reminded, 
        content=content
    )
```

### Yet another complex command example

Let's see one more complex user command:

{==

What is the weather in Paris and London?

==}

We will execute this command in a loop iterating over "Paris" and "London", althought it can be executed it in a sequence like previous commands.

Weather forecasts are returned in the `Weather.find_weather_forecasts(location: Optional[Location])`

```py
location1 = Location.resolve_from_text("Paris")
location2 = Location.resolve_from_text("London")
for location in [location1, location2]:
    weather_forecasts = Weather.find_weather_forecasts(location=location)
    response = weather_forecasts
    Responder.respond(response=response)
```
