pipeline {
  agent { dockerfile true }
  stages {
    stage('Build') {
          steps {
            sh 'echo "building the repo"'
            sh "docker build -t flask-app ."
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
        sh "docker run -p 5000:5000 --name flask-app -d flask-app "
      }
    }

  }

  post {
        always {
            echo 'The pipeline completed'
            junit allowEmptyResults: true, testResults:'**/test_reports/*.xml'
        }
        success {
            
            sh "sudo nohup python3 app.py > log.txt 2>&1 &"
            echo "Flask Application Up and running!!"
        }
        failure {
            echo 'Build stage failed'
            error('Stopping early…')
        }
      }
}
