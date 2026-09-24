import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.treinamento_page import *

@given(u'que a página de treinamento seja acessada')
def acessar_site_treinamento(context):
    get_driver().get("https://wcaquino.me/cypress/componentes.html")

@when(u'todos campos obrigatórios forem preenchidos')
def preencher_campos_obrigatorios(context):
    preencher_campos()


@then(u'o usuário deverá ser cadastrado com sucesso')
def validar_usuario_cadastrado_sucesso(context):
    assert valores_recuperados_em_tela() == valores_passados_no_teste(), f"\nEsperados: {valores_passados_no_teste()}\nRecebidos: {valores_recuperados_em_tela()}"


# Step criado apenas para demonstrar um teste falhando no report
# A tela sempre exibe "Cadastrado!", então qualquer outra mensagem esperada faz a validação falhar
@then(u'a mensagem de cadastro deverá ser "{mensagem}"')
def validar_mensagem_cadastro(context, mensagem):
    mensagem_em_tela = get_informacao_cadastrado()
    assert mensagem_em_tela == mensagem, f"\nEsperado: {mensagem}\nRecebido: {mensagem_em_tela}"
