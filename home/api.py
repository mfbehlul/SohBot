import requests
import json
while True:
    url = "https://sohbot.azurewebsites.net/qnamaker/knowledgebases/0ae40fea-8309-45cd-a3c8-b994b75f0801/generateAnswer"
    question=input("Lütfen sormak istediğiniz soruyu giriniz.")
    payload = json.dumps({
    "question": question
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'EndpointKey 7a814204-45c3-413c-be1c-9dbf46b83645',
    'Cookie': 'ARRAffinity=0f60b0add9cb5787812ad43041e37f1a658566dfb27a2b04d44e3e12f2d4257d; ARRAffinitySameSite=0f60b0add9cb5787812ad43041e37f1a658566dfb27a2b04d44e3e12f2d4257d'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)