# MessageStatus

## `MessageStatus.resolve_from_text`

This API allows us to resolve a message status from a user query. Statuses like "new", "unread" or "seen" for messages are common to be found and should be resolved.

``` py
MessageStatus.resolve_from_text(
    text: str
) : MessageStatus
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `text`        | `str`         | No        | Textual `MessageStatus` description        |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `MessageStatus`    | `MessageStatus` object |

**Example**

A `MessageStatus` denote the message status "read" in a user command:

{==

Delete every seen message from Google to me.

==}

``` py
message_status = MessageStatus.resolve_from_text("seen")
```
