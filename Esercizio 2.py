#Classe per la Lista
class Lista:
    def __init__(self):
        self.__lista = [] #Qui salviamo i numeri

#Funzione che ci permette di aggiungere i numeri alla lista
    def aggiungi_numero(self, numero):
        self.__lista.append(numero)

#Stampiamo i numeri che non si ripetono e controlliamo
#Se sono presenti nel dizionario creato precedentemente
#Se è già presente nel dizionario, aumenta il count
    def stampa_numeri_che_non_si_ripetono(self):
        numeri_non_ripetibili = {}
        for numero in self.__lista:
            if numero in numeri_non_ripetibili:
                numeri_non_ripetibili[numero] += 1
            else:
                numeri_non_ripetibili[numero] = 1
        #Questa è la lista che usiamo solo per i numeri unici
        numeri_unici = []
        #Ciclo for per aggiungere i numeri che non si ripetono alla lista
        for numero, count in numeri_non_ripetibili.items():
            if count == 1: 
                numeri_unici.append(numero)
        print(numeri_unici)

