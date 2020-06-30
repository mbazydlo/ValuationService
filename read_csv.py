import os
import pandas as pd

path = os.path.dirname(os.path.abspath(__file__))
csv_dir = os.path.join(path, 'csv_files')

csv_files = [pd.read_csv(os.path.join(csv_dir, file)) for file in os.listdir(csv_dir)]

concat = pd.concat(csv_files, ignore_index=True)

print(concat)

