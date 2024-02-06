import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
base_url = "https://curovms.com/VP/VisitorPass.aspx?i="
def extract_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting required data
        name_element = soup.find('div', {'class': 'visitor-detail-info'}).find('h2')
        name = name_element.text.strip() if name_element else ""

        contact_number_element = soup.find('div', {'class': 'visitor-detail-info'}).find_all('h2')[1]
        contact_number = contact_number_element.text.strip() if contact_number_element else ""

        address_element = soup.find('div', {'class': 'visitor-detail-info'}).find_all('h2')[2]
        address = address_element.text.strip() if address_element else ""

        # company_name_element = soup.find('div', {'class': 'visitor-top'}).find_all('h4', string='Company Name :')
        # company_name = company_name_element.find_next('h4').text.strip() if company_name_element and company_name_element.find_next('h4') else ""

        # meeting_person_element = soup.find('div', {'class': 'visitor-top'}).find('h4', string='Meeting Person :')
        # meeting_person = meeting_person_element.find_next('h4').text.strip() if meeting_person_element and meeting_person_element.find_next('h4') else ""

        # pass_type_element = soup.find('div', {'class': 'visitor-top'}).find('h4', string='Pass Type :')
        # pass_type = pass_type_element.find_next('h4').text.strip() if pass_type_element and pass_type_element.find_next('h4') else ""

        # entry_element = soup.find('div', {'class': 'visitor-top'}).find('h4', string='Entry :')
        # entry = entry_element.find_next('h4').text.strip() if entry_element and entry_element.find_next('h4') else ""

        # status_element = soup.find('div', {'class': 'visitor-top'}).find('h4', string='Status :')
        # status = status_element.find_next('h4').text.strip() if status_element and status_element.find_next('h4') else ""

        # purpose_element = soup.find('div', {'class': 'visitor-top'}).find('h4', string='Purpose of Visit :')
        # purpose = purpose_element.find_next('h4').text.strip() if purpose_element and purpose_element.find_next('h4') else ""

        # issued_datetime_element = soup.find('div', {'class': 'visitor-top'}).find('h4', string='Issued Datetime :')
        # issued_datetime = issued_datetime_element.find_next('h4').text.strip() if issued_datetime_element and issued_datetime_element.find_next('h4') else ""

        # valid_up_to_element = soup.find('div', {'class': 'visitor-top'}).find('h4', string='Valid Up To :')
        # valid_up_to = valid_up_to_element.find_next('h4').text.strip() if valid_up_to_element and valid_up_to_element.find_next('h4') else ""

        # Similarly, handle other elements

        data = {
            'Name': [name],
            'Contact Number': [contact_number],
            'Address': [address],
            # 'Company Name': [company_name],
            # 'Meeting Person': [meeting_person],
            # 'Pass Type': [pass_type],
            # 'Entry': [entry],
            # 'Status': [status],
            # 'Purpose of Visit': [purpose],
            # 'Issued Datetime': [issued_datetime],
            # 'Valid Up To': [valid_up_to],
            # Include other fields in a similar manner
        }

        return pd.DataFrame(data)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

# def main():
#     if len(sys.argv) != 2:
#         print("Usage: python script.py <URL>")
#         sys.exit(1)

base_url = "https://curovms.com/VP/VisitorPass.aspx?i="
project = "19"

# list = [68109284546219, 25858309136619, 25858309136219,68109284546219]


for i in range(258583,259000):
    for j in range(100000,999999):

        try:

            url = base_url+str(i)+str(j)+project
            data = data +  extract_data(url)
        

            if data is not None:
                try:
                    # Load existing data from the Excel file if it exists
                    existing_data = pd.read_excel('visitor_data.xlsx')
                    # Concatenate existing data with the new data
                    combined_data = pd.concat([existing_data, data], ignore_index=True)
                    # Save the combined data back to the Excel file
                    combined_data.to_excel('visitor_data.xlsx', index=False)
                    print("Data has been extracted and saved successfully.")
                except FileNotFoundError:
                    # If the file does not exist, save the new data directly
                    data.to_excel('visitor_data.xlsx', index=False)
                    print("Data has been extracted and saved successfully.")
        except:
            print("not available")

# if __name__ == "__main__":
#     main()
