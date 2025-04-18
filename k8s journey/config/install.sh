#minikube

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb

minikube start --driver=docker

curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/$(uname | tr '[:upper:]' '[:lower:]')/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/


kubectl apply -f nginx-pod.yaml

kubectl get pods
kubectl describe pod mon-nginx
kubectl logs mon-nginx


kubectl port-forward pod/mon-nginx 8080:80


