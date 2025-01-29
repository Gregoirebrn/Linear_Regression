import matplotlib
matplotlib.use("TkAgg")  # Utiliser un backend non interactif
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data.csv", names=["km", "price"])  # Ajouter les colonnes si pas d'en-tête
print(df.describe())
print(df.dtypes)

df["km"] = pd.to_numeric(df["km"], errors="coerce")
df["price"] = pd.to_numeric(df["price"], errors="coerce")
print(df.dtypes)
plt.scatter(df["km"], df["price"], color='blue', label="Données")
plt.xlabel("km (km)")
plt.ylabel("price (€)")
plt.title("Relation between km and price")
plt.legend()
plt.grid()
plt.show()
