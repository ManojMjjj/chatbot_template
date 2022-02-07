pipeline {
  agent any
  stages {
    stage('Build') {
          steps {
            bat 'echo "building the repo"'
            bat "docker build -t flask-app ."
          }
    }

    stage('Test') {
      steps {
        echo "TEST DONE"
      }
    }

    stage('Deploy')
    {
      steps {
        echo "deploying the application"
        bat "docker run -p 5000:5000 --name flask-app -d flask-app "
      }
    }

  }
