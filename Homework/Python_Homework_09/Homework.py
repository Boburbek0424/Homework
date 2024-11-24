import sqlite3
import pandas as pd

conn = sqlite3.connect('population.db')
cursor = conn.cursor()

# 1
query_florida_females = """
SELECT first_name AS FirstName, last_name AS LastName, salary AS Salary, gender AS Gender, state AS State
FROM population
WHERE state = 'Florida' AND gender = 'Female'
"""
florida_females_df = pd.read_sql_query(query_florida_females, conn)

# 2
query_apache_emails = """
SELECT gender, COUNT(*) 
FROM population
WHERE email LIKE '%@apache.org'
GROUP BY gender
"""
apache_email_gender_count = pd.read_sql_query(query_apache_emails, conn)

# 3
query_males_over_1M = """
SELECT COUNT(*) 
FROM population
WHERE gender = 'Male' AND salary > 1000000
"""
males_earning_over_1M = pd.read_sql_query(query_males_over_1M, conn).iloc[0, 0]

# 4
query_alabama_females_under_800K = """
SELECT first_name AS FirstName, last_name AS LastName, salary AS Salary
FROM population
WHERE state = 'Alabama' AND gender = 'Female' AND salary < 800000
"""
alabama_females_under_800K_df = pd.read_sql_query(query_alabama_females_under_800K, conn)

# 5
query_texas_hotmail = """
SELECT COUNT(*) 
FROM population
WHERE state = 'Texas' AND email LIKE '%@hotmail.com'
"""
texas_hotmail_count = pd.read_sql_query(query_texas_hotmail, conn).iloc[0, 0]

# 6
query_california_males_salary_range = """
SELECT * 
FROM population
WHERE state = 'California' AND gender = 'Male' AND salary BETWEEN 400000 AND 900000
"""
california_males_in_salary_range_df = pd.read_sql_query(query_california_males_salary_range, conn)

# 7
query_ny_females_over_500K = """
SELECT COUNT(*) 
FROM population
WHERE state = 'New York' AND gender = 'Female' AND salary > 500000
"""
new_york_females_over_500K_count = pd.read_sql_query(query_ny_females_over_500K, conn).iloc[0, 0]

# 8
query_georgia_top_10 = """
SELECT first_name AS FirstName, last_name AS LastName, salary AS Salary
FROM population
WHERE state = 'Georgia'
ORDER BY salary DESC
LIMIT 10
"""
georgia_top_10_highest_paid_df = pd.read_sql_query(query_georgia_top_10, conn)

# 9
query_last_name_s_high_salary = """
SELECT COUNT(*) 
FROM population
WHERE last_name LIKE 'S%' AND salary > 300000
"""
last_name_starting_with_s_high_salary_count = pd.read_sql_query(query_last_name_s_high_salary, conn).iloc[0, 0]

# 10
query_avg_salary_females_oklahoma = """
SELECT AVG(salary)
FROM population
WHERE state = 'Oklahoma' AND gender = 'Female'
"""
average_salary_females_oklahoma = pd.read_sql_query(query_avg_salary_females_oklahoma, conn).iloc[0, 0]

# 11
query_florida_net_emails = """
SELECT * 
FROM population
WHERE state = 'Florida' AND email LIKE '%.net'
"""
florida_net_emails_df = pd.read_sql_query(query_florida_net_emails, conn)

# 12
query_k_names_high_salary = """
SELECT COUNT(*) 
FROM population
WHERE first_name LIKE 'K%' AND salary > 1000000
"""
count_k_names_with_high_salary = pd.read_sql_query(query_k_names_high_salary, conn).iloc[0, 0]

# 13
query_gmail_low_salary = """
SELECT * 
FROM population
WHERE email LIKE '%gmail.com%' AND salary < 200000
"""
gmail_users_with_low_salary_df = pd.read_sql_query(query_gmail_low_salary, conn)

# 14
query_min_salary_males_ohio = """
SELECT MIN(salary)
FROM population
WHERE state = 'Ohio' AND gender = 'Male'
"""
min_salary_for_males_in_ohio = pd.read_sql_query(query_min_salary_males_ohio, conn).iloc[0, 0]

# 15
query_females_california_800K = """
SELECT COUNT(*) 
FROM population
WHERE state = 'California' AND gender = 'Female' AND salary > 800000
"""
females_in_california_with_salary_above_800K_count = pd.read_sql_query(query_females_california_800K, conn).iloc[0, 0]

