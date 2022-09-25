pipeline {
    agent { docker { image 'python:3.10' } }
    environment {
        imagename = "bajraktari/ci_backend_fastapi"
        dockerhub_usr = "bajraktari"
        dockerhub_pwd = credentials("dockerhub_pwd")
        branch_name = "${env.GIT_BRANCH}"
    }
    stages {
        stage('dependencies') {
            steps {
                sh "pip install --no-cache-dir --upgrade -r requirements.txt"
            }
        }
        stage('lint'){
            steps{
                sh "pycodestyle app"
            }
        }
        stage('test'){
            steps{
                sh "pytest app"   
            }
        }
        stage('build'){
            steps{
                echo "building..."   
            }
        }
        stage('deploy'){
            steps{
                echo "deploying ..."   
            }
        }
    }
}
