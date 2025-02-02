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

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image..."
                sh '''
                    docker build -t myflask:${BUILD_NUMBER} .
                    docker run -d --name my-flask -v $(pwd)/logs:/app/logs -p 5000:5000 myflask:${BUILD_NUMBER}
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing Docker Image..."
                sh '''

                '''
            }
        }

        stage('Clean Docker Image') {
            steps {
                echo "Cleaning Docker Image..."
                sh '''
                    docker kill my-flask
                    docker rm my-flask
                '''
            }
        }

        stage('Set Image Version') {
            steps {
                echo "Setting Image Version..."
                sh """
                    sed -i 's/^IMAGE_TAG=.*/IMAGE_TAG=${BUILD_NUMBER}/' .env
                """
            }
        }


        stage('Run Docker-compose') {
            steps {
                echo "Running Docker-compose..."
                sh '''
                    docker-compose up --build -d
                '''
            }
        }

        stage('Test dockerized app') {
            steps {
                echo "Testing dockerized app..."
                sh '''
                    docker exec flask-api python3 app/tests/backend_testing.py
                '''
            }
        }

        stage('Clean docker-compose') {
            steps {
                echo "Cleaning docker-compose environment..."
                sh '''
                    docker kill flask-api
                    docker kill mysql-container
                    docker rm mysql-container
                    docker rm flask-api
                '''
            }
        }
    }
}