# 16
query_males_over_1_2M = """
SELECT last_name AS LastName, salary AS Salary
FROM population
WHERE gender = 'Male' AND salary > 1200000
"""
males_earning_over_1_2M_df = pd.read_sql_query(query_males_over_1_2M, conn)

# 17
query_edu_high_salary = """
SELECT * 
FROM population
WHERE email LIKE '%edu%' AND salary > 1500000
"""
edu_domain_users_with_high_salary_df = pd.read_sql_query(query_edu_high_salary, conn)

# 18
query_alabama_low_salary = """
SELECT COUNT(*) 
FROM population
WHERE state = 'Alabama' AND salary < 100000
"""
alabama_users_with_low_salary_count = pd.read_sql_query(query_alabama_low_salary, conn).iloc[0, 0]

# 19
query_last_name_n_high_salary = """
SELECT * 
FROM population
WHERE last_name LIKE '%n' AND salary > 600000
"""
users_with_last_name_ending_in_n_and_high_salary_df = pd.read_sql_query(query_last_name_n_high_salary, conn)

# 20
query_max_salary_dc = """
SELECT MAX(salary)
FROM population
WHERE state = 'District of Columbia'
"""
max_salary_in_dc = pd.read_sql_query(query_max_salary_dc, conn).iloc[0, 0]

# 21
query_ny_females_salary_range = """
SELECT first_name AS FirstName, last_name AS LastName, salary AS Salary
FROM population
WHERE state = 'New York' AND gender = 'Female' AND salary BETWEEN 500000 AND 1000000
"""
new_york_females_with_salary_between_500K_and_1M_df = pd.read_sql_query(query_ny_females_salary_range, conn)

# 22
query_texas_yahoo_count = """
SELECT COUNT(*) 
FROM population
WHERE state = 'Texas' AND email LIKE '%yahoo.com%'
"""
texas_yahoo_count = pd.read_sql_query(query_texas_yahoo_count, conn).iloc[0, 0]

# 23
query_avg_male_salary_ca = """
SELECT AVG(salary)
FROM population
WHERE state = 'California' AND gender = 'Male'
"""
average_male_salary_in_ca = pd.read_sql_query(query_avg_male_salary_ca, conn).iloc[0, 0]

# 24
query_below_avg_salary_ca = """
SELECT * 
FROM population
WHERE state = 'California' AND salary < ?
"""
users_below_average_male_salary_in_ca_df = pd.read_sql_query(query_below_avg_salary_ca, conn, params=(average_male_salary_in_ca,))

conn.close()

# Printing the results
print(f"Florida Females:\n{florida_females_df}")
print(f"Apache Emails Gender Count:\n{apache_email_gender_count}")
print(f"Males earning over 1M: {males_earning_over_1M}")
print(f"Alabama Females under 800K:\n{alabama_females_under_800K_df}")
print(f"People from Texas with Hotmail email: {texas_hotmail_count}")
print(f"California Males earning between 400K and 900K:\n{california_males_in_salary_range_df}")
print(f"Females from New York with salary over 500K: {new_york_females_over_500K_count}")
print(f"Top 10 highest-paid people from Georgia:\n{georgia_top_10_highest_paid_df}")
print(f"People with last names starting with S and earning > 300K: {last_name_starting_with_s_high_salary_count}")
print(f"Average salary of females in Oklahoma: {average_salary_females_oklahoma}")
print(f"People from Florida with .net emails:\n{florida_net_emails_df}")
print(f"People with first names starting with K and earning over 1M: {count_k_names_with_high_salary}")
print(f"People with Gmail email and salary below 200K:\n{gmail_users_with_low_salary_df}")
print(f"Minimum salary for males in Ohio: {min_salary_for_males_in_ohio}")
print(f"Females from California with salary above 800K: {females_in_california_with_salary_above_800K_count}")
print(f"Males earning over 1.2M:\n{males_earning_over_1_2M_df}")
print(f"People with edu emails earning over 1.5M:\n{edu_domain_users_with_high_salary_df}")
print(f"People in Alabama earning below 100K: {alabama_users_with_low_salary_count}")
print(f"People with last names ending in 'n' and salary > 600K:\n{users_with_last_name_ending_in_n_and_high_salary_df}")
print(f"Highest salary in DC: {max_salary_in_dc}")
print(f"Females from New York with salaries between 500K and 1M:\n{new_york_females_with_salary_between_500K_and_1M_df}")
print(f"People from Texas with Yahoo email: {texas_yahoo_count}")
print(f"People below average salary for males in CA:\n{users_below_average_male_salary_in_ca_df}")
