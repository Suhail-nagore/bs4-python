import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def extract_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    name = soup.find_all('h2')[1].text.strip()
    phone = soup.find_all('h2')[2].text.strip()
    address = soup.find_all('h2')[3].text.strip()

    return name, phone, address

def write_to_excel(data, filename='visitor_info.xlsx'):
    if os.path.exists(filename):
        df = pd.read_excel(filename)
        new_df = pd.DataFrame(data, columns=['Name', 'Number', 'Address'])
        df = pd.concat([df, new_df])
    else:
        df = pd.DataFrame(data, columns=['Name', 'Number', 'Address'])
    df.to_excel(filename, index=False)

def main():
    url = 'https://curovms.com/VP/VisitorPass.aspx?i=68109284546219'
    data = []
    name, phone, address = extract_info(url)
    data.append([name, phone, address])
    write_to_excel(data)

if __name__ == "__main__":
    main()