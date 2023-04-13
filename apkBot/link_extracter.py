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


# appp_name="call of duty"
# link,title=paid_mod_games(appp_name)
# if(appp_name in title):
#     print(link,title)

# print(link,title) 

def get_simple_apps_games(app_name):
    app_name=app_name.split(' ')
    app_name='+'.join(app_name).lower()
    page_link=base_url+"/search?q="+app_name
    req=Request(url=page_link,headers={'User-Agent': 'Mozilla/5.0'})
    page_content=urlopen(req)
    raw_data=page_content.read()
    data=soup(raw_data,'html.parser')
    page_content.close()
    # print(page_link)
    # print(data)
    try:

        download_page=data.find_all('div',class_="first-info brand-info")[0]
        # print(download_page)
        a=download_page.find_all('a',class_="da")[0]
        # print(a.attrs['href'])
        # print(base_url+a.attrs['href'])
        req=Request(base_url+a.attrs['href'],headers={'User-Agent': 'Mozilla/5.0'})
        download_page_content=urlopen(req)
        download_page_raw_data=download_page_content.read()
        download_page_content.close()
        download_page_data=soup(download_page_raw_data,'html.parser')
        # print(download_page_data)
        dl=download_page_data.find_all('dl',class_="ny-dl ny-dl-n")[0]
        # print(dl)
        apk_link=dl.find_all('a',class_="da")[0]
        # print(apk_link.attrs['href'])

        return base_url+apk_link.attrs['href']

    except Exception:
        return Exception




keyboard_options=[["Apps and Games"],["Paid games"]]




# apk_link=get_link("facebook")
# print(apk_link)