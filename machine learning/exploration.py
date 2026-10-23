import pandas as pd
with open("train.csv","r") as file:
    data = pd.read_csv(file)
    print(data.describe())