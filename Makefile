# -- CONFIGS --
APP_NAME=luiza
VERSION=latest
PORT=5000
CONFIG_FILE=api.yaml
NAMESPACE=luiza-local

##@ Run with Python
dev: dev-prep dev-run  ## Setup and start Python backend locally

dev-prep:  ## Install Python dependencies
	pip install -r requirements.txt

dev-run:  ## Start Flask backend server
	FLASK_APP=app/app.py FLASK_ENV=developement FLASK_DEBUG=True flask run


##@ Run with Docker
docker: docker-build docker-run ## Build docker image and Run the container

docker-build: ## Build Docker Image
	docker build --tag $(APP_NAME):$(VERSION) .

docker-run: ## Run Docker Container
	docker run -ti --rm -p $(PORT):5000 \
	--name $(APP_NAME) $(APP_NAME):$(VERSION)

docker-sh: ## Start Bash session in container
	docker exec -ti $(APP_NAME) bash


kube-build-dev: kube-minicube-start docker-build kube-namespace kube-create

kube-run-dev: kube-minicube-start docker-build kube-create


kube-minicube-start:
	eval $(minikube docker-env)
	minikube start --driver=docker
	
kube-namespace:
	kubectl create namespace $(NAMESPACE)

kube-create:
	kubectl create -f $(CONFIG_FILE) --namespace=$(NAMESPACE)

kube-delete:
	kubectl delete -f $(CONFIG_FILE) --namespace=$(NAMESPACE)

kube-update: kube-delete kube-create