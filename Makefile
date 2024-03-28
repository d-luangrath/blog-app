# docker image commands
img-build:
	docker build -t blog-app:local .

img-run:
	docker run -rm blog-app:local

## docker compose commands

build: down
	docker compose build

up:
	docker compose up --remove-orphans --detach

down:
	docker compose down --remove-orphans

sh shell:
	docker compose exec app bash
