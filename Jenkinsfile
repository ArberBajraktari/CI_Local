pipeline {
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