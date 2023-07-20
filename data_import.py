# import urllib
import urllib.request

# import iris dataset into in einen Ordner
urllib.request.urlretrieve("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
                           "./data/iris.data")

# import von Pandas
import pandas as pd

# csv einlesen
df = pd.read_csv("./data/iris.data")
print(df.head())

# Spaltennamen hinzufügen
df = pd.read_csv("./data/iris.data", header=None)
print(df.head())
names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df.columns = names

# Ausgabe ersten 5 Datensätze, Infos und Auswertung
print(df.head())
print(df.info())
print(df.describe())
