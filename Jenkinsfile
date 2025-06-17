pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/UlyanaQA/Otus-UI-Diploma.git', branch: 'main'
            }
        }

        stage('Clean Allure Results') {
            steps {
                sh 'rm -rf allure-results/* || true'
                    }
            }

        stage('Install System Dependencies') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y wget unzip libnss3 libgconf-2-4 fonts-liberation
                '''
            }
        }

        stage('Install Chrome') {
            steps {
                sh '''
                    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
                    dpkg -i google-chrome-stable_current_amd64.deb || true
                    apt-get install -y -f
                    rm google-chrome-stable_current_amd64.deb
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    . /var/jenkins_home/venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . /var/jenkins_home/venv/bin/activate
                    python3 -m pytest tests/ -v --alluredir=./allure-results --headless
                '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
}