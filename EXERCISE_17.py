import requests
from bs4 import BeautifulSoup
import lxml

link = 'http://www.nytimes.com/'
get_link = requests.get(link)
get_html = get_link.text

get_soup = BeautifulSoup(get_html,features="html.parsel")
get_titles = get_soup.find_all(class =="balancedHeadline")

for line in lines:
    print(title.text)