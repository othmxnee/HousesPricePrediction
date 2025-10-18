import kagglehub
import pandas as pd

# # Download latest version
# path = kagglehub.dataset_download("dansbecker/melbourne-housing-snapshot")

# print("Path to dataset files:", path)

melbourne_data = pd.read_csv('/home/othmane/.cache/kagglehub/datasets/dansbecker/melbourne-housing-snapshot/versions/5/melb_data.csv')
print(melbourne_data.describe())

