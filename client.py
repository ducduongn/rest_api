import requests

url = "http://localhost:5000/posts"

headers = {
        "cache-control": "no-cache",
        "x-dreamfactory-api-key": "YOUR_API_KEY"
}

response = requests.request("GET", url, headers=headers)

print(response.text)