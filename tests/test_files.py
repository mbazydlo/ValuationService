from read_csv import rewrite_csv_to_df
from app import deal_with_data
import os
import pandas

def test_rewrite_csv_to_df():
    result = rewrite_csv_to_df()
    assert type(result) == pandas.core.frame.DataFrame

def test_deal_with_data():
    deal_with_data()
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assert 'top_products.csv' in os.listdir(path)
