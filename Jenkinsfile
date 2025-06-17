pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/UlyanaQA/Otus-UI-Diploma.git',  branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '. /var/jenkins_home/venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. /var/jenkins_home/venv/bin/activate && python3 -m pytest test_search_function.py -v --alluredir=./allure-results'
            }
        }

        stage('Publish Allure Report') {
            steps {
                sh '/usr/local/bin/allure generate ./allure-results --clean -o ./allure-report'
                allure([
                    includeProperties: false,
                    jdk: 'JDK',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}