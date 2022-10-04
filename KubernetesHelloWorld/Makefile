
.PHONY: test_program test_docker clean create_docker_registry


clean:
	docker rm helloworld_container || true
	docker rmi helloworld_image

test_app:
	FLASK_APP=HelloWorldApp.py FLASK_ENV=development flask run 


test_docker:
	docker build -t helloworld_image . && \
            docker run --rm -e FLASK_APP=HelloWorld.py -e FLASK_ENV=development  --name helloworld_container -p 5000:5000 helloworld_image 

#
# This one is daemonized un
#
create_docker_registry:
	if docker ps | grep -q 'local-registry'; \
	then echo "Local registry already exists"; \
	else docker run --name local-registry -d --restart=always -p 5000:5000 registry:2; \
	fi
