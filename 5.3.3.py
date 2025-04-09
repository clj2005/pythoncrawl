import requests
url="http://www.baidu.com"
response=requests.get(url)
response.encoding="utf-8"
content=response.text
print(content)