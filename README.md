# CI_Local

## Start Jenkins container
docker run --rm --detach -p 8888:8080 -p 50000:50000 --name jenkins --volume jenkins-docker:/var/jenkins_home --volume /var/run/docker.sock:/var/run/docker.sock jenkins-with-docker

## Start App container
docker run --name backend -p 80:80 -p 443:443 bajraktari/ci_backend_fastapi
