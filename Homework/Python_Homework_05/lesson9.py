import requests
import pandas as pd

# Define the base URL for JSONPlaceholder
base_url = "https://jsonplaceholder.typicode.com/"

# Define the resources and the corresponding CSV file names
resources = {
    "posts": "posts.csv",
    "comments": "comments.csv",
    "albums": "albums.csv",
    "photos": "photos.csv",
    "todos": "todos.csv",
    "users": "users.csv"
}

# Function to fetch data and save it to CSV
def fetch_and_save_data(resource, filename):
    # Make a GET request to fetch data from the API
    response = requests.get(f"{base_url}{resource}")
    
    # If the request was successful, process the data
    if response.status_code == 200:
        data = response.json()
        
        # Convert data to a pandas DataFrame
        df = pd.DataFrame(data)
        
        # Save the DataFrame to a CSV file
        df.to_csv(filename, index=False)
        print(f"Data for {resource} saved to {filename}")
    else:
        print(f"Failed to fetch data for {resource}")

# Fetch and save data for each resource
for resource, filename in resources.items():
    fetch_and_save_data(resource, filename)

print("All data has been saved to CSV files.")
