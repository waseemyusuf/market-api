# Market API

A web server API for the backend of a barebones online marketplace.

## Endpoints for:

1. **Fetching all products**
    ```
    GET /api/products
    ```
    An optional parameter, `available`, can be set to `true` to return products with inventory_count greater than 0 only.
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
2. **Fetching one product at a time**
  
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
3. **Purchasing a product**
   ```
   POST /api/purchase/<product_id>
   ```
   Error and success responses repectively:
   ```
   { "error": "No inventory, cannot purchase."}
   { "success": "item was purchased" }
   ```
   
# (Back end installation)
   
Create a PostgreSQL database and then save its database URI to an environment variable named `DATABASE_URI`, then run `create.py` to create a table in the database. Products have to be added to the table manually. The API can only perform above mentioned tasks.
