# Getting Started with Campus backend

This project was bootstrapped with django.

## Technologies explanation
### Backend
- [Django](https://www.djangoproject.com/) - main library.
- [Django REST Framework](https://www.django-rest-framework.org/) - useful addition to the default django functionality.
- Inject - dependency injection

**Note:** all packages can be restored from the **requirements.txt** in the root of any service.

## Files structure explanation **IMPORTANT!**
0. All services are fully separated and located in **services/** folder.
1. We use DDD with CQRS. Good example could be found [here](https://breadcrumbscollector.tech/the-clean-architecture-in-python-how-to-write-testable-and-flexible-code/).
2. **api/** contains api config and django settings. Changed rarely.
3. **service-name/** (for example **learn/**) - main code
    1. **api/** contains all routes and api related features like error handlers, controllers (views), serializers.
    2. **domain/** is a core folder. 
        1. **Entity** = [domain entity](https://khalilstemmler.com/articles/typescript-domain-driven-design/entities/), pure python class with methods. **IS NOT THE SAME AS A DATABASE ENTITY**.
        2. **Value object** = immutable entity. We reconstruct value object every it changed. A good example is a Age value object. We may need some additional methods for a Age (for example `add_days`) but do not want to overflow entity with it
    3. **infrastructure/** contains all external connections. For example database or mailer adapter.
        1. **Repository** = database connection with query/update methods. **RETURNS DOMAIN ENTITY**.
    4. **application/** contains Queries, Commands and Dtos
        1. **Query** = query data
        2. **Command** = update, delete, modify data
        3. **Dto** = object returned from commands and queries
    5. **migrations/** contains migrations [Why do we need it](https://www.prisma.io/dataguide/types/relational/what-are-database-migrations#what-are-database-migrations) - you need only "What are database migrations?" paragraph

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

## How to run
1. Create **.env** folder with env files from **.env.example**.
2. Start **docker-compose** file using command \
`docker-compose -f .docker/docker-compose.services.yml up`
3. Run migrations using command \
`python manage.py migrate`
4. Restore required packages from **requirements.txt**
5. `python manage.py runserver`

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

### `python manage.py seed`

Applies seed