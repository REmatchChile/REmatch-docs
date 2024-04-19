import wikipedia
text = wikipedia.page("Chile", auto_suggest=False).summary

# Imprimir los primeros 2000 caracteres
f = open("chile-wiki.txt", "x")
f.write(text)
f.close()