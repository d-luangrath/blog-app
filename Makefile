# docker image commands
img-build:
	docker build -t blog-app:local .

img-run:
	docker run --rm -p 8000:8000 blog-app:local

## docker compose commands

build: down
	docker compose build

up:
	docker compose up --remove-orphans --detach

down:
	docker compose down --remove-orphans

sh shell:
	docker compose exec app bash

logs:
	docker compose logs -f --tail 100 --timestamps app