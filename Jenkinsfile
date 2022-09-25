pipeline {
    agent { docker { image 'python:3.10' } }
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
