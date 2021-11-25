import requests
from bs4 import BeautifulSoup

# WEB SCRAPING

# enter a page and get info

URL = "https://lpf.ro/liga-1"
page = requests.get(URL)

# print(page)  # response type object
#
# print(page.content)  # HTML

# parse the content
soup = BeautifulSoup(page.content, 'html.parser')

results_table = soup.find(id='clasament_ajax')
# print(results_table)

team_rows = results_table.find_all(class_='echipa_row')  # filter
print(team_rows)

teams = []
for team in team_rows:
    team_cell = team.find('td', class_='echipa')
    team_name = team_cell.find('a').text.strip()  # get txt from links and truncate space
    team_position = team.find('td', class_='poz').text.strip()
    team_points = team.find('td', class_='puncte').text.strip()
    teams.append({
        'name': team_name,
        'position': team_position,
        'points': team_points
    })

print(teams)

# Tema: program consola cu meniu- 1 pt afisare; 2 pt afisare play-off, 3 pt afisare play out
