# Getting Started with Campus backend

This project was bootstrapped with django.

## Technologies explanation
### Backend
- [Django](https://www.djangoproject.com/) - main library.
- [Django REST Framework](https://www.django-rest-framework.org/) - useful addition to the default django functionality.

**Note:** all packages can be restored from the **requirements.txt** in the root of any service.

## Files structure explanation **IMPORTANT!**
0. All services are fully separated and located in **services/** folder.
1. We use 3layered architecture with some modifications. Good starting point is [this article](https://exceptionnotfound.net/the-repository-service-pattern-with-dependency-injection-and-asp-net-core/).
2. **api/** contains api config and django settings. Changed rarely.
3. **service-name/** (for example **learn/**) - main code
    1. **api/** contains all routes and serializers. **Serializer** = class that transforms from domain objects to JSON. This folder depends on **domain/**.
    2. **domain/** is a core folder. **Entity** = [domain entity](https://khalilstemmler.com/articles/typescript-domain-driven-design/entities/), pure python class with methods. **IS NOT THE SAME AS A DATABASE ENTITY**. **Service** = operations on entities. Depends on **infrastructure/**.
    3. **infrastructure/** contains all external connections. For example database or mailer adapter. **Repository** = database connection with query/update methods. **RETURNS DOMAIN ENTITY**.
    4. **migrations/** contains migrations [Why do we need it](https://www.prisma.io/dataguide/types/relational/what-are-database-migrations#what-are-database-migrations) - you need only "What are database migrations?" paragraph

## Additional conventions
### Backend
1. Import order (leave empty line between blocks)
    1. Libraries
    2. Custom Python code

Example:
```python
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from learn.api.constants import COMMON_ROUTE_URL
from learn.domain.posts.post_service import post_service
```

## Available Scripts

In the project directory, you can run:

### `python manage.py runserver`

Runs the API in the development mode.\
Open [http://localhost:8000](http://localhost:8000) to view it in the browser.

API will reload if you make edits.\
You will also see any lint errors in the console.

### `python manage.py makemigrations [appname]`

Creates migrations

### `python manage.py migrate [appname] [migrationname]`

Applies migrations