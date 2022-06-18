#!groovy

pipeline {
    agent any

    stages {
        stage('Install dependecies') {
            steps {
                sh "pip install -r requirements.txt "
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}