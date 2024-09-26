# Location-Vehicle

## Project Description

This project is a web application developed with Django. Developments will continue.

## Installation

### Requirements

- Docker
- Docker Compose

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/numpyasnp/iett_task.git
    cd iett_task
    ```

2. Build Docker images and start containers:
    ```bash
    docker compose up -d --build
    ```

3. Restore db dump
   ```bash
    docker cp <path>/iett.backup postgres_db:/.
    ```
   if your os mac/linux you can use this command:
   ```bash
    docker cp "$(pwd)/iett.backup" postgres_db:/.
    ```

4. Bash on Postgres:
    ```bash
    docker exec -it postgres_db bash
    ```
5. Execute pg_restore command for restore db backup:
    ```bash
    pg_restore -U postgres -d postgres ./iett.backup
    ```

6. If you restore db backup you can skip this step!! Run database migrations:
    ```bash
    docker exec -it iett_vehicle_tracking python manage.py migrate
    ```

7. Create a superuser:
    ```bash
    docker exec -it iett_vehicle_tracking python manage.py createsuperuser
    ```

8. The application will be running at [http://127.0.0.1:8000](http://localhost:8000).

9. Api: Redoc Api [http://127.0.0.1:8000/api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/)


## Usage

The project includes the following main models:
- `Driver`: Driver of Vehicle.
- `Location`: Location about the Vehicle.
- `Vehicle`: The Vehicle.


## Contributing

1. Fork this repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to your branch: `git push origin feature/your-feature`
5. Submit a pull request.

## License

This project is licensed under the **MIT License** - see the `LICE
