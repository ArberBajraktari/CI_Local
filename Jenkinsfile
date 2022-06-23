pipeline {
   agent { 
        docker {
            image "python:3.10"
            args '-u root -p 8081:8081 -v /var/run/docker.sock:/var/run/docker.sock  '
        }
    }
    environment {
        imagename = "bajraktari/ci_backend_fastapi"
        dockerhub_usr = "bajraktari"
        dockerhub_pwd = credentials("dockerhub_pwd")
        branch_name = "${env.GIT_BRANCH}"
        dockerHome = tool 'docker'
        ${env.PATH} = "${dockerHome}/bin:${env.PATH}"
    }

    stages{
        stage("Dependencies"){
            steps{
                sh "pip install --no-cache-dir --upgrade -r requirements.txt"
            }
        }
        stage("Lint"){
            steps{
                sh "pycodestyle app"
            }
        }
        stage("Test"){
            steps{
                sh "pytest app"
            }
        }
        stage("Build"){
            agent{
                docker{
                    image "docker"
                }
            }
            steps{
                sh "docker build -t $imagename ."
            }
        }
        stage("Deploy"){
            agent{
                docker{
                    image "docker"
                }
            }
            when{
                branch "master"
            }
            steps{
                sh "docker login -u $dockerhub_usr -p $dockerhub_pwd"
                sh "docker push $imagename"
            }
        }
    }
}