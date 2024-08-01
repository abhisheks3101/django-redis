# Django Redis Caching Project

This project demonstrates the use of Redis for caching in a Django application.

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/abhisheks3101/django-redis-caching.git
    cd django-redis-caching
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the requirements**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Redis**:
    Ensure Redis is installed and running on your machine. You can start Redis with:
    ```bash
    redis-server
    ```

5. **Run Django**:
    Apply migrations and start the Django development server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

## Caching with Redis

This project uses the `django-redis` package to implement Redis as a caching backend in Django.

## License

This project is licensed under the MIT License.
