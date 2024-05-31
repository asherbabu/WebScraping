import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/city/delhi"

fetchAndSaveToFile(url, "data/times1.html")