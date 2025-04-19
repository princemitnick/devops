"""
✅ Contenu inclus :
	•	php/ : ton app PHP (formulaire + connexion MySQL)
	•	mysql-init/ : script d’initialisation SQL
	•	Dockerfile : pour builder l’image PHP
	•	k8s/ : les fichiers YAML pour les 8 étapes :


Fichier
Ã‰tape couverte
php-deployment.yaml
DÃ©ploiement app PHP
mysql-deployment.yaml
DÃ©ploiement MySQL + volume
service-php.yaml
Service interne PHP
service-mysql.yaml
Service interne MySQL
configmap.yaml
Configuration app (ex : nom de la base)
secrets.yaml
Credentials (user/pass DB)
ingress.yaml
Ingress Controller avec nom de domaine local
(Ã  venir)
Monitoring (Prometheus) + CI GitHub Actions
"""

eval $(minikube docker-env)

docker build -t php-app:1.0 .

kubectl apply -f k8s/php-deployment.yaml

kubectl apply -f k8s/service-php.yaml

kubectl apply -f k8s/service-mysql.yaml


minikube addons enable ingress

sudo nano /etc/hosts
#<minikube-ip>    php.local

kubectl apply -f k8s/ingress.yaml

