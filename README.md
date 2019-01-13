# Market API

A web server API for the backend of a barebones online marketplace.

## Usage

All responses are in `application/JSON`

* **Get all products**
    ```bash
    GET /api/products
    ```
    An optional parameter, `available`, can be set to `true` (case-sensitive) to return products with inventory_count greater than 0 only.
    ```bash
    GET /api/products?available=true
    ```
    
    Example response:
    ```JSON
    {
      "products": [
        {
          "id": 5,
          "title": "Banana",
          "price": 3.75,
          "inventory_count": 100,
        },
        {...},
        {...},
        ...
      ]
    }
    ```