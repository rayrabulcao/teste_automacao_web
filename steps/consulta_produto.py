from behave import given, when, then

# Variável com a url do site a qual iremos utilizar
base_url= 'http://www.americanas.com.br/'

# Váriaveis dos elementos da página
element_input = 'h_search-input'
element_search = 'bhf_icon-search'

@given(u'acesso a pagina inicial da loja Americanas')
def step_impl(context):
    context.web.get(base_url)
    #raise NotImplementedError(u'STEP: Given acesso a pagina inicial da loja Americanas')


@given(u'eu insiro o produto desejado no campo de busca')
def step_impl(context):
    context.web.element_input = context.web.find_element_by_id('h_search-input')
    context.web.element_input.send_keys('Iphone 11')
    #raise NotImplementedError(u'STEP: Given eu insiro o produto desejado no campo de busca')


@when(u'clico na opção de pesquisar')
def step_impl(context):
    context.web.element_search = context.web.find_element_by_id(element_search)
    #context.web.element_search.click()
    context.web.element_search.send_keys(Keys.ENTER)
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
    context.web.base_url.quit()
