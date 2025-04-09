# Scrivi una funzione che analizzi una stringa di testo e restituisca un dizionario con il conteggio delle occorrenze di ciascuna parola. 
# Ignora la punteggiatura e considera le parole in modo case-insensitive.
import re

def conta_parole(testo):
    lista_parole = []
    occorrenze = {}
    
    testo = testo.lower()
    testo = re.sub(r'[,?!]', "", testo)
    
    lista_parole = testo.split()
    
    for parola in lista_parole:
        if parola in occorrenze:
            occorrenze[parola] += 1
        else:
            occorrenze[parola] = 1
    return occorrenze


    
    
print(conta_parole("Ciao! ciao, come stai? Stai bene?"))