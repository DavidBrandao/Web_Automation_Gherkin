Funcionalidade: Treinamento Automação

    @exercicio
    Cenário: Registrar um usuário no campo de treinamento
        Dado que a página de treinamento seja acessada
        Quando todos campos obrigatórios forem preenchidos
        Então o usuário deverá ser cadastrado com sucesso

    @exemplo_falha
    Cenário: Exemplo de teste que falha na validação do cadastro
        Dado que a página de treinamento seja acessada
        Quando todos campos obrigatórios forem preenchidos
        Então a mensagem de cadastro deverá ser "Erro ao cadastrar"
