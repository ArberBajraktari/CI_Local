pipeline {
    agent any
    environment {
        imagename = "bajraktari/ci_backend_fastapi"
    }

    stages{
        // stage("Installing dependencies"){
        //     agent{
        //         docker{
        //             image 'python:3.10'
        //         }
        //     }
        //     steps{
        //         sh "pip install --no-cache-dir --upgrade -r requirements.txt"
        //     }
        // }
        // stage("Lint"){
        //     agent{
        //         docker{
        //             image 'python:3.10'
        //         }
        //     }
        //     steps{
        //         sh "pycodestyle app"
        //     }
        // }
        // stage("Test"){
        //     agent{
        //         docker{
        //             image 'python:3.10'
        //         }
        //     }
        //     steps{
        //         sh "python3 python.py"
        //     }
        // }
        stage("Build"){
            steps{
                sh "docker build -t bajraktari/ci_backend_fastapi ."
            }
        }
        stage("Deploy"){
            steps{
                sh "docker login -u bajraktari -p Bajrak!10"
                sh "docker push bajraktari/ci_backend_fastapi"
            }
        }
    }
}