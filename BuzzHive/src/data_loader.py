import pandas as pd

def load_data(file_path):
    try:
        data = pd.read_csv(file_path, on_bad_lines='skip')
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
