import pandas as pd
import numpy as np

# Sample dataset
data = {
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red', 'Green'],
    'Size': ['S', 'M', 'L', 'S', 'M', 'L']
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)

# ---- Label Encoding ----
def label_encode(column):
    unique_vals = {val: idx for idx, val in enumerate(sorted(column.unique()))}
    return column.map(unique_vals), unique_vals

df['Color_Label'], color_map = label_encode(df['Color'])
df['Size_Label'], size_map = label_encode(df['Size'])

print("\nLabel Encoded:")
print(df[['Color', 'Color_Label', 'Size', 'Size_Label']])
print("\nEncoding Maps:")
print("Color:", color_map)
print("Size:", size_map)

# ---- One-Hot Encoding ----
def one_hot_encode(column):
    unique_vals = sorted(column.unique())
    return pd.DataFrame({f"{column.name}_{val}": (column == val).astype(int) for val in unique_vals})

color_onehot = one_hot_encode(df['Color'])
size_onehot = one_hot_encode(df['Size'])

# Combine with original data
df_encoded = pd.concat([df, color_onehot, size_onehot], axis=1)
print("\nOne-Hot Encoded Data:")
print(df_encoded)
