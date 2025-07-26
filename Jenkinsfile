pipeline {
  agent any

  environment {
    IMAGE_NAME = 'yourdockerhubuser/apache-flask-app'
    DOCKER_REGISTRY = 'docker.io'
  }

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://your-git-repo-url.git', branch: 'main'
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          sh 'docker build -t $IMAGE_NAME .'
        }
      }
    }

    stage('Docker Login') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
        }
      }
    }

    stage('Push Docker Image') {
      steps {
        script {
          sh 'docker push $IMAGE_NAME'
        }
      }
    }

    stage('Deploy (Optional)') {
      steps {
        echo 'Here you could use SSH or ECS CLI to deploy to production.'
        // For example, use ECS CLI or SSH to remote Docker host
      }
    }
  }

  post {
    always {
      echo 'Cleaning up...'
      sh 'docker system prune -f'
    }
  }
}