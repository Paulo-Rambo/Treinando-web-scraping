#pip install beautifulsoup4 (acessar e realizar busca no arquivo html)
#pip install requests       (fazer request das paginas para acessar o conteúdo)

from bs4 import BeautifulSoup
import requests

with open("index.html", "r") as pagina:
    paginaSopa = BeautifulSoup(pagina, "html.parser")

#print(paginaSopa)
#print(paginaSopa.prettify())
titulos1 = paginaSopa.th
titulos = paginaSopa.find_all("th")
print(titulos)
print(titulos1)
#print(titulos1.string)    ----> acessa a string dentro da primeira tag th

for e in titulos:          # ----> acessa a string dentro das tags th e mostra
    print(e.string)