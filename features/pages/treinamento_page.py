from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select

##################################################### MAPEANDO CAMPOS NA TELA #####################################################
# Mapeando campos da aplicação para interação
CAMPO_NOME = "#formNome"
CAMPO_SOBRENOME = "#formSobrenome"
RADIO_BUTTON_SEXO = "#formSexoMasc"
CHECKBOX_PIZZA = "#formComidaPizza"
DROPDOWN_ESCOLARIDADE = "#formEscolaridade"
LISTA_ESPORTES = "#formEsportes"
BOTAO_CADASTRAR = "#formCadastrar"
# Mapeando campos da aplicação para verificar resultados
MENSAGEM_CADASTRADO = "#resultado span"
TEXTO_NOME_CADASTRADO = "#descNome span"
TEXTO_SOBRENOME_CADASTRADO = "#descSobrenome span"
TEXTO_SEXO_CADASTRADO = "#descSexo span"
TEXTO_COMIDA_CADASTRADO = "#descComida span"
TEXTO_ESCOLARIDADE_CADASTRADO = "#descEscolaridade span"
TEXTO_ESPORTE_CADASTRADO = "#descEsportes span"

# Abaixo teremos 3 opções de achar o elemento checkbox na linha do UsuárioA na 

# Solução 1 - utilizando lógica de programação e CSS selector
LINHA_TABELA = "#tabelaUsuarios tbody tr"
CHECKBOX_TABELA = "input[type='checkbox']"

# Solução 2 - CSS selector baseado em posições
CHECKBOX_ELEMENTO_NAO_RECOMENDADO = "#tabelaUsuarios > tbody > tr:nth-child(3) > td:nth-child(4) > input[type=checkbox]"

# Solução 3 - XPATH baseado em busca
CHECKBOX_USUARIO_A_XPATH = "//table[@id='tabelaUsuarios']//tr[td[normalize-space(text())='Usuario A']]//input[@type='checkbox']"

##################################################### VARIAVEIS PARA AJUDAR O TESTE #####################################################
texto_cadastrado = "Cadastrado!"
nome = "David"
sobrenome = "Brandão"
sexo = "Masculino"
comida = "Pizza"
escolaridade = "Mestrado"
escolaridade_validacao = escolaridade.lower() # a escolaridade vinda da tela tem pegadinha, vem com caracteres minusculos
esporte = "Corrida"

##################################################### METODOS #####################################################
# Encapsular a lógica do cadastro em um método único
# Isso ajuda na hora de reaproveitar o teste
# Além disso, o gherkin fica mais comportamental e menos step by step
def preencher_campos():
    preencher_nome()
    preencher_sobrenome()
    clicar_sexo_masc()
    clicar_comida_favorita()
    selecionar_escolaridade()
    selecionar_esporte()
    # Recomendado
    # clicar_checkbox_usuario_a_VERSAO1()
    # Não Recomendado
    # clicar_checkbox_usuario_a_VERSAO2()
    # Recomendado
    clicar_checkbox_usuario_a_VERSAO3()
    clicar_botao_cadastrar()


def preencher_nome():
    find_element(CAMPO_NOME).send_keys(nome)

def preencher_sobrenome():
    find_element(CAMPO_SOBRENOME).send_keys(sobrenome)

def clicar_sexo_masc():
    find_element(RADIO_BUTTON_SEXO).click()

def clicar_comida_favorita():
    find_element(CHECKBOX_PIZZA).click()

def selecionar_escolaridade():
    dropdown_escolaridade = Select(find_element(DROPDOWN_ESCOLARIDADE))
    dropdown_escolaridade.select_by_visible_text(escolaridade)

def selecionar_esporte():
    dropdown_esporte = Select(find_element(LISTA_ESPORTES))
    dropdown_esporte.select_by_visible_text(esporte)

def clicar_botao_cadastrar():
    find_element(BOTAO_CADASTRAR).click()

