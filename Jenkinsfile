pipeline {
    agent any
    properties([
        pipelineTriggers([
            pollSCM('*/5 * * * *')
        ])
    ])
    stages {
        stage('Checkout') {
            steps {
                checkout scm: [
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/Jailer008/Flask_API_MVC',
                    ]]
                ]
            }
        }
        stage('Run Python') {
            steps {
                sh 'python3 script.py'
            }
        }
    }
}