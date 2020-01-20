__author__ = 'matiasalvo'

import pandas as pd

products= pd.read_csv("data/order_products.csv")
orders = pd.read_csv("data/orders.csv")
shoppers = pd.read_csv("data/shoppers.csv")
store = pd.read_csv("data/storebranch.csv")

print(len(products))

print(orders.columns)


