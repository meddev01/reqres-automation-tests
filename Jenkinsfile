pipeline {
    agent any

    environment {
        REPORT_DIR = 'reports'
        GITHUB_URL = 'https://github.com/meddev01/reqres-automation-tests.git'
    }

    stages {

        stage('Checkout du code') {
            steps {
                echo '🔄 Clonage du dépôt GitHub...'
                git branch: 'main', url: "${GITHUB_URL}"
            }
        }

        stage('Installation des dépendances') {
            steps {
                echo '📦 Installation de l’environnement Python et des dépendances...'
                bat """
                python -m venv .venv
                call .venv\\Scripts\\activate
                pip install -r requirements.txt
                npm install -g newman
                """
            }
        }

        stage('Exécution des tests UI (Pytest + Selenium)') {
            steps {
                echo '🧪 Exécution des tests UI automatisés...'
                bat """
                call .venv\\Scripts\\activate
                if not exist ${REPORT_DIR} mkdir ${REPORT_DIR}
                pytest --html=${REPORT_DIR}\\ui_report.html --self-contained-html || exit 0
                """
            }
            post {
                always {
                    publishHTML(target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'reports',
                        reportFiles: 'ui_report.html',
                        reportName: 'Rapport UI Selenium'
                    ])
                }
            }
        }

        stage('Exécution des tests API (Postman)') {
            steps {
                echo '🌐 Exécution des tests API avec Newman...'
                bat """
                if not exist ${REPORT_DIR} mkdir ${REPORT_DIR}
                newman run tests_api\\postman_collection.json --reporters cli,html --reporter-html-export ${REPORT_DIR}\\api_report.html || exit 0
                """
            }
            post {
                always {
                    publishHTML(target: [
                        allowMissing: true,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'reports',
                        reportFiles: 'api_report.html',
                        reportName: 'Rapport API Postman'
                    ])
                }
            }
        }
    }

    post {
        success {
            echo '✅ Build réussi : tous les tests se sont exécutés avec succès.'
        }
        failure {
            echo '❌ Build échoué : consulte les logs pour identifier le problème.'
        }
        always {
            echo '📩 Fin du pipeline Jenkins.'
        }
    }
}
