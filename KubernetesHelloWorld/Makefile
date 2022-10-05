
.PHONY: test_program test_docker clean create_docker_registry

nothing:
	@echo make test_app or make deployment_image 

clean:
	docker rm helloworld_container || true
	docker rmi helloworld_image:0.1.0 || true 
	minikube stop 

test_app:
	FLASK_APP=HelloWorldApp.py FLASK_ENV=development flask run 

build_docker: 
	docker build -t helloworld_image:0.1.0 .

test_docker: build_docker
	docker run --rm -e FLASK_APP=HelloWorld.py -e FLASK_ENV=development  --name helloworld_container -p 8080:8080 rogerpease/helloworld_image:0.1.0 

#
# This one is daemonized un
#
create_docker_registry:
	if docker ps | grep -q 'local-registry'; \
	then echo "Local registry already exists"; \
	else docker run --name local-registry -d --restart=always -p 5000:5000 registry:2; \
	fi


#
# This essentially spins (you guessed it) Virtual machines to act as nodes. 
#
create_minikube_cluster: build_docker create_docker_registry
	minikube start || true 
	minikube status 


publish_docker_image: create_minikube_cluster
	@echo "If this errors out you may need to do a docker login" 
	docker tag helloworld_image:0.1.0 rogerpease/helloworld_image:0.1.0 || true
	docker push rogerpease/helloworld_image:0.1.0 || true

deployment_image: publish_docker_image 
	kubectl create deployment helloroger --image=rogerpease/helloworld_image:0.1.0
	kubectl expose deployment helloroger --type=NodePort --port=8080
	@echo "Sleeping" 
	sleep 15
	@echo "Run this: kubectl port-forward service/hello-minikube 8080:8080" 
	@echo "Then from another window: wget 127.0.0.1:8080                  " 



deployment_info: 
	kubectl get pods -o wide 
	kubectl cluster-info 
	kubectl get services
