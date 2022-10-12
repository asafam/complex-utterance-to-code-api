# Resource

## `Resource.resolve_from_text`

This API allows us to resolve a resource in the form of an app or a website that will use to tp perform an action.

``` py
Resource.resolve_from_text(
    text: str
) : Resource
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `text`        | `str`         | No        | Textual `Resource` description        |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `Resource`    | `Resource` object |

**Example**

A `Resource` can be a specific app like Gmail

{==

Reply back to Sue on Facebook saying I did not get the invite

==}

``` py
resource = Resource.resolve_from_text("Facebook")
```
