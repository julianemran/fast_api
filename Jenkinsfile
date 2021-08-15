pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/julianemran/fast_api.git'
            }
        }
        stage('Build') {
            steps {
                sh 'npm install -r requirements.txt'
                echo 'Build completed'
            }
        }
        stage('Run') {
            steps {
                sh 'sh run.sh'
                echo 'Run completed'
            }
        }
        stage('Test') {
            steps {
                echo "----------------------------"
                sh 'pytest test_api.py -v'
                echo 'Testing completed'
                echo "----------------------------"
            }
        }
    }
}