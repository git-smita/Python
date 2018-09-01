pipeline {
    agent {label 'node-1'}
    
    parameters {
       string(name: 'BROWSER', defaultValue: 'IE', description: 'browser name')
    }
    
    stages {
        stage('Script-1') {
            steps {
                echo 'Run Script-1 ...'
                bat """
                    set exec_cmd = "robot -v BROWSER:%BROWSER% -d Results -l script-1-log.html -r script-1-report.html -o script-1-out.xml RF/TestSuite-1"	
                   	cmd /c call %exec_cmd%
               """ 
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
    
    post {
        always {
            reportResults
        }
		success {
			echo "Build is successfull."
		}
		
		failure {
			echo "Build has failed."		
		}		
    }
}
