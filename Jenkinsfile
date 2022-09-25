pipeline {
    agent { docker { image 'python:3.10' } }
    stages {
        
        stage('lint'){
            steps{
                sh "pycodestyle app"
            }
        }
    }
}
