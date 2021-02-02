from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome("C:\chromedriver.exe",options=options)


def get_team_stat(team_id):
    driver = webdriver.Chrome("C:\chromedriver.exe",options=options)
    driver.get("https://fantasy.premierleague.com/entry/{}/event/{}/".format(team_id,gw))
    content = driver.page_source
    driver.close()
    driver.quit()
    soup = BeautifulSoup(content)
    owner = soup.title.text
    players = soup.findAll(attrs={'class':'PitchElementData__ElementName-sc-1u4y6pr-0 eMnDEV'})
    points = soup.findAll(attrs={'class':'PitchElementData__ElementValue-sc-1u4y6pr-1 bcESdd'})
    stat_dict = {players[i].text:points[i].text for i in range(len(players))}

    print(owner)
    for pl,pt in stat_dict.items():
        print(pl,'---->',pt)

    return owner, stat_dict

if __name__=="__main__":
    monkeys = [7878728,7882961,6786042,7888441,7807933]
    opponent = [1732591,7507474,7850315,7824821,362867]
    gw = 22

    monkey_squad = []
    monkeys_dict = {}
    opponent_squad = []
    opponent_dict = {}

    for item in monkeys:
        owner, stat_dict = get_team_stat(item)
        monkeys_dict[owner] = stat_dict
        monkey_squad.append(list(stat_dict.keys()))

    monkey_squad_flattened = [player for team in monkey_squad for player in team]

    for item in opponent:
        owner, stat_dict = get_team_stat(item)
        opponent_dict[owner] = stat_dict
        opponent_squad.append(list(stat_dict.keys()))
    
    opponent_squad_flattened = [player for team in opponent_squad for player in team]

    monkey_differentials = []

    for player in monkey_squad_flattened:
        try:
            opponent_squad_flattened.remove(player)
        except:
            monkey_differentials.append(player)

    print("Hola Diego!!")
    


