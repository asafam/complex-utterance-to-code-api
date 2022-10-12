# Message

## `Message.get_messages`

This API provides us the messages in our mobile device.

``` py
Message.get_messages(
    date_time: Optional[DateTime],
    sender: Optional[Contact],
    recipient: Optional[Contact],
    content: Optional[Content],
    message_status: Optional[MessageStatus],
    message_content_type: Optional[MessageContentType],
    resource: Optional[Resurce]
) : Iterable[MessageEntity]
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `date_time`        | `DateTime`  | Yes        | Date and time the message was recieved        |
| `sender`        | `Contact`  | Yes        | Message sender        |
| `recipient`        | `Contact`  | Yes        | Message recipient        |
| `content`        | `Content`  | Yes        | Content within the message        |
| `message_status`        | `MessageStatus`  | Yes        | The message status. For example, "unread" or "new" |
| `message_content_type`        | `MessageContentType`  | Yes        | The message content type |
| `resource`        | `Resource`  | Yes        | The message resource application |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `Iterable[MessageEntity]`    | Iterable of `MessageEntity` objects |

**Example**

{==

Read the last message from aunt Bessy

==}

``` py
contact = Contact.resolve_from_text("aunt Bessy")
sender = contact
messages = Message.get_messages(
    sender=sender
)
message = messages.last()
response = message
Responder.respond(response=response)
```

## `Message.send_message`

This API provides us the functionality of sending a message.

``` py
Message.send_message(
    recipient: Optional[Contact],
    content: Optional[Content],
    message_content_type: Optional[MessageContentType],
    resource: Optional[Resurce]
) : MessageEntity
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `recipient`        | `Contact`  | Yes        | Message recipient        |
| `content`        | `Content`  | Yes        | Content within the message        |
| `message_content_type`        | `MessageContentType`  | Yes        | The message content type |
| `resource`        | `Resource`  | Yes        | The message resource application |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `MessageEntity`    | The message object that was sent |

**Example**

{==

Record a voice message for Daryl

==}

``` py
contact = Contact.resolve_from_text("Daryl")
sender = contact
message_content_type = MessageContentType.resolve_from_text("voice")
messages = Message.send_message(
    sender=sender,
    message_content_type=message_content_type
)
```

## `Message.reply_message`

This API provides us the functionality of replying to a message, when the user explicitly states a reply action.

``` py
Message.reply_message(
    recipient: Optional[Contact],
    content: Optional[Content],
    message_content_type: Optional[MessageContentType],
    resource: Optional[Resurce]
) : MessageEntity
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `recipient`        | `Contact`  | Yes        | Message recipient        |
| `content`        | `Content`  | Yes        | Content within the message        |
| `message_content_type`        | `MessageContentType`  | Yes        | The message content type |
| `resource`        | `Resource`  | Yes        | The message resource application |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `MessageEntity`    | The message object that was sent |

**Example**

{==

Reply with a voice message to Stephanie on Whatsapp

==}

``` py
contact = Contact.resolve_from_text("Stephanie")
sender = contact
message_content_type = MessageContentType.resolve_from_text("voice")
resource = Resource.resolve_from_text("Whatsapp")
messages = Message.reply_message(
    sender=sender,
    message_content_type=message_content_type,
    resource=resource
)
```

## `Message.delete_messages`

This API provides us the functionality to delete specific message or a group of messages.

``` py
Message.reply_messages(
    message: MessageEntity|Iterable[MessageEntity]
) : None
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `messages`        | `MessageEntity|Iterable[MessageEntity]`  | No        | A specific message to delete or an iterable that upon iteration - deletes every message       |

**Returns**

This function does not return.

**Example**

{==

Delete the last 2 messages

==}

``` py
messages = Message.get_messages()
messages = messages.last(2)
Message.delete_messages(messages=messages)
```
