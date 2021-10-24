## How to run k8s
1. You need minikube installed locally. Also, you need to alias `kubectl` to `k`. Or you can just replace all `k` by `kubectl` in the following commands.
2. Enable **Ingress** addon:\
`minikube addons enable ingress`
2. Build docker images\
`docker-compose -f .\docker-compose.k8s-build.yml up --build`
3. Optional. Tag docker images with versions (replace `version` by version **number** (for example 0.0.1)\
`docker tag docker_campus_learn_api docker_campus_learn_api:version`\
`docker tag docker_campus_frontend docker_campus_frontend:version`
4. Load images to minikube: (you can specify version instead of latest)\
`minikube image load docker_campus_learn_api:latest`\
`minikube image load docker_campus_frontend:latest`
5. Run database locally\
`docker-compose -f docker-compose.services.yml up`
6. Configure hosts to support `host.minikube.internal`: \
https://minikube.sigs.k8s.io/docs/handbook/host-access/ + https://gist.github.com/zenorocha/18b10a14b2deb214dc4ce43a2d2e2992
7. Create campus namespace:\
`k create -f campus.namespace.yml`
8. Create .env folder using .env.example. Load these secrets to k8s:\
`k create secret generic learn-api-secrets --from-env-file=.env/learn.env --namespace=campus-namespace`
9. Run k8s:\
`k apply -f frontend -f learn -f minikube-host.service.yml -f ingress.yml --namespace=campus-namespace`
10. Run `minikube ip` to get running service ip

## Useful commands:
1. Open minikube dashboard:\
`minikube dashboard`
2. Delete secrets:\
`k delete secret learn-api-secrets --namespace=campus-namespace`
3. Restart deployment:\
`k rollout restart deployment/learn-api-deployment --namespace=campus-namespace`\
`k rollout restart deployment/frontend-deployment --namespace=campus-namespace`
4. Get deployment logs:\
`k logs deploy/learn-api-deployment --namespace=campus-namespace`
5. Delete ingress:\
`k delete ingress campus-ingress`
6. Delete everything:\
`k delete all --all -n campus-namespace`
