pipeline {
    agent {label 'slaveNode1'}
    stages {
        stage('Build') {
            steps {
                echo 'building the application...'
                $WORKSPACE/test.sh

            }
        }
        stage('Test') {
            steps{
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
