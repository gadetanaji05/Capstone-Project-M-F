import requests

schemes = {
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841
}
for name ,code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    data = response.json()

    print("\nscheme:",name)
    print("Latest NAV:", data["data"][0]["nav"])
    print("Date:", data["data"][0]["date"])