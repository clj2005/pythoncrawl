import urllib.request
url="http://www.baidu.com"
respose=urllib.request.urlopen(url)
content=respose.read().decode('utf-8')
print(content)