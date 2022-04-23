VERSION_PROD=v0.0.1
VERSION_DEV=latest
DOCKER_FILE_DEV=dev.Dockerfile
CONTAINER_NAME=django
IMAGE_NAME=felipe6659/orbita
DOCKER_COMPOSE_DEV=docker-compose.dev.yml
DOCKER_COMPOSE_DEV_BD=docker-compose.dev.db.yml

## @ Start project
.PHONY: install up_all down_all
install: build_image up_all reset_passwords ## Gera a imagem do back-end e sobe TODOS os containers do projeto

up_all: up_infra_dev ## Sobe TODOS os containers do projeto

down_all: down_infra_dev down_plataforma ## Para TODOS os containers do projeto


## @ Django
.PHONY: up down bash logs build_image build_image_push build build_migrate
up: ## Sobe o container do orbita na porta 8000
	docker-compose -f $(DOCKER_COMPOSE_DEV) up -d --force-recreate

down: ## Para o container do orbita
	docker-compose -f $(DOCKER_COMPOSE_DEV) down --remove-orphans

build:  ## Instala oo pacotes contidos em requirements.txt e realiza o migrate
	docker exec -i ${CONTAINER_NAME} sh -c 'python3 -m pip install --no-cache-dir -r requirements.dev.txt'
	docker exec -i ${CONTAINER_NAME} sh -c 'python3 manage.py sync_roles'
	docker exec -i ${CONTAINER_NAME} sh -c 'python3 manage.py migrate'

build_migrate:   ## Roda o makemigrations e o migrate
	docker exec -i ${CONTAINER} sh -c 'python3 -m pip install --no-cache-dir -r requirements.txt'
	docker exec -i ${CONTAINER} sh -c 'python3 manage.py sync_roles'
	docker exec -i ${CONTAINER} sh -c 'python3 manage.py makemigrations'
	docker exec -i ${CONTAINER} sh -c 'python3 manage.py migrate'

build_image:  ## Gera a imagem do backend
	docker build -t $(IMAGE_NAME):$(VERSION_DEV) -f ${DOCKER_FILE_DEV} .

build_image_push:  ## Gera a imagem do backend e sobe para o dockerhub
	docker login 
	docker build -t $(IMAGE_NAME):$(VERSION_DEV) -f ${DOCKER_FILE_DEV} .
	docker push $(IMAGE_NAME):$(VERSION_DEV)

bash: ## Abre o bash de dentro do container backend
	docker exec -it ${CONTAINER_NAME} /bin/bash

logs: ## Lista todos os logs do dango
	docker logs  ${CONTAINER_NAME}  -f --tail=100

reset_passwords: ## Criar um admin no dango
	docker exec -i ${CONTAINER_NAME} sh -c "python reset_passwords.dev.py"


## @ Database
.PHONY: up_db down_db logs_db



