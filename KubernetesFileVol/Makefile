#
# How to update pods 
#


.PHONY: test_program test_docker clean create_docker_registry

nothing:
	@echo make deployment or clean 

clean: cleankube cleandocker 

cleandocker:
	docker rm helloworld_container || true
	docker rmi hellow_filesys_image  || true 
	docker rmi rogerpease/hellow_filesys_image:0.1.1 || true 

cleankube:
	kubectl delete deployment hellowfilesys || true 
	kubectl delete pod hellowfilesyspod || true 
	kubectl delete service hellowfilesys || true 
	kubectl delete pvc minikube-pvc || true 
	kubectl delete pv minikube-pv || true 

build_docker: create_docker_registry
	docker build -t hellow_filesys_image:0.1.3 HelloWorldV1
	@echo "If these pushes error out you may need to do a docker login" 
	docker tag hellow_filesys_image:0.1.3 rogerpease/hellow_filesys_image:0.1.3 || true
	docker push rogerpease/hellow_filesys_image:0.1.3 || true


create_docker_registry:
	if docker ps | grep -q 'local-registry'; \
	then echo "Local registry already exists"; \
	else docker run --name local-registry -d --restart=always -p 5000:5000 registry:2; \
	fi




deployment: 
	@echo "If you get any errors about missing images do build_docker" 
	# For any of these commands you could do:
	#  kubectl create <...> -dry-run=client --output=yaml > <...>.yaml        
	#  massage the yaml, then do
	#  kubectl apply -f <...>.yaml 
#	kubectl create deployment hellowfilesys --image=rogerpease/hellow_filesys_image:0.1.0 --replicas=3 --dry-run=client -o yaml > deployment.yaml
	kubectl apply -f persistentvolume.yaml        
	kubectl apply -f persistentvolumeclaim.yaml        
	kubectl apply -f deployment.yaml        
	kubectl apply -f service.yaml        
	@echo "Run this: kubectl port-forward service/hellowfilesys 9000:9000" 
	@echo "Then from another window: wget -q -O - 127.0.0.1:9000"
	@echo "This should reply      {\"version\": \"0.1.1\", text: "what.is.in./Kube/File.txt"}  " 


#
#	kubectl get pods -o wide 
#	kubectl cluster-info 
#	kubectl get services
#       kubectl get pods --show-labels                # shows labels 
#       kubectl set image deployment 
#  kubectl get pods 
# kubectl exec --stdin --tty hellowfilesys-9c64ccfb9-mp24c -- "bash"
#
# 
# LoginKube.py  -- to log into kube 
