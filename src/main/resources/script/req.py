import requests



response = requests.get("https://api.github.com")
result = response.content


