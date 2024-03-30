import requests

response = requests.post(
    "http://localhost:5000/mindmap/invoke",
    json={'input':{'topic': 'LangSmith'}}
    )

print(response.json()["output"]["content"])