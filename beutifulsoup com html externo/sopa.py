from bs4 import BeautifulSoup
import requests

url = "https://lista.mercadolivre.com.br/serra#D[A:serra]"  #serve para as seções de eletronicos, ferramentas, ainda precisa melhorar o filtro

resultado = requests.get(url)
#print(resultado.text)

pagina = BeautifulSoup(resultado.text, "html.parser")
busca1 = pagina.find_all(class_="ui-search-result__content-column ui-search-result__content-column--left")
buscaPreco = busca1[0].find_all(class_="price-tag-text-sr-only")
#print(busca2)
buscaTitulo = pagina.find_all(class_="ui-search-item__group__element ui-search-link")

numero = 0
for i in range(8):
    numero += 1
    print(buscaTitulo[numero].string)
    buscaPreco = busca1[numero].find_all(class_="price-tag-text-sr-only")  # acha a tag do valor que contem 2 tags
    print(buscaPreco[0].string)