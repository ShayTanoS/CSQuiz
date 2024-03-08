import cfscrape
from bs4 import BeautifulSoup as BS
import re

def url_is_valid(profile_number):
    scraper = cfscrape.create_scraper()
    url = f'https://www.hltv.org/player/{str(profile_number)}/find'
    return scraper.get(url).status_code == 200
def found_info(profile_number):
    scraper = cfscrape.create_scraper()
    url = f'https://www.hltv.org/player/{str(profile_number)}/find'
    html = scraper.get(url).content
    soup = BS(html, 'html.parser')
    name, surname = soup.find(class_='playerRealname').text.split()
    nickname = soup.find(class_='playerNickname').text
    country = soup.find(class_='playerRealname').find('img')['alt']
    age = re.search(r'\d+', soup.find(class_='playerAge').text).group()
    team = re.sub(r'Current teamTeam', '', soup.find(class_='playerTeam').text)
    major_winner = True if soup.findAll(class_='majorWinner') else False
    major_MVP = True if soup.findAll(class_='majorMVP') else False
    return name, surname, nickname, age, country, team, major_winner, major_MVP



