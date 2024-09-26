import matplotlib.pyplot as plt
import pandas as pd
import os
import seaborn as sns

path = str(os.path.dirname(__file__) + '/Housing.csv')
data = pd.read_csv(path)

colTBC = ("mainroad","guestroom","basement","hotwaterheating","airconditioning","prefarea","furnishingstatus")
for col in colTBC:
    data[col]=data[col].astype('category')

def createHistogram(data: pd.DataFrame, column: str):
    price = data['price']
    axis_second = data[column]

    fig, ax = plt.subplots()
    ax.set_xlabel('price')
    ax.set_ylabel(column)
    ax.set_title(str('price/'+column))

    hist = ax.hist2d(price, axis_second, bins=30)

def getAvgHousePrice(data: pd.DataFrame, column: str):
    data = data[['price', column]]

    data.groupby(column).mean().plot(kind='bar')

createHistogram(data, 'area')
createHistogram(data, 'bedrooms')
createHistogram(data, 'stories')
getAvgHousePrice(data, 'bathrooms')
getAvgHousePrice(data, 'furnishingstatus')

data[["mainroad","guestroom","basement","hotwaterheating","airconditioning","prefarea","furnishingstatus"]] = data[["mainroad","guestroom","basement","hotwaterheating","airconditioning","prefarea","furnishingstatus"]].apply(lambda x: pd.factorize(x)[0])

sns.heatmap(data.corr())

plt.show()