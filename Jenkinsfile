pipeline {
    agent any

    stages {
        stage('execute') {
            
            steps {
               script {
                
                    
                    env.TAG = sh (script: "printf \$(git rev-parse HEAD)", returnStdout: true)     
                    echo "this is the git revision "+env.TAG
                    env.PREVTAG = sh (script: "printf \$(git rev-parse HEAD~1)", returnStdout: true)

                    env.gitdiff = sh (script: "git diff --name-status $env.PREVTAG $env.TAG", returnStdout: true)
                    echo env.gitdiff
                    env.connectorURL="http://localhost:8083/connectors/"

                    
                    env.kafka_user="rahul"

                    sh ('/usr/local/bin/python connector.py')

                   
                }
            }
            }
        }
    
}
