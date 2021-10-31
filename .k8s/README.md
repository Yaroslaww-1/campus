## How to run k8s
1. You need minikube installed locally. Also, you need to alias `kubectl` to `k`. Or you can just replace all `k` by `kubectl` in the following commands.
2. Enable **Ingress** addon:\
`minikube addons enable ingress`
5. Enable automatic images load to minikube. **Note: you need to run these commands in PowerShell**\
`minikube docker-env`\
`minikube docker-env | Invoke-Expression`
4. Build docker images. **Note: you need to run these commands in the same terminal**\
`docker-compose -f ../.docker/docker-compose.k8s-build.yml build`
3. Run databases\
`docker-compose -f ../.docker/docker-compose.databases.yml up -d`
7. Configure hosts to support `host.minikube.internal`: \
https://minikube.sigs.k8s.io/docs/handbook/host-access/ + https://gist.github.com/zenorocha/18b10a14b2deb214dc4ce43a2d2e2992
8. Create campus namespace:\
`kubectl create -f campus.namespace.yml`
9. Create .env folder using .env.example. Load these secrets to k8s:\
`kubectl create secret generic learn-api-secrets --from-env-file=.env/learn.env --namespace=campus-namespace`
`kubectl create secret generic users-api-secrets --from-env-file=.env/users.env --namespace=campus-namespace`
10. Run k8s:\
`kubectl apply -f frontend -f rabbitmq -f gateway-api -f users -f learn -f ingress.yml --namespace=campus-namespace`
11. Run `minikube ip` to get running service ip

## Useful commands:
1. Open minikube dashboard:\
`minikube dashboard`
2. Delete secrets:\
`kubectl delete secret learn-api-secrets --namespace=campus-namespace`
`kubectl delete secret users-api-secrets --namespace=campus-namespace`
3. Restart deployment:\
`kubectl rollout restart deployment/learn-api-deployment --namespace=campus-namespace`\
`kubectl rollout restart deployment/frontend-deployment --namespace=campus-namespace`
`kubectl -n campus-namespace rollout restart deploy`
4. Get deployment logs:\
`kubectl logs deploy/learn-api-deployment --namespace=campus-namespace`
`kubectl logs deploy/frontend-deployment --namespace=campus-namespace`
5. Delete ingress:\
`kubectl delete ingress campus-ingress`
6.
`kubectl delete --all deployments --namespace=campus-namespace`
6. Delete everything:\
`kubectl delete all --all -n campus-namespace`
