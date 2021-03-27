import requests
from bs4 import BeautifulSoup
import csv
model_list = [
    {
        'model name': 'Apple iPhone 6',
        'model id': 'iphone-6',
        'capacity': ['16', '32', '64', '128']
    },
    {
        'model name': 'Apple iPhone 6 Plus',
        'model id': 'iphone-6-plus',
        'capacity': ['16', '64', '128']
    }
]
'''
    {
        'model name': 'Apple iPhone 6s',
        'model id': 'iphone-6s',
        'capacity': ['16', '32', '64', '128']
    },

    {
        'model name': 'Apple iPhone 6s Plus',
        'model id': 'iphone-6s-plus',
        'capacity': ['16', '32', '64', '128']
    },
    {
        'model name': 'Apple iPhone 7',
        'model id': 'iphone-7',
        'capacity': ['32', '128', '256']
    },
    {
        'model name': 'Apple iPhone 7 Plus',
        'model id': 'iphone-7-plus',
        'capacity': ['32', '128', '256']
    },
    {
        'model name': 'Apple iPhone 8',
        'model id': 'iphone-8',
        'capacity': ['64', '128', '256']
    },
    {
        'model name': 'Apple iPhone 8 Plus',
        'model id': 'iphone-8-plus',
        'capacity': ['64', '128', '256']
    },
    {
        'model name': 'Apple iPhone SE (2nd Generation)',
        'model id': 'iphone-se-2020',
        'capacity': ['64', '128', '256']
    },
    {
        'model name': 'Apple iPhone X',
        'model id': 'iphone-x',
        'capacity': ['64', '256']
    },
    {
        'model name': 'Apple iPhone XR',
        'model id': 'iphone-xr',
        'capacity': ['64', '128', '256']
    },
    {
        'model name': 'Apple iPhone XS',
        'model id': 'iphone-xs',
        'capacity': ['64', '256', '512']
    },
    {
        'model name': 'Apple iPhone XS Max',
        'model id': 'iphone-xs-max',
        'capacity': ['64', '256', '512']
    },
    {
        'model name': 'Apple iPhone 11',
        'model id': 'iphone-11',
        'capacity': ['64', '128', '256']
    },
    {
        'model name': 'Apple iPhone 11 Pro',
        'model id': 'iphone-11-pro',
        'capacity': ['64', '256', '512']
    },
    {
        'model name': 'Apple iPhone 11 Pro Max',
        'model id': 'iphone-11-pro-max',
        'capacity': ['64', '256', '512']
    },
    {
        'model name': 'Apple iPhone 12',
        'model id': 'iphone-12',
        'capacity': ['64', '128', '256']
    },
    {
        'model name': 'Apple iPhone 12 mini',
        'model id': 'iphone-12-mini',
        'capacity': ['64', '128', '256']
    },
    {
        'model name': 'Apple iPhone 12 Pro',
        'model id': 'iphone-12-pro',
        'capacity': ['128', '256', '512']
    },
    {
        'model name': 'Apple iPhone 12 Pro Max',
        'model id': 'iphone-12-pro-max',
        'capacity': ['128', '256', '512']
    }
]
'''
carrier_list = [
    {
        'carrier name': 'Unlocked',
        'carrier id': 'unlocked'
    },
    {
        'carrier name': 'Verizon',
        'carrier id': 'verizon'
    },
    {
        'carrier name': 'ATT',
        'carrier id': 'at-t'
    },
    {
        'carrier name': 'T-Mobile',
        'carrier id': 't-mobile'
    },
    {
        'carrier name': 'Sprint',
        'carrier id': 'sprint'
    },
    {
        'carrier name': 'Other',
        'carrier id': 'sprint'
    }
]
all_models = []
condition_list = ['good', 'fair', 'broken']
for attributes in model_list:
    for capacity in attributes['capacity']:
        for carrier in carrier_list:
            model_name = attributes['model name']
            model_id = attributes['model id']
            carrier_name = carrier['carrier name']
            carrier_id = carrier['carrier id']

            url = f'https://recell.io/iphone/{model_id}/{carrier_id}/{model_id}-{capacity}gb-{carrier_name}'
            print(url)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            for condition in condition_list:
                price = soup.find(class_=condition).attrs['data-price']
                all_models.append((model_name, capacity, carrier_name, condition, price))
                print((model_name, capacity, carrier_name, condition, price))

with open('recellio.csv', 'w') as file:
    file.write('model,storage,carrier,condition,price\n')
    writer = csv.writer(file)
    for model, storage, carrier, condition, price in all_models:
        writer.writerow((model, storage, carrier, condition, price))