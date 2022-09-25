pipeline {
    agent { docker { image 'python:3.10' } }
    stages {
        stage('lint') {
            steps {
                sh "pip install --no-cache-dir --upgrade -r requirements.txt"
                sh "pycodestyle app"
            }
        }
    }
}
