pipeline {
    agent any
    options([
        pipelineTriggers([
            pollSCM('* * * * *')
        ])
    ])
    stages {
        stage('Checkout') {
            steps {
                checkout scm: [
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/Jailer008/Flask_API_MVC'
                    ]]
                ]
            }
        }
        stage('Run Python') {
            steps {
                echo "Hello ...."
            }
        }
    }
}