# Vamos procurar um locator para a linha da tabela -> #tabelaUsuarios tbody tr
# Como todas as linhas são iguais, precisamos percorrer uma a uma buscando a informação que precisamos
def clicar_checkbox_usuario_a_VERSAO1():
    # Retornar todas a linhas da tabela -> perceba que o comando agora é find_elementS (com s no final)
    # Esse comando retorna uma lista com todos elementos
    LINHA_TABELA = "#tabelaUsuarios tbody tr"

    CHECKBOX_TABELA = "input[type='checkbox']"
    linhas = find_elements(LINHA_TABELA)
    
    # Usaremos o foreach para percorrer cada um destes elementos
    for linha in linhas:
        # Vamos agora procurar quais os nomes em cada um elemento
        nome = linha.find_elements(By.TAG_NAME, "td")[0].text.strip()
        # Verificar se o nome é o que desejamos
        if nome == "Usuario A":
            # Se o nome for o que queremos, basta procurar o type checkbox (agora só vai existir um)
            checkbox = linha.find_element(By.CSS_SELECTOR, CHECKBOX_TABELA)
            # Clicamos no campo
            checkbox.click()
            # Forçamos a saída do loop for 
            break

# Esta versão localiza um elemento diretamente de acordo com sua posição
# É um metodo mais simples, porém é mais fraco pois se um novo elemento for adicionado 
    # ou qualquer ordem for alterada, o teste irá falhar
def clicar_checkbox_usuario_a_VERSAO2():
    find_element(CHECKBOX_ELEMENTO_NAO_RECOMENDADO).click()

# Utilziando XPATH nos podemos localizar elementos mais "dificeis" e sem muito esforço
# A sua sintaxe nos permite inserir "lógicas" na construção de um seletor 
def clicar_checkbox_usuario_a_VERSAO3():
    # explicando a estrutura do elemento -> "//table[@id='tabelaUsuarios']//tr[td[normalize-space(text())='Usuario A']]//input[@type='checkbox']"

    # "//table[@id='tabelaUsuarios']"
    # Este comando é a busca pelo ID utlizando XPATH

    # "//tr[td[normalize-space(text())='Usuario A']]"
    # O nome dos usuários esta em (tr td) -> acessamos esta hierarquia para buscar o nome que desejamos

    # "//input[@type='checkbox']"
    # → Agora que achamos o nome, basta procurar por um checkbox no elmeento

    # Com isso montado e separado por // selecionamos o checkbox que está na mesma linha em que o texto "Usuario A"
    # OBS: o // serve para buscarmos em qualquer nivelde profundidade

    # Perceba que aqui estou utilizano o driver pois não estou procurando um elemento com CSS SELECTOR
    get_driver().find_element(By.XPATH, CHECKBOX_USUARIO_A_XPATH).click()

def get_informacao_cadastrado():
    return get_element_text(MENSAGEM_CADASTRADO)

def get_valor_nome_cadastrado():
    return get_element_text(TEXTO_NOME_CADASTRADO)

def get_valor_sobrenome_cadastrado():
    return get_element_text(TEXTO_SOBRENOME_CADASTRADO)

def get_valor_sexo_cadastrado():
    return get_element_text(TEXTO_SEXO_CADASTRADO)

def get_valor_comida_cadastrado():
    return get_element_text(TEXTO_COMIDA_CADASTRADO)

def get_valor_escolaridade_cadastrado():
    return get_element_text(TEXTO_ESCOLARIDADE_CADASTRADO)

def get_valor_esportes_cadastrado():
    return get_element_text(TEXTO_ESPORTE_CADASTRADO)

def valores_recuperados_em_tela():
    return [
        get_informacao_cadastrado(),
        get_valor_nome_cadastrado(),
        get_valor_sobrenome_cadastrado(),
        get_valor_sexo_cadastrado(),
        get_valor_comida_cadastrado(),
        get_valor_escolaridade_cadastrado(),
        get_valor_esportes_cadastrado()
    ]

def valores_passados_no_teste():
    return [
        texto_cadastrado,
        nome,
        sobrenome,
        sexo,
        comida,
        escolaridade_validacao,
        esporte
    ]

