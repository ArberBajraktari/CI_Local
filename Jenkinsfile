pipeline {
    agent any
    environment {
        imagename = "bajraktari/ci_backend_fastapi"
        dockerhub_usr = "bajraktari"
        dockerhub_pwd = credentials("dockerhub_pwd")
    }

    stages{
        stage("Lint"){
            agent{
                docker{
                    image 'python:3.10'
                }
            }
            steps{
                sh "pip install --no-cache-dir --upgrade -r requirements.txt"
                sh "pycodestyle app"
            }
        }
        stage("Test"){
            agent{
                docker{
                    image 'python:3.10'
                }
            }
            steps{
                sh "pip install --no-cache-dir --upgrade -r requirements.txt"
                sh "python3 python.py"
            }
        }
        stage("Build"){
            steps{
                sh "docker build -t $imagename ."
            }
        }
        stage("Deploy"){
            steps{
                sh "docker login -u $dockerhub_usr -p $dockerhub_pwd"
                sh "docker push $imagename"
            }
        }
    }
}