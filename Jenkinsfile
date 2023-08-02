pipeline {
    agent { label 'slaveNode1' }
    stages {
        stage('Build') {
            steps {
                echo 'building the application...'
                script {
                    dir('/Users/mortimer/slave/workspace/my-app-pipeline_main') {
                        sh 'chmod +x build.sh'
                        sh './build.sh' 
                    }
                }
            }
        }
        stage('Test') {
            steps {
                echo 'testing the application...'
                dir('/Users/mortimer/slave/workspace/my-app-pipeline_main') {
                    sh 'chmod +x ping.py'
                    sh 'python3 ping.py --hostname localhost --port 8090 --count 5'
                }
            }
        }
    }
}
