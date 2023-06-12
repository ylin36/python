# conda install beautifulsoup4
# conda install requests
# or
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.youtube.com/watch?v=NJ87xIPEEKQ'

# this doesn't work well with dynamic websites. need something like selenium to get site first.

def get_all_videos():
    """
    Get all videos
    """

    driver = webdriver.Chrome()
    driver.get(url)

    ## using selenium instead of original html
    # req = requests.get(url)
    # html = req.text
    # soup = BeautifulSoup(html, 'html.parser')

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    potentially_be_videos = soup.findAll('div')

    print(potentially_be_videos)


    links = {i.a['href']: i.text.strip()
                for i in potentially_be_videos if i.a}
    
    print(links)

    for link in links:
        s = '{title}: {url}'.format(title=links[link].encode('utf-8'),url=link)
        print(s)

    return links

if __name__ == '__main__':
    links = get_all_videos()