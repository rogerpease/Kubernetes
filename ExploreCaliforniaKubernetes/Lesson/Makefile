
all: 
	@echo "Specify run_website or create_kind_cluster_with_registry"

PHONY: run_website stop_website install_kind make_kind_cluster build_local_registry connect_registry_to_kind_network 

run_website: 
	docker build -t explorecalifornia.com . && \
            docker run --rm --name explorecalifornia.com -p 5000:80 explorecalifornia.com

stop_website:
	docker stop explorecalifornia.com || true 

#
# Assuming kind and kubectl are already installed since 
# class uses brew. 
#
#
#

connect_registry_to_kind_network:
	docker network connect kind local-registry || true;                                                                                                                           
connect_registry_to_kind: connect_registry_to_kind_network
	kubectl apply -f kind_configmap.yaml

#
# Starts a docker image which hosts registries locally.  
#
create_docker_registry:
	if docker ps | grep -q 'local-registry'; \
	then echo "Local registry already exists"; \
	else docker run --name local-registry -d --restart=always -p 5000:5000 registry:2; \
	fi

#
# A kind cluster runs kind daemon within a docker image. 
# 
create_kind_cluster: create_docker_registry
	kind create cluster --retain --image=kindest/node:v1.21.12 --name explorecalifornia.com --config ./kind_config.yaml || true
	kubectl get nodes 

#
# The registry needs to be connected to kind. 
#


create_kind_cluster_with_registry:
	$(MAKE) create_kind_cluster && $(MAKE) connect_registry_to_kind

delete_cluster:
	kind delete cluster --name explorecalifornia.com 

clean: stop_website delete_cluster 


# kubectl create deployment --dry-run=client --image=localhost:5000/explorecalifornia.com explorecalifornia.com --output=yaml  > deployment.yaml
#   Options: --dry-run=server 
#  docker tag explorecalifornia.com localhost:5000/explorecalifornia.com   
#    Makes sure our image is accessible by our localhost. 
#  docker push localhost:5000/explorecalifornia.com   
#   kubectl apply -f deployment.yaml 
#   kubectl get pods -l app=explorecalifornia.com 
#   kubectl port-forward deployment/explorecalifornia.com 8080:80 
# 
#  kubectl create service clusterip --dry-run=client --tcp=80:80 explorecalifornia.com --output=yaml 
#  kubectl get all -l app=explorecalifornia.com
#   kubectl port-forward service/explorecalifornia-svc 8080:80 
# Build Ingress 
#   kubectl create ingress explorecalifornia.com --rule="explorecalifornia.com/=explorecalifornia-svc:80" --dry-run=client --output=yaml > ingress.yaml
#  
