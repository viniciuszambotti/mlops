
# Desafio MLE
  

O desafio consiste em criar um modelo de machine learning e em seguida uma API que consuma esse modelo para realizar classificações.

  
  

## Tecnologias utilizadas

- Python 3.8.10

- Docker 20.10.2

- Minikube 1.22.0

- Kubeflow 1.21.3

  

## Rodando o projeto

Todos os comandos estão documentados no arquivo Makefile

  

#### Link do GCP

#### http://34.95.245.106:5000/swagger-ui/ (desativado)

  

#### Localmente

Altere os arquivos .env

	make dev

  

#### Docker local

Altere os arquivos .env

	make docker

  

#### Kubernets local usando o minikube

Altere os arquivos .env

	minikube start --driver=docker
	eval $(minikube docker-env)
	make kube-build-dev
	kubectl get pods
	kubectl port-forward {pod_id} 5000:5000 --namespace=mlops-local

  

#### Criar e subir imagem no Artifact registry no GCP

	make docker-gcloud

#### Acesse a url local: **localhost:500/swagger-ui/**

  

## Navegando nos arquivos do projeto

  

*  **Makefile**: Automatiza comandos de docker, ambiente local, kubernets e operações no GCP

*  **Dockerfile**: Configurações do container

*  **entry.sh** : Comando para iniciar gunicorn

*  **api.yaml**: Arquivo de configuração para o deploy do serviço e deployment no kubernets

*  **app/**: Local onde está o código da API

*  *  **app/app.py**: Configuração de inicialização da API, como rotas e swagger

*  *  **app/.env**: Variáveis de ambiente

*  *  **app/controller**: Lógica de negócio dos endpoints

*  *  **app/data**: Arquivos utilizados para o funcionamento da API

*  **/notebooks**: Jupyter notebooks usados na exploração e treinamento

*  *  **/notebooks/classes**: Arquivos para auxiliar no treinamento do modelo

*  *  **/notebooks/data**: Dados utilizados e gerados no treinamento/exploração

*  **scripts**: Scripts de automação