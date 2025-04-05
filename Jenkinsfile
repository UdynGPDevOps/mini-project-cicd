pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-devops-app"
        DOCKER_REGISTRY = "https://udayandevops.jfrog.io/artifactory/docker-local-docker-local/" // 🔁 Replace this
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo '✅ Source code is pulled from GitLab via Jenkins SCM config'
            }
        }

        stage('Install Dependencies (optional)') {
            steps {
                sh 'pip install -r app/requirements.txt || true'
                echo '✅ Dependencies installed locally for testing (optional)'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}", "app")
                    echo "✅ Docker image '${IMAGE_NAME}' built successfully."
                }
            }
        }

        stage('Push to JFrog Artifactory') {
            steps {
                script {
                    docker.withRegistry("https://${DOCKER_REGISTRY}", 'jfrog-creds-id') {
                        docker.image("${IMAGE_NAME}").push("latest")
                        echo "✅ Docker image pushed to JFrog!"
                    }
                }
            }
        }
    }

    post {
        success {
            echo '🎉 Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs.'
        }
    }
}
