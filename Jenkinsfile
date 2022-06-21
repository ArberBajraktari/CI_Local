pipeline {
    agent any
    environment {
        imagename = "bajraktari/ci_backend_fastapi"
    }

    stages{
        stage("Installing dependencies"){
            agent{
                docker{
                    image 'python:3.10'
                }
            }
            steps{
                sh "pip install --no-cache-dir --upgrade -r requirements.txt"
            }
        }
        stage("Lint"){
            agent{
                docker{
                    image 'python:3.10'
                }
            }
            steps{
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
                sh "python3 python.py"
            }
        }
        stage("Build"){
            agent any
            steps{
                sh "docker ps"
            }
        }
        stage("Deploy"){
            steps{
                sh "docker login -u bajraktari -p $dockerhub_pwd"
                sh "docker push bajraktari/ci_frontend_flask"
            }
        }
    }
}