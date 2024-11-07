class insiemeNumeri:
     def __init__(self):
        self.numeri = [] 

    #Valorizziamo la lista con 5 numeri e verifichiamo che l'input sia un numero
     def valorizza_lista(self):
        while len(self.numeri) < 5:
            numero = input(f"Inserisci il numero {len(self.numeri) + 1}")
            if numero.isdigit(): 
                self.numeri.append(int(numero))
            else:
                print("Devi inserire un numero valido")

class ConfrontoInsieme:
    def __init__(self, insieme1, insieme2):
        self.insieme1 = insieme1
        self.insieme2 = insieme2

    def somma(self):
        somma_risultato = []
        for num in range(len(self.insieme1.numeri)):
            somma_risultato.append(self.insieme1.numeri[num] + self.insieme2.numeri[num])
        return somma_risultato
    
    def confronto(self):
        somma_risultato = self.somma() 
        print("Somma degli insiemi = ", somma_risultato)

    def main():
        while True:
            insieme1 = InsiemeNumeri()
            insieme2 = InsiemeNumeri()

            print("Valorizza la prima lista di numeri:")
            insieme1.valorizza_lista()
            print("Valorizza la seconda lista di numeri:")
            insieme2.valorizza_lista()

            confronto = ConfrontoInsieme(insieme1, insieme2)
            confronto.confronto() 

            ripeti = input("Ripetere il processo? (sì/no): ")
            if ripeti == "no":
                break


    
    


