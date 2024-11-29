class Libro:
    def __init__(self, titolo, autore, anno, quantita):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.quantita = quantita

    def __str__(self):
      return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno: {self.anno}, Quantità: {self.quantita}"

class Libreria:
    def __init__(self):
        self.libri = {}

    def aggiungi_libro(self):
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        anno = int(input("Inserisci l'anno di pubblicazione: "))
        quantita = int(input("Inserisci la quantità del libro: "))

        if titolo in self.libri:
            print("Il libro esiste già nella libreria. Aggiungiamo una copia in più.")
            self.libri[titolo].quantita += quantita
        else:
            self.libri[titolo] = Libro(titolo, autore, anno, quantita)
            print("Libro aggiunto con successo!")

    def visualizza_libri(self):
        if self.libri:
            for libro in self.libri.values():
                print(libro)
        else:
            print("Non ci sono libri nella libreria.")

    def cerca_libro(self):
        titolo = input("Inserisci il titolo del libro da cercare: ")
        if titolo in self.libri:
            print(self.libri[titolo])
        else:
            print("Libro non trovato.")

    def gestione_libri(self):
        titolo = input("Inserisci il titolo del libro da gestire: ")
        if titolo in self.libri:
            libro = self.libri[titolo]
            print(f"Gestendo il libro: {libro}")
            scelta = input("Vuoi (r)imuovere una copia, (a)ggiungere una copia o (m)odificare i dettagli? ")
            if scelta == 'r':
                quantita = int(input("Quante copie vuoi rimuovere? "))
                if libro.quantita >= quantita:
                    libro.quantita -= quantita
                    print(f"Rimosse {quantita} copie del libro.")
                else:
                    print("Quantità insufficiente per rimuovere.")
            elif scelta == 'a':
                quantita = int(input("Quante copie vuoi aggiungere? "))
                libro.quantita += quantita
                print(f"Aggiunte {quantita} copie del libro.")
            elif scelta == 'm':
                nuovo_titolo = input("Nuovo titolo (premi invio per mantenere invariato): ")
                if nuovo_titolo:
                    libro.titolo = nuovo_titolo
                nuovo_autore = input("Nuovo autore (premi invio per mantenere invariato): ")
                if nuovo_autore:
                    libro.autore = nuovo_autore
                nuovo_anno = input("Nuovo anno (premi invio per mantenere invariato): ")
                if nuovo_anno:
                    libro.anno = int(nuovo_anno)
                print("Dettagli libro aggiornati.")
        else:
            print("Libro non trovato.")


libreria = Libreria()

# Esempi di utilizzo del programma:
libreria.aggiungi_libro()  # Aggiungi un libro
libreria.visualizza_libri()  # Visualizza tutti i libri
libreria.cerca_libro()  # Cerca un libro per titolo
libreria.gestione_libri()  # Gestisci un libro