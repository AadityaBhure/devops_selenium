pipeline {
    agent any

    environment {
        APP_PORT = "5000"
    }

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Start Flask Server') {
            steps {
                bat 'start "" /B python app.py'
                sleep 8
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat 'python test_form.py'
            }
        }
    }

    post {
        always {
            echo '🔁 Cleaning up...'
            bat 'taskkill /F /IM python.exe /T || exit 0'
        }
        success {
            echo '✅ Build Successful: All tests passed!'
        }
        failure {
            echo '❌ Build Failed: Check errors in console output.'
        }
    }
}