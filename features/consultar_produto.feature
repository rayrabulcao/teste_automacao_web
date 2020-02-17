#language: pt
Funcionalidade: Consultar um produto no site da Americanas

   '''Eu como usuario quero acessar a pagina da loja Americanas
   para realizar a consulta de um produto a qual eu quero adquirir.'''

   Cenario: Consultar um produto disponível no site da loja Americanas
   Dado acesso a pagina inicial da loja Americanas
   E eu insiro o produto desejado no campo de busca
   Quando clico na opção de pesquisar
   E a pesquisa me retornar um lista com o produto que busquei
   Então devo selecionar o produto desejado
   E então poder adicionar ao carrinho e finalizar a compra