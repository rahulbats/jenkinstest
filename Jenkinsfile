pipeline {
    agent any

    stages {
        stage('Hello') {
            
            steps {
               script {
                
                
                def userInput = input(
                 id: 'userInput', message: 'Let\'s promote?', parameters: [
                 [$class: 'TextParameterDefinition', defaultValue: 'uat', description: 'Environment', name: 'env'],
                 [$class: 'TextParameterDefinition', defaultValue: 'uat1', description: 'Target', name: 'target']
                ])
                
                echo "this is userinput ${userInput['env']}"
               
                def output = readFile file: "/Users/rahul/inputfile.txt"
                def outputjson = readJSON file: "/Users/rahul/inputfile.json"
                for (ii = 0; ii < outputjson.projects.project.size(); ii++)
                    echo outputjson.projects.project[ii].name
                echo outputjson.projects.project[1].name
                echo output
                def response = sh(script: 'curl http://www.example.org/', returnStdout: true)
                echo response
                }
            }
            }
        }
    
}

