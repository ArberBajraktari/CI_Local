pipeline {
    agent any
    stages{
        stage("test"){
            agent{  
                docker {
                    image "pypy"
                }
            }
            steps{
                sh "echo hello"
            }
        }
    }
}