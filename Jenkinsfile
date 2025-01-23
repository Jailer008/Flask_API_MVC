pipeline {
    agent any
    options {
        buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20'))
        skipDefaultCheckout(true)
    }
    parameters {
        choice(name: 'TEST_MODE', choices: ['1', '2', '3'], description: 'Select test mode: 1 for Frontend, 2 for Backend, 3 for Combined')
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
                    unzip chromedriver-linux64.zip -y
                    mkdir -p $WORKSPACE/bin
                    mv chromedriver-linux64/chromedriver $WORKSPACE/bin/
                    chmod +x $WORKSPACE/bin/chromedriver
                    export PATH=$WORKSPACE/bin:$PATH
                '''
            }
        }

        stage('Run Tests Based on TEST_MODE') {
            steps {
                script {
                    echo "Selected TEST_MODE: ${params.TEST_MODE}"
                    if (params.TEST_MODE == '1') {
                        echo "Running Frontend Tests"
                        sh '''
                            . .venv/bin/activate
                            cd app/tests/
                            export PYTHONPATH=$PYTHONPATH:${WORKSPACE}
                            python3 frontend_testing.py > frontend_testing.log 2>&1
                        '''
                    } else if (params.TEST_MODE == '2') {
                        echo "Running Backend Tests"
                        sh '''
                            . .venv/bin/activate
                            cd app/tests/
                            export PYTHONPATH=$PYTHONPATH:${WORKSPACE}
                            python3 backend_testing.py > backend_testing.log 2>&1
                        '''
                    } else if (params.TEST_MODE == '3') {
                        echo "Running Combined Tests"
                        sh '''
                            . .venv/bin/activate
                            cd app/tests/
                            export PYTHONPATH=$PYTHONPATH:${WORKSPACE}
                            python3 combined_testing.py > combined_testing.log 2>&1
                        '''
                    } else {
                        error("Invalid TEST_MODE selected: ${params.TEST_MODE}")
                    }
                }
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

    post {
        failure {
            archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true
            emailext(
                subject: "Build failed: ${currentBuild.fullDisplayName}",
                body: """
                    The build has failed.
                    Check the logs here: ${BUILD_URL}
                    Logs are archived in the artifacts section.
                """,
                to: "jailer_fonseca@hotmail.com"
            )
        }
    }
}
