import urllib.request, json

url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=b36c3a892340239a7c7a0dc35f709c91"

resposta = urllib.request.urlopen(url)

dados = resposta.read()
guidata = json.loads(dados)
print(guidata['results'])