import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
model_list = [
    {
        'model': 'Apple iPhone 6',
        'storage': ['i000000001312', 'i000000004648', 'i000000001319', 'i000000001305']
    },
    {
        'model': 'Apple iPhone 6 Plus',
        'storage': ['i000000001387', 'i000000001394', 'i000000001380']
    },

    {
        'model': 'Apple iPhone 6s',
        'storage': ['i000000001486', 'i000000004698', 'i000000001517', 'i000000001455']
    },

    {
        'model': 'Apple iPhone 6s Plus',
        'storage': ['i000000001579', 'i000000004729', 'i000000001610', 'i000000001548']
    },
    {
        'model': 'Apple iPhone 7',
        'storage': ['i000000004392', 'i000000004427', 'i000000004462']
    },
    {
        'model': 'Apple iPhone 7 Plus',
        'storage': ['i000000004497', 'i000000004532', 'i000000004567']
    },
    {
        'model': 'Apple iPhone 8',
        'storage': ['i000000007916', 'i000000019109', 'i000000007860']
    },
    {
        'model': 'Apple iPhone 8 Plus',
        'storage': ['i000000007944', 'i000000019137', 'i000000007888']
    },
    {
        'model': 'Apple iPhone SE (2nd Generation)',
        'storage': ['i000000021003', 'i000000021004', 'i000000021005']
    },
    {
        'model': 'Apple iPhone X',
        'storage': ['i000000008064', 'i000000008043']
    },
    {
        'model': 'Apple iPhone XR',
        'storage': ['i000000011414', 'i000000011463', 'i000000011512']
    },
    {
        'model': 'Apple iPhone XS',
        'storage': ['i000000011246', 'i000000011274', 'i000000011302']
    },
    {
        'model': 'Apple iPhone XS Max',
        'storage': ['i000000011330', 'i000000011358', 'i000000011386']
    },
    {
        'model': 'Apple iPhone 11',
        'storage': ['i000000018674', 'i000000018723', 'i000000018772']
    },
    {
        'model': 'Apple iPhone 11 Pro',
        'storage': ['i000000018821', 'i000000018856', 'i000000018891']
    },
    {
        'model': 'Apple iPhone 11 Pro Max',
        'storage': ['i000000018926', 'i000000018961', 'i000000018996']
    },
    {
        'model': 'Apple iPhone 12',
        'storage': ['i000000022632', 'i000000022674', 'i000000022716']
    },
    {
        'model': 'Apple iPhone 12 mini',
        'storage': ['i000000022758', 'i000000022800', 'i000000022842']
    },
    {
        'model': 'Apple iPhone 12 Pro',
        'storage': ['i000000022884', 'i000000022919', 'i000000022954']
    },
    {
        'model': 'Apple iPhone 12 Pro Max',
        'storage': ['i000000022989', 'i000000023024', 'i000000023059']
    }
]
carrier_list = [
    {
        'network': 'unlocked',
        'depreciation': 1
    },
    {
        'network': 'verizon',
        'depreciation': 1
    },

    {
        'network': 'AT&T',
        'depreciation': 0.847
    },
    {
        'network': 'T-Mobile',
        'depreciation': 0.773
    },
    {
        'network': 'sprint',
        'depreciation': 0.713
    },
    {
        'network': 'other',
        'depreciation': 0.44
    }

]


condition_list = ['good', 'poor', 'faulty']
all_models = []
for attribute in model_list:
    for storage in attribute['storage']:
        for carrier in carrier_list:
            for condition in condition_list:
                url = f'https://www.decluttr.com/product-details?barcode={storage}'
                page = requests.get(url)
                soup = BeautifulSoup(page.content, 'html.parser')
                model = attribute['model']
                carrier_name = carrier['network']
                carrier_value = carrier['depreciation']
                storage_name = soup.find(class_='features-list').find_all('span')[3].text
                price = float(soup.find(id=f'condition-{condition}-tab').attrs['data-price'])
                price = round(price * carrier_value, 2)
                all_models.append((model, storage_name, carrier_name, condition, price))


with open('decluttr.csv', 'w') as file:
    file.write('model,storage,carrier,condition,price\n')
    writer = csv.writer(file)
    for model, storage, carrier, condition, price in all_models:
        writer.writerow((model, storage, carrier, condition, price))


'''
for items in soup.find_all(class_='grid-item-inner'):
    model_name = items.find(class_='grid-item-name').text
    for attributes in items.find_all(class_='capacity-btn'):
        capacity = attributes.attrs['title']
        barcode = attributes.attrs['href'][25:]
        print(f'{model_name} - {capacity} - Barcode: {barcode}')
'''