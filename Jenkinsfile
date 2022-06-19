pipeline {
    agent any
    stages{
        stage("test"){
            agent{  
                docker {
                    image "python:3.10"
                    args '-u 0'
                }
            }
            steps{
                sh "python3 --version"
            }
        }
    }
}