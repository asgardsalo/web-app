def call () {

 stage('Stop Old Container') {
        steps {
            script {
                sh "docker rm -f calc-app || true"
            }
        }
    }

    stage('Run New Container') {
        steps {
            script {
                sh """
                docker run -d \
                -p 8081:8081 \
                --name calc-app \
                calculator-web
            """
            }
        }
    }

    stage('Verify Container') {
        steps {
            script {
                sh """
                sleep 3
                curl -f http://localhost:8081
                """
            }
        }
    }
}
