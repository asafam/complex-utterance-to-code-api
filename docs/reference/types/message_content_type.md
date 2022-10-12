# MessageContentType

## `MessageContentType.resolve_from_text`

This API allows us to resolve the message type that should be sent. Commonly we may find the textual decription for message content type like "audio" or "voice" .

``` py
MessageContentType.resolve_from_text(
    text: str
) : MessageContentType
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `text`        | `str`         | No        | Textual `MessageContentType` description        |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `MessageContentType`    | `MessageContentType` object |

**Example**

Sending a voice message requires the `MessageContentType` to be resolved.

{==

Send a voice message to Ted

==}

``` py
message_content_type = MessageContentType.resolve_from_text("voice")
```
