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
    }
}
