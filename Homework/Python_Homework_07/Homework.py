import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/"

resources = {
    "posts": "posts.csv",
    "comments": "comments.csv",
    "albums": "albums.csv",
    "photos": "photos.csv",
    "todos": "todos.csv",
    "users": "users.csv"
}

def fetch_and_save_data(resource, filename):
    response = requests.get(f"{url}{resource}")
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        
        df.to_csv(filename, index=False)
        print(f"Data for {resource} saved to {filename}")
    else:
        print(f"Failed to fetch data for {resource}")

for resource, filename in resources.items():
    fetch_and_save_data(resource, filename)

print("All data has been saved to CSV files.")
