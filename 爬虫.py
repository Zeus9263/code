import requests  # 导入requests包
from bs4 import BeautifulSoup

proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.110 Safari/537.36'}
response: object = request.get(url,headers=headers)
response = requests.get(url, proxies=proxies)
url = 'http://www.cntour.cn/'
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text, 'lxml')
data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
print(data)
for item in data:
    result = {
        'title': item.get_text(),
        'link': item.get('href')
    }
print(result)
import re

for item in data:
    result = {
        "title": item.get_text(),
        "link": item.get('href'),
        'ID': re.findall('\d+', item.get('href'))
    }
print(result)
