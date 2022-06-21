pipeline {
    agent{  
        docker {
            image "python:3.10"
            args '-u 0'
        }
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
                sh "python3 python.py"
            }
        }
        stage("Deploy"){
            steps{
                sh "python3 python.py"
            }
        }
    }
}