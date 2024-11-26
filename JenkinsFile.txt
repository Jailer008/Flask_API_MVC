pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git 'https://github.com/Jailer008/Flask_API_MVC'
            }
        }
        stage('run python') {
            steps {
                script {
                    echo 'Hello'
                }
            }
        }
    }
}