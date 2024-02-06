import requests
from bs4 import BeautifulSoup
import pandas as pd
import concurrent.futures
import openpyxl
from openpyxl import load_workbook


base_url = "https://curovms.com/VP/VisitorPass.aspx?i="
project = "19"

def extract_data(url):
    # print("checks")
    response = requests.get(url)

    if response.status_code == 200:
        print("200")
        soup = BeautifulSoup(response.text, 'html.parser')

        name_element = soup.find('div', {'class': 'visitor-detail-info'}).find('h2')
        name = name_element.text.strip() if name_element else ""

        contact_number_element = soup.find('div', {'class': 'visitor-detail-info'}).find_all('h2')[1]
        contact_number = contact_number_element.text.strip() if contact_number_element else ""

        address_element = soup.find('div', {'class': 'visitor-detail-info'}).find_all('h2')[2]
        address = address_element.text.strip() if address_element else ""

        data = {
            'Name': [name],
            'Contact Number': [contact_number],
            'Address': [address],
        }

        return pd.DataFrame(data)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

def process_url(url):
    data = extract_data(url)
    if data is not None:
        try:
            existing_data = pd.read_excel('visitor_data.xlsx')
            combined_data = pd.concat([existing_data, data], ignore_index=True)
            combined_data.to_excel('visitor_data.xlsx', index=False)
            print("Data has been extracted and saved successfully.")
        except FileNotFoundError:
            data.to_excel('visitor_data.xlsx', index=False)
            print("Data has been extracted and saved successfully.")
    else:
        print(f"The data is not found for this {url}")




def main():
    start=int(input("Enter the starting ULR key"))
    size = int(input("Enter the chunk size for each thread"))
    size=size*10
    # thread_count=int(input("Enter the No. of threads"))


    i_start = int(start/size)
    i_end=i_start+1
    j_start=start%size
    j_end=j_start+(int(size/10))


    url_series = [
        # (i_start, i_end, j_start, j_end),
        (i_start, i_end, j_start, j_end),
        (i_start+1, i_end+1, j_end+1, j_end+(int(size/10))),
        (i_start+2, i_end+2,j_end+2,j_end+(int(size/10))),
        (i_start+3, i_end+3, j_end+3, j_end+(int(size/10))),
        (i_start+4, i_end+4, j_end+4, j_end+(int(size/10))),
        (i_start+5, i_end+5, j_end+5, j_end+(int(size/10))),
        (i_start+6, i_end+6, j_end+6, j_end+(int(size/10))),
        (i_start+7, i_end+7, j_end+7, j_end+(int(size/10))),
        (i_start+8, i_end+8, j_end+8, j_end+(int(size/10))),
        (i_start+9, i_end+9, j_end+9, j_end+(int(size/10))),


        # Add more series as needed
    ]

    urls = []
    for i_start, i_end, j_start, j_end in url_series:
        for i in range(i_start, i_end):
            for j in range(j_start, j_end):
                url = f"{base_url}{i}{j}{project}"
                urls.append(url)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_url, urls)

if __name__ == "__main__":
    main()
