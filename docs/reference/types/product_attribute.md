# ProductAttribute

## `ProductAttribute.resolve_from_text`

This API allows us to resolve attributes of a product from a textual description.

``` py
ProductAttribute.resolve_from_text(
    text: str
) : ProductAttribute
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `text`        | `str`         | No        | Textual `ProductAttribute` description        |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `ProductAttribute`    | `ProductAttribute` object |

**Example**

A `ProductAttribute` can be a specific app like Gmail

{==

Order 2 packages organic creamy peanut butter from WholeFood.

==}

``` py
resource = ProductAttribute.resolve_from_text("organic creamy peanut butter from WholeFood")
```
