
import os
import requests

DATA_URL = "https://01.tomorrow-school.ai/api/content/root/public/subjects/ai/time-series/data/AAPL.csv"
DATA_DIR = "../data"
FILE_PATH = os.path.join(DATA_DIR, "AAPL.csv")

def download_data():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    print(f"Downloading data from {DATA_URL}...")
    response = requests.get(DATA_URL)
    
    if response.status_code == 200:
        with open(FILE_PATH, "wb") as f:
            f.write(response.content)
        print(f"Data save to {FILE_PATH}")
    else:
        print(f"Failed to download data. Status code: {response.status_code}")

if __name__ == "__main__":
    download_data()
