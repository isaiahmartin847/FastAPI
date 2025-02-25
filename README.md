# Project Structure

This project follows a specific folder structure to organize the codebase effectively. Below is an overview of the main folders and their purposes:

## Folder Structure

- **app/**: Contains the main application code.
  - \***\*init**.py\*\*: Marks the directory as a Python package.
  - **api/**: Contains the API-related code.
    - \***\*init**.py\*\*: Marks the directory as a Python package.
    - **v1/**: Contains version 1 of the API.
      - \***\*init**.py\*\*: Marks the directory as a Python package.
      - **endpoints/**: Contains the endpoint definitions for the API.
        - \***\*init**.py\*\*: Marks the directory as a Python package.
        - **api.py**: Contains the FastAPI router and endpoint definitions.
  - **repository/**: Contains data access logic and database interactions.
    - \***\*init**.py\*\*: Marks the directory as a Python package.
    - **models.py**: Defines the data models used in the application.
    - **repository.py**: Contains functions to interact with the database.
  - **service/**: Contains business logic and service layer code.
    - \***\*init**.py\*\*: Marks the directory as a Python package.
    - **user_service.py**: Contains user-related business logic.
    - **product_service.py**: Contains product-related business logic.

## File Descriptions

- **app/main.py**: The entry point of the FastAPI application.
- **app/api/v1/endpoints/api.py**: Defines the API routes and their corresponding logic.
- **app/api/**init**.py**: Initializes the API package.
- **app/**init**.py**: Initializes the main application package.
- **app/api/v1/**init**.py**: Initializes the version 1 API package.
- **app/api/v1/endpoints/**init**.py**: Initializes the endpoints package.
- **app/repository/**init**.py**: Initializes the repository package.
- **app/repository/models.py**: Defines the data models used in the application.
- **app/repository/repository.py**: Contains functions to interact with the database.
- **app/service/**init**.py**: Initializes the service package.
- **app/service/user_service.py**: Contains user-related business logic.
- **app/service/product_service.py**: Contains product-related business logic.

## Getting Started

To get the project up and running from scratch, follow these steps:

1. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment**:

   ```bash
   source venv/bin/activate
   ```

3. **Install the required packages**:

   ```bash
   pip install fastapi uvicorn
   ```

4. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

Now you should be able to access the API at `http://127.0.0.1:8000`.
If you go to the route `http://127.0.0.1:8000/docs` it will give you a UI for all the routes.
