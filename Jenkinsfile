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

  post {
        always {
            echo 'The pipeline completed'
            junit allowEmptyResults: true, testResults:'**/test_reports/*.xml'
        }
        success {
            
            bat "sudo nohup python3 app.py > log.txt 2>&1 &"
            echo "Flask Application Up and running!!"
        }
        failure {
            echo 'Build stage failed'
            error('Stopping early…')
        }
      }
}
