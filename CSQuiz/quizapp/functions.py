import cfscrape
from bs4 import BeautifulSoup as BS
import re
from .models import Players
from .constants import COUNTRY_REGIONS


def url_is_valid(sector, profile_number):
    scraper = cfscrape.create_scraper()
    url = f'https://www.hltv.org/{sector}/{str(profile_number)}/find'
    status = scraper.get(url).status_code
    return status == 200


def found_info(profile_number):
    scraper = cfscrape.create_scraper()
    url = f'https://www.hltv.org/player/{str(profile_number)}/find'
    html = scraper.get(url).content
    soup = BS(html, 'html.parser')
    name, *surname = soup.find(class_='playerRealname').text.split()
    surname = ' '.join(surname)
    nickname = soup.find(class_='playerNickname').text
    country = soup.find(class_='playerRealname').find('img')['alt']
    age = re.search(r'\d+', soup.find(class_='playerAge').text).group()
    team = re.sub(r'Current teamTeam', '', soup.find(class_='playerTeam').text)
    major_winner = True if soup.findAll(class_='majorWinner') else False
    major_MVP = True if soup.findAll(class_='majorMVP') else False
    full_player_name = f"{name} '{nickname}' {surname}"
    for reg in COUNTRY_REGIONS:
        if country in COUNTRY_REGIONS[reg]:
            region = reg

    url = f'https://www.hltv.org/stats/players/weapon/{str(profile_number)}/find'
    status = 403
    while status == 403:
        req = scraper.get(url)
        status = req.status_code
    html = req.content
    soup = BS(html, 'html.parser')
    weapon = 'AWP' if soup.find(class_='stats-row').find_all('span')[1].text.strip() == 'awp' else 'Rifler'

    url = f'https://www.hltv.org/player/{str(profile_number)}/find#tab-achievementBox'
    html = scraper.get(url).content
    soup = BS(html, 'html.parser')
    res = soup.find(class_='sub-tab-content')
    if res.text.split()[0] == 'Major':
        major_played = res.find_all(class_='highlighted-stat')[1].find(class_='stat').text
    else:
        major_played = 0
    return name, surname, nickname, age, country, team, major_winner, major_MVP, full_player_name, region, weapon, major_played


def update_player(player):
    name, surname, nickname, age, country, team, major_winner, major_MVP, full_player_name, region, weapon, major_played = found_info(
        player.profile_number)
    player.name = name
    player.surname = surname
    player.nickname = nickname
    player.age = age
    player.country = country
    player.team = team
    player.major_winner = major_winner
    player.major_MVP = major_MVP
    player.full_player_name = full_player_name
    player.region = region
    player.weapon = weapon
    player.major_played = major_played
    player.save()


def add_player_to_DB(number):
    if Players.objects.filter(profile_number=number).exists():
        message = f'{Players.objects.filter(profile_number=number)[0].nickname} in DB already exists'
    else:
        if url_is_valid('player', number):
            name, surname, nickname, age, country, team, major_winner, major_MVP, full_player_name, region, weapon, major_played = found_info(
                number)
            Players.objects.create(profile_number=number,
                                   nickname=nickname,
                                   name=name,
                                   surname=surname,
                                   age=age,
                                   country=country,
                                   team=team,
                                   major_winner=major_winner,
                                   major_MVP=major_MVP,
                                   full_player_name=full_player_name,
                                   region=region,
                                   weapon=weapon,
                                   major_played=major_played)
            message = 'Successfully added ' + nickname + ' to DB'
        else:
            message = 'Invalid URL'
    return message


def add_team_to_DB(number):
    if url_is_valid('team', number):
        scraper = cfscrape.create_scraper()
        url = f'https://www.hltv.org/team/{str(number)}/find'
        html = scraper.get(url).content
        soup = BS(html, 'html.parser')
        player_list = [i['href'].split('/')[2] for i in soup.find(class_='bodyshot-team g-grid').find_all('a')]
        message = []
        for number in player_list:
            message.append(add_player_to_DB(number))
        return message
    else:
        return ['Invalid URL']

