# -- CONFIGS --
APP_NAME=luiza
VERSION=v2
PORT=5000
CONFIG_FILE=api.yaml
NAMESPACE=luiza-local
GCLOUD_URL=southamerica-east1-docker.pkg.dev/groovy-smithy-255116/luiza-labs/


## AMBIENTE LOCAL
dev: dev-prep dev-run 

dev-prep: # instala bibliotecas locais
	pip install -r requirements.txt


dev-run: # roda o app flask na porta 5000
	FLASK_APP=app/app.py FLASK_ENV=developement FLASK_DEBUG=True flask run


## DOCKER LOCAL
docker: docker-build docker-run 


docker-build: # constroi a imagem Docker
	docker build --tag $(APP_NAME):$(VERSION) .

docker-run: # Roda a imagem Docker na porta 5000
	docker run -ti --rm -p $(PORT):5000 \
	--name $(APP_NAME) $(APP_NAME):$(VERSION)

docker-sh: # acessa o container
	docker exec -ti $(APP_NAME) bash


## KUBERNETS LOCAL
kube-build-dev: kube-minicube-start docker-build kube-namespace kube-create

kube-run-dev: kube-minicube-start docker-build kube-update

kube-minicube-start: # inicia o minikube
	minikube start --driver=docker
	eval $(minikube docker-env)
	
kube-namespace: # Cria um namespace
	kubectl create namespace $(NAMESPACE)

kube-create: # Cria o deployment/pods
	kubectl create -f $(CONFIG_FILE) --namespace=$(NAMESPACE)

kube-delete: # Deleta  deployment/pods
	kubectl delete -f $(CONFIG_FILE) --namespace=$(NAMESPACE)

kube-update: kube-delete kube-create


## ATUALIZAR IMAGEM NO ARTIFACT REGISTRY
docker-gcloud: docker-build-gcloud docker-push-gcloud

docker-build-gcloud: # Cria imagem para o GCP
	docker build --tag $(GCLOUD_URL)$(APP_NAME):$(VERSION) .

docker-push-gcloud: # Manda a imagem para o Artifact registry
	docker push $(GCLOUD_URL)$(APP_NAME):$(VERSION)

