pipeline {
    agent{  
        docker {
            image "python:3.10"
            args '-u 0'
        }
    }
    stages{
        stage("test"){
            steps{
                sh "python3 python.py"
            }
        }
    }
}