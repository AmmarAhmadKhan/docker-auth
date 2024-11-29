# FastAPI Auth APIs

A backend for Auth Service

## Running the Application with Docker Compose

1. Build and start the containers:
   ```sh
   docker compose up --build
   ```

2. Stop the containers:
   ```sh
   docker compose down
   ```

3. To rebuild the containers without using cache:
   ```sh
   docker compose build --no-cache
   ```

## Notes
- The API runs on port `8000`.
- Authentication is handled using JWT tokens.
- Docker Compose is used to manage services and environments.
