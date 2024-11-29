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
                    . .venv/bin/activate
                    pip install -r requirements.txt
                    export PYTHONPATH=$PYTHONPATH:$(pwd)
                '''
            }
        }

        stage('Install ChromeDriver') {
            steps {
                sh '''
                # Extraer y mover al PATH
                    unzip chromedriver_linux64.zip
                    mkdir -p $WORKSPACE/bin
                    mv chromedriver $WORKSPACE/bin/
                    chmod +x $WORKSPACE/bin/chromedriver
                    export PATH=$WORKSPACE/bin:$PATH
                '''
            }
        }

        stage('Verify WebDriver') {
            steps {
                sh '''
                    echo "Verifying WebDriver installation..."
                    which chromedriver || echo "Chromedriver not found!"
                    chromedriver --version || echo "Chromedriver version not accessible!"
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
        stage('Run Backend Test') {
            steps {
                echo "Starting Backend Test ...."
                    sh'''
                        . .venv/bin/activate
                        cd app/tests/
                        export PYTHONPATH=$PYTHONPATH:${WORKSPACE}
                        python3 backend_testing.py > Backend_testing.log 2>&1 &
                    '''
            }
        }
        stage('Run Frontend Test') {
            steps {
                echo "Starting Frontend Test ...."
                sh'''
                    . .venv/bin/activate
                    cd app/tests/
                    export PYTHONPATH=$PYTHONPATH:${WORKSPACE}
                    python3 frontend_testing.py > frontend_testing.log 2>&1 &
                '''
            }
        }
        stage('Run Combine test') {
            steps {
                echo "Starting Combine test ...."
                sh'''
                    . .venv/bin/activate
                    cd app/tests/
                    export PYTHONPATH=$PYTHONPATH:${WORKSPACE}
                    python3 combiend_testing.py > combiend_testing.log 2>&1 &
                '''
            }
        }
        stage('Run clean module') {
            steps {
                echo "Hello ...."
            }
        }
    }
}
