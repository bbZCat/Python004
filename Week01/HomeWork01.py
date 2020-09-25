import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3&sortId=1'

response = requests.get(myurl, headers=header)
#print(response.text)

fulllist = []

if(response.status_code == 200):
    bs_info = bs(response.text, 'html.parser')
    for hover_tag in bs_info.find_all('div', attrs={'class':'movie-item-hover'}, limit=10):
        tag_info = hover_tag.find('div', ).text
        file_info = tag_info.split('\n')
        movie_name = file_info[2].strip()
        movie_type = file_info[7].strip()
        plan_date = file_info[15].strip()
        mylist = [movie_name, movie_type, plan_date]
        fulllist.append(mylist)

#print(fulllist)

if(len(fulllist)!=0):
    homework01 = pd.DataFrame(data = fulllist)
    homework01.to_csv('./HomeWork01.csv', encoding='utf8', index=False, header=False)

