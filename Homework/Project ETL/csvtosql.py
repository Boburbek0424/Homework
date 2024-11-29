import os
import pandas as pd
import pyodbc
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# SQL Server connection setup
SQL_SERVER = "BOBURBEK\\SQLEXPRESS"
DATABASE = "CsvToSQL"
USERNAME = "Boburbek Hakimov"
PASSWORD = "81339447"
CONNECTION_STRING = f"DRIVER={{SQL Server}};SERVER={SQL_SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}"

def create_table_and_insert_data(file_path, conn):
    # Extract table name from the file name
    table_name = os.path.splitext(os.path.basename(file_path))[0]

    # Load CSV data
    df = pd.read_csv(file_path)

    # Create table if not exists
    columns = ", ".join([f"[{col}] NVARCHAR(MAX)" for col in df.columns])
    create_table_query = f"CREATE TABLE [{table_name}] ({columns});"

    try:
        with conn.cursor() as cursor:
            # Check if the table exists, and create it if not
            cursor.execute(
                f"IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='{table_name}' AND xtype='U') BEGIN {create_table_query} END"
            )
            conn.commit()

        # Insert data into the table
        for _, row in df.iterrows():
            placeholders = ", ".join(["?"] * len(row))
            insert_query = f"INSERT INTO [{table_name}] VALUES ({placeholders})"
            with conn.cursor() as cursor:
                cursor.execute(insert_query, tuple(row))
            conn.commit()

        print(f"Data from {file_path} inserted into {table_name} successfully.")
    except Exception as e:
        print(f"Error while processing {file_path}: {e}")

class CSVHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.csv'):
            print(f"New file detected: {event.src_path}")
            try:
                conn = pyodbc.connect(CONNECTION_STRING)
                create_table_and_insert_data(event.src_path, conn)
                conn.close()
            except Exception as e:
                print(f"Error connecting to the database: {e}")

if __name__ == "__main__":
    # Set the folder to watch for new CSV files
    folder_to_watch = r"C:\Users\Boburbek Hakimov\Downloads"

    event_handler = CSVHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=False)
    observer.start()

    print(f"Watching folder: {folder_to_watch}")
    try:
        while True:
            pass  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
