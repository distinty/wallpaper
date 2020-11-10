import requests
import re
from lxml import etree
from time import sleep
import random

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

# for i in range(2, pages + 1):
#     # https://www.macapp.so/wallpaper/index_2.html
#     r = requests.get(url=base_url + "index_" + i + ".html", headers=header)
#
#     r.encoding = req.apparent_encoding  # 设置编码
#     html = r.text  # 提取文本
#     html_etree = etree.HTML(html)
#     hrefs = html_etree.xpath('//div[@class="wrap wallpaper cfix"]/ul/li/a/@href')  # # 每页的列表

# print(hrefs)
# print(pages)
sleep(1.12)
r = session.get(url=web_url + hrefs[1], headers=header)
r.encoding = r.apparent_encoding
detail_html = r.text
detail_html_etree = etree.HTML(detail_html)
href_img = detail_html_etree.xpath('//div[@class="wrap bimg cfix"]/p/a/@href')[0]

print(href_img)


def openDetail(list):
    for i in list:
        r = requests.get(url=web_url + i, headers=header)
        r.encoding = r.apparent_encoding
        html = r.text
        html_etree = etree.HTML(html)
        # https://static.torrentsky.com/bizhi/MacWallpaper_WWDC2020_FlareZephyr.png
        href_img = html_etree.xpath('//div[@class="wrap bimg cfix"]/p/a/@href')[0]


def saveImg(imgUrl):
    r = requests.get(url=imgUrl, headers=header)
    fileName = imgUrl.split("/")[-1]
    try:
        with open(fileName, 'wb') as f:
            f.write(r.content)
            f.close()
    except FileExistsError:
        with open(fileName + str(random.random()) + ".png", 'wb') as f:
            f.write(r.content)
            f.close()
