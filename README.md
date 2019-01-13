# Market API

A web server API for the backend of a barebones online marketplace.

## Endpoints

All responses are in `application/JSON`.

1. **Fetch all products**
    ```
    GET /api/products
    ```
    An optional parameter, `available`, can be set to `true` (case-sensitive) to return products with inventory_count greater than 0 only.
    ```
    GET /api/products?available=true
    ```
    
    Example response:
    ```
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
2. **Fetch one product at a time**
  
  A particular product can be fetched by its unique id.
  ```
  GET /api/products/<product_id>
  ```
  If no product with specified id is found in the database, a 422 error will be thrown and the JSON response will be:
  ```
  { "error": "Invalid product id" }
  ```
  
  Example successful response:
  ```
  {
    "id": 5,
    "title": "Banana",
    "price": 3.75,
    "inventory_count": 100
  }
  ```
