eval $(minikube docker-env)

docker build -t php-app:1.0 .

kubectl apply -f k8s/php-deployment.yaml

kubectl apply -f k8s/service-php.yaml

kubectl apply -f k8s/service-mysql.yaml

