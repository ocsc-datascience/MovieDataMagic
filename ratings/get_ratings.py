#!/usr/bin/env python3
import sys
import requests
import re
import pandas as pd
import lxml
from bs4 import BeautifulSoup




df = pd.read_csv("../data/metadata_all_movies.csv")

df['RT_title'] = ""
df['critics_rating'] = ""
df['audience_rating'] = ""

for index,row in df.iterrows():

    skip_critics = False
    skip_audience = False

    title = row['movie_title']
    
    #############################################################
    # manual data cleaning -- name mismatches
    RT_title = re.sub(':', '', re.sub(' ', '_', str(title)))
    RT_title = RT_title.replace('-_','')
    RT_title = RT_title.replace('!','')
    RT_title = RT_title.replace('(','')
    RT_title = RT_title.replace(')','')
    RT_title = RT_title.replace("'",'')
    RT_title = RT_title.replace(".",'')
    RT_title = RT_title.replace(",",'')
    RT_title = RT_title.replace("&",'and')
    
    if title == 'Princess Mononoke - Studio Ghibli (2018)':
        RT_title = 'princess_mononoke_studio_ghibli_fest_2018'
        critics = -1
        skip_critics = True

    if title == 'Labyrinth (2018 Fathom Event)':
        RT_title = 'labyrinth_2018'
        critics = -1
        skip_critics = True

    if title == 'Met Opera: Cendrillon':
        RT_title = 'the_metropolitan_opera_cendrillon'
        critics = -1
        audience = -1
        skip_critics = True
        skip_audience = True

    if title == 'Met Opera: Semiramide':
        RT_title = 'the_metropolitan_opera_semiramide'
        critics = -1
        audience = -1
        skip_critics = True
        skip_audience = True

    if title == 'Met Opera: La Bohème (2018)':
        RT_title = 'the_metropolitan_opera_la_boheme'
        critics = -1
        audience = -1
        skip_critics = True
        skip_audience = True

    if title == "Met Opera: L'Elisir d'Amore (2018)":
        RT_title = 'the_metropolitan_opera_lelisir_damore_2018'
        critics = -1
        audience = -1
        skip_critics = True
        skip_audience = True

    if title == "Met Opera: Tosca":
        RT_title = 'the_metropolitan_opera_tosca'
        critics = -1
        audience = -1
        skip_critics = True
        skip_audience = True
        
    if title == 'The Dark Crystal (special re-release)':
        RT_title = 'universal_pictures_presents_the_dark_crystal'
        critics = -1
        skip_critics = True
        
    if title == 'Truth or Dare':
        RT_title = 'blumhouses_truth_or_dare'

    if title == '85: The Greatest Team in Football History':
        critics = -1
        audience = -1
        skip_critics = True
        skip_audience = True

    if title == 'Coco':
        RT_title = 'coco_2017'

        
    year_fix_2018 = ['Skyscraper','Tag','Upgrade',\
                     'Life of the Party','Traffik',\
                     'Isle Of Dogs','Midnight Sun',\
                     'I Can Only Imagine','Tomb Raider',\
                     'A Wrinkle in Time','Gringo',\
                     'Black Panther','Samson',
                     'Peter Rabbit']

       
    if title in year_fix_2018:
        RT_title = RT_title.lower() + '_2018'

    year_fix_2017 = ['The Shape of Water','Darkest Hour',\
                     'Father Figures','Justice League','Jigsaw',\
                     'Only The Brave','The Snowman','The Foreigner',\
                     'My Little Pony: The Movie', 'The Stray', \
                     'American Made', 'Stronger',\
                     'American Assassin','mother!','It', 'Home Again',\
                     'Wind River','The Glass Castle','The Dark Tower',\
                     'Detroit','Atomic Blonde','Dunkirk','The House',\
                     'All Eyez on Me']

    if title in year_fix_2017:
        RT_title = RT_title.lower() + '_2017'

    year_fix_2016 = ['Fences','Incarnate','Arrival',\
                     'Doctor Strange','Inferno','Denial',\
                     'The Accountant','The Birth of a Nation',\
                     'When the Bough Breaks',"Don't Breathe",\
                     'War Dogs','Florence Foster Jenkins',\
                     'Suicide Squad','Cafe Society','Nerve',\
                     'Lights Out','The BFG']
    
    if title in year_fix_2016:
        RT_title = RT_title.lower() + '_2016'
        
    if title == 'TCM: West Side Story':
        RT_title = 'west_side_story_presented_by_tcm'
        critics = -1
        audience = -1
        skip_critics = True
        skip_audience = True

    if title == 'TCM Presents Casablanca 75th Anniversary':
        RT_title = 'casablanca_75th_anniversary_presented_by_tcm'
        critics = -1
        skip_critics = True

    if title == 'Spirited Away (Fathom Event)':
        RT_title = 'spirited_away_studio_ghibli_fest_2018'
        critics = -1
        audience = -1
        skip_critics = True
        skip_audience = True


    if title == 'Kirk Cameron REVIVE US 2':
        critics = -1
        audience = -1
        skip_critics = True
        skip_audience = True

    if title == 'Close Encounters of the Third Kind (40th Anniversary)':
        RT_title = 'close_encounters_of_the_third_kind_40th_anniversary_release'

    if title == 'The Wild Life (2016)':
        RT_title = 'the_wild_life'
        
        
    #############################################################
    print(index,title,RT_title)
    df.loc[index,'RT_title'] = RT_title

    tomato_base_url = 'https://www.rottentomatoes.com/m/'

    try:
        tomato_url = tomato_base_url + RT_title
        soup = BeautifulSoup(requests.get(tomato_url).text,"lxml")
    except:
        print("request failed")

    if not skip_critics:
        try:
            critics = int(min(soup.find('span', \
                {'class': 'meter-value superPageFontColor'}).contents[0]))
        except:
            print("critics failed")
            print(tomato_url)
            sys.exit()

    if not skip_audience:

        try:
            res = soup.find_all('span', {'class': 'superPageFontColor'})
            for tag in res:
                if 'style' in tag.attrs.keys():
                    audience = int((str(tag.text)).replace('%',''))
        except:
            print("audience failed")
            print(RT_title)
            sys.exit()

    print(title,critics,audience)
    df.loc[index,'critics_rating'] = critics
    df.loc[index,'audience_rating'] = audience


df.to_csv("../data/all_movies_with_ratings.csv",header=True,index=False)

