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
        stage('Setup virtual environment'){
            steps{
                echo "Setting up virtual environment ...."
                sh '''
                    python3 -m venv .venv
                    pip install -r requirements.txt
                    export PYTHONPATH=$PYTHONPATH:$(pwd)
                '''
            }
        }
        stage('Run Backend server') {
            steps {
                echo "Starting backend server ...."
                sh "nohup python3 run.py > server_backend.log 2>&1 &"
            }
        }
         stage('Run Frontend server') {
            steps {
                echo "Starting frontend server ...."
                dir("${env.WORKSPACE}/app/web/"){
                    sh "nohup python3 web_api.py > server_frontend.log 2>&1 &"
                }

            }
        }
        stage('Run Backend test') {
            steps {
                echo "Starting frontend server ...."
                dir("${env.WORKSPACE}/app/tests/"){
                    sh "python3 backend_testing.py > backend_testing.log 2>&1 &"
                }
            }
        }
        stage('Run Frontend test') {
            steps {
                echo "Starting frontend server ...."
                dir("${env.WORKSPACE}/app/tests/"){
                    sh "python3 frontend_testing.py > frontend_testing.log 2>&1 &"
                }
            }
        }
        stage('Run Combine test') {
            steps {
                echo "Starting frontend server ...."
                dir("${env.WORKSPACE}/app/tests/"){
                    sh "python3 combiend_testing.py > combiend_testing.log 2>&1 &"
                }
            }
        }
        stage('Run clean module') {
            steps {
                echo "Hello ...."
            }
        }
    }
}
