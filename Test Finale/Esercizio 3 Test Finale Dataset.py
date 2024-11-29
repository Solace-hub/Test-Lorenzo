#Tutti gli import necessari
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Generazione dei numeri approssimandoli
data = np.linspace(1, 100, 50)
data = np.round(data).astype(int)
print(data)

#Reshape dei data
reshaped_data = data.reshape(10, 5)
print(reshaped_data)

#Ciclo for per evidenziare duplicati e quindi assicurarci la diversità dei numeri
for riga in reshaped_data:
  if len(np.unique(riga)) != len(riga):
    print(f"Ho trovato questi duplicati nella riga {riga}")
  else:
    print(f"Tutto ok qui: {riga}")

#Stampa del dataset
print("Il dataset è il seguente: ", reshaped_data)

#Grafico che mostra il dataset
plt.plot(np.arange(50), data, marker='o', linestyle='-', color='b')
plt.title('Grafico dei dati generati')
plt.xlabel('Posizioni')
plt.ylabel('Valori')
plt.show()