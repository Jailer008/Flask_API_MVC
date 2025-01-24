pipeline {
    agent any
    options {
        buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20'))
        skipDefaultCheckout(true)
    }
    triggers {
        pollSCM('* * * * *') // Poll every 1 minutes
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/docker-jenkins-integration']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/Jailer008/Flask_API_MVC'
                    ]]
                ])
            }
        }

        stage('Setup virtual environment') {
            steps {
                echo "Setting up virtual environment ...."
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                    export PYTHONPATH=$PYTHONPATH:$(pwd)
                '''
            }
        }

        stage('Install ChromeDriver') {
            steps {
                echo "Installing ChromeDriver ...."
                sh '''
                    unzip -o chromedriver-linux64.zip
                    mkdir -p $WORKSPACE/bin
                    mv chromedriver-linux64/chromedriver $WORKSPACE/bin/
                    chmod +x $WORKSPACE/bin/chromedriver
                    export PATH=$WORKSPACE/bin:$PATH
                '''
            }
        }

        stage('Run Backend server') {
            steps {
                echo "Starting backend server ...."
                sh'''
                    . .venv/bin/activate
                    export PYTHONPATH=$PYTHONPATH:${WORKSPACE}
                    nohup python3 run.py > server_backend.log 2>&1 &
                '''

            }
        }

         stage('Run Frontend server') {
            steps {
                echo "Starting frontend server ...."
                sh'''
                    . .venv/bin/activate
                    cd app/web/
                    export PYTHONPATH=$PYTHONPATH:${WORKSPACE}
                    nohup   python3 web_api.py > server_frontend.log 2>&1 &
                '''
            }
        }

        stage('Run Backend Tests') {
            steps {
                echo "Running Backend Tests"
                sh '''
                    . .venv/bin/activate
                    cd app/tests/
                    export PYTHONPATH=$PYTHONPATH:${WORKSPACE}
                    python3 backend_testing.py > backend_testing.log 2>&1
                '''
            }
        }

        stage('Cleanup') {
            steps {
                echo "Stopping background processes..."
                sh '''
                    pkill -f "python3 run.py"
                    pkill -f "python3 web_api.py"
                '''
            }
        }
    }
}
