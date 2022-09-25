pipeline {
    agent any
    environment {
        imagename = "bajraktari/ci_backend_fastapi"
        dockerhub_usr = credentials("dockerhub_username")
        dockerhub_pwd = credentials("dockerhub_pwd")
        branch_name = "${env.GIT_BRANCH}"
    }
    stages {
        stage('lint') {
            agent { docker { image 'python:3.10' } }
            steps {
                sh "pip install --no-cache-dir --upgrade -r requirements.txt"
                sh "pycodestyle app"
            }
        }
        stage('test'){
            agent { docker { image 'python:3.10' } }
            steps {
                sh "pip install --no-cache-dir --upgrade -r requirements.txt"
                sh "pytest app"   
            }
        }
        stage('build'){
            steps{
                sh "docker build -t $imagename ."
            }
        }
        stage('deploy'){
            steps{
                echo "deploying ..."   
            }
        }
    }
}
