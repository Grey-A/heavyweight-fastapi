## Heavyweight(FastAPI) Starter Template for Large Applications

This repository provides a robust template for creating powerful FastAPI applications that leverage Postgres and Alembic. Inspired by [Radoslav Georgiev's Django Structure for Scale lecture](https://youtu.be/yG3ZdxBb1oo?si=D6A9dHyhKb_Kf-J7) and my own personal experience, this template offers a structured approach to building scalable web applications.

### Project Structure
```
.vscode
alembic/
app/
    common/
        __init__.py
        dependencies.py
        paginators.py
        regex.py
        schemas.py
        security.py
        types.py
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
    main.py
.gitignore
alembic.ini
docker-compose.yml
Dockerfile
env_sample.txt
railway.toml
requirements.txt
start.sh
```

### Components

**.vscode:** Configuration files for Visual Studio Code.

**alembic/:** Contains Alembic settings and migrations.

**config/:** Holds project settings.
- **database.py:** Manages database connection, session settings, and the base database model.
- **settings.py:** Utilizes pydantic_settings to load environment variables. Change the `SECRET_KEY` from the default value on Railway.

**app/:** The main FastAPI project directory.
  - **common/:**:
    - **dependencies.py:** The common dependencies used by all the modules
    - **paginators.py:** The collection of helpers for response pagination
    - **regex.py:** Where common regular expressions will be kept
    - **schemas.py:** Where you will keep your general/generic schemas
    - **security.py:** Where the authentication functions are kept
    - **types.py:** Where general/generic types are kept

  - **config/:** Holds project settings.
    - **database.py:** Manages database connection, session settings, and the base database model.
    - **settings.py:** Utilizes pydantic_settings to load environment variables. Change the `SECRET_KEY` from the default value on Railway.

  - **example_module/:**
    An Example of how you might structure your different modules/apps, doing it this way makes it easy to decouple/seggregate
    - **apis.py:** Houses endpoints like `user_create`, `user_login`, and `user_details`.
    - **models.py:** Uses SQLAlchemy to draft the user table. Alembic handles migrations.
    - **schemas.py:** Defines schemas for create, details, login, and token requests.
    - **selectors.py:** Manages GET operations, fetching data from the database.
    - **services.py:** Handles POST, PUT, PATCH, and DELETE operations, manipulating database data.
  - **main.py:** Entry point of the application

**.gitignore:** This specifies which folders/files to not push to github
**env_sample.txt:** Sample environment variable list. Create a `.env` file and provide values.

### Getting Started

1. Setup Virtual Environment (If you are not using docker)
   ```shell
   $ py -m venv .venv
   $ .venv\Scripts\activate
   ```
   NOTE: If you are using VsCode and you see a popup that says use env as workspace env then click yes

</br>
2. Install dependencies:
   Locally

   ```shell
   $ pip install -r requirements.txt
   ```
</br>
    With Docker
   
   ```shell
   docker-compose up
   ```
</br>

3. Create a `.env` file and input environment variables.
</br>

4. Initialize database tables:
   ```
   alembic upgrade head
   ```

</br>

5. Start the application in development mode:
   ```
   uvicorn app.main:app --reload
   ```

</br>

6. Test the application by making requests to endpoints.

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


### Contact

If you have any questions or suggestions, feel free to reach out to me:
(P.S I am looking for a job, i consult and i tutor :)

- Name: Bello Shehu Ango
- Email: angobello0@gmail.com
- GitHub: https://github.com/Grey-A
- Linkedin: https://linkedin.com/in/angobello0
- Upwork: https://www.upwork.com/freelancers/~01bb1007bf8311388a
- Instagram: https://www.instagram.com/bello_ango0/
