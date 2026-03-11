import requests

url = "https://mc3f9k8p9q1g.rest.marketingcloudapis.com/data/v1/async/dataextensions/key:DE_CARRINHO_ABANDONO/rows"

headers = {
    "Authorization": "Bearer ACCESS_TOKEN_SFMC",
    "Content-Type": "application/json"
}

payload = {
    "items": [
        {
            "SubscriberKey": "cliente_983746",
            "checkout_id": "chk_874563",
            "email": "cliente@email.pt",
            "created_at": "2024-09-15T10:12:00Z",
            "abandoned_at": "2024-09-15T11:12:00Z",
            "total_value": 79.90
        }
    ]
}

requests.post(url, json=payload, headers=headers)
