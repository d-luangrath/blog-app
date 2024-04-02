## docker compose commands

build: down
	docker compose build

up:
	docker compose up --remove-orphans --detach

down:
	docker compose down --remove-orphans

restart: down up

sh shell:
	docker compose exec app bash

logs:
	docker compose logs -f --tail 100 --timestamps

db-shell:
	docker compose exec postgres psql -h 0.0.0.0 -p 5432 -d mydb -U myuser

migrations:
	docker compose exec app python manage.py makemigrations

migrate: migrations
	docker compose exec app python manage.py migrate

# docker image commands
img-build:
	docker build -t blog-app:local .

img-run:
	docker run \
		--rm \
		-p 8000:8000 \
		-e DB_NAME=mydb \
		-e DB_USER=myuser \
		-e DB_PASSWORD=mysecretpassword \
		-e DB_HOST=192.168.144.1 \
	 blog-app:local