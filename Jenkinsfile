pipeline {
   agent { 
        docker {
            image "python:3.10"
        }
    }
    environment {
        imagename = "bajraktari/ci_backend_fastapi"
        dockerhub_usr = "bajraktari"
        dockerhub_pwd = credentials("dockerhub_pwd")
        branch_name = "${env.GIT_BRANCH}"
    }

    stages{
        stage("Lint"){
            steps{
                sh "pip install --no-cache-dir --upgrade -r requirements.txt"
                sh "pycodestyle app"
            }
        }
        stage("Test"){
            steps{
                sh "pip install --no-cache-dir --upgrade -r requirements.txt"
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