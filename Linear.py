import matplotlib
matplotlib.use("TkAgg")  # Utiliser un backend non interactif
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

theta_0 = 1   # Ordonnée à l'origine
theta_1 = 0  # Pente (influence du kilométrage sur le prix)

# Hyperparamètres
learning_rate = 0.0000001  # Petit pas pour éviter d'aller trop vite
iterations = 1000  # Nombre d'itérations pour l'entraînement

df = pd.read_csv("data.csv", names=["km", "price"])  # Ajouter les colonnes si pas d'en-tête
print(df.describe())
print(df.dtypes)

estimated_prices = []
mils = []
m = len(df)
for _, row in df.iterrows():
    mil = row["price"]
    mils = np.array(mil)

# On prend tout les erreurs et on en fait une moyenne
errors = []
for i in range(iterations):
    error = 0
    for (price, (_, row)) in zip(estimated_prices, df.iterrows()):
        mileage = row["km"]
        estimated_price = theta_1 + theta_0 * mileage
        estimated_prices.append(estimated_price)
        estim = row["price"]
        errors.append(price - estim)
    # Mise à jour des paramètres
    theta_0 -= learning_rate * np.sum(errors) / m
    theta_1 -= learning_rate * np.sum(errors * mils) / m


for i in estimated_prices:
    print(i)
