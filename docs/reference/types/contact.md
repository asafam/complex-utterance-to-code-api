# Contact

## `Contact.resolve_from_text`

This API allows us to resolve a Contact from a given user input, for example, a recipient of a message or a contact to create a reminder to.

``` py
Contact.resolve_from_text(
    text: str
) : Contact
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `text`        | `str`         | No        | Textual Contact description        |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `Contact`    | `Contact` object |

**Example**

{==

Remind me tomorrow to postpone my dentist appointment

==}

``` py
contact = Contact.resolve_from_text("me")
```
