import pandas as pd
import matplotlib.pyplot as plt


data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}
df4 = pd.DataFrame(data4)

# Exercise 1
total_revenue = df4['Total_Price'].sum()
print("Total revenue from all orders:", total_revenue)
print('-'*50)
# Exercise 2
most_ordered_product = df4['Product'].mode()[0]
print("Most ordered product:", most_ordered_product)
print('-'*50)
# Exercise 3
average_quantity = df4['Quantity'].mean()
print("Average quantity of products ordered:", average_quantity)


# Exercise 4
sales_by_product = df4.groupby('Product')['Total_Price'].sum()
plt.figure(figsize=(8, 8))
sales_by_product.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Sales Across Different Products')
plt.ylabel('')
plt.tight_layout()
plt.show()
