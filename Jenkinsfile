pipeline {
    agent any
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
