
.PHONY: test_program test_docker clean create_docker_registry

nothing:
	@echo make deployment or clean 

clean:
	docker rm helloworld_container || true
	docker rmi hellow_versioned_image:0.1.0 || true 
	docker rmi hellow_versioned_image:0.2.0 || true 
	kubectl delete deployment hellowvers || true 
	kubectl delete service hellowvers || true 
	minikube stop || true 

build_docker: create_docker_registry
	docker build -t hellow_versioned_image:0.1.0 HelloWorldV1
	docker build -t hellow_versioned_image:0.2.0 HelloWorldV2
	@echo "If these pushes error out you may need to do a docker login" 
	docker tag hellow_versioned_image:0.1.0 rogerpease/hellow_versioned_image:0.1.0 || true
	docker push rogerpease/hellow_versioned_image:0.1.0 || true
	docker tag hellow_versioned_image:0.2.0 rogerpease/hellow_versioned_image:0.2.0 || true
	docker push rogerpease/hellow_versioned_image:0.2.0 || true


create_docker_registry:
	if docker ps | grep -q 'local-registry'; \
	then echo "Local registry already exists"; \
	else docker run --name local-registry -d --restart=always -p 5000:5000 registry:2; \
	fi




deployment: build_docker
	minikube start || true 
	minikube status 
	# For any of these commands you could do:
	#  kubectl create <...> -dry-run=client --output=yaml > <...>.yaml        
	#  massage the yaml, then do
	#  kubectl apply -f <...>.yaml 
#	kubectl create deployment hellowvers --image=rogerpease/hellow_versioned_image:0.1.0 --replicas=3 --dry-run=client -o yaml > deployment.yaml
	kubectl apply -f deployment.yaml        
#	kubectl expose deployment hellowvers --type=NodePort --port=8080 --dry-run=client -o yaml > service.yaml
	kubectl apply -f service.yaml        
	@echo "Sleeping" 
	sleep 15
	@echo "Run this: kubectl port-forward service/hellowvers 8080:8080" 
	@echo "Then from another window: wget -q -O - 127.0.0.1:8080"
	@echo "This should reply       : Hello Roger" 
	@echo " We updated deployment to set container name to hellow-versioned. So we can do this now:" 
	@echo "kubectl set image deployment.apps/hellowvers hellow-versioned=rogerpease/hellow_versioned_image:0.2.0"


#
#	kubectl get pods -o wide 
#	kubectl cluster-info 
#	kubectl get services
#       kubectl get pods --show-labels                # shows labels 
#       kubectl set image deployment 
