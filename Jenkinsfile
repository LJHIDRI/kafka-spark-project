pipeline {
    agent any

    environment {
        // IMPORTANT: Remplacez 'votre-nom-dockerhub' par votre vrai nom d'utilisateur Docker Hub
        DOCKER_IMAGE_NAME = "lou19/kafka-spark-processor-json"
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Étape 1: Récupération du code depuis GitHub...'
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                // Jenkins utilise le Dockerfile dans le dossier spark-app
                echo "Étape 2: Construction de l'image Docker de l'application Spark..."
                // ${BUILD_NUMBER} est une variable de Jenkins (1, 2, 3...)
                sh "docker build -t ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER} ./spark-app"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "Étape 3: Publication de l'image sur Docker Hub..."
                // 'dockerhub-credentials' est l'ID que nous créerons dans l'interface de Jenkins
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin"
                    sh "docker push ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER}"
                }
            }
        }
    }
}