import requests
from bs4 import BeautifulSoup as soup
from requests_html import AsyncHTMLSession
import pyppdf.patch_pyppeteer
from typing import Awaitable
import asyncio
import webbrowser
import time

print("hey")

#html_content = f"<html> <head> </head> <"

search = str(input("what are you looking for today?: "))

url = "https://www.aliexpress.com/af/" + search + ".html"
#print(url)

async def main():
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

        asession = AsyncHTMLSession()
        r = await asession.get(url, headers=headers)

        await r.html.arender()
        h1 = r.html.find('._9tla3')

        sheet = []
        i=0
        for item in h1:
                newItem = str(item)
                start = newItem.find("href='") + len("href='")
                end = newItem.find("' target='_blank'")

                link = "http://aliexpress.com" + newItem[start:end]
                sheet.append(link)
        time.sleep(8)
        return(sheet)



async def main2():

        urlList = await main()
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
        #print(urlList)

        for link in urlList:

                asession = AsyncHTMLSession()
                r = await asession.get(link, headers=headers)


                await r.html.arender()

                if r.html.find('.video-wrap') == -1:
                        continue
                else:
                        h1 = r.html.find('.disable-download')
                        #print(h1)

                newItem = str(h1)
                start = newItem.find("src='") + len("src='")
                end = newItem.find("' style='background")

                link = newItem[start:end]
                print(link)

                webbrowser.open(link, new=2)
                time.sleep(8)






asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_until_complete(main2())