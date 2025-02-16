# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1htgukvRwf3cQLlHSN4wXQK3sVuZpxcGW
"""

pip install pandas

import pandas as pd

# Read data from CSV files, ensuring file paths are correct
df_country = pd.read_csv('./Country.csv')  # Assuming Country.csv is in the same directory
df_market_trends = pd.read_csv('./Market.csv')  # Assuming Market.csv is in the same directory
df_product = pd.read_csv('./Product.csv')  # Assuming Product.csv is in the same directory


print("\nCountry Data:\n", df_country.head())
print("\nMarket Data:\n", df_market_trends.head())
print("\nProduct Data:\n", df_product.head())

!pip install matplotlib

import matplotlib.pyplot as plt

# Lấy dữ liệu GDP của các quốc gia
plt.figure(figsize=(12, 6))
plt.bar(df_country['CountryName'], df_country['GDP'], color='#1f77b4', edgecolor='black')
plt.xlabel('Country', fontsize=14, fontweight='bold')
plt.ylabel('GDP (in billion USD)', fontsize=14, fontweight='bold')
plt.title('GDP of Countries', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7, axis='y')
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
# Lấy dữ liệu tỷ lệ các loại thị trường
market_trends = df_market_trends['MarketType'].value_counts()
plt.figure(figsize=(10, 8))
plt.pie(
    market_trends,
    labels=market_trends.index,
    autopct='%1.1f%%',
    colors=['#4CAF50', '#FF5722', '#03A9F4', '#FFC107'],
    startangle=140,
    wedgeprops={'edgecolor': 'black'},
    textprops={'fontsize': 12, 'color': 'black'}
)
plt.title('Distribution of Market Types', fontsize=16, fontweight='bold')
plt.show()

import matplotlib.pyplot as plt
# Lấy dữ liệu giá và chi phí của sản phẩm
plt.figure(figsize=(10, 6))
plt.scatter(df_product['UnitPrice'], df_product['CostPrice'], color='darkorange', edgecolor='black', alpha=0.7)
plt.xlabel('Unit Price (USD)', fontsize=14, fontweight='bold')
plt.ylabel('Cost Price (USD)', fontsize=14, fontweight='bold')
plt.title('Unit Price vs. Cost Price of Products', fontsize=16, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
# Lấy dữ liệu phân phối giá của sản phẩm
plt.figure(figsize=(12, 6))
plt.hist(df_product['UnitPrice'], bins=10, color='#87CEEB', edgecolor='white', alpha=0.8)
plt.xlabel('Unit Price (USD)', fontsize=14, fontweight='bold')
plt.ylabel('Frequency', fontsize=14, fontweight='bold')
plt.title('Distribution of Product Prices', fontsize=16, fontweight='bold')
plt.grid(True, linestyle=':', color='gray', alpha=0.7)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
# Tạo DataFrame để tính số lượng thị trường theo quốc gia
market_counts = df_market_trends.groupby('CountryID').size()
country_names = df_country.set_index('CountryID').reindex(market_counts.index)['CountryName']

plt.figure(figsize=(12, 6))
plt.plot(country_names, market_counts, marker='o', linestyle='-', color='b')
plt.xlabel('Country', fontsize=14, fontweight='bold')
plt.ylabel('Number of Markets', fontsize=14, fontweight='bold')
plt.title('Number of Markets by Country', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

from google.colab import files

uploaded = files.upload()