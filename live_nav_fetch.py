import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)
data = response.json()


scheme_name = data["meta"]["scheme_name"]
latest_nav = data["data"][0]["nav"]
latest_date = data["data"][0]["date"]

print("Scheme:", scheme_name)
print("Latest NAV:", latest_nav)
print("Date:", latest_date)

df = pd.DataFrame(data["data"])
df.to_csv("Data/Processed/live_nav.csv", index = False)

print("CSV Saved Successfully")