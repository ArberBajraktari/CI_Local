pipeline {
    agent{  
        docker {
            image "python:3.10"
            args '-u 0'
        }
    }

    environment {
        imagename = "bajraktari/ci_backend_fastapi"
    }

    stages{
        stage("Installing dependencies"){
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
                sh "python3 python.py"
            }
        }
        stage("Build"){
            steps{
                sh "docker build -t ci_backend_fastapi ."
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