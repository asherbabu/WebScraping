import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}

requests.get("https://api64.ipify.org?format=json", proxies=proxies)