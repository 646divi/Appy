from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import requests



base_url="https://apkpure.com"
# /search?q=whatsapp
base_url1="https://www.apksum.com"
#/search?q=


def paid_mod_games(app_name):
    app_name=app_name.split(' ')
    app_name='+'.join(app_name).lower()
# /search?q=
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36'
    }
    url=base_url1+"/search?q="+app_name
    page_data=requests.get(url,headers=headers)
    # print(page_data.content)
    page_data=soup(page_data.content,'html.parser')
    # print(page_data)]

    left=page_data.find('div',class_="left")
    # print(box)
    ui=left.findAll('ul',class_="category-template may2")[0]
    # print(ui)
    div=ui.find_all('div',class_="category-template-title")[0]
    # print(div)
    a=div.find('a')
    # print(a.attrs)
    title=a.attrs['title']
    page_link=base_url1+a.attrs['href']
    print(page_link)

    download_page=requests.get(page_link,headers=headers)
    download_page=soup(download_page.content,'html.parser')
    # print(download_page)

    try:
        download_link=download_page.find('div',class_="ny-down")
        # print(download_link)
        link=download_link.find('a',class_="ga da")
        return base_url1+link.attrs['href'], title.lower()

    except Exception:
        # print(Exception)
        return Exception
    

link=paid_mod_games("pokemongo")
print(type(link))