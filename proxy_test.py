import requests

proxies = {
    'https': 'http://103.252.1.137:3128'
}

response = requests.get("https://ipinfo.io/json", proxies=proxies)
print(response.json())
