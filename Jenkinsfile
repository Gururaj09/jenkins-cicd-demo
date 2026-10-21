pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh '''
                    python -m venv venv
                    ./venv/bin/pip install --no-cache-dir -r requirements.txt
                    ./venv/bin/pytest test_app.py
                '''
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withCredentials([string(credentialsId: 'sonarqube-token', variable: 'SONAR_TOKEN')]) {
                    sh '''
                        docker run --rm \
                          -v "$(pwd):/usr/src" \
                          sonarqube/sonar-scanner \
                          -Dsonar.host.url=http://172.17.0.1:9000 \
                          -Dsonar.token=$SONAR_TOKEN
                    '''
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-cicd-app:latest .'
            }
        }
    }
}
