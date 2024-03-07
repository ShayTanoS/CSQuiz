import cfscrape
from bs4 import BeautifulSoup as BS
import re


def found_info(profile_number, nickname):
    scraper = cfscrape.create_scraper()
    url = f'https://www.hltv.org/player/{str(profile_number)}/{nickname.lower()}'
    html = scraper.get(url).content
    soup = BS(html, 'html.parser')
    name, surname = soup.find(class_='playerRealname').text.split()
    country = soup.find(class_='playerRealname').find('img')['alt']
    age = re.search(r'\d+', soup.find(class_='playerAge').text).group()
    team = re.sub(r'Current teamTeam', '', soup.find(class_='playerTeam').text)
    major_winner = True if soup.findAll(class_='majorWinner') else False
    major_MVP = True if soup.findAll(class_='majorMVP') else False
    return name, surname, age, country, team, major_winner, major_MVP


a, b, c, d, e, f, g = found_info(7998, 's1mple')
