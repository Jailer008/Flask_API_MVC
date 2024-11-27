pipeline {
    agent any
    options {
        buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20'))
        skipDefaultCheckout(true) // Skip default checkout if using explicit `checkout` step
    }
    triggers {
        pollSCM('* * * * *') // Poll every 1 minutes
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
        stage('Run Backend server') {
            steps {
                echo "Starting server ...."
                echo "El espacio de trabajo es: ${env.WORKSPACE}"
                sh "nohup python3 run.py > server.log 2>&1 &"
            }
        }
         stage('Run Frontend server') {
            steps {
                echo "Hello ...."
            }
        }
        stage('Run Backend test') {
            steps {
                echo "Hello ...."
            }
        }
        stage('Run Frontend test') {
            steps {
                echo "Hello ...."
            }
        }
        stage('Run Combine test') {
            steps {
                echo "Hello ...."
            }
        }
        stage('Run clean module') {
            steps {
                echo "Hello ...."
            }
        }
    }
}
