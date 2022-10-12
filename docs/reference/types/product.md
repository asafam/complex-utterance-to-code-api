# Product

## `Product.resolve_from_text`

This API allows us to resolve a product from a text. A product is not limited to the product category but can also include the product brand and manufacturer, For example, the text "car insurance", "iPhone 14", "Detroit deep dish pizza" or "polka dot black dress" should all be reolved in this API.

``` py
Product.resolve_from_text(
    text: str
) : Product
```

**Arguments**

| Name          | Type          | Optional  | Description                              |
| ------------- | --------------| --------- | ---------------------------------------- |
| `text`        | `str`         | No        | Textual `Product` description        |

**Returns**

| Type          | Description       |
| ------------- | ----------------- |
| `Product`    | `Product` object |

**Example**

A `Product` can be include the product's brand, vendor, name and different features. Please note the price cmparison should be achieved using the `min` utility functions (see more in the Advanced Topics section).

{==

Where can I find a store cheapest price for the new Lego knights castle that has it in stock?

==}

``` py
resource = Product.resolve_from_text("the new Lego knights castle")
```
