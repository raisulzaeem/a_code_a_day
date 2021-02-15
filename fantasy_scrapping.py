from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = True
driver = webdriver.Chrome("C:\chromedriver.exe",options=options)


def get_team_stat(team_id):
    driver = webdriver.Chrome("C:\chromedriver.exe",options=options)
    driver.get("https://fantasy.premierleague.com/entry/{}/event/{}/".format(team_id,gw))
    time.sleep(5)
    content = driver.page_source
    driver.close()
    driver.quit()
    soup = BeautifulSoup(content)
    owner = soup.title.text
    # players = soup.findAll(attrs={'class':'PitchElementData__ElementName-sc-1u4y6pr-0 eMnDEV'})
    pitch = soup.findAll(attrs={'class':'Pitch__StyledPitchElement-sc-1mctasb-5 igRGnf'})
    # points = soup.findAll(attrs={'class':'PitchElementData__ElementValue-sc-1u4y6pr-1 bcESdd'})
    # stat_dict = {players[i].text:points[i].text for i in range(11)}
    stat_dict = {player.div.contents[0].text:player.div.contents[1].text for player in pitch} 

    print(owner)
    for pl,pt in stat_dict.items():
        print(pl,'---->',pt)

    return owner, stat_dict

if __name__=="__main__":
    monkeys = [7878728,7882961,6786042,7888441,7807933]
    opponent = [5857310,2887945,3046358,3546962,5971879]
    gw = 24

    monkey_squad = []
    monkeys_dict = {}
    opponent_squad = []
    opponent_dict = {}

    for item in monkeys:
        owner, stat_dict = get_team_stat(item)
        monkeys_dict[owner] = stat_dict
        monkey_squad.append(list(stat_dict.items()))

    monkey_squad_flattened = [player for team in monkey_squad for player in team]

    for item in opponent:
        owner, stat_dict = get_team_stat(item)
        opponent_dict[owner] = stat_dict
        opponent_squad.append(list(stat_dict.items()))
    
    opponent_squad_flattened = [player for team in opponent_squad for player in team]

    monkey_differentials = []

    for player in monkey_squad_flattened:
        try:
            opponent_squad_flattened.remove(player)
        except:
            monkey_differentials.append(player)

    print("monkey_differentials: ", monkey_differentials, "\n\n\n","opponent_differentials: ", opponent_squad_flattened)
    dashedline = "\n--------------------------------------------------------------------------\n"
    with open("Fantasy_data.txt","w") as f:
        f.write("#### ---- Monkey Squad ---- ####\n")
        for owner, squad in monkeys_dict.items():
            f.write(owner)
            f.write(dashedline)
            for player, point in squad.items():
                f.write(player+' ----> '+point+'\n')
            f.write("\n\n")
        f.write("\n#### ---- Opponent Squad ---- ####\n")
        for owner, squad in opponent_dict.items():
            f.write(owner)
            f.write(dashedline)
            for player, point in squad.items():
                f.write(player+' ----> '+point+'\n')
            f.write("\n\n")
        f.write("\n#### ---- Monkey Differentials ---- ####"+2*dashedline)
        for player, point in monkey_differentials:
            f.write(player+' ----> '+point)
            f.write("\n")
        f.write('\n'+2*dashedline)
        f.write("\n#### ---- Opponent Differentials ---- ####"+2*dashedline)
        for player, point in monkey_differentials:
            f.write(player+' ----> '+point)
            f.write("\n")
        f.write('\n'+2*dashedline)

    print("Hola Diego!!")
    


