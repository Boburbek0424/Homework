import requests

url='https://www.w3schools.com/'
res=requests.get(url)

with open('w3schoolpage.html',mode='wt', encoding='utf8') as file:
    file.write(res.text)