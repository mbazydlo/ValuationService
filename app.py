import pandas as pd
from read_csv import rewrite_csv_to_df
import os

def deal_with_data():
    df = rewrite_csv_to_df()
    df['total_price'] = df['price'] * df['quantity']
    products_max = df.loc[df.groupby(['matching_id'])['total_price'].idxmax()]
    products_max = products_max.set_index('currency')
    
    for currency in df['currency'].dropna().unique():
        avg = df[df['currency'] == currency]['price'].mean()
        products_max.loc[currency,'avg_price'] = avg
        print(products_max)

    df = products_max[['matching_id','total_price','avg_price']]
    df.to_csv('top_products.csv', sep=';')


deal_with_data()
