import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

#Creazione dei dati e reshape
data = np.linspace(1, 100, 50)
reshaped_data = data.reshape(10, 5)
print("Matrice reshaped:")
print(reshaped_data)

#Normalizzazione
scaler = MinMaxScaler()
reshaped_data_normalized = scaler.fit_transform(reshaped_data)
print("\nMatrice normalizzata:")
print(reshaped_data_normalized)

#Rendiamo i dati normalizzati in interi
reshaped_data_int = np.round(reshaped_data_normalized * 100).astype(int)
print("\nMatrice con valori interi:")
print(reshaped_data_int)

#Ciclo per assicurarci che non ci siano duplicati
for i in range(reshaped_data_int.shape[0]):
    riga = reshaped_data_int[i]

    #Insieme che conserva i valori duplicati e ciclo while che li rimuove
    valori_duplicati = set()
    for j in range(len(riga)):
        #Cerca il valore con il while e assegna il nuovo valore
        while riga[j] in valori_duplicati:
            riga[j] = np.random.randint(0, 101)
        valori_duplicati.add(riga[j])

    reshaped_data_int[i] = riga

print("\nMatrice finale (valori unici per riga):")
print(reshaped_data_int)

#grafico
plt.figure(figsize=(8, 6))
plt.imshow(reshaped_data_int, cmap='viridis', aspect='auto')
plt.colorbar(label='Valori')
plt.title('Matrice Finale dei Dati')
plt.xlabel('Colonne')
plt.ylabel('Righe')
plt.show()