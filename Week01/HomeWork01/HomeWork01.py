import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = 'User-Agent:Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11' 
header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?sortId=1'
#myurl = 'https://maoyan.com/films?showType=3&sortId=1'

response = requests.get(myurl, headers=header)
#print(response.text)

fulllist = []

if(response.status_code == 200):
    bs_info = bs(response.text, 'html.parser')
    for hover_tag in bs_info.find_all('div', attrs={'class':'movie-item-hover'}, limit=10):
        tag_info = hover_tag.find('div', ).text
        film_info = tag_info.split('\n')
        movie_name = film_info[2].strip()
        movie_type = film_info[7].strip()
        plan_date = film_info[15].strip()
        mylist = [movie_name, movie_type, plan_date]
        fulllist.append(mylist)

#print(fulllist)

if(len(fulllist)!=0):
    homework01 = pd.DataFrame(data = fulllist)
    homework01.to_csv('./HomeWork01.csv', encoding='utf8', index=False, header=False)

