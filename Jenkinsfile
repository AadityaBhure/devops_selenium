pipeline {
    agent any

    environment {
        APP_PORT = "5000"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/AadityaBhure/devops_selenium.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Start Flask Server') {
            steps {
                bat 'start /B python app.py'
                sleep 5
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat 'python test_form.py'
            }
        }
    }

    post {
        success {
            echo '✅ Build Successful: All tests passed!'
        }
        failure {
            echo '❌ Build Failed: Check errors in console output.'
        }
        always {
            echo '🔁 Pipeline execution completed.'
        }
    }
}