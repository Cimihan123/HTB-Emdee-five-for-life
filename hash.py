import requests
from bs4 import BeautifulSoup
import hashlib
import re

#change the port accordingly
url="http://139.59.202.58:31744/"
req=requests.session()
r=req.get(url)

#scraping hash
soup=BeautifulSoup(r.text,'html.parser')
result=(soup.find('h3',attrs={'align':'center'}))
a=[i for i in result][0]

print("The hash is",a,end="\n\n")
#encrpyting md5 hash
ok=hashlib.md5(a.encode('utf-8')).hexdigest()
print("The md5 is",ok,end="\n\n")

#flag
data=dict(hash=ok)
rpost=req.post(url=url,data=data)

b=rpost.content

#flag by regex

print("The flag is",re.findall(b'HTB\{.*\}',b)[0])

