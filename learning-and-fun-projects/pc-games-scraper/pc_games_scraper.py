import requests  
from bs4 import BeautifulSoup  

name_list = []  
  
response = requests.get('https://www.pcgamer.com/the-top-100-pc-games-2023/')  
web_content = response.text  
soup = BeautifulSoup(web_content, 'html.parser')  
 
getname = soup.find_all('h2')   

for i in getname:  
    game_name = i.text.strip()   
    if "." in game_name: 
        print(game_name) 
