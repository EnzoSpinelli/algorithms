def lower_bound (arr, target):        #["abacaxi", "banana", "laranja", "baicon", "abobrinha", "berinjela"]
  st, en = 0, len (arr)
  while st < en: # enquanto 0 for menor qque 5
    mid = (st + en) // 2 # mid = (0 + 5) // 2 = 2,5 = int 2
    if arr[mid] < target: #2 < 0
      st = mid +1 # 0 = 2 + 1 = 3
    else:
      en = mid # en = 3
  return st

def suggestionWord (products, searchWord): #estamos criando uma função chamada suggestionWord e passando os parametros products e searchWord; products sendo a lista de produtos e o searchWord a paralvra que o usuário digita
  products.sort () #método para ordem alfabetica ( colocamos todos os nomes da lista products em ordem alfabetica)

  result = [] # aqui é o onde guardaremos as sugestões para cada letra digitada 
  prefix = ""


  for char in searchWord: # para cada letra que estiver em searchWord, vamos repetir a intrução dentro do laço de repetição
    prefix += char # += acrescentamos a letra nova ao nosso prefixo

    i = lower_bound(products, prefix) # encontre o ponto de partida com nossa função lower_bound, retorna um indice " i " que diz onde devemos começar a procurar

    sugest = [] # criamos a caixinha para guardar sugestões até 3 diferentes

    for k in range(i, min(i +3, len(products))): #para k de i até i + 2(máximos de 3 itens), mas sem ultrapassar o fim da lista
      if products[k].startswith(prefix): #verifica se o produto na posição k começa mesmo com o prefixo, startswith é um metodo nativo de string que retorna True se a palavra tiver o começo
        sugest.append(products[k]) # Se começar, guarda ( append ) o produto dentro da lista de sugestões
      else:
        break

    result.append(sugest)
  return result

products = ["abacaxi", "banana", "laranja", "baicon", "abobrinha", "berinjela"]
searchWord = str(input("Search: "))
print(suggestionWord(products, searchWord))
