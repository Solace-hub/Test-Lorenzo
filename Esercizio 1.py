#Creo la classe Dato
class Dato:
    def __init__(self):
        self.int_list = []
        self.float_list = []
        self.str_list = []

#Aggiungo il dato tramite la funzione e con
#isinstance controllo se un oggetto è di quello 
#specifico tipo

    def aggiungi_dato(self, dato):
        if isinstance(dato, int):
            self.int_list.append(dato)
        elif isinstance(dato, float):
            self.float_list.append(dato)
        elif isinstance(dato, str):
            self.str_list.append(dato)
            
#Funzione che stampa tutte le liste
    def stampa_liste(self):
        print("Interi:", self.int_list)
        print("Float:", self.float_list)
        print("Stringhe:", self.str_list)