import requests
from bs4 import BeautifulSoup

usuario_github = input('Digite o nome do Usuário no GitHub: ')
url = 'https://github.com/' + usuario_github
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
imagem_do_perfil = soup.find('img',{'alt':'Avatar'})['src']
print(imagem_do_perfil)