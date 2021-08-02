# -- CONFIGS --
APP_NAME=luiza
VERSION=v2
PORT=5000
CONFIG_FILE=api.yaml
NAMESPACE=luiza-local
GCLOUD_URL=southamerica-east1-docker.pkg.dev/groovy-smithy-255116/luiza-labs/


## AMBIENTE LOCAL
dev: dev-prep dev-run 

dev-prep: 
	pip install -r requirements.txt

dev-run: 
	FLASK_APP=app/app.py FLASK_ENV=developement FLASK_DEBUG=True flask run


## DOCKER LOCAL
docker: docker-build docker-run 

docker-build: 
	docker build --tag $(APP_NAME):$(VERSION) .

docker-run: 
	docker run -ti --rm -p $(PORT):5000 \
	--name $(APP_NAME) $(APP_NAME):$(VERSION)

docker-sh: 
	docker exec -ti $(APP_NAME) bash


## KUBERNETS LOCAL
kube-build-dev: kube-minicube-start docker-build kube-namespace kube-create

kube-run-dev: kube-minicube-start docker-build kube-update

kube-minicube-start:
	minikube start --driver=docker
	eval $(minikube docker-env)
	
kube-namespace:
	kubectl create namespace $(NAMESPACE)

kube-create:
	kubectl create -f $(CONFIG_FILE) --namespace=$(NAMESPACE)

kube-delete:
	kubectl delete -f $(CONFIG_FILE) --namespace=$(NAMESPACE)

kube-update: kube-delete kube-create


## ATUALIZAR IMAGEM NO ARTIFACT REGISTRY
docker-gcloud: docker-build-gcloud docker-push-gcloud

docker-build-gcloud:
	docker build --tag $(GCLOUD_URL)$(APP_NAME):$(VERSION) .

docker-push-gcloud:
	docker push $(GCLOUD_URL)$(APP_NAME):$(VERSION)

