import requests
from datetime import datetime

USERNAME = "subhamdash"
TOKEN = "hjer34h3euis34kd4kjdj43" 
GRAPH_ID = "graph43"
pixela_endpoint = "https://pixe.la/v1/users"
user_param = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
    
}
# response = requests.post(url=pixela_endpoint,json=user_param)

graph_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Programing Graph",
    "unit":"min",
    "type":"int",
    "color":"sora",
}
headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_enpoint,json=graph_config,headers=headers)
# print(response.text)

pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today =  datetime.now()

pixela_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many minutes did you code today? "),
}

response = requests.post(url=pixela_creation_endpoint,json=pixela_data,headers=headers)
print(response.text)

update_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{pixela_data['date']}"

new_pixela_data = {
    "quantity":"23"
}

# response = requests.put(url=update_enpoint,json=new_pixela_data,headers=headers)
# print(response.text)

delete_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{pixela_data['date']}"

# response = requests.delete(url=delete_enpoint,headers=headers)
# print(response.text)