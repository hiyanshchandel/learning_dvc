import os
import pandas as pd

#create a simple dataframe with column names

data = {
    'Name' : ['Alice', 'Bob', 'charlie'],
    'Age' : [25, 30, 35],
    'City' : ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

#to ensure the "data" directory exists at the root level
data_dir = 'data'

os.makedirs(data_dir, exist_ok = True) #exist = True means it won't raise an error if the directory already exists and will not overwrite it

#define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)  #index = False means it won't write row indices to the file

print("csv file created successfully at:", file_path) 