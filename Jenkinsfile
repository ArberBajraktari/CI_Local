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
                sh "print('ckemi')"
            }
        }
    }
}