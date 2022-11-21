import requests 
from bs4 import BeautifulSoup
from tqdm import tqdm 
from time import sleep
from colorama import init, Fore
import os 
from pyautogui import prompt 
##

init()
##

url = 'https://www.python.org/downloads/'

get_url = requests.get(url)

get_file_path = prompt(text='Enter path to output file')

bs = BeautifulSoup(get_url.content, 'lxml')

versions_list = bs.find_all("span", class_='release-number')


with open(get_file_path, 'w', encoding='utf-8') as file:
    
    for version in tqdm(versions_list):

        file.write(f'{version.text}\n')
        
    print(Fore.RED + '\nDone!')

    file.close()

os.system(get_file_path)
