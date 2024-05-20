import requests

response = requests.get(url="https://opentdb.com/api.php",params={"amount":10,"type":"boolean","category":18})

response.raise_for_status()
data = response.json()
question_data =data["results"]
