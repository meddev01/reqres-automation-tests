pipeline {
    agent any

    environment {
        // Variables d'environnement globales
        REPORT_DIR = 'reports'
        PYTHON = '/usr/bin/python3'
    }

    stages {

        stage('Checkout du code') {
            steps {
                git branch: 'main', url: 'https://github.com/ton-utilisateur/ton-projet.git'
            }
        }

        stage('Installation des dépendances') {
            steps {
                sh '''
                pip install -r requirements.txt
                npm install -g newman
                '''
            }
        }

        stage('Exécution des tests UI (Selenium)') {
            steps {
                sh '''
                mkdir -p $REPORT_DIR/ui
                $PYTHON tests_ui/selenium_test.py > $REPORT_DIR/ui/result.txt || true
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'reports/ui/result.txt', fingerprint: true
                }
            }
        }

        stage('Exécution des tests API (Postman)') {
            steps {
                sh '''
                mkdir -p $REPORT_DIR/api
                newman run tests_api/postman_collection.json --reporters cli,html --reporter-html-export $REPORT_DIR/api/report.html || true
                '''
            }
            post {
                always {
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'reports/api',
                        reportFiles: 'report.html',
                        reportName: 'Rapport API Postman'
                    ])
                }
            }
        }

    }

    post {
        always {
            emailext(
                subject: "Pipeline Jenkins - Rapport de test",
                to: "tonemail@exemple.com",
                body: "Les tests CI/CD ont été exécutés. Consulte le rapport Jenkins.",
                attachLog: true
            )
        }
    }
}
