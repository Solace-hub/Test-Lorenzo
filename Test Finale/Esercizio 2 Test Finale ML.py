#Tutti gli import necessari
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#Caricamento del dataset
iris = load_iris()
X = iris.data
y = iris.target

#Esplorazione del dataset
print("Caratteristiche:", iris.feature_names)
print("Classi:", iris.target_names)
print(np.unique(y))
print(iris["DESCR"])

#Split del dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Pre-processing del dataset di addestramento
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#Principal Component Analysis per minimizzare le features
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

#Scelta del modello
model = RandomForestClassifier(random_state=42)

#Fine tuning degli iperparametri
param_grid = {
    "n_estimators": [100, 150, 200],
    "max_depth": [None, 10, 20, 30],
    'criterion': ['gini', 'entropy'],
    "max_features": ["sqrt", "log2", None]
}

kfold = KFold(n_splits=5, shuffle=True, random_state=42)

grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=kfold, scoring="accuracy", n_jobs=-1)
grid_search.fit(X_train_pca, y_train)

print("Migliori parametri trovati:", grid_search.best_params_)

#Migliori parametri trovati
opt_model = grid_search.best_estimator_

#Prediction
y_pred = opt_model.predict(X_test_pca)

#Classification Report
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

#Grafico con la matrice di confusione
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.title("Matrice di Confusione")
plt.xlabel("Predizione")
plt.ylabel("Verità")
plt.show()


