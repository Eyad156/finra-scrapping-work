import requests 
from bs4 import BeautifulSoup
import csv

def fetch_broker_dealer_list():
    url = 'https://www.finra.org/about/firms-we-regulate/broker-dealer-firms-we-regulate'
    response = requests.get(url)
    if response.status_code == 200:
        print("The website is working...")
        soup = BeautifulSoup(response.content, 'html.parser')
        broker_dealer_list = soup.find_all('div', class_='field-content')
        
        # Create a list to hold the broker/dealer names
        broker_dealers = []
        
        for item in broker_dealer_list:
            broker_dealers.append(item.text.strip(),'\n')
        
        # Save the extracted data to a CSV file
        with open('broker_dealer_list.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Broker/Dealer Name'])  # Write the header
            for broker in broker_dealers:
                writer.writerow([broker])
        
        print("Data has been successfully extracted and saved to broker_dealer_list.csv")
    else:
        print("I can't find the website.")

fetch_broker_dealer_list()
