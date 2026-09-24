# Roda os testes com o behave, gera o relatório do Allure e abre no navegador.
#
# Uso:
#   .\run_tests.ps1                        roda todos os cenários
#   .\run_tests.ps1 --tags=@exercicio      roda só os cenários com a tag
#   .\run_tests.ps1 features/feature_files/treinamento.feature
#
# Tudo que vier depois do nome do script é repassado direto para o behave.

# Usa o Python da venv do projeto, sem precisar ativá-la antes
& ".\venv\Scripts\python.exe" -m behave @args

# Gera o HTML a partir dos resultados, mesmo quando algum teste falhou
allure generate reports/allure-results -o reports/allure-report --clean

# Abre o relatório no navegador (encerre com Ctrl+C)
allure open reports/allure-report
