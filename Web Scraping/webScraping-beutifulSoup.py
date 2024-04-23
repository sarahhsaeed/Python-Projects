import requests as rq
from bs4 import BeautifulSoup
import csv
import sys,pyperclip
import webbrowser as wb
'''
beutiful soup will convert the byte code return of page.content into more readable code in html/text
notes:
- the class_ argument is used to locate code by css tags and it's ( _) to avoid conflicting with class keyword
- previous editions of bs hasn't class_ argument, so there was the dict way of argument then specify the tag as key and its title as value
- championship=soup.find_all("div",class_="2829 matchCard matchesList")#return resultSet, this's how we search by css class
-The only difference is that find_all() returns a list containing the single result, and find() just returns the result.
-If find_all() can’t find anything, it returns an empty list. If find() can’t find anything, it returns None:
'''

def data_formating(date):
    #here i want to make swapping between the month and day
    date_list=list(date)
    copy_day=date_list[0:2]
    date_list[0:2]=date_list[3:5]
    date_list[3:5]=copy_day
    formated_date=''.join(date_list)
    return formated_date



if len(sys.argv)>1:
    input_date=''.join(sys.argv[1])# this should be written as mm/dd/yyyy
else:
    input_date=pyperclip.paste()

website_url='https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date='+data_formating(input_date)
page=rq.get(website_url)

def get_match_info(championships):
    for champ in championships:#has a [title,ul]
        championship_title = champ.find('h2').text.strip()
        teams=champ.find("div",class_="ul")
        teams_inEach_championship=teams.find_all("div",class_="item finish liItem")
        print(f"this championship has number of matches equel to :  {len(teams_inEach_championship)}")
    
    ''' 
        championship_broadcasting_channel=champ.find("div",class_="channel icon-channel")
        championship_date=champ.find("div",class_="date").text.strip()
        championship_status=champ.find("div",class_="matchStatus").text.strip()
        championship_time=champ.find("span",class_="time").text.strip()
        teamA=champ.find("div",class_="teams teamA").text.strip()
        teamB=champ.find("div",class_="teams teamB").text.strip()
        
        result_element = champ.find('div', class_='MResult')
        score_elements = result_element.find_all('span', class_='score')

        first_score = score_elements[0].text.strip()
        second_score = score_elements[1].text.strip()
        print(teamA," and ",teamB)

    '''

        
        

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    matches_details = []
    championships = soup.find_all("div", {"class": "matchCard"})
    get_match_info(championships)
    
    
main(page)

