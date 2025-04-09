# Descrizione: 
# Scrivi una funzione che calcoli la media mobile di una lista di numeri. 
# La media mobile di un elemento è definita come la media degli ultimi n elementi della lista, inclusi l'elemento corrente.

# lista = [1,2,3,4,5,6,7,8,9,10]

lista = [1, 3, 5, 7, 9, 2, 4, 6, 8]
n = 3
media_mobile = []

for i in range(len(lista)):
    # Prendi gli ultimi n elementi fino all'indice i
    _slice = lista[max(0, i-n+1) : i+1] 
    media_mobile.append(sum(_slice) / len(_slice))

print(media_mobile)



    


