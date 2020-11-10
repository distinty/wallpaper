import requests
import re
from lxml import etree

web_url = 'https://www.macapp.so'
base_url = 'https://www.macapp.so/wallpaper/'
session = requests.session()
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.83 Safari/537.36 "
}
req = session.get(url=base_url, headers=header)
req.encoding = req.apparent_encoding
html = req.text
html_etree = etree.HTML(html)
hrefs = html_etree.xpath('//div[@class="wrap wallpaper cfix"]/ul/li/a/@href')
pages = html_etree.xpath('//div[@class="page"]/a/@href')[-1]
pages = int(re.findall('/wallpaper/index_(.*?)\.html', pages)[0])
print(hrefs)
print(pages)

r = session.get(url=web_url + hrefs[0], headers=header)
r.encoding = r.apparent_encoding
detail_html = r.text

print(detail_html)
