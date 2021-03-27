import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def get_average(lst):
    sum = 0
    length = len(lst)
    for price in lst:
        sum = sum + price
    return round(sum/length, 2)

def reject_outliers(data):
    m = 2
    u = np.mean(data)
    s = np.std(data)
    filtered = [e for e in data if (u - 2 * s < e < u + 2 * s)]
    return filtered



def requestPage(keyword, added_word, model, network, storage, condition, buying_format):
    raw_model = model.replace(' ', '%2520').replace('(', '%2528').replace(')', '%2529')
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={keyword}+{added_word}&_sacat=0&Model={raw_model}&Network={network}&Storage%2520Capacity={storage}%2520GB&_dcat=9355&LH_ItemCondition={condition}&rt=nc&LH_Sold=1&LH_Complete=1&_ipg=200&_pgn=1&_ipg=200&LH_{buying_format}=1'
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    print()
    results = int(soup.find(class_='srp-controls__count-heading').find(class_='BOLD').text.replace(',', ''))
    return soup, results

def getUnfilteredPrices(soup):
    title_list = [value.text.strip().lower() for value in soup.find_all(class_='s-item__title s-item__title--has-tags')]
    price_list = [value.text.strip().lower() for value in soup.find_all(class_='s-item__price')]
    zipped = list(zip(title_list, price_list))
    return zipped


def getFilteredPrices(title_price_list):
    all_title_and_price = []
    all_prices = []
    for tp in title_price_list:
        if 'to' not in tp[1] and all([w not in tp[0] for w in excludedPhrases]):
            all_title_and_price.append(tp)
            all_prices.append(float(tp[1][1:].replace(',', '')))
    return all_title_and_price, all_prices

def getAveragePrice(prices):
    average_price = get_average(reject_outliers(prices))
    return average_price


def plot(all_prices, average_price, result):
    plt.hist(reject_outliers(all_prices), bins=30)
    plt.axvline(x=average_price, color='r', linestyle='dashed', linewidth=2)
    plt.title(f'{model} - ({carrierName}) - ({storage}GB) - ({conditionName}) - ({result} results)')
    plt.xlabel(f'Sold Price ($) - Average Price: ({average_price})')
    plt.ylabel('Volume')
    plt.show()

def writeCSV(msp, file_name):
    with open(file_name, 'w') as file:
        file.write('model,storage,carrier,condition,price\n')
        writer = csv.writer(file)
        for model, storage, carrier, condition, price in msp:
            writer.writerow((model, storage, carrier, condition, price))

        file.close()


networks = {
    'Unlocked': 'Unlocked',
    'Verizon': 'Verizon',
    'AT&T': 'AT%2526T',
    'T-Mobile': 'T%252DMobile',
    'Sprint': 'Sprint'

}


buying_format_dict = {'Buy It Now': 'BIN', 'Auction': 'Auction'}


conditions = {

    'Like New': {
        'conditionID': '3000',
        'excludedPhrases': ['read', 'face', 'see', 'not', 'lot', 'protector', 'case', 'bad', 'touch', 'fair', 'ic', 'poor', 'lcd'],
        'addedWord': 'excellent'
    },
    'Good': {
        'conditionID': '3000',
        'excludedPhrases': ['read', 'face', 'see', 'not', 'lot', 'protector', 'case', 'bad', 'touch', 'fair', 'ic', 'poor', 'lcd'],
        'addedWord': ''
    },
    'Fair': {
        'conditionID': '3000',
        'excludedPhrases': ['face', 'lot', 'protector', 'case', 'touch', 'ic'],
        'addedWord': ''
    },
    'Broken': {
        'conditionID': '7000',
        'excludedPhrases': ['lot', 'protector', 'case', 'ic'],
        'addedWord': ''
    }
}




keyword = 'iPhone'
buying_format = buying_format_dict['Buy It Now']



carrierName = 'AT&T'
carrierID = networks[carrierName]
conditionName = 'Like New'
conditionID = conditions[conditionName]['conditionID']

excludedPhrases = conditions[conditionName]['excludedPhrases']
includedPhrase = conditions[conditionName]['addedWord']
model = 'Apple iPhone XR'
storage = '64'
soup = requestPage(keyword, includedPhrase, model, carrierID, storage, conditionID, buying_format)

title_and_prices = getUnfilteredPrices(soup[0])
try:
    results = soup[1]
except:
    results = 0

filtered_prices = getFilteredPrices(title_and_prices)
if results >= 25:
    try:

        average_price = getAveragePrice(filtered_prices[1])
        #plot(filtered_prices[1], average_price, results)
        print((model, storage, carrierName, conditionName, average_price))
    except Exception as e:
        print((model, storage, carrierName, conditionName, e))
else:
    print((model, storage, carrierName, conditionName, "**NOT ENOUGH RESULTS**"))

