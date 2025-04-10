from math import pi as PI

print("[ACCESS GRANTED] >> Perimeter_Calculator.exe booting... \nWelcome, operative.\n")
print("scegli da quelle elencate la figura di cui calcolare il perimetro:\n1. triangolo equilatero\n2. quadrato\n3. rettangolo\n4. cerchio\n0 per uscire")

while True:
    try:
        scelta = int(input("\nnumero scelta >> "))
    
        if scelta == 1:
            lato = float(input("inserisci la lungheza del lato:\n>> "))
            print(f"il perimetro del tuo triangolo e': {lato * 3}")
            
        elif scelta == 2:
            lato = float(input("inserisci la lungheza del lato:\n>> "))
            print(f"il perimetro del tuo quadrato e': {lato * 4}")
            
        elif scelta == 3:
            lato, lato1 = map(float, input("inserisci la lungheza dei lati separati da spazio:\n>> ").split())
            print(f"il perimetro del tuo rettangolo e': {(lato + lato1) * 2}")
            
        elif scelta == 4:
            raggio = float(input("inserisci il raggio del cerchio:\n>> "))
            print(f"La cinconferenza del tuo cerchio e': {2 * PI * raggio}")
            
        elif scelta == 0:
            print(">> Mission complete. Disconnecting from geometric mainframe...")  
            break

        else:
            print("scelta non supportata >:(")
            
    except ValueError:
        print("errore nell'inserimento dei dati. riprovare.")
