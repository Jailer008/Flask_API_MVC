pipeline {
    agent any
    properties([
        pipelineTriggers([
            pollSCM('* * * * *')
        ])
    ])
    options([
        timestamps(),    // Adds timestamps to log output
        timeout(time: 1, unit: 'MINUTES') // Sets a timeout for the pipeline
    ])
    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/Jailer008/Flask_API_MVC'
                    ]]
                ])
            }
        }
        stage('Run Python') {
            steps {
                echo "Hello ...."
            }
        }
    }
}
