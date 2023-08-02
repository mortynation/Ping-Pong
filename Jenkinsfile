pipeline {
    agent { label 'slaveNode1' }
    stages {
        stage('Build') {
            steps {
                echo 'building the application...'
                script {
                    // Change to the desired directory where test.sh is located
                    dir('/Users/mortimer/slave/workspace/ping-pong-freestyle') {
                        sh 'chmod +x build.sh' // Optional: Ensure test.sh has executable permissions
                        sh './build.sh' // Execute the test.sh script
                    }
                }
            }
        }
        stage('Test') {
            steps {
                echo 'testing the application...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'deploying the application...'
            }
        }
    }
}
