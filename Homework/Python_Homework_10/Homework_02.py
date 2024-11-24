import pandas as pd

# Create DataFrame
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}
df3 = pd.DataFrame(data3)

# Exercise 1
avg_salary_per_dept = df3.groupby('Department')['Salary'].mean()
print("Average salary for each department:\n", avg_salary_per_dept)
print('-'*50)
# Exercise 2
employee_with_most_experience = df3.loc[df3['Experience (Years)'].idxmax()]
print("Employee with the most experience:\n", employee_with_most_experience[['Name', 'Experience (Years)']])
print('-'*50)
# Exercise 3
min_salary = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary) * 100
print("Data with 'Salary Increase' column:\n", df3[['Name', 'Salary', 'Salary Increase']])
import matplotlib.pyplot as plt

# Exercise 4
department_counts = df3['Department'].value_counts()

plt.figure(figsize=(8, 6))
department_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Employees Across Departments')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
