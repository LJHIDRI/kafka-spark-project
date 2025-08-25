pipeline {
    agent {
        // --- LA CORRECTION EST ICI ---
        // On dit à Jenkins d'exécuter les étapes dans un conteneur
        // qui utilise le même agent, mais en forçant l'utilisateur à 'root'
        docker {
            image 'jenkins/jenkins:lts-jdk11' // On peut se baser sur l'image de base ici
            args '-u root'
        }
    }

    environment {
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
                echo "Étape 2: Construction de l'image Docker de l'application Spark..."
                // La commande est maintenant exécutée en tant que root, qui a les permissions
                sh "docker build -t ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER} ./spark-app"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "Étape 3: Publication de l'image sur Docker Hub..."
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin"
                    sh "docker push ${DOCKER_IMAGE_NAME}:${BUILD_NUMBER}"
                }
            }
        }
    }
}