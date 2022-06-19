pipeline {
    agent any
    stages{
        stage("test"){
            agent{  
                docker {
                    image "python:3.10"
                }
            }
            steps{
                sh "python python.py"
            }
        }
    }
}