from behave import given, when, then

# Variável com a url do site a qual iremos utilizar
base_url= 'http://www.americanas.com.br/'

@given(u'acesso a pagina inicial da loja Americanas')
def step_impl(context):
    context.web.get(base_url)
    #raise NotImplementedError(u'STEP: Given acesso a pagina inicial da loja Americanas')


@given(u'eu insiro o produto desejado no campo de busca')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given eu insiro o produto desejado no campo de busca')


@when(u'clico na opção de pesquisar')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clico na opção de pesquisar')


@when(u'a pesquisa me retornar um lista com o produto que busquei')
def step_impl(context):
    raise NotImplementedError(u'STEP: When a pesquisa me retornar um lista com o produto que busquei')


@then(u'devo selecionar o produto desejado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then devo selecionar o produto desejado')


@then(u'então poder adicionar ao carrinho e finalizar a compra')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then então poder adicionar ao carrinho e finalizar a compra')
