pipeline {
    agent {
        docker {
            image 'python:3.5.1'
        }
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('package') {
            steps {
                sh '''
                echo $PWD
                ls -ltrh
                zip ${JOB_NAME}.zip -r .
                '''
            }
        }
    }
    post {
        success {
            archiveArtifacts artifacts: '${JOB_NAME}.zip', fingerprint: true
        }
    }
}
