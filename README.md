# Gherkin Automation

Projeto de treinamento em automação de testes com BDD, usando **behave** (Gherkin em português), **Selenium** e relatórios com **Allure**.

## Pré-requisitos

- Python 3.10 ou superior
- Google Chrome instalado
- Node.js (para instalar o Allure CLI)
- Java 8 ou superior (o Allure CLI precisa dele para rodar)

## 1. Criar e ativar a venv

Na raiz do projeto:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

No Linux ou macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Com a venv ativa, instale as dependências:

```bash
pip install -r requirements.txt
```

## 2. Rodar os testes

Com a venv ativa, na raiz do projeto:

```bash
behave
```

O `behave.ini` já aponta para a pasta `features/feature_files` e configura dois formatadores: o `pretty` no terminal e o Allure gravando em `reports/allure-results`.

Para rodar só um cenário, use a tag:

```bash
behave --tags=@exercicio
behave --tags=@exemplo_falha
```

O cenário `@exemplo_falha` falha de propósito, para demonstrar como um teste quebrado aparece no report, com screenshot anexado.

### Atalho: rodar e abrir o report num comando só

O script `run_tests.ps1` roda o `behave`, gera o HTML do Allure e abre no navegador. Ele usa o Python da venv diretamente, então não precisa ativá-la antes. Tudo que vier depois do nome do script é repassado ao `behave`:

```powershell
.\run_tests.ps1
.\run_tests.ps1 --tags=@exercicio
.\run_tests.ps1 --tags=@exemplo_falha
```

Requer o Allure CLI instalado (seção 3). Se o Windows bloquear a execução de scripts, rode assim:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_tests.ps1 --tags=@exercicio
```

## 3. Setup do Allure

O `allure-behave` (biblioteca Python) já vem no `requirements.txt`. O que falta é o **Allure CLI**, que gera e abre o relatório HTML.

Instale uma vez, de forma global:

```bash
npm install -g allure-commandline
```

Confira a instalação:

```bash
allure --version
```

## 4. Abrir o report

Se você usou o `run_tests.ps1`, o report já abre sozinho. Rodando o `behave` direto, os resultados ficam em `reports/allure-results` e o HTML precisa ser gerado. Para abrir o relatório no navegador:

```bash
allure serve reports/allure-results
```

O comando sobe um servidor local e abre o report. Encerre com `Ctrl+C`.

Se preferir gerar um HTML estático para guardar ou enviar:

```bash
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

## Estrutura do projeto

```
features/
  feature_files/   cenários em Gherkin
  steps/           implementação dos steps
  pages/           Page Objects (seletores e ações na tela)
  helpers/         controle do driver do Selenium
  environment.py   hooks do behave (abre e fecha o navegador, screenshot em falha)
behave.ini         configuração do behave e dos formatadores
requirements.txt   dependências Python
run_tests.ps1      roda os testes, gera e abre o report do Allure
```

As pastas `reports/` e `screenshots/` são geradas a cada execução e estão no `.gitignore`.
