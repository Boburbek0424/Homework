import pandas as pd
import matplotlib.pyplot as plt

# Creating a dataframe
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}
df2 = pd.DataFrame(data2)

# Exercise 1
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print("Total sales for each product:\n", total_sales)
print('-'*50)
# Exercise 2
df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
highest_sales_date = df2.loc[df2['Total_Sales'].idxmax(), 'Date']
print("Date with the highest total sales:", highest_sales_date)
print('-'*50)
# Exercise 3
percentage_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
print("Percentage change in sales for each product:\n", percentage_change)
print('-'*50)
# Exercise 4
plt.figure(figsize=(10, 6))
for product in ['Product_A', 'Product_B', 'Product_C']:
    plt.plot(df2['Date'], df2[product], label=product)

plt.title('Sales Trends for Each Product Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
