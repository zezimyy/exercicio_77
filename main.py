lista_palavras = (
  "maracuja",
  "uva",
  "azeitona",
  "ovo",
  "livro",
)
numero = 0

# separa a tupla em palavras
for c in lista_palavras:
  if "a" or "e" or "i" or "o" or "u" in lista_palavras:
    print(c)
    palavra = c

    # separa as palavras em letras
    for vogal in palavra:
      if "a" or "e" or "i" or "o" or "u" in palavra:
        letra = vogal

        # verifica se tem vogais nas palavras
        for vogais in letra:
          if "a" in vogais:
            print(vogais)
          if "e" in vogais:
            print(vogais)
          if "i" in vogais:
            print(vogais)
          if "o" in vogais:
            print(vogais)
          if "u" in vogais:
            print(vogais)
