## Heavyweight(FastAPI) Starter Template for Large Applications

This repository provides a robust template for creating powerful FastAPI applications that leverage Postgres and Alembic. Inspired by [Radoslav Georgiev's Django Structure for Scale lecture](https://youtu.be/yG3ZdxBb1oo?si=D6A9dHyhKb_Kf-J7), this template offers a structured approach to building scalable web applications.

### Project Structure

```
.vscode
alembic/
app/
    config/
        __init__.py
        database.py
        settings.py
    example_module/
        __init__.py
        apis.py
        models.py
        schemas.py
        selectors.py
        services.py
    __init__.py
    dependencies.py
    main.py
.gitignore
alembic.ini
env_sample.txt
requirements.txt
```

### Components

**.vscode:** Configuration files for Visual Studio Code.

**alembic/:** Contains Alembic settings and migrations.

**env_sample.txt:** Sample environment variable list. Create a `.env` file and provide values.

**config/:** Holds project settings.
- **database.py:** Manages database connection, session settings, and the base database model.
- **settings.py:** Utilizes pydantic_settings to load environment variables. Change the `SECRET_KEY` from the default value on Railway.

**app/:** The main FastAPI project directory.
- **main.py:** Entry point of the application, with a router linking to the `user/` module.
- **dependencies.py:** Initializes the database session.
- **user/:** Contains code and functionality related to users.
  - **apis.py:** Houses endpoints like `user_create`, `user_login`, and `user_details`.
  - **models.py:** Uses SQLAlchemy to draft the user table. Alembic handles migrations.
  - **schemas.py:** Defines schemas for create, details, login, and token requests.
  - **selectors.py:** Manages GET operations, fetching data from the database.
  - **services.py:** Handles POST, PUT, PATCH, and DELETE operations, manipulating database data.

### Getting Started

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Create a `.env` file and input environment variables.

3. Initialize database tables:
   ```
   alembic upgrade head
   ```

4. Start the application in development mode:
   ```
   uvicorn app.main:app --reload
   ```

5. Test the application by making requests to endpoints.

### Contribute to the Project

We welcome contributions from the community to make this FastAPI Starter Template even better. If you have ideas for improvements, new features, or bug fixes, feel free to:

- Fork the repository and create a new branch for your contribution.
- Submit pull requests to propose changes to the project.
- Engage in discussions and share your thoughts on enhancements.

By contributing, you help make this template more valuable for developers building FastAPI applications. Together, we can create a robust foundation for large-scale projects. Thank you for your support!

For detailed information, refer to the following resources:

- FastAPI documentation: https://fastapi.tiangolo.com/
- Alembic documentation: https://alembic.sqlalchemy.org/en/latest/
- Django Structure for Scale lecture: https://youtu.be/yG3ZdxBb1oo?si=D6A9dHyhKb_Kf-J7
