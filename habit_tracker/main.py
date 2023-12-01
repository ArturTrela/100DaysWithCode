import requests
TOKEN = "qwertyuiop"
USERNAME = "arturt"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_params ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes",

}
# POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config={
    "id":GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN":TOKEN,
}
# graph_response = requests.post(url=graph_endpoint, json=graph_config,headers=headers )
# print(graph_response.text)

put_params={
    "date":"20231201",
    "quantity": "50.74",
}

#
# graph_put_endpoint =f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
# graph_put_response = requests.post(url=graph_put_endpoint,json=put_params,headers=headers)
# print(graph_put_response.text)

# DELETE
date = "20231201"
# graph_delete_endpoint = f'{graph_put_endpoint}/{date}'
# graph_delete_response = requests.delete(graph_delete_endpoint, headers=headers)
# print(graph_delete_response.text)

# PUT - UPDATE
update_params ={
    "quantity": "120",
}
# graph_update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}'
# graph_update_endpoint = requests.put(graph_update_endpoint,json=update_params,headers=headers)
# print(graph_update_endpoint.text)
