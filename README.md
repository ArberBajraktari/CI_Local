# CI_Local

## Start Jenkins container
docker run --rm --detach --publish 8888:8080 --publish 50000:50000 --name jenkins --volume jenkins-data:/var/jenkins_home --volume /var/run/docker.sock:/var/run/docker.sock jenkins-with-docker
