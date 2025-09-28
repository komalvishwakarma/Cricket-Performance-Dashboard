import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"
headers = {
    "X-RapidAPI-Key": "5740a65ae6msh99f186348d59578p1446d2jsnbcdc5a0f8ff6",  # Replace this with your actual key
    "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())