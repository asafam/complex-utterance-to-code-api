# Exercises

Follow the quick Get Started tutorial and the conding convention we present there and try writing a code for given user (complex) commands challenges.

## Exercise 1

Try to write code for the following user command. This time, we will provide a solution to this exercise.

{==

What will the weather be in two hours, and remind me to go running then.

==}

??? question "Solution"

    ``` python
    date_time = DateTime.resolveFromText("in two hours")
    weather_forecast = WeatherQuery.find_weather_forecasts(
        date_time=date_time
    )
    response = weather_forecast
    Responder.respond(response=response)

    content = Content.resolve_from_text("go running")
    contact = Contact.resolve_from_text("me")
    person_reminded = contact
    create_reminder(
        content=content, 
        person_reminded=person_reminded, 
        date_time=date_time
    )
    ```

## Exercise 2

Try to write code for the following user command:

{==

If there's a concert in the park next month, remind me next week to check for discounted tickets.

==}

## Exercise 3

Write code for the following user command:

{==

Read me my new emails in my mailbox and archive them once they are read.

==}

## Exercise 4

{==

I need you to give me directions to a place where I can rent the cheapest tux in town, and then directions from there to the wedding reception event I have scheduled.

==}
