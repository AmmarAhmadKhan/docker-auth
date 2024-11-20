# Makefile for Docker Deployment

.PHONY: build-and-deploy build-only build-no-cache compose-up compose-down

# Build and deploy the system
build-and-deploy:
	docker compose up --build -d

# Build the Docker images only
build-only:
	docker compose build

# Build the Docker images without using the cache
build-no-cache:
	docker compose build --no-cache

# Start the containers using Docker Compose
compose-up:
	docker compose up -d

# Stop and remove the containers using Docker Compose
down:
	docker compose down
