def call () {

    stage('Stop Old Container') {
        script {
            sh '/usr/local/bin/docker ps -q | xargs -r /usr/local/bin/docker rm -f'
        }
    }

    stage('Run New Container') {
        script {
            sh '''
                /usr/local/bin/docker run -d \
                -p 8081:8081 \
                calculator-web
            '''
        }
    }

    stage('Verify Container') {
        script {
            sh """
            sleep 3
            curl -f http://localhost:8081
            """
        }
    }
}
