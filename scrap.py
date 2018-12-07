import requests
from bs4 import BeautifulSoup
import re

def format_meaning(text):
    text = ((text.replace("Meaning","")).replace("meaning","")).replace('"','')
    text = (text.lstrip()).rstrip()
    text = re.sub("[\(\[].*?[\)\]]", "", text)
    return(text)

def format_slang(text):
    text = text.lstrip()
    text = text.rstrip()
    return(text)

def save_file(slang_list,slang_meaning_list):

    assert len(slang_list) == len(slang_meaning_list)

    for i in range(len(slang_list)):
        with open('emoji.txt', 'a') as the_file:
            the_file.write(slang_list[i] + "=" + slang_meaning_list[i] + "\n")

def main():
    slang_list = []
    slang_meaning_list = []

    r =  requests.get('https://www.webopedia.com/quick_ref/textmessageabbreviations.asp')
    soup = BeautifulSoup(r.content, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')

    for row in rows:
        row_data = row.find_all('td')
        if(len(row_data) == 2):
            slang_list.append(format_slang(row_data[0].text))
            slang_meaning_list.append(format_meaning(row_data[1].text))

    save_file(slang_list,slang_meaning_list)

if __name__ == '__main__':
    main()
