pipeline {

    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building application...'

                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests...'

                sh '''
                    . venv/bin/activate
                    pytest
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'

                sh '''
                    docker build -t cicd-demo:${BUILD_NUMBER} .
                    docker tag cicd-demo:${BUILD_NUMBER} cicd-demo:latest
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'

                sh '''
                    docker rm -f cicd-demo || true

                    docker run -d \
                    --name cicd-demo \
                    -p 5000:5000 \
                    cicd-demo:latest
                '''
            }
        }

    }

    post {

        success {
            echo 'Deployment successful!'
        }

        failure {
            echo 'Pipeline failed!'
        }

    }
}
