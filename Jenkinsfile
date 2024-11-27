pipeline {
    agent any
    options {
        skipDefaultCheckout(true) // Skip default checkout if using explicit `checkout` step
    }
    triggers {
        pollSCM('* * * * *') // Poll every 5 minutes
    }
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
